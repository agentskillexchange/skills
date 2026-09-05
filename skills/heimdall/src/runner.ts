/**
 * The runner: resolve each case's driver, gate risky cases, run cdp/container
 * cases through their drivers (with a concurrency pool), block what Heimdall
 * can't run honestly, and emit a {@link RunReport}.
 */
import { mkdir, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { chromium } from "playwright";
import type { Driver, Plan, Redaction, Result, RunReport, Step, TestCase } from "./schema.js";
import { fidelityForDriver } from "./schema.js";
import { runHookSteps } from "./execute.js";
import { redactWithSpec, redactString, clearSecrets } from "./redact.js";
import { CdpDriver } from "./drivers/cdp.js";
import { ContainerDriver } from "./drivers/container.js";
import type { CaptureMode, CaseDriver, RunContext } from "./drivers/types.js";
import { log, c } from "./log.js";
import { VERSION } from "./version.js";

export interface RunOptions {
  outDir: string;
  baseUrl?: string;
  storageState?: string;
  allowRisk: boolean;
  headed: boolean;
  concurrency: number;
  /** Force every case onto this driver, ignoring per-case/plan settings. */
  driverOverride?: Driver;
  /** Only run cases whose id or tags match one of these (substring / exact tag). */
  filter?: string[];
  /** Disable TLS validation (opt-in). Ignored when a storageState is injected. */
  insecureTLS?: boolean;
  /** Retry a failed/errored case up to this many extra times (default 0). */
  retries?: number;
  /** Default overall wall-clock budget per case in ms; per-case timeoutMs wins. */
  timeoutMs?: number;
  /** When to keep a Playwright trace.zip per case (default "off"). */
  trace?: CaptureMode;
  /** When to keep a Playwright video per case (default "off"). */
  video?: CaptureMode;
  /**
   * Extra redaction (typically the resolved `heimdall.config.json` spec) folded with
   * `plan.redaction`: response-header names + regex sources scrubbed from the report
   * AND the on-disk HAR, on top of the per-run `${env.X}` secrets. Omitted => legacy
   * behaviour (report byte-identical to a `redactDeep`-only run).
   */
  redaction?: Redaction;
  /**
   * Results produced OUTSIDE this runner (e.g. `driver: extension` cases executed via
   * the agent's real-Chrome browser tools) to fold into the report. A result whose id
   * matches a (blocked) plan case REPLACES that entry verbatim - its status + evidence
   * are kept exactly, never fabricated green; an id absent from the plan is surfaced as
   * an extra result; the summary is then recomputed from the merged truth.
   */
  externalResults?: Result[];
}

/** Union the header names + regex sources of two redaction specs; `undefined` when both are empty. */
function mergeRedaction(a?: Redaction, b?: Redaction): Redaction | undefined {
  const headers = [...(a?.headers ?? []), ...(b?.headers ?? [])];
  const patterns = [...(a?.patterns ?? []), ...(b?.patterns ?? [])];
  if (headers.length === 0 && patterns.length === 0) return undefined;
  return {
    ...(headers.length ? { headers } : {}),
    ...(patterns.length ? { patterns } : {}),
  };
}

/**
 * Fold externally-produced results into the runner's results: replace the entry whose
 * id matches a non-run PLACEHOLDER (a `blocked`/`skipped` case, typically an
 * extension case) verbatim, and append any id the plan does not contain so it is
 * surfaced honestly rather than dropped. A real verdict Heimdall produced is NEVER
 * overwritten — that would fabricate a green over a genuine fail — only ignored with
 * a warning. The external status/evidence is otherwise kept exactly.
 */
export function mergeExternalResults(results: Result[], external?: Result[]): Result[] {
  if (!external || external.length === 0) return results;
  const indexById = new Map(results.map((r, i) => [r.id, i]));
  const merged = [...results];
  for (const ext of external) {
    const idx = indexById.get(ext.id);
    if (idx === undefined) {
      // A case Heimdall never planned (e.g. an extension-only case) — add it.
      merged.push(ext);
    } else if (merged[idx]!.status === "blocked" || merged[idx]!.status === "skipped") {
      // Only a non-run PLACEHOLDER may be filled by an externally-driven result.
      merged[idx] = ext;
    } else {
      // Never let an external file overwrite a verdict Heimdall actually produced —
      // that would fabricate a green over a real fail/error and corrupt the summary.
      log.warn(
        `--merge-results: ignoring external result for "${ext.id}" — it would overwrite a real ${merged[idx]!.status} result (only blocked/skipped placeholders may be merged).`,
      );
    }
  }
  return merged;
}

/** True when the filter matched no cases — the caller should fail loudly, not pass green. */
export function filterMatchedNothing(plan: Plan, opts: Pick<RunOptions, "filter">): boolean {
  if (!opts.filter || opts.filter.length === 0) return false;
  return !plan.cases.some((tc) => matchesFilter(tc, opts.filter));
}

const RISKY = new Set(["destructive", "paid", "prod"]);

function resolveDriver(tc: TestCase, plan: Plan, override?: Driver): Driver {
  return override ?? tc.driver ?? plan.defaultDriver;
}

function matchesFilter(tc: TestCase, filter?: string[]): boolean {
  if (!filter || filter.length === 0) return true;
  return filter.some((f) => tc.id.includes(f) || tc.tags.includes(f));
}

/** Run an array of thunks with a bounded concurrency, preserving order. */
async function pool<T>(items: (() => Promise<T>)[], limit: number): Promise<T[]> {
  const results: T[] = new Array(items.length);
  let next = 0;
  const workers = Array.from({ length: Math.min(limit, items.length) }, async () => {
    while (true) {
      const i = next++;
      if (i >= items.length) return;
      results[i] = await items[i]!();
    }
  });
  await Promise.all(workers);
  return results;
}

function errorResult(tc: TestCase, driver: Driver, reason: string, durationMs = 0): Result {
  return {
    id: tc.id,
    status: "error",
    driver,
    fidelityTier: fidelityForDriver(driver),
    observed: reason,
    failures: [reason],
    evidence: { screenshots: [], consoleErrors: [], responses: [] },
    durationMs,
  };
}

/** Run a single case once: enforce an overall timeout and never throw. */
async function runOnce(
  driver: CaseDriver,
  driverName: Exclude<Driver, "extension">,
  tc: TestCase,
  ctx: RunContext,
  budgetMs: number | undefined,
): Promise<Result> {
  const attempt = (async () => {
    try {
      return await driver.runCase(tc, ctx);
    } catch (e) {
      // A driver should return an error Result, never throw — contain it to this case.
      return errorResult(tc, driverName, `uncaught driver error: ${e instanceof Error ? e.message : String(e)}`);
    }
  })();

  if (!budgetMs) return attempt;

  let timer: ReturnType<typeof setTimeout>;
  const timeout = new Promise<Result>((resolve) => {
    timer = setTimeout(
      () => resolve(errorResult(tc, driverName, `timed out after ${budgetMs}ms`, budgetMs)),
      budgetMs,
    );
  });
  return Promise.race([attempt.finally(() => clearTimeout(timer)), timeout]);
}

/** Run a case with retries: retry while fail/error, keep the last attempt's result. */
async function runWithRetries(
  driver: CaseDriver,
  driverName: Exclude<Driver, "extension">,
  tc: TestCase,
  ctx: RunContext,
  opts: RunOptions,
): Promise<Result> {
  const budgetMs = tc.timeoutMs ?? opts.timeoutMs;
  const maxAttempts = 1 + Math.max(0, opts.retries ?? 0);
  let result!: Result;
  let attempt = 0;
  for (attempt = 1; attempt <= maxAttempts; attempt++) {
    result = await runOnce(driver, driverName, tc, ctx, budgetMs);
    if (result.status === "pass" || result.status === "blocked") break;
  }
  if (maxAttempts > 1) result.attempts = Math.min(attempt, maxAttempts);
  return result;
}

function blocked(tc: TestCase, driver: Driver, reason: string): Result {
  return {
    id: tc.id,
    status: "blocked",
    driver,
    fidelityTier: fidelityForDriver(driver),
    observed: reason,
    failures: [],
    evidence: { screenshots: [], consoleErrors: [], responses: [] },
    durationMs: 0,
    notes: reason,
  };
}

/**
 * Run a plan-level hook (Plan.setup / Plan.teardown) ONCE in a throwaway Chromium
 * context, reusing the shared step interpreter. Returns the first step's error, or
 * undefined on success. Honours the same baseUrl / storageState / TLS gating as a
 * case; the context is always torn down. Never throws — failures come back as a string.
 */
async function runPlanHook(steps: Step[], ctx: RunContext, label: string): Promise<string | undefined> {
  let browser;
  try {
    browser = await chromium.launch({ headless: !ctx.headed });
    const context = await browser.newContext({
      baseURL: ctx.baseUrl,
      storageState: ctx.storageState,
      ignoreHTTPSErrors: ctx.insecureTLS ?? false,
    });
    try {
      const page = await context.newPage();
      const { error } = await runHookSteps(steps, page, ctx.baseUrl);
      return error;
    } finally {
      await context.close().catch(() => {});
    }
  } catch (e) {
    return `${label}: ${e instanceof Error ? e.message : String(e)}`;
  } finally {
    await browser?.close().catch(() => {});
  }
}

export async function runPlan(plan: Plan, opts: RunOptions): Promise<RunReport> {
  const startedAt = new Date().toISOString();
  const start = Date.now();
  await mkdir(opts.outDir, { recursive: true });

  // Secret redaction is scoped to THIS run: clear any ${env.*} values registered by
  // a previous runPlan in the same process (e.g. a long-lived MCP server or the
  // live-test embedder) so redaction never depends on prior-call order and the
  // registry cannot grow unbounded across runs.
  clearSecrets();

  // Resolve the redaction spec once: the plan's spec merged with the config/CLI one.
  // Threaded onto the context so the cdp driver scrubs the raw HAR after context close,
  // and applied to the final report below. Undefined => no extra redaction (legacy path).
  const redaction = mergeRedaction(plan.redaction, opts.redaction);

  const storageState = opts.storageState ?? plan.storageState;
  const ctx: RunContext & { redaction?: Redaction } = {
    outDir: opts.outDir,
    baseUrl: opts.baseUrl ?? plan.baseUrl,
    storageState,
    allowRisk: opts.allowRisk,
    headed: opts.headed,
    // Never disable TLS validation while injecting live credentials (MITM → leaked session).
    insecureTLS: Boolean(opts.insecureTLS) && !storageState,
    trace: opts.trace ?? "off",
    video: opts.video ?? "off",
    redaction,
  };
  if (opts.insecureTLS && storageState) {
    log.warn("--insecure ignored: refusing to disable TLS validation while a storageState session is injected.");
  }

  // Plan each case: where it runs, and whether it can run at all.
  type Planned = { tc: TestCase; driver: Driver; runnable: boolean; blockReason?: string };
  const planned: Planned[] = plan.cases
    .filter((tc) => matchesFilter(tc, opts.filter))
    .map((tc) => {
      const driver = resolveDriver(tc, plan, opts.driverOverride);
      if (driver === "extension") {
        return {
          tc,
          driver,
          runnable: false,
          blockReason:
            "driver=extension: Heimdall cannot drive the real-Chrome extension; run this case via the agent's browser tools (see live-test skill).",
        };
      }
      if (RISKY.has(tc.risk) && !opts.allowRisk) {
        return {
          tc,
          driver,
          runnable: false,
          blockReason: `risk=${tc.risk}: blocked unless --allow-risk is set (and confirmed by a human).`,
        };
      }
      return { tc, driver, runnable: true };
    });

  const results: Result[] = [];

  // Pre-block the non-runnable cases.
  for (const p of planned.filter((p) => !p.runnable)) {
    results.push(blocked(p.tc, p.driver, p.blockReason!));
    log.warn(`${p.tc.id}: ${p.blockReason}`);
  }

  let runnable = planned.filter((p) => p.runnable);

  // Plan-level setup runs ONCE before any case — but only when something would
  // actually run (a fully-blocked plan seeds nothing). A setup failure blocks
  // every runnable case with the reason, so nothing silently passes on bad state.
  //
  // By design, plan hooks are TRUSTED, author-controlled fixtures and run UNGATED:
  // unlike cases, they are not subject to the RISKY/--allow-risk gate (a hook has
  // no per-step risk field). Authors must keep destructive ops out of plan
  // setup/teardown unless they intend them to run unconditionally (documented on
  // Plan.setup/teardown in schema.ts and in the README's Config & secrets section).
  const hadRunnable = runnable.length > 0;
  if (plan.setup && plan.setup.length > 0 && hadRunnable) {
    log.info(c.cyan("▶ plan setup") + c.dim(` — ${plan.setup.length} step(s)`));
    const setupError = await runPlanHook(plan.setup, ctx, "plan setup");
    if (setupError) {
      // A hook error string can embed a resolved ${env.*} secret (e.g. a Playwright
      // error quoting the request URL); redact before it reaches stderr, matching
      // the report.json redaction so the terminal-scrub promise holds on every path.
      const reason = redactString(`plan setup failed: ${setupError}`);
      log.err(reason);
      for (const p of runnable) {
        results.push(blocked(p.tc, p.driver, reason));
        log.warn(`${p.tc.id}: ${reason}`);
      }
      runnable = [];
    }
  }

  // Group runnable cases by driver so each driver sets up once.
  const byDriver = new Map<Exclude<Driver, "extension">, TestCase[]>();
  for (const p of runnable) {
    const key = p.driver as Exclude<Driver, "extension">;
    (byDriver.get(key) ?? byDriver.set(key, []).get(key)!).push(p.tc);
  }

  for (const [driverName, cases] of byDriver) {
    const driver: CaseDriver = driverName === "container" ? new ContainerDriver() : new CdpDriver();
    log.info(c.cyan(`▶ ${driverName}`) + c.dim(` — ${cases.length} case(s), concurrency ${opts.concurrency}`));
    try {
      await driver.setup(ctx);
    } catch (e) {
      const reason = e instanceof Error ? e.message : String(e);
      log.err(`${driverName} setup failed: ${reason}`);
      for (const tc of cases) {
        results.push({
          id: tc.id,
          status: "error",
          driver: driverName,
          fidelityTier: fidelityForDriver(driverName),
          observed: `driver setup failed: ${reason}`,
          failures: [reason],
          evidence: { screenshots: [], consoleErrors: [], responses: [] },
          durationMs: 0,
        });
      }
      continue;
    }

    const ran = await pool(
      cases.map((tc) => async () => {
        const r = await runWithRetries(driver, driverName, tc, ctx, opts);
        const mark =
          r.status === "pass" ? c.green("PASS") : r.status === "fail" ? c.red("FAIL") : c.yellow(r.status.toUpperCase());
        const retried = r.attempts && r.attempts > 1 ? c.dim(` ×${r.attempts}`) : "";
        log.info(`  ${mark} ${c.bold(tc.id)}${retried} ${c.dim(`(${r.durationMs}ms)`)}`);
        return r;
      }),
      opts.concurrency,
    );
    results.push(...ran);
    await driver.teardown();
  }

  // Plan-level teardown runs ONCE after every case as best-effort cleanup. It is
  // skipped for a plan that never ran anything (nothing to clean), and a failure
  // here is logged but never fatal — the report already reflects the real run.
  if (plan.teardown && plan.teardown.length > 0 && hadRunnable) {
    log.info(c.cyan("▶ plan teardown") + c.dim(` — ${plan.teardown.length} step(s)`));
    const teardownError = await runPlanHook(plan.teardown, ctx, "plan teardown");
    if (teardownError)
      log.warn(redactString(`plan teardown (best-effort) did not fully complete: ${teardownError}`));
  }

  // Fold in any externally-produced results (e.g. extension cases run via the agent's
  // browser tools) BEFORE ordering/summary so the report - and exitCodeFor - reflects
  // merged truth, not the pre-blocked placeholders.
  const finalResults = mergeExternalResults(results, opts.externalResults);

  // Keep report order aligned to the plan order; ids the plan does not contain (extra
  // external results) trail the plan cases rather than jumping to the front.
  const order = new Map(plan.cases.map((tc, i) => [tc.id, i]));
  finalResults.sort((a, b) => (order.get(a.id) ?? plan.cases.length) - (order.get(b.id) ?? plan.cases.length));

  const summary = {
    total: finalResults.length,
    pass: finalResults.filter((r) => r.status === "pass").length,
    fail: finalResults.filter((r) => r.status === "fail").length,
    blocked: finalResults.filter((r) => r.status === "blocked").length,
    skipped: finalResults.filter((r) => r.status === "skipped").length,
    error: finalResults.filter((r) => r.status === "error").length,
  };

  const rawReport: RunReport = {
    plan: plan.name,
    heimdallVersion: VERSION,
    startedAt,
    finishedAt: new Date().toISOString(),
    durationMs: Date.now() - start,
    summary,
    results: finalResults,
  };

  // Scrub any env-resolved secret (e.g. a `${env.TOKEN}` spliced into a URL or an
  // error message) before the report is persisted, returned, or rendered - every
  // downstream consumer (report.json, --json, html, junit, formatReport, --diff)
  // sees the redacted copy. With a resolved redaction spec this ALSO blanks the spec's
  // header values + regex matches; with none it is byte-identical to a redactDeep run.
  // The on-disk network.har is scrubbed with this spec in the driver via scrubHar
  // (cdp directly; container via the threaded sub-plan). The binary trace.zip/video
  // are NOT scrubbed - treat the run's output dir as sensitive. See redact.ts.
  const report = redactWithSpec(rawReport, redaction);

  await writeFile(join(opts.outDir, "report.json"), JSON.stringify(report, null, 2), "utf8");
  return report;
}

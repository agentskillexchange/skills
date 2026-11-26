import { readFile } from "node:fs/promises";
import { join, resolve } from "node:path";
import type { Command } from "commander";
import { Plan, Driver, type Result, type RunReport, type TestCase } from "../schema.js";
import { collectPlanErrors, validateCasesIndividually } from "./validate.js";
import { runPlan, filterMatchedNothing } from "../runner.js";
import { formatReport, exitCodeFor, type CaseMeta, type ReportFormatOptions } from "../reporter.js";
import { writeHtmlReport } from "../reporters/html.js";
import { writeJUnitReport, type JUnitOptions } from "../reporters/junit.js";
import { diffReports, formatDiff, writeDiffReport } from "../reporters/diff.js";
import { loadConfig } from "../config.js";
import { log, setVerbose, c } from "../log.js";

export interface RunCmdOpts {
  driver?: string;
  out: string;
  baseUrl?: string;
  storageState?: string;
  concurrency: string;
  retries?: string;
  timeout?: string;
  allowRisk?: boolean;
  headed?: boolean;
  insecure?: boolean;
  trace?: "off" | "on" | "on-failure";
  video?: "off" | "on" | "on-failure";
  html?: string | boolean;
  junit?: string;
  groupBy?: "tag" | "dimension";
  diff?: string;
  config?: string;
  filter?: string[];
  json?: boolean;
  verbose?: boolean;
  lenient?: boolean;
  /**
   * Externally-produced results (e.g. `driver: extension` cases run via the agent's
   * real-Chrome tools) loaded from `--merge-results <file>` and folded into the
   * report by the runner — a matching (blocked) id is REPLACED verbatim, never
   * fabricated green. Loaded/validated by the CLI before dispatch.
   */
  externalResults?: Result[];
}

/**
 * Resolve a run-level numeric (concurrency/retries) honouring CLI > config > builtin.
 *
 * `cliAtDefault` must come from commander's `getOptionValueSource(name) === "default"`:
 * an EXPLICIT flag that happens to equal the builtin default (e.g. `--concurrency 4`,
 * `--retries 0`) is still a user choice and must beat config — a literal-string
 * comparison (`opts.concurrency === "4"`) cannot tell the two apart and would let
 * config override an explicitly-passed default, violating CLI > config precedence.
 */
export function resolveRunNumber(
  cliValue: string | undefined,
  cliAtDefault: boolean,
  configValue: number | undefined,
  min: number,
): number {
  const raw = cliAtDefault && configValue !== undefined ? configValue : cliValue;
  const parsed = typeof raw === "number" ? raw : Number.parseInt(raw ?? "", 10);
  return Math.max(min, Number.isFinite(parsed) ? parsed : min);
}

/** Build a per-case tags/dimension map keyed by case id, for report grouping. */
function metaFor(cases: TestCase[]): Record<string, CaseMeta> {
  const meta: Record<string, CaseMeta> = {};
  for (const tc of cases) meta[tc.id] = { tags: tc.tags, dimension: tc.dimension };
  return meta;
}

export async function runCommand(planPath: string, opts: RunCmdOpts, command?: Command): Promise<void> {
  setVerbose(Boolean(opts.verbose));

  // Load optional config FIRST: it seeds process.env (so plan `${env.NAME}` tokens
  // resolve) and supplies run-level defaults. Precedence is CLI > plan > config, so
  // config only fills a value the CLI flag (and, in runPlan, the plan) left unset.
  const config = loadConfig(opts.config ?? "heimdall.config.json");

  // Validate --driver up front: a typo must not silently fall through to cdp, and
  // extension cannot be forced (those cases are agent-driven, not Heimdall-driven).
  let driverOverride: Driver | undefined;
  if (opts.driver !== undefined) {
    if (opts.driver === "extension") {
      log.err("--driver extension is not runnable by Heimdall (extension cases are agent-driven); use cdp or container.");
      process.exitCode = 2;
      return;
    }
    const parsed = Driver.safeParse(opts.driver);
    if (!parsed.success) {
      log.err(`unknown --driver "${opts.driver}" — use cdp or container`);
      process.exitCode = 2;
      return;
    }
    driverOverride = parsed.data;
  }

  const raw = await readFile(resolve(planPath), "utf8");
  let parsedJson: unknown;
  try {
    parsedJson = JSON.parse(raw);
  } catch (e) {
    log.err(`could not parse plan JSON: ${e instanceof Error ? e.message : String(e)}`);
    process.exitCode = 2;
    return;
  }

  const errors = collectPlanErrors(parsedJson);
  let plan: Plan;
  if (errors.length === 0) {
    // Fast path: the whole plan is valid; parse it (applies defaults).
    plan = Plan.parse(parsedJson);
  } else if (opts.lenient) {
    // Lenient: salvage the valid cases, skip+warn the invalid ones.
    const checked = validateCasesIndividually(parsedJson);
    const valid = checked.filter((c) => c.errors.length === 0);
    const invalid = checked.filter((c) => c.errors.length > 0);

    for (const cv of invalid) {
      const where = cv.id ? `cases[${cv.index}] (id=${cv.id})` : `cases[${cv.index}]`;
      log.warn(`skipping invalid case ${where}: ${cv.errors.join("; ")}`);
    }

    if (valid.length === 0) {
      log.err(`--lenient: all ${checked.length} case(s) are invalid — nothing to run`);
      process.exitCode = 2;
      return;
    }

    // Rebuild a plan from only the valid raw cases. Reuse the plan wrapper's own
    // fields but substitute the salvaged cases; re-parse so defaults still apply.
    const wrapper = parsedJson !== null && typeof parsedJson === "object" ? (parsedJson as Record<string, unknown>) : {};
    const leniently = Plan.safeParse({ ...wrapper, cases: valid.map((c) => c.raw) });
    if (!leniently.success) {
      // Plan-level (non-case) problems remain even after salvaging cases.
      log.err("--lenient: plan is invalid beyond its cases:");
      for (const line of collectPlanErrors({ ...wrapper, cases: valid.map((c) => c.raw) })) {
        log.info(c.red("  • ") + line);
      }
      process.exitCode = 2;
      return;
    }
    plan = leniently.data;
    log.warn(`--lenient: running ${valid.length} valid case(s), skipped ${invalid.length}`);
  } else {
    log.err(`invalid plan — ${errors.length} problem${errors.length === 1 ? "" : "s"} (use --lenient to run the valid cases):`);
    for (const line of errors) log.info(c.red("  • ") + line);
    process.exitCode = 2;
    return;
  }

  // Fold config defaults into the plan where the plan left them unset, so the final
  // precedence is CLI > plan > config: the CLI flags below still beat the plan, and
  // the plan still beats config (config only fills a hole the plan author left open).
  const rawPlan = parsedJson !== null && typeof parsedJson === "object" ? (parsedJson as Record<string, unknown>) : {};
  if (plan.baseUrl === undefined && config.baseUrl !== undefined) plan.baseUrl = config.baseUrl;
  if (plan.storageState === undefined && config.storageState !== undefined) plan.storageState = config.storageState;
  // plan.defaultDriver is always populated by Zod's default; only honour the config
  // value when the plan JSON did not declare its own defaultDriver.
  if (rawPlan.defaultDriver === undefined && config.defaultDriver !== undefined) {
    plan.defaultDriver = config.defaultDriver;
  }

  // A typo'd --filter must fail loudly, not "pass" having tested nothing.
  if (filterMatchedNothing(plan, { filter: opts.filter })) {
    log.err(`--filter ${(opts.filter ?? []).join(", ")} matched no cases in the plan`);
    process.exitCode = 2;
    return;
  }

  const outDir = resolve(opts.out);
  // Concurrency/retries are run-level (no plan field). A config value only fills in
  // when the CLI flag is STILL AT ITS COMMANDER DEFAULT (source === "default"); an
  // explicitly-passed flag — even one equal to the default — beats config. We ask
  // commander for the value's source rather than string-comparing against "4"/"0".
  const concAtDefault = command?.getOptionValueSource("concurrency") === "default";
  const retriesAtDefault = command?.getOptionValueSource("retries") === "default";
  const concurrency = resolveRunNumber(opts.concurrency, concAtDefault, config.concurrency, 1);
  const retries = resolveRunNumber(opts.retries, retriesAtDefault, config.retries, 0);
  const timeoutMs = opts.timeout ? Math.max(0, Number.parseInt(opts.timeout, 10) || 0) || undefined : undefined;
  const report = await runPlan(plan, {
    outDir,
    baseUrl: opts.baseUrl,
    storageState: opts.storageState ? resolve(opts.storageState) : undefined,
    allowRisk: Boolean(opts.allowRisk),
    headed: Boolean(opts.headed),
    insecureTLS: Boolean(opts.insecure),
    trace: opts.trace ?? "off",
    video: opts.video ?? "off",
    concurrency,
    retries,
    timeoutMs,
    driverOverride,
    filter: opts.filter,
    externalResults: opts.externalResults,
    // Extra redaction declared in heimdall.config.json: runPlan folds it with the
    // plan's own `redaction` via mergeRedaction, so config-level header/pattern
    // scrubbing reaches the report AND the HAR (not just plan-level redaction).
    redaction: config.redaction,
  });

  // Report grouping options (group-by + the always-on blocked panel) are threaded
  // into every renderer. `meta` carries the tags/dimension the report itself omits.
  const reportOpts: ReportFormatOptions | undefined = opts.groupBy
    ? { groupBy: opts.groupBy, meta: metaFor(plan.cases), blocked: true }
    : undefined;

  // Optional extra report formats.
  if (opts.html) {
    const htmlPath = typeof opts.html === "string" ? resolve(opts.html) : join(outDir, "report.html");
    await writeHtmlReport(report, htmlPath, reportOpts);
    log.info(c.dim(`html: ${htmlPath}`));
  }
  if (opts.junit) {
    const junitPath = resolve(opts.junit);
    const junitOpts: JUnitOptions | undefined = opts.groupBy
      ? { classnameBy: opts.groupBy, meta: metaFor(plan.cases) }
      : undefined;
    await writeJUnitReport(report, junitPath, junitOpts);
    log.info(c.dim(`junit: ${junitPath}`));
  }

  if (opts.json) {
    process.stdout.write(JSON.stringify(report, null, 2) + "\n");
  } else {
    process.stderr.write(formatReport(report, outDir, reportOpts) + "\n");
  }

  // Optional regression diff against a previous run's report.json, printed to stderr.
  if (opts.diff) {
    try {
      const prev = JSON.parse(await readFile(resolve(opts.diff), "utf8")) as RunReport;
      const regression = diffReports(prev, report);
      process.stderr.write("\n" + formatDiff(regression) + "\n");
      // Persist the machine-readable diff next to the report for CI/tooling.
      const diffPath = join(outDir, "diff.json");
      await writeDiffReport(regression, diffPath);
      log.info(c.dim(`diff: ${diffPath}`));
    } catch (e) {
      log.warn(`--diff: could not read previous report ${opts.diff}: ${e instanceof Error ? e.message : String(e)}`);
    }
  }

  process.exitCode = exitCodeFor(report);
}

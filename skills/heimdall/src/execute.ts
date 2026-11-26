/**
 * Step interpreter: drives a single case's steps against a Playwright Page,
 * builds an {@link Observation}, and evaluates the case's oracles.
 *
 * Shared by the `cdp` driver and (inside the container image) the `container`
 * driver — both ultimately drive a real Chromium page, so the logic is identical.
 */
import { existsSync } from "node:fs";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";
import type { Page, Response } from "playwright";
import type { CapturedResponse, Oracle, Step, TestCase } from "./schema.js";
import {
  evaluateOracles,
  getByPath,
  type Observation,
  type ObservedResponse,
  type OracleRecord,
} from "./oracle.js";
import { runAxe } from "./a11y.js";
import { comparePng } from "./visualDiff.js";
import { formatLoadStats, modalStatus, runConcurrent, summarizeLoad, type LoadSample } from "./load.js";
import { registerSecret } from "./redact.js";
import { log } from "./log.js";

export interface ExecOutcome {
  status: "pass" | "fail";
  observed: string;
  failures: string[];
  screenshots: string[];
  consoleErrors: string[];
  responses: CapturedResponse[];
  /** One record per oracle (pass AND fail), in evaluation order; `[]` when the case has no oracles. */
  oracleResults: OracleRecord[];
  /** Best-effort teardown trouble, surfaced without flipping the verdict. */
  notes?: string;
}

function resolveUrl(url: string, baseUrl: string | undefined): string {
  if (/^https?:\/\//i.test(url)) return url;
  if (!baseUrl) throw new Error(`relative url "${url}" but no baseUrl is set (plan.baseUrl / --base-url)`);
  return new URL(url, baseUrl).toString();
}

function tryParseJson(text: string): unknown {
  try {
    return JSON.parse(text);
  } catch {
    return undefined;
  }
}

/**
 * Substitute `${name}` tokens with values from the per-case variable map.
 *
 * A token whose name begins with `env.` (e.g. `${env.API_TOKEN}`) resolves from
 * `process.env` at runtime instead of the capture bag — this is how a plan injects
 * secrets via the environment rather than inlining them. Unknown env vars resolve
 * to an empty string (never crash, never leak the literal token). All other tokens
 * keep the existing behavior: known capture vars are substituted, unknown tokens
 * are left verbatim. The function is a no-op when there is no `${...}` present, so
 * all existing (token-free) plans are unaffected. NB: `env.*` is a RESERVED token
 * namespace — a `${env.NAME}` token always reads `process.env`, so a capture var
 * literally named `env.something` is shadowed and cannot be referenced this way.
 *
 * Secret hygiene (honest scope): each env-resolved value is registered with the
 * {@link registerSecret} redactor so it is scrubbed from the serialized report
 * (`responses[].url`, `failures[]`, `observed`) and every rendered report — even
 * when a secret is spliced into a request URL. It is NOT scrubbed from the binary
 * Playwright evidence files (HAR retains request headers/URLs; trace.zip likewise);
 * those, like an injected storageState, are secret-bearing — treat the run's output
 * directory as sensitive. See {@link import("./redact.js")}.
 */
export function applyVars(str: string, vars: Record<string, string>): string {
  if (!str.includes("${")) return str;
  // `[\w.]+` admits the dotted `env.NAME` form; bare `${name}` tokens are unchanged.
  return str.replace(/\$\{([\w.]+)\}/g, (whole, name: string) => {
    if (name.startsWith("env.")) {
      const value = process.env[name.slice(4)] ?? "";
      registerSecret(value); // track for report redaction; trivial/empty values are ignored
      return value;
    }
    return Object.prototype.hasOwnProperty.call(vars, name) ? vars[name]! : whole;
  });
}

/** Template every value of a headers record; undefined passes through untouched. */
function applyVarsHeaders(
  headers: Record<string, string> | undefined,
  vars: Record<string, string>,
): Record<string, string> | undefined {
  if (!headers) return undefined;
  const out: Record<string, string> = {};
  for (const [k, v] of Object.entries(headers)) out[k] = applyVars(v, vars);
  return out;
}

/** Apply a step's `capture` spec to its observed response, writing into store.vars. */
function applyCapture(
  capture: Record<string, { jsonPath?: string; header?: string }> | undefined,
  observed: ObservedResponse,
  vars: Record<string, string>,
): void {
  if (!capture) return;
  for (const [name, spec] of Object.entries(capture)) {
    vars[name] = spec.jsonPath
      ? String(getByPath(observed.json, spec.jsonPath))
      : spec.header
        ? (observed.headers[spec.header.toLowerCase()] ?? "")
        : "";
  }
}

/** Execute one case on an already-created page; returns evidence + pass/fail. */
export async function executeCase(
  tc: TestCase,
  page: Page,
  opts: { caseDir: string; baseUrl: string | undefined },
): Promise<ExecOutcome> {
  const consoleErrors: string[] = [];
  const responses: CapturedResponse[] = [];
  const named: Record<string, ObservedResponse> = {};
  const vars: Record<string, string> = {};
  let last: ObservedResponse | undefined;
  const screenshots: string[] = [];
  const failures: string[] = [];

  page.on("console", (msg) => {
    if (msg.type() === "error") consoleErrors.push(msg.text());
  });
  page.on("pageerror", (err) => consoleErrors.push(String(err)));

  // All responses seen, so waitForResponse can match ones that already arrived.
  const seenResponses: Response[] = [];
  page.on("response", (r) => seenResponses.push(r));

  const snap = async (name: string) => {
    const file = join(opts.caseDir, `${name}.png`);
    try {
      await page.screenshot({ path: file, fullPage: false });
      screenshots.push(file);
    } catch (e) {
      log.debug(`screenshot "${name}" failed: ${String(e)}`);
    }
  };

  const store = {
    named,
    setLast: (r: ObservedResponse) => (last = r),
    responses,
    seenResponses,
    vars,
  };

  // Run one phase of steps (setup / main / teardown). Returns the first step's
  // error string, or undefined if every step succeeded. The `screenshot` action
  // is handled inline (it writes to the case dir + records evidence); everything
  // else flows through the shared `runStep` interpreter, so hooks may be any step.
  const runPhase = async (steps: Step[], label: string): Promise<string | undefined> => {
    for (const [i, step] of steps.entries()) {
      try {
        if (step.action === "screenshot") {
          // Confined to the case dir + sanitized + recorded as evidence (not cwd).
          const name = (step.name ?? `${label}-${i + 1}`).replace(/[^a-zA-Z0-9_-]/g, "_");
          await snap(name);
        } else {
          await runStep(step, page, opts.baseUrl, store);
        }
      } catch (e) {
        return `${label} step ${i + 1} (${step.action}): ${e instanceof Error ? e.message : String(e)}`;
      }
    }
    return undefined;
  };

  // 1. Per-case setup runs BEFORE the steps on the same page/vars. A failing
  //    setup step means the case never reached a testable state, so we record a
  //    clear failure and skip both the steps and the oracles (but still teardown).
  let setupError: string | undefined;
  if (tc.setup && tc.setup.length > 0) {
    setupError = await runPhase(tc.setup, "setup");
    if (setupError) failures.push(setupError);
  }

  // 2. The case's own steps — only when setup got us into a testable state.
  let stepError: string | undefined;
  if (!setupError) {
    stepError = await runPhase(tc.steps, "step");
    if (stepError) failures.push(stepError);
  }

  // Always capture a final screenshot as evidence (UI cases especially).
  await snap("final");

  // Capture the page (or a single selector) AT MOST ONCE per selector for the life of
  // this case. The `screenshotMatches` oracle and the baseline/diff persist step both
  // shoot the same selector with no page mutation in between, so without this memo each
  // such oracle pays for two real Playwright captures (a browser round-trip + PNG encode)
  // — the dominant cost. Keyed by selector ("" = full page); the cached Promise is shared.
  const shotCache = new Map<string, Promise<Buffer>>();
  const captureShot = (selector?: string): Promise<Buffer> => {
    const key = selector ?? "";
    let pending = shotCache.get(key);
    if (!pending) {
      pending = selector
        ? page.locator(selector).first().screenshot()
        : page.screenshot({ fullPage: false });
      shotCache.set(key, pending);
    }
    return pending;
  };

  const obs: Observation = {
    url: () => page.url(),
    title: () => page.title().catch(() => ""),
    isVisible: async (selector) => {
      try {
        return await page.locator(selector).first().isVisible();
      } catch {
        return false;
      }
    },
    textOf: async (selector) => {
      try {
        return await page.locator(selector).first().textContent();
      } catch {
        return null;
      }
    },
    count: async (selector) => {
      try {
        return await page.locator(selector).count();
      } catch {
        return 0;
      }
    },
    attribute: async (selector, name) => {
      try {
        return await page.locator(selector).first().getAttribute(name);
      } catch {
        return null;
      }
    },
    consoleErrors: () => consoleErrors,
    response: (name) => (name ? named[name] : last),
    evaluate: (expression) => page.evaluate(expression),
    // Inject axe-core into the live page and run the audit; the `a11y` oracle filters.
    axe: (options) => runAxe(page, options),
    // Capture a PNG of the page (or a single selector) for the `screenshotMatches` oracle.
    // Memoized per selector so the verdict and the baseline/diff persist share one capture.
    screenshot: captureShot,
  };

  // 3. Oracles — skipped when setup never established the state under test
  //    (the setup failure already condemns the case; re-running oracles would
  //    just pile on noise about a state that was never reached).
  let oraclePassed = false;
  let oracleResults: OracleRecord[] = [];
  if (!setupError) {
    const oracleOutcome = await evaluateOracles(tc.oracle, obs);
    failures.push(...oracleOutcome.failures);
    oraclePassed = oracleOutcome.passed;
    oracleResults = oracleOutcome.records;
    // Visual-regression evidence (#13): persist a missing baseline as the current
    // capture, and write a highlighted diff PNG into the case dir on subsequent runs.
    // The oracle owns the pass/fail verdict; the file writes live here in the driver.
    await persistVisualBaselines(tc.oracle, obs, opts.caseDir, screenshots);
  }

  const passed = !setupError && !stepError && oraclePassed;

  // 4. Teardown is best-effort cleanup: it ALWAYS runs (even on failure, even on
  //    a failed setup that may have half-created a resource), shares the case's
  //    page + captured ${vars} so it can delete what setup created, and NEVER
  //    flips the verdict — a teardown failure is surfaced as a note, not a failure.
  let notes: string | undefined;
  if (tc.teardown && tc.teardown.length > 0) {
    const teardownError = await runPhase(tc.teardown, "teardown");
    if (teardownError) notes = `teardown (best-effort) did not fully complete: ${teardownError}`;
  }

  const observed =
    (passed
      ? `all ${tc.oracle.length} oracle(s) satisfied at ${page.url()}`
      : `${failures.length} failure(s): ${failures.slice(0, 3).join("; ")}`) + (notes ? ` — ${notes}` : "");

  return {
    status: passed ? "pass" : "fail",
    observed,
    failures,
    screenshots,
    consoleErrors,
    responses,
    oracleResults,
    notes,
  };
}

/**
 * Side-effecting companion to the (pure) `screenshotMatches` oracle: for each such
 * oracle, capture the page/selector once more and either seed a missing baseline
 * (first run) or write a highlighted diff PNG into the case evidence dir. A bad
 * baseline path or a dimension mismatch is swallowed — the oracle has already
 * rendered the verdict, so persistence must never crash or flip the case.
 */
async function persistVisualBaselines(
  oracles: Oracle[],
  obs: Observation,
  caseDir: string,
  screenshots: string[],
): Promise<void> {
  for (const [i, o] of oracles.entries()) {
    if (o.assert !== "screenshotMatches") continue;
    try {
      const current = await obs.screenshot(o.selector);
      if (!existsSync(o.baseline)) {
        await writeFile(o.baseline, current); // first run: the current capture becomes the baseline
        continue;
      }
      const baseline = await readFile(o.baseline);
      const { diffBuffer } = comparePng(baseline, current);
      const diffPath = join(caseDir, `screenshot-diff-${i + 1}.png`);
      await writeFile(diffPath, diffBuffer);
      screenshots.push(diffPath);
    } catch (e) {
      log.debug(`screenshot baseline/diff for oracle ${i + 1} failed: ${String(e)}`);
    }
  }
}

/**
 * Run plan-level hook steps (Plan.setup / Plan.teardown) against a throwaway page,
 * reusing the very same {@link runStep} interpreter as cases. Hooks have no oracles
 * — they exist purely for their side effects (seed or clean shared state) — so this
 * just returns the first step's error string, or undefined if all of them passed.
 */
export async function runHookSteps(
  steps: Step[],
  page: Page,
  baseUrl: string | undefined,
): Promise<{ error?: string }> {
  const responses: CapturedResponse[] = [];
  const named: Record<string, ObservedResponse> = {};
  const vars: Record<string, string> = {};
  const seenResponses: Response[] = [];
  page.on("response", (r) => seenResponses.push(r));
  // setLast is a no-op here: plan hooks have no oracles, but captures + ${var}
  // templating still work across a hook's own step chain (named/vars are live).
  const store = { named, setLast: () => {}, responses, seenResponses, vars };
  for (const [i, step] of steps.entries()) {
    // Hooks are side-effect only; there is no per-case evidence dir to snap into.
    if (step.action === "screenshot") continue;
    try {
      await runStep(step, page, baseUrl, store);
    } catch (e) {
      return { error: `hook step ${i + 1} (${step.action}): ${e instanceof Error ? e.message : String(e)}` };
    }
  }
  return {};
}

async function runStep(
  step: Step,
  page: Page,
  baseUrl: string | undefined,
  store: {
    named: Record<string, ObservedResponse>;
    setLast: (r: ObservedResponse) => void;
    responses: CapturedResponse[];
    seenResponses: Response[];
    /** Per-case variable map for `capture` writes and `${name}` templating. */
    vars: Record<string, string>;
  },
): Promise<void> {
  switch (step.action) {
    case "goto":
      await page.goto(resolveUrl(applyVars(step.url, store.vars), baseUrl), { waitUntil: step.waitUntil ?? "load" });
      return;
    case "click":
      await page.locator(step.selector).first().click();
      return;
    case "fill":
      await page.locator(step.selector).first().fill(step.value);
      return;
    case "select":
      await page.locator(step.selector).first().selectOption(step.value);
      return;
    case "hover":
      await page.locator(step.selector).first().hover();
      return;
    case "check":
      await page.locator(step.selector).first().check();
      return;
    case "uncheck":
      await page.locator(step.selector).first().uncheck();
      return;
    case "setViewport":
      await page.setViewportSize({ width: step.width, height: step.height });
      return;
    case "press":
      if (step.selector) await page.locator(step.selector).first().press(step.key);
      else await page.keyboard.press(step.key);
      return;
    case "waitFor":
      if (step.selector) {
        await page.locator(step.selector).first().waitFor({
          state: step.state ?? "visible",
          timeout: step.timeoutMs,
        });
      } else {
        await page.waitForLoadState("networkidle");
      }
      return;
    case "wait":
      await page.waitForTimeout(step.ms);
      return;
    case "screenshot":
      // Handled in executeCase's loop via snap() (writes to the case dir + records
      // evidence); kept here only for switch exhaustiveness.
      return;
    case "eval":
      await page.evaluate(step.expression);
      return;
    case "sse": {
      const url = resolveUrl(applyVars(step.url, store.vars), baseUrl);
      // EventSource is governed by the page's origin (same-origin / CORS), so a
      // stream-only case sitting on about:blank can't open it — land on the
      // target's origin first, exactly like the `fetch` step does.
      if (page.url() === "about:blank") {
        try {
          await page.goto(new URL(url).origin, { waitUntil: "domcontentloaded" });
        } catch {
          /* best effort — the EventSource below will surface a real failure if it mattered */
        }
      }
      const timeoutMs = step.timeoutMs ?? 10000;
      const t0 = Date.now();
      const events = (await page.evaluate(
        (args: { url: string; maxEvents?: number; timeoutMs: number; closeAfterMs?: number }) =>
          new Promise<Array<{ event: string; data: string; id: string }>>((resolve) => {
            const collected: Array<{ event: string; data: string; id: string }> = [];
            const es = new EventSource(args.url, { withCredentials: true });
            const timers: ReturnType<typeof setTimeout>[] = [];
            let done = false;
            const finish = () => {
              if (done) return;
              done = true;
              for (const t of timers) clearTimeout(t); // don't leave timers pending after early finish
              try {
                es.close();
              } catch {
                /* already closing */
              }
              resolve(collected);
            };
            es.onmessage = (ev: MessageEvent) => {
              collected.push({ event: "message", data: String(ev.data), id: String(ev.lastEventId ?? "") });
              if (args.maxEvents !== undefined && collected.length >= args.maxEvents) finish();
            };
            // The server ending the stream surfaces as an error (EventSource would
            // otherwise reconnect and re-collect); once we have events, that's done.
            es.onerror = () => {
              if (collected.length > 0) finish();
            };
            timers.push(setTimeout(finish, args.timeoutMs));
            if (args.closeAfterMs !== undefined) timers.push(setTimeout(finish, args.closeAfterMs));
          }),
        { url, maxEvents: step.events, timeoutMs, closeAfterMs: step.closeAfterMs },
      )) as Array<{ event: string; data: string; id: string }>;
      const durationMs = Date.now() - t0;
      const bodyText = events.map((e) => e.data).join("\n");
      const status = events.length > 0 ? 200 : 0;
      const observed: ObservedResponse = {
        name: step.as,
        url,
        method: "GET",
        status,
        ok: events.length > 0,
        headers: {},
        bodyText,
        json: events,
        events,
        durationMs,
      };
      store.setLast(observed);
      if (step.as) store.named[step.as] = observed;
      store.responses.push({ name: step.as, url, method: "GET", status });
      return;
    }
    case "waitForResponse": {
      const urlContains = applyVars(step.urlContains, store.vars);
      const matches = (r: Response) => r.url().includes(urlContains);
      // Match a response that already arrived, else wait for a future one.
      const resp = store.seenResponses.find(matches) ?? (await page.waitForResponse(matches, { timeout: step.timeoutMs }));
      const bodyText = await resp.text().catch(() => "");
      const headers = lowerCaseHeaders(await resp.allHeaders().catch(() => resp.headers()));
      let durationMs: number | undefined;
      try {
        const t = resp.request().timing();
        if (t && t.responseEnd >= 0 && t.requestStart >= 0) durationMs = Math.round(t.responseEnd - t.requestStart);
      } catch {
        /* timing unavailable */
      }
      const observed: ObservedResponse = {
        name: step.as,
        url: resp.url(),
        method: resp.request().method(),
        status: resp.status(),
        ok: resp.ok(),
        headers,
        bodyText,
        json: tryParseJson(bodyText),
        durationMs,
      };
      store.setLast(observed);
      if (step.as) store.named[step.as] = observed;
      applyCapture(step.capture, observed, store.vars);
      store.responses.push({
        name: step.as,
        url: resp.url(),
        method: resp.request().method(),
        status: resp.status(),
        headers,
      });
      return;
    }
    case "fetch": {
      const url = resolveUrl(applyVars(step.url, store.vars), baseUrl);
      // An in-page fetch needs a same-origin document; a fetch-only case starts on
      // about:blank (null origin), so a fetch to the API would be cross-origin and
      // CORS-blocked. If we haven't navigated yet, land on the target's origin first.
      if (page.url() === "about:blank") {
        try {
          await page.goto(new URL(url).origin, { waitUntil: "domcontentloaded" });
        } catch {
          /* best effort — the fetch below will surface a real failure if this mattered */
        }
      }
      const t0 = Date.now();
      const result = (await page.evaluate(
        async (args: { url: string; method: string; headers?: Record<string, string>; body?: string }) => {
          const r = await fetch(args.url, {
            method: args.method,
            headers: args.headers,
            body: args.body,
            credentials: "include",
          });
          const bodyText = await r.text();
          const headers: Record<string, string> = {};
          r.headers.forEach((value: string, key: string) => {
            headers[key.toLowerCase()] = value;
          });
          return { url: r.url, status: r.status, ok: r.ok, headers, bodyText };
        },
        {
          url,
          method: step.method ?? "GET",
          headers: applyVarsHeaders(step.headers, store.vars),
          body: step.body === undefined ? undefined : applyVars(step.body, store.vars),
        },
      )) as { url: string; status: number; ok: boolean; headers: Record<string, string>; bodyText: string };
      const durationMs = Date.now() - t0;

      const observed: ObservedResponse = {
        name: step.as,
        url: result.url,
        method: step.method ?? "GET",
        status: result.status,
        ok: result.ok,
        headers: result.headers,
        bodyText: result.bodyText,
        json: tryParseJson(result.bodyText),
        durationMs,
      };
      store.setLast(observed);
      if (step.as) store.named[step.as] = observed;
      applyCapture(step.capture, observed, store.vars);
      store.responses.push({
        name: step.as,
        url: result.url,
        method: step.method ?? "GET",
        status: result.status,
        headers: result.headers,
      });
      return;
    }
    case "request": {
      const url = resolveUrl(applyVars(step.url, store.vars), baseUrl);
      const method = step.method ?? "GET";
      // A browser-context API request: not subject to page CORS and needs no goto.
      const rc = page.context().request;
      const t0 = Date.now();
      // redirect:'manual' returns the raw 3xx with readable headers (location/
      // hx-redirect/...). The in-page `fetch` step cannot do this (opaqueredirect).
      const r = await rc.fetch(url, {
        method,
        headers: applyVarsHeaders(step.headers, store.vars),
        data: step.body === undefined ? undefined : applyVars(step.body, store.vars),
        ...(step.redirect === "manual" ? { maxRedirects: 0 } : {}),
      });
      const durationMs = Date.now() - t0;
      const rawHeaders = await r.headers();
      const headers = lowerCaseHeaders(rawHeaders);
      const bodyText = await r.text().catch(() => "");
      const observed: ObservedResponse = {
        name: step.as,
        url: r.url(),
        method,
        status: r.status(),
        ok: r.ok(),
        headers,
        bodyText,
        json: tryParseJson(bodyText),
        durationMs,
      };
      store.setLast(observed);
      if (step.as) store.named[step.as] = observed;
      applyCapture(step.capture, observed, store.vars);
      store.responses.push({ name: step.as, url: r.url(), method, status: r.status(), headers });
      return;
    }
    case "load": {
      const method = step.method ?? "GET";
      const concurrency = step.concurrency ?? Math.min(step.times, 10);
      const rc = page.context().request;
      // Resolve once up-front: every iteration hits the same target. `${vars}` are
      // already bound by the time this step runs, so this is stable across calls.
      const url = resolveUrl(applyVars(step.url, store.vars), baseUrl);
      const headers = applyVarsHeaders(step.headers, store.vars);
      const data = step.body === undefined ? undefined : applyVars(step.body, store.vars);
      const samples = await runConcurrent<LoadSample>(step.times, concurrency, async () => {
        const t0 = Date.now();
        try {
          const r = await rc.fetch(url, { method, headers, data });
          const sample = { status: r.status(), durationMs: Date.now() - t0, error: !r.ok() };
          // Dispose immediately: a load step exists to drive high `times`, and an
          // undisposed APIResponse keeps its body buffered in the browser process
          // until the context closes — memory would grow O(times × bodySize).
          await r.dispose();
          return sample;
        } catch {
          // A thrown request (DNS/connection/timeout) counts as an error sample.
          return { status: 0, durationMs: Date.now() - t0, error: true };
        }
      });
      const stats = summarizeLoad(samples);
      const status = modalStatus(samples);
      const bodyText = formatLoadStats(stats);
      const observed: ObservedResponse = {
        name: step.as,
        url,
        method,
        status,
        ok: stats.errors === 0,
        headers: {},
        bodyText,
        json: stats,
        durationMs: stats.maxMs,
        load: stats,
      };
      store.setLast(observed);
      if (step.as) store.named[step.as] = observed;
      store.responses.push({ name: step.as, url, method, status });
      return;
    }
    case "pollUntil": {
      const method = step.method ?? "GET";
      const intervalMs = step.intervalMs ?? 1000;
      const timeoutMs = step.timeoutMs ?? 30000;
      const rc = page.context().request;
      const deadline = Date.now() + timeoutMs;
      let lastFailures: string[] = ["pollUntil: never issued a request"];
      let attempts = 0;
      while (true) {
        attempts++;
        const url = resolveUrl(applyVars(step.url, store.vars), baseUrl);
        const t0 = Date.now();
        const r = await rc.fetch(url, {
          method,
          headers: applyVarsHeaders(step.headers, store.vars),
          data: step.body === undefined ? undefined : applyVars(step.body, store.vars),
        });
        const durationMs = Date.now() - t0;
        const headers = lowerCaseHeaders(await r.headers());
        const bodyText = await r.text().catch(() => "");
        const polled: ObservedResponse = {
          name: step.as,
          url: r.url(),
          method,
          status: r.status(),
          ok: r.ok(),
          headers,
          bodyText,
          json: tryParseJson(bodyText),
          durationMs,
        };
        // Poll oracles are response-based; the DOM-shaped Observation members return
        // harmless defaults (a DOM oracle here would simply never pass).
        const obs: Observation = {
          url: () => polled.url,
          title: async () => "",
          isVisible: async () => false,
          textOf: async () => null,
          count: async () => 0,
          attribute: async () => null,
          consoleErrors: () => [],
          response: () => polled,
          evaluate: async () => undefined,
          // pollUntil has no live page to audit/snapshot; a DOM/visual/a11y oracle here
          // fails honestly (mirroring the benign-default DOM members above) rather than
          // pretending a clean page.
          axe: async () => {
            throw new Error("a11y audit unavailable in a pollUntil context (no page)");
          },
          screenshot: async () => {
            throw new Error("screenshot unavailable in a pollUntil context (no page)");
          },
        };
        const outcome = await evaluateOracles(step.oracle as Oracle[], obs);
        if (outcome.passed) {
          store.setLast(polled);
          if (step.as) store.named[step.as] = polled;
          store.responses.push({ name: step.as, url: polled.url, method, status: polled.status, headers });
          return;
        }
        lastFailures = outcome.failures;
        if (Date.now() + intervalMs >= deadline) {
          throw new Error(
            `pollUntil: condition not met after ${attempts} poll(s) / ${timeoutMs}ms — last failures: ${lastFailures.join("; ")}`,
          );
        }
        await page.waitForTimeout(intervalMs);
      }
    }
    case "route": {
      // Install a persistent interception that governs every matching request for
      // the REST of the case (page.route stays active until the context closes).
      const urlContains = applyVars(step.urlContains, store.vars);
      const matches = (u: URL) => u.href.includes(urlContains);
      switch (step.mode) {
        case "block":
        case "abort":
          await page.route(matches, (route) => route.abort());
          return;
        case "fulfill": {
          // A synthetic response demands a status; a fulfill without one is a bad
          // plan, not a silent default — fail loudly at install time.
          if (step.status === undefined) {
            throw new Error(`route fulfill on "${urlContains}" requires a status`);
          }
          const status = step.status;
          await page.route(matches, async (route) => {
            if (step.delayMs !== undefined) await delay(step.delayMs);
            await route.fulfill({ status, body: step.body ?? "", headers: step.headers });
          });
          return;
        }
        case "delay": {
          // Pure latency injection: the real response is unchanged, just slowed.
          if (step.delayMs === undefined) {
            throw new Error(`route delay on "${urlContains}" requires delayMs`);
          }
          const delayMs = step.delayMs;
          await page.route(matches, async (route) => {
            await delay(delayMs);
            await route.continue();
          });
          return;
        }
        default: {
          const _exhaustiveMode: never = step.mode;
          throw new Error(`unknown route mode: ${JSON.stringify(_exhaustiveMode)}`);
        }
      }
    }
    case "race": {
      // Run the nested network steps CONCURRENTLY and wait for all to settle; each
      // registers itself as a (named) response via the shared store, exactly as it
      // would when run on its own. Racing a page-mutating step has no honest meaning
      // (the page is single-threaded), so guard it at runtime too — the schema rejects
      // it at parse time, but a hand-built Plan reaching runPlan must still fail clearly.
      for (const nested of step.steps) {
        if (!RACE_ALLOWED.has(nested.action)) {
          throw new Error(`race only supports request/fetch/load steps — got '${nested.action}'`);
        }
      }
      await Promise.all(step.steps.map((nested) => runStep(nested, page, baseUrl, store)));
      return;
    }
    default: {
      // Exhaustiveness guard: a new Step action added to schema.ts but not wired
      // here becomes a COMPILE error rather than a silent no-op. Unreachable at
      // runtime — Zod's strict discriminated union gates the input first.
      const _exhaustive: never = step;
      throw new Error(`unhandled step action: ${JSON.stringify(_exhaustive)}`);
    }
  }
}

/** Network actions a `race` may nest — mirrors the schema's RACE_ALLOWED guard. */
const RACE_ALLOWED: ReadonlySet<Step["action"]> = new Set(["request", "fetch", "load"]);

/** Promise-based sleep for `route` latency injection (delay / fulfill+delayMs). */
function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/** Lower-case header names for case-insensitive lookup. */
function lowerCaseHeaders(h: Record<string, string>): Record<string, string> {
  const out: Record<string, string> = {};
  for (const [k, v] of Object.entries(h)) out[k.toLowerCase()] = v;
  return out;
}

/** Ensure a per-case evidence directory exists and return its path. */
export async function ensureCaseDir(outDir: string, caseId: string): Promise<string> {
  const dir = join(outDir, "cases", caseId.replace(/[^a-zA-Z0-9_-]/g, "_"));
  await mkdir(dir, { recursive: true });
  return dir;
}

/** Persist a small JSON artifact next to a case's evidence. */
export async function writeJson(path: string, data: unknown): Promise<void> {
  await writeFile(path, JSON.stringify(data, null, 2), "utf8");
}

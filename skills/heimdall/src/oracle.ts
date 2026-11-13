/**
 * Oracle evaluation — the pass/fail decision layer.
 *
 * This is deliberately decoupled from the browser: oracles are evaluated against
 * an {@link Observation}, an interface the driver fulfils. That keeps the
 * decision logic pure and unit-testable without launching Chromium.
 */
import { existsSync } from "node:fs";
import { readFile } from "node:fs/promises";
import type { Oracle, CapturedResponse, LoadStats } from "./schema.js";
import { filterViolations, type AxeResultLike } from "./a11y.js";
import { comparePng } from "./visualDiff.js";

/** A captured HTTP response available to oracles, with parsed body. */
export interface ObservedResponse extends CapturedResponse {
  ok: boolean;
  /** Response headers with lower-cased names for case-insensitive lookup. */
  headers: Record<string, string>;
  bodyText: string;
  json: unknown;
  /** Wall-clock duration of the request, when measurable. */
  durationMs?: number;
  /** Aggregate stats when this entry is the result of a `load` step. */
  load?: LoadStats;
  /** Collected events when this entry is the result of an `sse` step. */
  events?: Array<{ event: string; data: string; id: string }>;
}

/** What the driver exposes to oracle evaluation after a case's steps have run. */
export interface Observation {
  url(): string;
  title(): Promise<string>;
  isVisible(selector: string): Promise<boolean>;
  textOf(selector: string): Promise<string | null>;
  count(selector: string): Promise<number>;
  attribute(selector: string, name: string): Promise<string | null>;
  consoleErrors(): string[];
  /** Named responses captured via `fetch`/`waitForResponse` steps (most recent is "last"). */
  response(name?: string): ObservedResponse | undefined;
  evaluate(expression: string): Promise<unknown>;
  /**
   * Run an axe-core accessibility audit over the page and return the raw result.
   * The driver owns axe injection and the live page; the `a11y` oracle merely
   * filters the result by impact.
   */
  axe(options: { include?: string[]; exclude?: string[] }): Promise<AxeResultLike>;
  /**
   * Capture a PNG screenshot of the page (or `selector`, when given) as a Buffer.
   * The driver owns the live page; the `screenshotMatches` oracle reads the
   * baseline and pixel-compares. Baseline file writes live in the driver.
   */
  screenshot(selector?: string): Promise<Buffer>;
}

/**
 * A per-oracle record produced for BOTH passing and failing oracles. `detail`
 * is concrete (the observed value/selector/reason), never vacuous, so a report
 * can show what each oracle actually saw — not just that it "passed".
 */
export interface OracleRecord {
  kind: Oracle["assert"];
  passed: boolean;
  detail: string;
}

export interface OracleOutcome {
  passed: boolean;
  failures: string[];
  /** One record per oracle, in evaluation order, mirroring `failures` on the failing entries. */
  records: OracleRecord[];
}

/** Outcome of a single oracle evaluation: a pass/fail flag plus a concrete detail. */
interface EvalResult {
  passed: boolean;
  detail: string;
}

const ok = (detail: string): EvalResult => ({ passed: true, detail });
const no = (detail: string): EvalResult => ({ passed: false, detail });

/** Resolve a dot/`$.`-prefixed path against a parsed JSON value. */
export function getByPath(obj: unknown, path: string): unknown {
  const clean = path.replace(/^\$\.?/, "");
  if (clean === "") return obj;
  const parts = clean.split(".").filter(Boolean);
  let cur: unknown = obj;
  for (const part of parts) {
    if (cur == null || typeof cur !== "object") return undefined;
    cur = (cur as Record<string, unknown>)[part];
  }
  return cur;
}

const eq = (a: unknown, b: unknown) => JSON.stringify(a) === JSON.stringify(b);

/** Classify a JSON value into the jsonType oracle's vocabulary. */
function typeOf(val: unknown): "string" | "number" | "boolean" | "array" | "object" | "null" | "undefined" {
  if (val === null) return "null";
  if (val === undefined) return "undefined";
  if (Array.isArray(val)) return "array";
  const t = typeof val;
  if (t === "string" || t === "number" || t === "boolean") return t;
  if (t === "object") return "object";
  return "undefined";
}

async function evalOne(o: Oracle, obs: Observation): Promise<EvalResult> {
  switch (o.assert) {
    case "status": {
      const r = obs.response(o.of);
      if (!r) return no(`status: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      return r.status === o.equals
        ? ok(`status: ${r.status} (== ${o.equals})`)
        : no(`status: expected ${o.equals}, got ${r.status}`);
    }
    case "responseOk": {
      const r = obs.response(o.of);
      if (!r) return no(`responseOk: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      return r.ok ? ok(`responseOk: ${r.status} is 2xx`) : no(`responseOk: expected 2xx, got ${r.status}`);
    }
    case "statusIn": {
      const r = obs.response(o.of);
      if (!r) return no(`statusIn: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      return o.values.includes(r.status)
        ? ok(`statusIn: ${r.status} ∈ [${o.values.join(", ")}]`)
        : no(`statusIn: expected one of [${o.values.join(", ")}], got ${r.status}`);
    }
    case "statusRange": {
      const r = obs.response(o.of);
      if (!r) return no(`statusRange: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      return r.status >= o.min && r.status <= o.max
        ? ok(`statusRange: ${r.status} within ${o.min}..${o.max}`)
        : no(`statusRange: expected ${o.min}..${o.max}, got ${r.status}`);
    }
    case "jsonPath": {
      const r = obs.response(o.of);
      if (!r) return no(`jsonPath: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      const val = getByPath(r.json, o.path);
      if (o.exists !== undefined) {
        const present = val !== undefined;
        if (present !== o.exists) return no(`jsonPath "${o.path}": expected exists=${o.exists}, got ${present}`);
      }
      if ("equals" in o && o.equals !== undefined) {
        if (!eq(val, o.equals)) {
          return no(`jsonPath "${o.path}": expected ${JSON.stringify(o.equals)}, got ${JSON.stringify(val)}`);
        }
      }
      // value-free on PASS: the observed value may be a secret/PII; do not serialize it.
      return ok(`jsonPath "${o.path}": matched`);
    }
    case "visible": {
      return (await obs.isVisible(o.selector))
        ? ok(`visible: "${o.selector}" is visible`)
        : no(`visible: "${o.selector}" not visible`);
    }
    case "hidden": {
      return (await obs.isVisible(o.selector))
        ? no(`hidden: "${o.selector}" is visible`)
        : ok(`hidden: "${o.selector}" is not visible`);
    }
    case "textContains": {
      const text = (await obs.textOf(o.selector)) ?? "";
      return text.includes(o.value)
        ? ok(`textContains: "${o.selector}" contains "${o.value}"`)
        : no(`textContains: "${o.selector}" did not contain "${o.value}" (got "${text.slice(0, 120)}")`);
    }
    case "urlContains": {
      const u = obs.url();
      return u.includes(o.value)
        ? ok(`urlContains: "${o.value}" found in URL`)
        : no(`urlContains: "${u}" did not contain "${o.value}"`);
    }
    case "titleContains": {
      const t = await obs.title();
      return t.includes(o.value)
        ? ok(`titleContains: title contains "${o.value}"`)
        : no(`titleContains: "${t}" did not contain "${o.value}"`);
    }
    case "count": {
      const n = await obs.count(o.selector);
      return n === o.equals
        ? ok(`count: "${o.selector}" == ${o.equals}`)
        : no(`count: "${o.selector}" expected ${o.equals}, got ${n}`);
    }
    case "attribute": {
      const v = await obs.attribute(o.selector, o.name);
      // `exists` is checked first so presence/absence can be asserted independent
      // of value (e.g. boolean/aria attributes like 'required', 'aria-expanded').
      if (o.exists !== undefined) {
        const present = v !== null;
        if (present !== o.exists) {
          return no(`attribute "${o.name}": expected exists=${o.exists}, got ${present}`);
        }
        // exists:false is satisfied by absence; nothing further to check.
        if (o.exists === false) return ok(`attribute "${o.name}": absent (exists=false)`);
      }
      if (v === null) return no(`attribute: "${o.selector}" has no "${o.name}"`);
      if (o.equals !== undefined && v !== o.equals) {
        return no(`attribute "${o.name}": expected "${o.equals}", got "${v}"`);
      }
      if (o.contains !== undefined && !v.includes(o.contains)) {
        return no(`attribute "${o.name}": "${v}" did not contain "${o.contains}"`);
      }
      if (o.matches !== undefined && !new RegExp(o.matches).test(v)) {
        return no(`attribute "${o.name}": "${v}" did not match /${o.matches}/`);
      }
      return ok(`attribute "${o.name}": matched`);
    }
    case "responseTime": {
      const r = obs.response(o.of);
      if (!r) return no(`responseTime: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      if (r.durationMs === undefined) return no(`responseTime: timing unavailable for the response`);
      return r.durationMs <= o.maxMs
        ? ok(`responseTime: ${r.durationMs}ms ≤ ${o.maxMs}ms`)
        : no(`responseTime: ${r.durationMs}ms exceeded ${o.maxMs}ms`);
    }
    case "header": {
      const r = obs.response(o.of);
      if (!r) return no(`header: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      const key = o.name.toLowerCase();
      const val = (r.headers ?? {})[key];
      if (val === undefined) return no(`header "${o.name}": absent on the response`);
      if (o.equals !== undefined && val !== o.equals) {
        return no(`header "${o.name}": expected "${o.equals}", got "${val}"`);
      }
      if (o.contains !== undefined && !val.includes(o.contains)) {
        return no(`header "${o.name}": "${val}" did not contain "${o.contains}"`);
      }
      return ok(`header "${o.name}": matched`);
    }
    case "jsonType": {
      const r = obs.response(o.of);
      if (!r) return no(`jsonType: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      const val = getByPath(r.json, o.path);
      const actual = typeOf(val);
      return actual === o.type
        ? ok(`jsonType "${o.path}": ${actual}`)
        : no(`jsonType "${o.path}": expected ${o.type}, got ${actual}`);
    }
    case "nonEmpty": {
      const r = obs.response(o.of);
      if (!r) return no(`nonEmpty: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      if (o.path === undefined) {
        return r.bodyText.length > 0
          ? ok(`nonEmpty: body has ${r.bodyText.length} char(s)`)
          : no(`nonEmpty: response body is empty`);
      }
      const val = getByPath(r.json, o.path);
      if (typeof val === "string")
        return val.length > 0
          ? ok(`nonEmpty "${o.path}": string length ${val.length}`)
          : no(`nonEmpty "${o.path}": string is empty`);
      if (Array.isArray(val))
        return val.length > 0
          ? ok(`nonEmpty "${o.path}": array length ${val.length}`)
          : no(`nonEmpty "${o.path}": array is empty`);
      return no(`nonEmpty "${o.path}": expected a non-empty string or array, got ${typeOf(val)}`);
    }
    case "bodyContains": {
      const r = obs.response(o.of);
      if (!r) return no(`bodyContains: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      return r.bodyText.includes(o.value)
        ? ok(`bodyContains: body contains "${o.value}"`)
        : no(`bodyContains: body did not contain "${o.value}"`);
    }
    case "jsonMatch": {
      const r = obs.response(o.of);
      if (!r) return no(`jsonMatch: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      const val = getByPath(r.json, o.path);
      if (typeof val !== "string") return no(`jsonMatch "${o.path}": expected a string, got ${typeOf(val)}`);
      return new RegExp(o.pattern).test(val)
        ? ok(`jsonMatch "${o.path}": matched /${o.pattern}/`)
        : no(`jsonMatch "${o.path}": "${val.slice(0, 120)}" did not match /${o.pattern}/`);
    }
    case "titleMatches": {
      const t = await obs.title();
      return new RegExp(o.pattern).test(t)
        ? ok(`titleMatches: matched /${o.pattern}/`)
        : no(`titleMatches: "${t}" did not match /${o.pattern}/`);
    }
    case "urlMatches": {
      const u = obs.url();
      return new RegExp(o.pattern).test(u)
        ? ok(`urlMatches: matched /${o.pattern}/`)
        : no(`urlMatches: "${u}" did not match /${o.pattern}/`);
    }
    case "noConsoleErrors": {
      const errs = obs.consoleErrors();
      return errs.length === 0
        ? ok(`noConsoleErrors: 0 console error(s)`)
        : no(`noConsoleErrors: ${errs.length} console error(s): ${errs[0]}`);
    }
    case "evalTruthy": {
      const v = await obs.evaluate(o.expression);
      return v
        ? ok(`evalTruthy: "${o.expression}" was truthy`)
        : no(`evalTruthy: "${o.expression}" was falsy (${JSON.stringify(v)})`);
    }
    case "errorRate": {
      const r = obs.response(o.of);
      if (!r) return no(`errorRate: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      if (!r.load) return no(`errorRate: response${o.of ? ` "${o.of}"` : ""} carries no load stats (not a load step?)`);
      return r.load.errorRate <= o.max
        ? ok(
            `errorRate: ${(r.load.errorRate * 100).toFixed(1)}% (${r.load.errors}/${r.load.count}) ≤ ${(o.max * 100).toFixed(1)}%`,
          )
        : no(
            `errorRate: ${(r.load.errorRate * 100).toFixed(1)}% (${r.load.errors}/${r.load.count}) exceeded ${(o.max * 100).toFixed(1)}%`,
          );
    }
    case "eventCount": {
      // Defence-in-depth: a bounds-less eventCount is rejected at parse time (see
      // the Oracle superRefine), but a hand-built oracle could bypass parsing — an
      // unbounded check must FAIL, never silently pass, or it proves nothing.
      if (o.min === undefined && o.equals === undefined) {
        return no(`eventCount: needs at least one of min/equals (an unbounded eventCount asserts nothing)`);
      }
      const r = obs.response(o.of);
      if (!r) return no(`eventCount: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      // The `sse` step puts its collected events on `events` (and mirrors them on
      // `json`); fall back to a JSON array so a hand-built aggregate still works.
      const events = r.events ?? (Array.isArray(r.json) ? (r.json as unknown[]) : undefined);
      if (!events) return no(`eventCount: response${o.of ? ` "${o.of}"` : ""} carries no events (not an sse step?)`);
      const n = events.length;
      if (o.equals !== undefined && n !== o.equals) return no(`eventCount: expected exactly ${o.equals}, got ${n}`);
      if (o.min !== undefined && n < o.min) return no(`eventCount: expected at least ${o.min}, got ${n}`);
      return ok(`eventCount: ${n} event(s)`);
    }
    case "percentile": {
      const r = obs.response(o.of);
      if (!r) return no(`percentile: no response captured${o.of ? ` named "${o.of}"` : ""}`);
      if (!r.load) return no(`percentile: response${o.of ? ` "${o.of}"` : ""} carries no load stats (not a load step?)`);
      const actual =
        o.p === "max" ? r.load.maxMs : o.p === 50 ? r.load.p50 : o.p === 95 ? r.load.p95 : r.load.p99;
      return actual <= o.maxMs
        ? ok(`percentile p${o.p}: ${actual}ms ≤ ${o.maxMs}ms`)
        : no(`percentile p${o.p}: ${actual}ms exceeded ${o.maxMs}ms`);
    }
    case "a11y": {
      // The driver injects axe-core and runs the audit; we only filter by impact.
      const result = await obs.axe({ include: o.include, exclude: o.exclude });
      const report = filterViolations(result, o.maxImpact);
      return report.passed ? ok(report.summary) : no(report.summary);
    }
    case "screenshotMatches": {
      const current = await obs.screenshot(o.selector);
      // Missing baseline is the first run: there is nothing to diff against, so it
      // passes with an honest note. The driver persists `current` as the baseline.
      if (!existsSync(o.baseline)) {
        return ok(`screenshotMatches: no baseline at "${o.baseline}" — first run, captured as baseline`);
      }
      const baseline = await readFile(o.baseline);
      const { ratio } = comparePng(baseline, current);
      return ratio <= o.maxDiffRatio
        ? ok(`screenshotMatches: ${ratio.toFixed(4)} diff ratio ≤ ${o.maxDiffRatio} (baseline "${o.baseline}")`)
        : no(`screenshotMatches: ${ratio.toFixed(4)} diff ratio exceeded ${o.maxDiffRatio} (baseline "${o.baseline}")`);
    }
    default: {
      // Exhaustiveness guard: a new Oracle variant added to schema.ts but not wired
      // here becomes a COMPILE error rather than silently falling through to a falsy
      // (= passing) result. Unreachable at runtime — Zod gates the input first.
      const _exhaustive: never = o;
      return no(`unhandled oracle: ${JSON.stringify(_exhaustive)}`);
    }
  }
}

/**
 * Evaluate all oracles; a case passes only if every oracle passes.
 *
 * Alongside the byte-stable `{ passed, failures }` contract this also returns
 * `records`: one `{ kind, passed, detail }` per oracle (pass AND fail), in
 * evaluation order. `failures` is exactly the `detail` of the failing records,
 * so the two views stay in lock-step.
 */
export async function evaluateOracles(oracles: Oracle[], obs: Observation): Promise<OracleOutcome> {
  const failures: string[] = [];
  const records: OracleRecord[] = [];
  for (const o of oracles) {
    try {
      const r = await evalOne(o, obs);
      records.push({ kind: o.assert, passed: r.passed, detail: r.detail });
      if (!r.passed) failures.push(r.detail);
    } catch (e) {
      // A throwing oracle (e.g. bad evalTruthy JS) fails THAT oracle — it must not
      // crash the whole case as an error and mask the case's other oracles.
      const detail = `${o.assert}: threw ${e instanceof Error ? e.message : String(e)}`;
      records.push({ kind: o.assert, passed: false, detail });
      failures.push(detail);
    }
  }
  return { passed: failures.length === 0, failures, records };
}

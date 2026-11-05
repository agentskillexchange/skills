/**
 * Heimdall plan & result schemas — the single source of truth.
 *
 * Zod schemas define the on-disk test-plan format and the run-report format,
 * and TypeScript types are derived from them. `heimdall schema` emits the JSON
 * Schema so other tools (e.g. the live-test skill) can author plans against it.
 */
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

/* ------------------------------------------------------------------ drivers */

/**
 * Execution regime for a case.
 * - `extension`  the user's real logged-in Chrome (highest fidelity). Heimdall
 *   CANNOT drive this itself — it is driven by an agent's browser tools. Heimdall
 *   marks such cases `blocked` so reports stay honest.
 * - `cdp`        Playwright/CDP, parallel contexts, per-target input. The default.
 * - `container`  `cdp` inside a disposable Docker + Xvfb sandbox (Linux Chrome).
 */
export const Driver = z.enum(["extension", "cdp", "container"]);
export type Driver = z.infer<typeof Driver>;

/** Evidence-fidelity tier, derived from the driver that produced a result. */
export const FidelityTier = z.enum(["high", "medium", "medium-linux"]);
export type FidelityTier = z.infer<typeof FidelityTier>;

export function fidelityForDriver(driver: Driver): FidelityTier {
  switch (driver) {
    case "extension":
      return "high";
    case "cdp":
      return "medium";
    case "container":
      return "medium-linux";
  }
}

/* -------------------------------------------------------------------- steps */

const WaitUntil = z.enum(["load", "domcontentloaded", "networkidle", "commit"]);

/**
 * Per-step capture spec: pull values out of a step's response into the per-case
 * variable map (`store.vars`) for later `${name}` templating. Each entry captures
 * EITHER a JSON path out of the parsed body OR a response header (case-insensitive).
 */
const Capture = z
  .record(
    z
      .object({
        jsonPath: z.string().optional().describe("dot path into the response JSON body"),
        header: z.string().optional().describe("response header name (case-insensitive)"),
      })
      .strict(),
  )
  .optional()
  .describe("capture values from this step's response into per-case ${vars}");

const StepBaseUnion = z.discriminatedUnion("action", [
  z
    .object({
      action: z.literal("goto"),
      url: z.string().describe("absolute URL or path resolved against baseUrl"),
      waitUntil: WaitUntil.optional(),
    })
    .strict(),
  z.object({ action: z.literal("click"), selector: z.string() }).strict(),
  z.object({ action: z.literal("fill"), selector: z.string(), value: z.string() }).strict(),
  z
    .object({
      action: z.literal("select"),
      selector: z.string(),
      value: z.union([z.string(), z.array(z.string())]).describe("option value(s) to select"),
    })
    .strict(),
  z.object({ action: z.literal("hover"), selector: z.string() }).strict(),
  z.object({ action: z.literal("check"), selector: z.string() }).strict(),
  z.object({ action: z.literal("uncheck"), selector: z.string() }).strict(),
  z
    .object({
      action: z.literal("setViewport"),
      width: z.number().int().positive(),
      height: z.number().int().positive(),
    })
    .strict(),
  z
    .object({
      action: z.literal("waitForResponse"),
      urlContains: z.string().describe("substring matched against response URLs"),
      timeoutMs: z.number().int().positive().optional(),
      as: z.string().optional().describe("name to store the response under for oracles"),
      capture: Capture,
    })
    .strict(),
  z
    .object({
      action: z.literal("press"),
      key: z.string().describe("e.g. 'Enter', 'Control+A'"),
      selector: z.string().optional(),
    })
    .strict(),
  z
    .object({
      action: z.literal("waitFor"),
      selector: z.string().optional(),
      state: z.enum(["visible", "hidden", "attached", "detached"]).optional(),
      timeoutMs: z.number().int().positive().optional(),
    })
    .strict(),
  z.object({ action: z.literal("wait"), ms: z.number().int().nonnegative() }).strict(),
  z
    .object({
      action: z.literal("fetch"),
      url: z.string(),
      method: z.string().optional(),
      headers: z.record(z.string()).optional(),
      body: z.string().optional(),
      as: z.string().optional().describe("name to store the response under for oracles"),
      capture: Capture,
    })
    .strict(),
  z
    .object({
      action: z.literal("request"),
      url: z.string(),
      method: z.string().optional(),
      headers: z.record(z.string()).optional(),
      body: z.string().optional(),
      as: z.string().optional().describe("name to store the response under for oracles"),
      capture: Capture,
      redirect: z
        .enum(["follow", "manual"])
        .optional()
        .describe(
          "redirect handling; 'manual' returns the 3xx with readable headers (location/hx-redirect/...). Default 'follow'.",
        ),
    })
    .strict()
    .describe(
      "browser-context API request via Playwright's APIRequestContext — no page/goto needed, not subject to page CORS",
    ),
  z
    .object({
      action: z.literal("pollUntil"),
      url: z.string(),
      method: z.string().optional(),
      headers: z.record(z.string()).optional(),
      body: z.string().optional(),
      // Oracle is declared AFTER Step in this file; z.lazy defers the reference so
      // there is no forward-reference crash and the file order stays intact.
      oracle: z
        .lazy(() => z.array(Oracle))
        .describe("response-based oracles re-evaluated each poll until they all pass"),
      intervalMs: z.number().int().positive().optional().describe("delay between polls (default 1000)"),
      timeoutMs: z.number().int().positive().optional().describe("give up after this long (default 30000)"),
      as: z.string().optional().describe("name to store the passing response under for oracles"),
    })
    .strict()
    .describe(
      "poll a URL via the browser-context APIRequestContext until its response-oracles pass, or time out",
    ),
  z
    .object({
      action: z.literal("load"),
      url: z.string(),
      method: z.string().optional(),
      headers: z.record(z.string()).optional(),
      body: z.string().optional(),
      times: z.number().int().positive().describe("total number of request iterations to issue"),
      concurrency: z
        .number()
        .int()
        .positive()
        .optional()
        .describe("max in-flight requests; defaults to min(times, 10)"),
      as: z.string().optional().describe("name to store the load aggregate under for oracles"),
    })
    .strict()
    .describe(
      "fire the same request `times` times via the browser-context APIRequestContext (bounded by `concurrency`) and store an aggregate (errorRate + latency percentiles) for the errorRate/percentile oracles. NOTE: the aggregate's `status` is a synthesized representative (the modal sample status), so a `status`/`responseOk` oracle over a load step asserts a FABRICATED value (the run may be 200 while a minority 500'd) — prefer the honest `errorRate`/`percentile` oracles",
    ),
  z
    .object({
      action: z.literal("sse"),
      url: z.string().describe("absolute URL or path resolved against baseUrl; opened as an EventSource"),
      events: z
        .number()
        .int()
        .positive()
        .optional()
        .describe("resolve once this many events have been collected (else run until timeout/closeAfterMs)"),
      timeoutMs: z.number().int().positive().optional().describe("overall budget for the stream (default 10000)"),
      closeAfterMs: z
        .number()
        .int()
        .positive()
        .optional()
        .describe("hard stop: close the stream after this long regardless of event count"),
      as: z.string().optional().describe("name to store the collected events under for oracles"),
    })
    .strict()
    .describe(
      "open a Server-Sent-Events stream, collect message events into an aggregate (events array under json, newline-joined data under bodyText) the eventCount/bodyContains/jsonPath oracles can read. NOTE: the aggregate's `status` is synthesized (200 if any event arrived, else 0) and does NOT reflect the real handshake status — prefer the honest `eventCount` oracle over `status`/`responseOk`",
    ),
  z
    .object({
      action: z.literal("eval"),
      expression: z.string().describe("JS evaluated in the page (for side effects)"),
    })
    .strict(),
  z.object({ action: z.literal("screenshot"), name: z.string().optional() }).strict(),
  z
    .object({
      action: z.literal("route"),
      urlContains: z
        .string()
        .describe(
          "substring matched against request URLs to intercept. NOTE: interception covers PAGE-originated requests only (goto navigations + in-page fetch/eval). It does NOT affect the request/load/pollUntil steps, which use Playwright's APIRequestContext and bypass page.route — route those flows through an in-page `fetch` step if you need them faulted.",
        ),
      mode: z
        .enum(["block", "abort", "fulfill", "delay"])
        .describe(
          "block/abort fail the request; fulfill returns a synthetic status/body/headers; delay slows it by delayMs",
        ),
      status: z.number().int().optional().describe("response status for `fulfill`"),
      body: z.string().optional().describe("response body for `fulfill`"),
      headers: z.record(z.string()).optional().describe("response headers for `fulfill`"),
      delayMs: z.number().int().nonnegative().optional().describe("added latency for `delay` (also usable with fulfill)"),
    })
    .strict()
    .describe(
      "install a network interception for matching PAGE-originated request URLs (fault injection / stubbing). Does NOT intercept the APIRequestContext-based request/load/pollUntil steps — see urlContains.",
    ),
]);

/**
 * The `race` step is self-referential (it nests an array of Steps). Recursive Zod
 * schemas can't be inferred via `z.infer`, so the type is declared explicitly here —
 * the race-free base union is inferred, then the recursive `race` arm is added by
 * hand (mirroring the canonical Zod recursive-type recipe). The runtime schema reuses
 * the base union's members so the action set stays EXHAUSTIVE and single-sourced.
 */
type StepBase = z.infer<typeof StepBaseUnion>;
export type Step = StepBase | { action: "race"; steps: Step[] };

const StepUnion = z.discriminatedUnion("action", [
  ...StepBaseUnion.options,
  z
    .object({
      action: z.literal("race"),
      // z.lazy defers the reference to Step (declared above) exactly like pollUntil.oracle
      // defers to Oracle; the explicit return type pins the recursive element so the
      // surrounding union stays inferrable.
      steps: z
        .lazy(() => z.array(Step) as unknown as z.ZodType<Step[]>)
        .describe("network steps (request/fetch/load) raced concurrently"),
    })
    .strict()
    .describe(
      "run several network steps concurrently and wait for ALL of them to settle, capturing every response; only request/fetch/load are allowed as nested steps (enforced below)",
    ),
]);

/**
 * The Step schema = the discriminated union plus a cross-field guard.
 *
 * A `race` step may only nest network steps (`request`/`fetch`/`load`): racing a
 * page-mutating action (goto/click/fill/…) against itself has no honest meaning —
 * the page is single-threaded — so such a plan is rejected at parse time. The union
 * itself cannot host the refinement (a discriminatedUnion member must stay a plain
 * object), so it is applied here at the union level, mirroring {@link Oracle}.
 */
const RACE_ALLOWED = new Set(["request", "fetch", "load"]);
// The explicit type annotation breaks the value self-reference (StepUnion → Step → StepUnion);
// `unknown` as the input parameter lets the defaulted-field ZodEffects stay assignable.
export const Step: z.ZodType<Step, z.ZodTypeDef, unknown> = StepUnion.superRefine((s, ctx) => {
  if (s.action === "race") {
    s.steps.forEach((nested, i) => {
      if (!RACE_ALLOWED.has(nested.action)) {
        ctx.addIssue({
          code: z.ZodIssueCode.custom,
          path: ["steps", i],
          message: `race only supports request/fetch/load steps — got '${nested.action}'`,
        });
      }
    });
  }
});

/* ------------------------------------------------------------------ oracles */

const OracleUnion = z.discriminatedUnion("assert", [
  z
    .object({
      assert: z.literal("status"),
      equals: z.number().int(),
      of: z.string().optional().describe("named fetch response; defaults to the last"),
    })
    .strict(),
  z.object({ assert: z.literal("responseOk"), of: z.string().optional() }).strict(),
  z
    .object({
      assert: z.literal("statusIn"),
      values: z.array(z.number().int()).min(1).describe("acceptable HTTP status codes"),
      of: z.string().optional().describe("named response; defaults to the last"),
    })
    .strict(),
  z
    .object({
      assert: z.literal("statusRange"),
      min: z.number().int().describe("inclusive lower bound"),
      max: z.number().int().describe("inclusive upper bound"),
      of: z.string().optional().describe("named response; defaults to the last"),
    })
    .strict(),
  z
    .object({
      assert: z.literal("jsonPath"),
      path: z.string().describe("dot path, e.g. 'data.user.id' or '$.ok'"),
      equals: z.unknown().optional(),
      exists: z.boolean().optional(),
      of: z.string().optional(),
    })
    .strict(),
  z.object({ assert: z.literal("visible"), selector: z.string() }).strict(),
  z.object({ assert: z.literal("hidden"), selector: z.string() }).strict(),
  z
    .object({ assert: z.literal("textContains"), selector: z.string(), value: z.string() })
    .strict(),
  z.object({ assert: z.literal("urlContains"), value: z.string() }).strict(),
  z.object({ assert: z.literal("titleContains"), value: z.string() }).strict(),
  z
    .object({
      assert: z.literal("count"),
      selector: z.string(),
      equals: z.number().int().nonnegative(),
    })
    .strict(),
  z
    .object({
      assert: z.literal("attribute"),
      selector: z.string(),
      name: z.string().describe("attribute name, e.g. 'href', 'aria-disabled'"),
      equals: z.string().optional(),
      contains: z.string().optional(),
      exists: z
        .boolean()
        .optional()
        .describe("true => attribute present (any value); false => attribute absent"),
      matches: z.string().optional().describe("RegExp source the attribute value must match"),
    })
    .strict(),
  z
    .object({
      assert: z.literal("responseTime"),
      maxMs: z.number().int().positive(),
      of: z.string().optional().describe("named response; defaults to the last"),
    })
    .strict(),
  z
    .object({
      assert: z.literal("header"),
      name: z.string().describe("response header name (matched case-insensitively)"),
      equals: z.string().optional(),
      contains: z.string().optional(),
      of: z.string().optional().describe("named response; defaults to the last"),
    })
    .strict(),
  z
    .object({
      assert: z.literal("jsonType"),
      path: z.string().describe("dot path, e.g. 'data.user.id' or '$.ok'"),
      type: z.enum(["string", "number", "boolean", "array", "object", "null"]),
      of: z.string().optional(),
    })
    .strict(),
  z
    .object({
      assert: z.literal("nonEmpty"),
      path: z.string().optional().describe("JSON path; if omitted, checks the response bodyText"),
      of: z.string().optional(),
    })
    .strict(),
  z
    .object({
      assert: z.literal("bodyContains"),
      value: z.string(),
      of: z.string().optional(),
    })
    .strict(),
  z
    .object({
      assert: z.literal("jsonMatch"),
      path: z.string().describe("dot path to a string value"),
      pattern: z.string().describe("RegExp source matched against the string at path"),
      of: z.string().optional(),
    })
    .strict(),
  z
    .object({
      assert: z.literal("titleMatches"),
      pattern: z.string().describe("RegExp source matched against the page title"),
    })
    .strict(),
  z
    .object({
      assert: z.literal("urlMatches"),
      pattern: z.string().describe("RegExp source matched against the current URL"),
    })
    .strict(),
  z.object({ assert: z.literal("noConsoleErrors") }).strict(),
  z
    .object({
      assert: z.literal("evalTruthy"),
      expression: z.string().describe("JS evaluated in the page; must be truthy"),
    })
    .strict(),
  z
    .object({
      assert: z.literal("errorRate"),
      max: z.number().min(0).max(1).describe("maximum acceptable error rate (0..1) for a load step's aggregate"),
      of: z.string().optional().describe("named load aggregate; defaults to the last response"),
    })
    .strict(),
  z
    .object({
      assert: z.literal("eventCount"),
      min: z.number().int().nonnegative().optional().describe("at least this many collected events"),
      equals: z.number().int().nonnegative().optional().describe("exactly this many collected events"),
      of: z.string().optional().describe("named sse aggregate; defaults to the last response"),
    })
    .strict()
    .describe("assert how many events an `sse` step collected (min and/or equals)"),
  z
    .object({
      assert: z.literal("percentile"),
      p: z
        .union([z.literal(50), z.literal(95), z.literal(99), z.literal("max")])
        .describe("which latency percentile of a load step's aggregate to bound"),
      maxMs: z.number().int().positive().describe("the percentile must be ≤ this many milliseconds"),
      of: z.string().optional().describe("named load aggregate; defaults to the last response"),
    })
    .strict(),
  z
    .object({
      assert: z.literal("a11y"),
      maxImpact: z
        .enum(["minor", "moderate", "serious", "critical"])
        .default("serious")
        .describe("the worst axe-core impact tolerated; any violation at or above this fails"),
      include: z.array(z.string()).optional().describe("CSS selectors to restrict the scan to"),
      exclude: z.array(z.string()).optional().describe("CSS selectors to exclude from the scan"),
    })
    .strict()
    .describe("run an axe-core accessibility audit over the page and fail on violations at/above maxImpact"),
  z
    .object({
      assert: z.literal("screenshotMatches"),
      baseline: z.string().describe("path to the baseline PNG to compare the capture against"),
      maxDiffRatio: z
        .number()
        .min(0)
        .max(1)
        .default(0.01)
        .describe("maximum fraction of differing pixels tolerated (0..1)"),
      selector: z.string().optional().describe("clip the capture to this element instead of the full page"),
    })
    .strict()
    .describe("pixel-compare a screenshot against a stored baseline (pixelmatch); fail above maxDiffRatio"),
]);

/**
 * The Oracle schema = the discriminated union plus a cross-field guard.
 *
 * `eventCount` is rejected at parse time when it carries NEITHER `min` NOR
 * `equals`: such an oracle asserts nothing (any event count, including zero,
 * passes), which would let a case satisfy its mandatory ≥1-oracle rule with a
 * vacuous check — "otherwise it is a click, not a test". The union itself cannot
 * host the refinement (a discriminatedUnion member must stay a plain object), so
 * it is applied here at the union level. `evalOne` carries a defence-in-depth
 * failure for the same shape in case a hand-built oracle bypasses parsing.
 */
export const Oracle = OracleUnion.superRefine((o, ctx) => {
  if (o.assert === "eventCount" && o.min === undefined && o.equals === undefined) {
    ctx.addIssue({
      code: z.ZodIssueCode.custom,
      message: "eventCount needs at least one of min/equals — an unbounded eventCount asserts nothing",
    });
  }
});
export type Oracle = z.infer<typeof Oracle>;

/* ---------------------------------------------------------------- load stats */

/**
 * Aggregate result of a `load` step: the sampled per-call outcomes reduced to an
 * error rate plus latency percentiles. Carried on an {@link CapturedResponse}-like
 * entry so the `errorRate`/`percentile` oracles can read it via `response(of)`.
 */
export const LoadStats = z
  .object({
    count: z.number().int().nonnegative().describe("number of requests issued"),
    errors: z.number().int().nonnegative().describe("non-2xx or thrown requests"),
    errorRate: z.number().describe("errors / count, in 0..1"),
    minMs: z.number().nonnegative(),
    p50: z.number().nonnegative(),
    p95: z.number().nonnegative(),
    p99: z.number().nonnegative(),
    maxMs: z.number().nonnegative(),
  })
  .strict();
export type LoadStats = z.infer<typeof LoadStats>;

/* ----------------------------------------------------------------- testcase */

export const Risk = z.enum(["read-only", "writes", "destructive", "paid", "prod"]);
export type Risk = z.infer<typeof Risk>;

export const Priority = z.enum(["p0", "p1", "p2", "p3"]);
export type Priority = z.infer<typeof Priority>;

export const TestCase = z
  .object({
    id: z.string().min(1),
    title: z.string().optional(),
    dimension: z.string().optional().describe("which expert/lens authored this"),
    driver: Driver.optional().describe("overrides the plan defaultDriver"),
    baseUrl: z.string().optional().describe("overrides the plan baseUrl for this case"),
    setup: z
      .array(Step)
      .optional()
      .describe(
        "steps run BEFORE this case's steps (share its page + ${vars}); a failing setup step fails the case and skips its steps/oracles",
      ),
    steps: z.array(Step).default([]),
    teardown: z
      .array(Step)
      .optional()
      .describe(
        "best-effort cleanup steps run AFTER oracles regardless of pass/fail (share the case's page + captured ${vars}); a teardown failure is noted, never flips the verdict",
      ),
    oracle: z.array(Oracle).min(1, "a case needs at least one oracle — otherwise it is a click, not a test"),
    risk: Risk.default("read-only"),
    priority: Priority.default("p2"),
    tags: z.array(z.string()).default([]),
    timeoutMs: z
      .number()
      .int()
      .positive()
      .optional()
      .describe("overall wall-clock budget for this case; overrides the run --timeout"),
  })
  .strict();
export type TestCase = z.infer<typeof TestCase>;

/* --------------------------------------------------------------------- plan */

/**
 * Plan-level redaction spec: extra response-header names and regex patterns to
 * scrub from the report/stderr on top of the per-run `${env.X}` secrets. Exported
 * so the runner/redact layer can consume it.
 */
export const Redaction = z
  .object({
    headers: z.array(z.string()).optional().describe("response header names whose values are redacted (case-insensitive)"),
    patterns: z.array(z.string()).optional().describe("RegExp sources; any match in report strings is redacted"),
  })
  .strict();
export type Redaction = z.infer<typeof Redaction>;

export const Plan = z
  .object({
    name: z.string().default("heimdall-plan"),
    baseUrl: z.string().optional(),
    defaultDriver: Driver.default("cdp"),
    storageState: z.string().optional().describe("path to a Playwright storageState for injected auth"),
    redaction: Redaction.optional().describe("extra header names / regex patterns to scrub from the report"),
    setup: z
      .array(Step)
      .optional()
      .describe(
        "steps run ONCE before any case (in a throwaway context) to seed shared state; if any fails, every runnable case is marked blocked. TRUSTED, author-controlled fixtures: plan hooks run UNGATED — they are NOT subject to the per-case risk/--allow-risk gate, so keep destructive operations out of them unless you intend them to run unconditionally",
      ),
    teardown: z
      .array(Step)
      .optional()
      .describe(
        "best-effort steps run ONCE after all cases to clean up shared state; failures are logged, never fatal. Like plan.setup, these are TRUSTED fixtures that run UNGATED (not subject to the risk/--allow-risk gate)",
      ),
    cases: z.array(TestCase).min(1),
  })
  .strict();
export type Plan = z.infer<typeof Plan>;

/* ------------------------------------------------------------------ results */

export const ResultStatus = z.enum(["pass", "fail", "blocked", "skipped", "error"]);
export type ResultStatus = z.infer<typeof ResultStatus>;

export const CapturedResponse = z
  .object({
    name: z.string().optional(),
    url: z.string(),
    method: z.string(),
    status: z.number(),
    headers: z.record(z.string()).optional().describe("response headers, lower-cased keys"),
  })
  .strict();
export type CapturedResponse = z.infer<typeof CapturedResponse>;

export const Result = z
  .object({
    id: z.string(),
    status: ResultStatus,
    driver: Driver,
    fidelityTier: FidelityTier,
    observed: z.string(),
    failures: z.array(z.string()).default([]),
    evidence: z
      .object({
        screenshots: z.array(z.string()).default([]),
        har: z.string().optional(),
        trace: z.string().optional().describe("Playwright trace.zip path (open with `npx playwright show-trace`)"),
        video: z.string().optional().describe("Playwright video path"),
        consoleErrors: z.array(z.string()).default([]),
        responses: z.array(CapturedResponse).default([]),
      })
      .strict()
      .default({ screenshots: [], consoleErrors: [], responses: [] }),
    durationMs: z.number().nonnegative(),
    attempts: z.number().int().positive().optional().describe("how many times the case ran (>1 ⇒ retried)"),
    oracleResults: z
      .array(
        z
          .object({
            kind: z.string().describe("the oracle's `assert` discriminant"),
            passed: z.boolean(),
            detail: z.string().describe("human-readable pass/fail explanation"),
          })
          .strict(),
      )
      .optional()
      .describe("per-oracle pass/fail breakdown (optional — older reports omit it)"),
    notes: z.string().optional(),
  })
  .strict();
export type Result = z.infer<typeof Result>;

export const RunReport = z
  .object({
    plan: z.string(),
    heimdallVersion: z.string(),
    startedAt: z.string(),
    finishedAt: z.string(),
    durationMs: z.number().nonnegative(),
    summary: z.object({
      total: z.number().int(),
      pass: z.number().int(),
      fail: z.number().int(),
      blocked: z.number().int(),
      skipped: z.number().int(),
      error: z.number().int(),
    }),
    results: z.array(Result),
  })
  .strict();
export type RunReport = z.infer<typeof RunReport>;

/** Parse + validate an unknown value as a Plan, applying defaults. */
export function parsePlan(input: unknown): Plan {
  return Plan.parse(input);
}

/** The JSON Schema for a plan — for editors/other tools. Single source of truth. */
export function planJsonSchema(): object {
  return zodToJsonSchema(Plan, { name: "HeimdallPlan", $refStrategy: "none" });
}

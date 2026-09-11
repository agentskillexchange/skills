import axe from "axe-core";

/**
 * Accessibility scanning via axe-core, kept deliberately decoupled from
 * Playwright: {@link runAxe} talks to a structurally typed {@link AxeBridge}
 * (any object exposing an `evaluate` that matches a Playwright `Page`), and
 * {@link filterViolations} is a pure severity filter over a raw axe result.
 */

/** axe-core impact levels, ordered least → most severe. */
export type Impact = "minor" | "moderate" | "serious" | "critical";

/** A single rule violation as reported by axe-core (subset we rely on). */
export interface AxeNode {
  html?: string;
  target?: unknown;
  failureSummary?: string;
}

export interface AxeViolation {
  id: string;
  impact?: Impact | null;
  help?: string;
  description?: string;
  helpUrl?: string;
  nodes?: AxeNode[];
}

/** The shape of `axe.run`'s result that we depend on (structurally typed). */
export interface AxeResultLike {
  violations: AxeViolation[];
}

/**
 * A structurally typed handle to a live page. A Playwright `Page` satisfies
 * this directly; tests can supply a mock. The string overload mirrors
 * Playwright's `page.evaluate(script)`, used to inject the axe-core source.
 */
export interface AxeBridge {
  evaluate<R = unknown>(pageFunction: string): Promise<R>;
  evaluate<R, A>(pageFunction: (arg: A) => R | Promise<R>, arg: A): Promise<R>;
}

/** Selector context for limiting the scan; forwarded verbatim to `axe.run`. */
export interface AxeContextOptions {
  include?: unknown[];
  exclude?: unknown[];
}

/** Outcome of {@link filterViolations}. */
export interface A11yReport {
  passed: boolean;
  maxImpact: Impact;
  violations: AxeViolation[];
  summary: string;
}

const IMPACT_ORDER: Record<Impact, number> = {
  minor: 0,
  moderate: 1,
  serious: 2,
  critical: 3,
};

function buildContext(options: AxeContextOptions): AxeContextOptions | undefined {
  const context: AxeContextOptions = {};
  if (options.include) context.include = options.include;
  if (options.exclude) context.exclude = options.exclude;
  return context.include || context.exclude ? context : undefined;
}

/**
 * Inject the axe-core source into the page, run it, and return the raw result.
 * `include`/`exclude` selectors are forwarded as the axe run context.
 */
export async function runAxe(
  bridge: AxeBridge,
  options: AxeContextOptions = {},
): Promise<AxeResultLike> {
  await bridge.evaluate(axe.source);
  const context = buildContext(options);
  return bridge.evaluate(
    (ctx: AxeContextOptions | undefined) => {
      const runner = (globalThis as { axe?: { run: (c?: unknown) => Promise<AxeResultLike> } }).axe;
      if (!runner) throw new Error("axe-core was not injected into the page");
      return runner.run(ctx ?? (globalThis as { document?: unknown }).document);
    },
    context,
  );
}

/**
 * Pure filter: keep only violations whose impact is at or above `maxImpact`
 * (minor < moderate < serious < critical). Violations with a null/unknown
 * impact are ignored. `passed` is true iff nothing survives the filter.
 */
export function filterViolations(result: AxeResultLike, maxImpact: Impact): A11yReport {
  const threshold = IMPACT_ORDER[maxImpact];
  const all = result.violations ?? [];
  const violations = all.filter((v) => {
    const impact = v.impact;
    if (!impact || !(impact in IMPACT_ORDER)) return false;
    return IMPACT_ORDER[impact] >= threshold;
  });
  const passed = violations.length === 0;
  const summary = passed
    ? `No accessibility violations at or above ${maxImpact}.`
    : `${violations.length} accessibility violation(s) at or above ${maxImpact}: ` +
      violations.map((v) => `${v.id} (${v.impact})`).join(", ");
  return { passed, maxImpact, violations, summary };
}

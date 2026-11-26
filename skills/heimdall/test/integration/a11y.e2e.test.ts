/**
 * REAL end-to-end test for the `a11y` oracle (#11).
 *
 * This launches actual Chromium (via Playwright) through Heimdall's public
 * `runPlan` API and drives the cdp driver against the node:http fixture server.
 * It is not a mock: a browser starts, the violating/clean fixture pages are
 * navigated, axe-core is injected into the LIVE page, the audit runs, and the
 * `a11y` oracle filters by impact — exactly as production does.
 *
 *   a11y-bad-fails        -> goto "/a11y-bad", a11y(maxImpact "minor") FAILS;
 *                            the evidence summary names the offending axe rule
 *                            ids (image-alt, label) and their critical impact.
 *   a11y-good-passes      -> goto "/a11y-good", a11y(default "serious") PASSES.
 *   severity-detects-mod  -> clean page + an injected orphan (a `region`
 *                            violation, impact moderate); a11y(maxImpact
 *                            "minor") FAILS naming region/moderate — proving the
 *                            moderate violation is genuinely present.
 *   severity-filter-pass  -> same injected moderate violation, but
 *                            a11y(maxImpact "serious") PASSES, because the only
 *                            present violation is below the threshold. This is
 *                            the severity-filtering pass: a maxImpact above the
 *                            present violations passes, NOT the absence of any.
 */
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterAll, beforeAll, describe, expect, it } from "vitest";

import { runPlan, type Plan, type RunOptions } from "../../src/index.js";
import { startFixtureServer, type FixtureServer } from "../fixtures/server.js";

let fixture: FixtureServer;
let outDir: string;

beforeAll(async () => {
  fixture = await startFixtureServer();
  outDir = await mkdtemp(join(tmpdir(), "heimdall-a11y-e2e-"));
});

afterAll(async () => {
  await fixture?.stop();
  if (outDir) {
    await rm(outDir, { recursive: true, force: true }).catch(() => {});
  }
});

// Appends a paragraph of content as a direct child of <body>, outside any
// landmark — axe flags this with the `region` rule at moderate impact. Used to
// stage a sub-critical violation the fixtures don't otherwise carry.
const INJECT_ORPHAN =
  "(() => { const p = document.createElement('p'); " +
  "p.textContent = 'orphan content outside any landmark'; " +
  "document.body.appendChild(p); })()";

describe("a11y oracle end-to-end", () => {
  it(
    "fails the violating page, passes the clean page, and filters by severity",
    async () => {
      const plan: Plan = {
        name: "a11y-e2e",
        defaultDriver: "cdp",
        cases: [
          {
            id: "a11y-bad-fails",
            title: "violating page fails with axe rule ids + impacts as evidence",
            method: "ui",
            steps: [{ action: "goto", url: "/a11y-bad", waitUntil: "load" }],
            // minor = the lowest threshold, so every real violation is reported.
            oracle: [{ assert: "a11y", maxImpact: "minor" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "a11y-good-passes",
            title: "clean page passes the default (serious) audit",
            method: "ui",
            steps: [{ action: "goto", url: "/a11y-good", waitUntil: "load" }],
            oracle: [{ assert: "a11y" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "severity-detects-moderate",
            title: "an injected moderate (region) violation is caught at maxImpact minor",
            method: "ui",
            steps: [
              { action: "goto", url: "/a11y-good", waitUntil: "load" },
              { action: "eval", expression: INJECT_ORPHAN },
            ],
            oracle: [{ assert: "a11y", maxImpact: "minor" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "severity-filter-passes",
            title: "the same moderate violation passes when maxImpact is serious",
            method: "ui",
            steps: [
              { action: "goto", url: "/a11y-good", waitUntil: "load" },
              { action: "eval", expression: INJECT_ORPHAN },
            ],
            oracle: [{ assert: "a11y", maxImpact: "serious" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const opts: RunOptions = {
        outDir,
        baseUrl: fixture.baseUrl,
        allowRisk: false,
        headed: false,
        concurrency: 2,
        driverOverride: "cdp",
      };

      const report = await runPlan(plan, opts);

      // Surface failure detail before the summary asserts if the run is off.
      const byId = (id: string) => report.results.find((r) => r.id === id);
      const bad = byId("a11y-bad-fails");
      const good = byId("a11y-good-passes");
      const detect = byId("severity-detects-moderate");
      const filtered = byId("severity-filter-passes");

      if (!bad || !good || !detect || !filtered) {
        const detail = report.results
          .map((r) => `${r.id}: ${r.status} — ${r.observed} [${r.failures.join("; ")}]`)
          .join("\n");
        throw new Error(`missing case result(s)\n${detail}`);
      }

      // The violating page FAILS, and the axe summary carried in `failures`
      // names the specific offending rule ids and their impact — not a vacuous
      // "something failed".
      expect(bad.status).toBe("fail");
      const badFailures = bad.failures.join("\n");
      expect(badFailures).toContain("image-alt");
      expect(badFailures).toContain("label");
      expect(badFailures).toContain("critical");
      // The summary attributes the impact to the rules, not just somewhere in
      // the string — both critical violations are reported.
      expect(badFailures).toContain("image-alt (critical)");
      expect(badFailures).toContain("label (critical)");

      // The clean page PASSES the default serious audit (zero violations).
      expect(good.status).toBe("pass");
      expect(good.failures).toHaveLength(0);
      expect(good.observed).toContain("oracle(s) satisfied");

      // The injected moderate `region` violation is genuinely present: at the
      // minor threshold it FAILS and names the rule id + impact. This is what
      // makes the next (severity-filter) pass non-vacuous.
      expect(detect.status).toBe("fail");
      const detectFailures = detect.failures.join("\n");
      expect(detectFailures).toContain("region (moderate)");
      // The two critical fixture violations are absent — only the orphan remains.
      expect(detectFailures).not.toContain("image-alt");
      expect(detectFailures).not.toContain("critical");

      // Severity filtering: the SAME moderate violation passes once maxImpact is
      // raised to serious — a maxImpact above the present violations passes,
      // proven not-vacuous by the failing `detect` case above.
      expect(filtered.status).toBe("pass");
      expect(filtered.failures).toHaveLength(0);

      expect(report.summary.total).toBe(4);
      expect(report.summary.pass).toBe(2);
      expect(report.summary.fail).toBe(2);
    },
    60_000,
  );
});

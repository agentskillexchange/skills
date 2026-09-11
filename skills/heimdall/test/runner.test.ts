/**
 * Unit test for the two-lane merge: `runPlan({ externalResults })` /
 * `mergeExternalResults` — the honesty-critical fold of externally-produced
 * results (e.g. `driver: extension` cases run via the agent's real-Chrome tools)
 * into the runner's own report.
 *
 * The plan here is ALL-extension, so every case is pre-blocked and NO driver
 * (and no Chromium) ever runs — this stays a fast unit test while exercising the
 * real `runPlan` path: pre-block → mergeExternalResults → plan-order sort →
 * recomputed summary → exitCodeFor.
 *
 * It pins the guarantees the README/ROADMAP make:
 *   (a) a matching BLOCKED/SKIPPED placeholder is REPLACED verbatim (status +
 *       evidence kept exactly, never fabricated green);
 *   (b) an id absent from the plan is APPENDED (surfaced honestly, not dropped);
 *   (c) results are sorted back into PLAN ORDER, with unknown ids trailing via the
 *       `?? plan.cases.length` fallback, and the summary is recomputed over the
 *       merged truth;
 *   (d) a passing external result does NOT flip `exitCodeFor` to green when another
 *       merged result is a genuine failure;
 *   (e) honesty: an external result is NEVER allowed to overwrite a REAL verdict
 *       Heimdall produced (a `pass`/`fail`/`error`) — only blocked/skipped
 *       placeholders may be filled (tested directly on `mergeExternalResults`).
 */
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterAll, beforeAll, describe, expect, it } from "vitest";

import { runPlan, exitCodeFor, type Plan, type Result, type RunOptions } from "../src/index.js";
import { mergeExternalResults } from "../src/runner.js";

let outDir: string;

beforeAll(async () => {
  outDir = await mkdtemp(join(tmpdir(), "heimdall-runner-merge-"));
});

afterAll(async () => {
  if (outDir) await rm(outDir, { recursive: true, force: true }).catch(() => {});
});

/** Build a minimal-but-valid external Result for a given id/status. */
function ext(id: string, status: Result["status"]): Result {
  return {
    id,
    status,
    driver: "extension",
    fidelityTier: "high",
    observed: `external ${status} for ${id}`,
    failures: status === "fail" ? [`${id} failed externally`] : [],
    evidence: { screenshots: [], consoleErrors: [], responses: [] },
    durationMs: 7,
  };
}

function baseOpts(externalResults: Result[]): RunOptions {
  return {
    outDir,
    allowRisk: false,
    headed: false,
    concurrency: 1,
    externalResults,
  };
}

describe("runPlan two-lane merge (externalResults)", () => {
  it(
    "replaces matching ids verbatim, appends unknown ids in plan order, and recomputes the summary",
    async () => {
      const plan: Plan = {
        name: "merge-plan",
        defaultDriver: "extension",
        cases: [
          {
            id: "ext-a",
            title: "extension case A (pre-blocked, replaced by an external PASS)",
            method: "ui",
            steps: [{ action: "goto", url: "https://example.test/a" }],
            oracle: [{ assert: "urlContains", value: "/a" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "ext-b",
            title: "extension case B (pre-blocked, replaced by an external FAIL)",
            method: "ui",
            steps: [{ action: "goto", url: "https://example.test/b" }],
            oracle: [{ assert: "urlContains", value: "/b" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      // ext-a/ext-b replace the two blocked placeholders; "ext-extra" is unknown to
      // the plan and must be appended (and trail the plan cases after sorting).
      const external = [ext("ext-extra", "pass"), ext("ext-b", "fail"), ext("ext-a", "pass")];
      const report = await runPlan(plan, baseOpts(external));

      // (a) matching ids replaced verbatim — no blocked placeholder survives.
      const a = report.results.find((r) => r.id === "ext-a");
      const b = report.results.find((r) => r.id === "ext-b");
      expect(a?.status).toBe("pass");
      expect(b?.status).toBe("fail");
      expect(b?.failures).toEqual(["ext-b failed externally"]);
      expect(report.results.some((r) => r.status === "blocked")).toBe(false);

      // (b)+(c) unknown id appended and (c) results sorted into plan order, unknown trailing.
      expect(report.results.map((r) => r.id)).toEqual(["ext-a", "ext-b", "ext-extra"]);

      // (c) summary recomputed over the merged truth (not the pre-blocked placeholders).
      expect(report.summary).toMatchObject({ total: 3, pass: 2, fail: 1, blocked: 0 });

      // (d) a passing external result does NOT mask the genuine external failure.
      expect(exitCodeFor(report)).not.toBe(0);
    },
    30_000,
  );

  // (e) Direct, driver-free test of the honesty rule: a real verdict is never
  // overwritten by an external file; only blocked/skipped placeholders are filled.
  describe("mergeExternalResults honesty (no fabricated green over a real verdict)", () => {
    const real = (id: string, status: Result["status"]): Result => ({ ...ext(id, status), driver: "cdp", fidelityTier: "medium" });

    it("fills a blocked placeholder but REFUSES to overwrite a genuine fail/pass/error", () => {
      const planResults: Result[] = [
        real("ran-and-failed", "fail"), // Heimdall actually ran this and it FAILED
        ext("blocked-ext", "blocked"), // a non-run placeholder
        real("ran-and-passed", "pass"),
        ext("skipped-one", "skipped"),
      ];
      const external: Result[] = [
        ext("ran-and-failed", "pass"), // a malicious/mistaken file trying to flip a real fail to pass
        ext("blocked-ext", "pass"), // legitimately fills the placeholder
        ext("ran-and-passed", "fail"), // tries to overwrite a real pass — must be ignored
        ext("skipped-one", "pass"), // fills the skipped placeholder
        ext("brand-new", "pass"), // unknown id — appended
      ];

      const merged = mergeExternalResults(planResults, external);
      const byId = Object.fromEntries(merged.map((r) => [r.id, r]));

      // Real verdicts are PRESERVED, not overwritten:
      expect(byId["ran-and-failed"]!.status).toBe("fail");
      expect(byId["ran-and-passed"]!.status).toBe("pass");
      // Placeholders are FILLED by the external results:
      expect(byId["blocked-ext"]!.status).toBe("pass");
      expect(byId["skipped-one"]!.status).toBe("pass");
      // Unknown id is appended:
      expect(byId["brand-new"]!.status).toBe("pass");
      expect(merged).toHaveLength(5);
    });

    it("is a no-op when there are no external results", () => {
      const planResults = [real("a", "pass")];
      expect(mergeExternalResults(planResults, undefined)).toBe(planResults);
      expect(mergeExternalResults(planResults, [])).toBe(planResults);
    });
  });
});

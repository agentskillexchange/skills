/**
 * REAL end-to-end test for the `screenshotMatches` visual-regression vertical (#13).
 *
 * This launches actual Chromium (via Playwright) through Heimdall's public
 * `runPlan` API and drives the cdp driver against the pixel-stable `/pixel`
 * fixture page. It exercises the whole vertical — the side-effecting baseline
 * seeding / diff writing in `execute.ts` AND the pure pass/fail verdict in
 * `oracle.ts` — not a mock.
 *
 * Baselines live in a throwaway temp dir (NOT the repo), so a run never pollutes
 * the working tree. Acceptance:
 *   1. FIRST run, missing baseline -> oracle PASSES and the current capture is
 *      written AS the baseline file; this seeding run writes NO diff PNG (the
 *      observable "first run" signal).
 *   2. SECOND run, baseline present -> oracle PASSES (`ratio <= maxDiffRatio`),
 *      the baseline is left byte-identical, and a diff PNG IS produced.
 *   3. ALTERED page (same viewport, different content) -> oracle FAILS with an
 *      "exceeded" failure and a diff PNG is written into the case evidence dir.
 */
import { existsSync } from "node:fs";
import { mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterAll, beforeAll, describe, expect, it } from "vitest";

import { runPlan, type Plan, type RunOptions } from "../../src/index.js";
import { startFixtureServer, type FixtureServer } from "../fixtures/server.js";

const DIFF_PNG = /screenshot-diff-\d+\.png$/;

let fixture: FixtureServer;
let outDir: string;
let baselineDir: string;

beforeAll(async () => {
  fixture = await startFixtureServer();
  outDir = await mkdtemp(join(tmpdir(), "heimdall-visual-e2e-"));
  baselineDir = await mkdtemp(join(tmpdir(), "heimdall-visual-baseline-"));
});

afterAll(async () => {
  await fixture?.stop();
  for (const dir of [outDir, baselineDir]) {
    if (dir) await rm(dir, { recursive: true, force: true }).catch(() => {});
  }
});

function baseOpts(): RunOptions {
  return {
    outDir,
    baseUrl: fixture.baseUrl,
    allowRisk: false,
    headed: false,
    concurrency: 1,
    driverOverride: "cdp",
  };
}

describe("screenshotMatches oracle end-to-end (cdp)", () => {
  it(
    "seeds a missing baseline on the first run, then passes the diff on the second",
    async () => {
      const baseline = join(baselineDir, "pixel-stable.png");
      expect(existsSync(baseline)).toBe(false);

      const plan: Plan = {
        name: "visual-baseline-seed",
        defaultDriver: "cdp",
        cases: [
          {
            id: "pixel-stable",
            title: "/pixel renders a stable swatch",
            method: "ui",
            steps: [{ action: "goto", url: "/pixel", waitUntil: "load" }],
            oracle: [{ assert: "screenshotMatches", baseline, selector: "#swatch", maxDiffRatio: 0.01 }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      // First run: no baseline -> capture is seeded as the baseline, oracle passes.
      // A seeding run has nothing to diff against, so it writes NO diff PNG: that
      // absence is the observable "first run" signal.
      const first = await runPlan(plan, baseOpts());
      const firstCase = first.results.find((r) => r.id === "pixel-stable");
      expect(firstCase?.status).toBe("pass");
      expect(firstCase?.failures).toEqual([]);
      expect(existsSync(baseline)).toBe(true);
      expect(firstCase?.evidence.screenshots.some((p) => DIFF_PNG.test(p))).toBe(false);

      const seeded = await readFile(baseline);
      expect(seeded.length).toBeGreaterThan(0);

      // Second run: baseline present -> a real pixel diff that stays within ratio.
      // It passes AND now emits a diff PNG (proving it diffed rather than re-seeded).
      const second = await runPlan(plan, baseOpts());
      const secondCase = second.results.find((r) => r.id === "pixel-stable");
      expect(secondCase?.status).toBe("pass");
      expect(secondCase?.failures).toEqual([]);
      expect(secondCase?.evidence.screenshots.some((p) => DIFF_PNG.test(p))).toBe(true);

      // The seeded baseline is byte-stable: a passing second run does not rewrite it.
      const afterSecond = await readFile(baseline);
      expect(afterSecond.equals(seeded)).toBe(true);
    },
    90_000,
  );

  it(
    "fails on an altered page and writes a diff PNG into the case evidence dir",
    async () => {
      const baseline = join(baselineDir, "viewport-altered.png");

      // Seed the baseline from the home page at a fixed viewport.
      const seedPlan: Plan = {
        name: "visual-alter-seed",
        defaultDriver: "cdp",
        cases: [
          {
            id: "altered-visual",
            title: "home page at a fixed viewport seeds the baseline",
            method: "ui",
            steps: [
              { action: "setViewport", width: 320, height: 240 },
              { action: "goto", url: "/", waitUntil: "load" },
            ],
            // No selector -> full-viewport capture; both runs share the 320x240
            // viewport, so dimensions match and a real pixel diff is possible.
            oracle: [{ assert: "screenshotMatches", baseline, maxDiffRatio: 0.01 }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };
      const seed = await runPlan(seedPlan, baseOpts());
      expect(seed.results.find((r) => r.id === "altered-visual")?.status).toBe("pass");
      expect(existsSync(baseline)).toBe(true);

      // Now run the SAME case id against a visibly different page (/pixel) at the
      // SAME viewport -> dimensions match, content differs -> the diff exceeds the
      // tolerance and the oracle fails.
      const alterPlan: Plan = {
        name: "visual-alter-run",
        defaultDriver: "cdp",
        cases: [
          {
            id: "altered-visual",
            title: "a different page at the same viewport breaks the baseline",
            method: "ui",
            steps: [
              { action: "setViewport", width: 320, height: 240 },
              { action: "goto", url: "/pixel", waitUntil: "load" },
            ],
            oracle: [{ assert: "screenshotMatches", baseline, maxDiffRatio: 0.01 }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };
      const altered = await runPlan(alterPlan, baseOpts());
      const alteredCase = altered.results.find((r) => r.id === "altered-visual");
      expect(alteredCase?.status).toBe("fail");
      expect(alteredCase?.failures.some((f) => /screenshotMatches/i.test(f) && /exceeded/i.test(f))).toBe(true);

      // A diff PNG is written into the case evidence dir and surfaced as evidence.
      const diffShot = alteredCase?.evidence.screenshots.find((p) => DIFF_PNG.test(p));
      expect(diffShot, "expected a diff PNG in case evidence").toBeTruthy();
      expect(diffShot!.startsWith(outDir)).toBe(true);
      expect(existsSync(diffShot!)).toBe(true);
      const diffBytes = await readFile(diffShot!);
      expect(diffBytes.length).toBeGreaterThan(0);
    },
    90_000,
  );
});

/**
 * REAL end-to-end test for the `load` step + errorRate/percentile oracles.
 *
 * Launches actual Chromium through Heimdall's public `runPlan` API and fires a
 * `load` step at the fixture's flaky `/slow` route (a deterministic 1-in-5 500).
 * The load engine issues N concurrent browser-context requests, aggregates the
 * per-call status + latency into a LoadStats, and the errorRate/percentile
 * oracles decide pass/fail against it.
 *
 *   pass case -> load /slow x20 @ concurrency 5; assert errorRate <= 0.3 (real
 *                rate is 0.2) and p95 latency under a generous bound.
 *   fail case -> same load; assert errorRate <= 0 (it isn't) -> the oracle must
 *                honestly fail, proving the aggregate carries the real errors.
 *
 * We assert the run summary: pass === 1, fail === 1.
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
  outDir = await mkdtemp(join(tmpdir(), "heimdall-load-e2e-"));
});

afterAll(async () => {
  await fixture?.stop();
  if (outDir) {
    await rm(outDir, { recursive: true, force: true }).catch(() => {});
  }
});

describe("load step end-to-end", () => {
  it(
    "fires a concurrent load and evaluates errorRate + percentile oracles honestly",
    async () => {
      const loadStep = { action: "load" as const, url: "/slow", times: 20, concurrency: 5, as: "lt" };
      const plan: Plan = {
        name: "load-e2e",
        defaultDriver: "cdp",
        cases: [
          {
            id: "load-within-budget",
            title: "20 requests, error rate within 30% and p95 under budget",
            steps: [loadStep],
            oracle: [
              { assert: "errorRate", max: 0.3, of: "lt" },
              { assert: "percentile", p: 95, maxMs: 5000, of: "lt" },
              { assert: "percentile", p: "max", maxMs: 10000, of: "lt" },
            ],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "load-zero-errors-required",
            title: "demanding a zero error rate must fail against a flaky endpoint",
            steps: [loadStep],
            oracle: [{ assert: "errorRate", max: 0, of: "lt" }],
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
        // concurrency 1 so the two cases do NOT interleave on the fixture's shared
        // /slow counter: the first case consumes counter 1..20 and the second 21..40,
        // so each sees exactly 4 of its 20 requests 500 (every 5th) — deterministic.
        concurrency: 1,
        driverOverride: "cdp",
      };

      const report = await runPlan(plan, opts);

      const pass = report.results.find((r) => r.id === "load-within-budget");
      const fail = report.results.find((r) => r.id === "load-zero-errors-required");

      // Surface detail if the within-budget case did not pass as expected.
      if (pass?.status !== "pass") {
        throw new Error(`expected load-within-budget to pass, got ${JSON.stringify(pass)}`);
      }

      expect(report.summary.total).toBe(2);
      expect(report.summary.pass).toBe(1);
      expect(report.summary.fail).toBe(1);

      expect(pass.status).toBe("pass");
      expect(pass.driver).toBe("cdp");

      expect(fail?.status).toBe("fail");
      // The aggregate carried the real 20% error rate (4 of 20 requests 500'd).
      expect(fail?.failures.join(" ")).toContain("errorRate");
      expect(fail?.failures.join(" ")).toContain("(4/20)");
    },
    60_000,
  );
});

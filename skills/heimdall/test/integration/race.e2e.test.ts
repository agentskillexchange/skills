/**
 * REAL end-to-end test for the `race` concurrent-step (#15).
 *
 * Launches actual Chromium (via Playwright) through the public `runPlan` API and
 * drives the cdp driver against the contended-write `/api/counter` fixture, which
 * atomically increments a shared counter and returns the new value. Firing N
 * writers CONCURRENTLY via a single `race` step and then reading the counter
 * exercises the real runtime path — not just the schema parse:
 *
 *   - each nested step registers its own named response in the SHARED store
 *     (so a per-writer `status`/`jsonType` oracle can see it — proving per-step
 *     capture under concurrency);
 *   - all N increments land (the final counter == N), which — from a counter that
 *     starts at 0 with N atomic increments — means the writers returned exactly the
 *     set 1..N with no lost updates, i.e. they truly ran concurrently;
 *   - the runtime RACE_ALLOWED guard rejects a hand-built race nesting a non-network
 *     step (`goto`), even though such a plan bypasses the schema's parse-time guard.
 */
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterAll, beforeAll, describe, expect, it } from "vitest";

import { runPlan, type Oracle, type Plan, type RunOptions, type Step } from "../../src/index.js";
import { startFixtureServer, type FixtureServer } from "../fixtures/server.js";

const N = 5;

let fixture: FixtureServer;
let outDir: string;

beforeAll(async () => {
  fixture = await startFixtureServer();
  outDir = await mkdtemp(join(tmpdir(), "heimdall-race-e2e-"));
});

afterAll(async () => {
  await fixture?.stop();
  if (outDir) await rm(outDir, { recursive: true, force: true }).catch(() => {});
});

function baseOpts(): RunOptions {
  return {
    outDir,
    baseUrl: fixture.baseUrl,
    allowRisk: false,
    headed: false,
    concurrency: 2,
    driverOverride: "cdp",
  };
}

describe("race concurrent-step end-to-end (cdp)", () => {
  it(
    "races N writers, each registering its own response, and lands exactly N increments",
    async () => {
      // N concurrent POST writers, each captured under a unique name w1..wN AND a
      // distinct URL (?w=i) so we can later prove each nested step registered ITS OWN
      // response (a capture-aliasing bug would collapse them to fewer distinct URLs).
      const writers: Step[] = Array.from({ length: N }, (_, i) => ({
        action: "request",
        url: `/api/counter?w=${i + 1}`,
        method: "POST",
        as: `w${i + 1}`,
      }));
      // Per-writer oracles: each named response must exist (proving the nested step
      // registered into the shared store under concurrency) and carry a numeric value.
      const writerOracles: Oracle[] = Array.from({ length: N }, (_, i) => [
        { assert: "status", equals: 200, of: `w${i + 1}` } as Oracle,
        { assert: "jsonType", path: "value", type: "number", of: `w${i + 1}` } as Oracle,
      ]).flat();

      const plan: Plan = {
        name: "race-e2e",
        defaultDriver: "cdp",
        cases: [
          {
            id: "race-counter",
            title: "N concurrent counter writers each land a unique value",
            method: "fetch",
            steps: [
              { action: "race", steps: writers },
              // After the race, read the counter: it must equal N (no lost updates),
              // which from 0 means the writers returned exactly 1..N — true concurrency.
              { action: "request", url: "/api/counter", method: "GET", as: "final" },
            ],
            oracle: [
              ...writerOracles,
              { assert: "status", equals: 200, of: "final" },
              { assert: "jsonPath", path: "value", equals: N, of: "final" },
            ],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, baseOpts());
      const race = report.results.find((r) => r.id === "race-counter");
      const detail = `${race?.status} — ${race?.observed}${race?.failures.length ? ` [${race?.failures.join("; ")}]` : ""}`;
      expect(race?.status, detail).toBe("pass");
      expect(race?.failures, detail).toEqual([]);

      // Each nested writer registered its OWN response: the captured evidence holds
      // exactly N distinct writer URLs (?w=1..N). A capture-aliasing bug (all nested
      // steps sharing one response) would yield fewer than N distinct writer URLs,
      // which the jsonType-number oracles alone could not detect.
      const writerUrls = (race?.evidence.responses ?? [])
        .map((r) => r.url)
        .filter((u) => /[?&]w=\d+/.test(u));
      const distinct = new Set(writerUrls);
      expect(distinct.size, `distinct writer URLs: ${[...distinct].join(", ")}`).toBe(N);
    },
    90_000,
  );

  it(
    "rejects a hand-built race nesting a non-network step at runtime",
    async () => {
      // A schema-bypassing plan: a `race` nesting a `goto` would be rejected at parse
      // time, but a hand-built Plan reaching runPlan must still fail clearly via the
      // runtime RACE_ALLOWED guard rather than silently doing nothing.
      const plan: Plan = {
        name: "race-guard",
        defaultDriver: "cdp",
        cases: [
          {
            id: "race-bad-nesting",
            title: "racing a goto is rejected at runtime",
            method: "ui",
            steps: [{ action: "race", steps: [{ action: "goto", url: "/" }] }],
            oracle: [],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, baseOpts());
      const bad = report.results.find((r) => r.id === "race-bad-nesting");
      expect(bad?.status).toBe("fail");
      expect(bad?.failures.some((f) => /race only supports request\/fetch\/load/i.test(f))).toBe(true);
    },
    60_000,
  );
});

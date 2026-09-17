/**
 * REAL end-to-end test for the `route` fault-injection step (#12).
 *
 * Launches actual Chromium (via Playwright) through the public `runPlan` API and
 * drives the cdp driver against the `/flaky-page` + `/api/flaky` fixtures. The
 * page fetches /api/flaky on load and renders "success"/"error" into #status, so
 * faulting that route via `page.route` lets us observe the real interception path
 * — not just the schema parse:
 *
 *   block   -> the fetch is aborted -> the page's catch renders "error";
 *   fulfill -> a synthetic 503 is returned -> !r.ok throws -> "error";
 *   delay   -> the real 200 is slowed but unchanged -> "success" (continue path);
 *   fulfill without a status -> the install-time guard THROWS, failing the case
 *              with "requires a status" (never a silent default).
 *
 * Each case installs the route FIRST, then navigates, so the page-load fetch is
 * intercepted. A short `wait` lets the async fetch+render settle before the oracle.
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
  outDir = await mkdtemp(join(tmpdir(), "heimdall-route-e2e-"));
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

describe("route fault-injection end-to-end (cdp)", () => {
  it(
    "drives each interception mode against /flaky-page and observes the real UI/verdict",
    async () => {
      const plan: Plan = {
        name: "route-e2e",
        defaultDriver: "cdp",
        cases: [
          {
            id: "route-block",
            title: "block aborts the fetch -> the page renders the error branch",
            method: "ui",
            steps: [
              { action: "route", urlContains: "/api/flaky", mode: "block" },
              { action: "goto", url: "/flaky-page", waitUntil: "load" },
              { action: "wait", ms: 400 },
            ],
            oracle: [{ assert: "textContains", selector: "#status", value: "error" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "route-fulfill-503",
            title: "fulfill 503 -> !r.ok throws -> the error branch renders",
            method: "ui",
            steps: [
              { action: "route", urlContains: "/api/flaky", mode: "fulfill", status: 503, body: "{}" },
              { action: "goto", url: "/flaky-page", waitUntil: "load" },
              { action: "wait", ms: 400 },
            ],
            oracle: [{ assert: "textContains", selector: "#status", value: "error" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "route-delay",
            title: "delay slows but does not change the real 200 -> success still renders",
            method: "ui",
            steps: [
              { action: "route", urlContains: "/api/flaky", mode: "delay", delayMs: 200 },
              { action: "goto", url: "/flaky-page", waitUntil: "load" },
              { action: "wait", ms: 800 },
            ],
            oracle: [{ assert: "textContains", selector: "#status", value: "success" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "route-fulfill-no-status",
            title: "fulfill without a status fails loudly at install time",
            method: "ui",
            steps: [
              { action: "route", urlContains: "/api/flaky", mode: "fulfill" },
              { action: "goto", url: "/flaky-page", waitUntil: "load" },
            ],
            oracle: [],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "route-delay-timing",
            title: "delay ACTUALLY slows the request (proven by wall-clock) — not a no-op",
            method: "fetch",
            steps: [
              // 700ms latency injected on /api/health; page.route also intercepts the
              // in-page fetch below, so the request is genuinely held ~700ms.
              { action: "route", urlContains: "/api/health", mode: "delay", delayMs: 700 },
              { action: "fetch", url: "/api/health", as: "h" },
            ],
            oracle: [{ assert: "status", equals: 200, of: "h" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, baseOpts());
      const byId = (id: string) => report.results.find((r) => r.id === id);

      const block = byId("route-block");
      const fulfill = byId("route-fulfill-503");
      const delay = byId("route-delay");
      const noStatus = byId("route-fulfill-no-status");

      // Surface detail if any of the three rendering cases misbehaved.
      const detail = report.results
        .map((r) => `${r.id}: ${r.status} — ${r.observed}${r.failures.length ? ` [${r.failures.join("; ")}]` : ""}`)
        .join("\n");

      expect(block?.status, detail).toBe("pass");
      expect(fulfill?.status, detail).toBe("pass");
      expect(delay?.status, detail).toBe("pass");

      // The no-status fulfill must fail with the explicit install-time guard message,
      // proving the runtime throw (not just the schema's optional `status`).
      expect(noStatus?.status).toBe("fail");
      expect(noStatus?.failures.some((f) => /requires a status/i.test(f))).toBe(true);

      // The delay must REALLY be applied: an isolated fetch through a 700ms-delayed
      // route makes the whole case take well over half a second. A no-op delay would
      // complete a localhost fetch in tens of ms, so this lower bound proves the
      // latency injection is live (the rendering case above can't — "success" renders
      // regardless of speed).
      const delayTiming = byId("route-delay-timing");
      expect(delayTiming?.status, detail).toBe("pass");
      expect(delayTiming?.durationMs ?? 0).toBeGreaterThanOrEqual(600);
    },
    90_000,
  );
});

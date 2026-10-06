/**
 * REAL end-to-end test for the cdp driver.
 *
 * This launches actual Chromium (via Playwright) through Heimdall's public
 * `runPlan` API and drives it against a real node:http fixture server. It is
 * not a mock: a browser is started, pages are navigated, an in-page fetch is
 * issued, oracles are evaluated, and a RunReport is produced.
 *
 *   ui case    -> goto "/", assert #app is visible, #app text contains
 *                 "Heimdall OK", and no console errors.
 *   fetch case -> goto "/" (to establish a same-origin page context), fetch
 *                 "/api/health", assert status 200 and jsonPath ok === true.
 *
 * We assert the run summary: pass === 2, fail === 0.
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
  outDir = await mkdtemp(join(tmpdir(), "heimdall-cdp-e2e-"));
});

afterAll(async () => {
  await fixture?.stop();
  if (outDir) {
    await rm(outDir, { recursive: true, force: true }).catch(() => {});
  }
});

describe("cdp driver end-to-end", () => {
  it(
    "runs a ui case and a fetch case against a live server and passes both",
    async () => {
      const plan: Plan = {
        name: "cdp-e2e",
        defaultDriver: "cdp",
        cases: [
          {
            id: "ui-home-renders",
            title: "home page renders #app with Heimdall OK",
            method: "ui",
            steps: [{ action: "goto", url: "/", waitUntil: "load" }],
            oracle: [
              { assert: "visible", selector: "#app" },
              { assert: "textContains", selector: "#app", value: "Heimdall OK" },
              { assert: "noConsoleErrors" },
            ],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "api-health-ok",
            title: "health endpoint returns 200 and ok:true",
            method: "fetch",
            // Navigate first so the in-page fetch runs from a same-origin
            // document rather than about:blank.
            steps: [
              { action: "goto", url: "/", waitUntil: "load" },
              { action: "fetch", url: "/api/health", method: "GET", as: "health" },
            ],
            oracle: [
              { assert: "status", equals: 200, of: "health" },
              { assert: "jsonPath", path: "ok", equals: true, of: "health" },
            ],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "api-request-mode",
            title: "request mode hits /api/health with no page and asserts headers + jsonType",
            method: "fetch",
            // No goto: the request step uses the browser-context APIRequestContext.
            steps: [{ action: "request", url: "/api/health", as: "h" }],
            oracle: [
              { assert: "status", equals: 200, of: "h" },
              { assert: "header", name: "content-type", contains: "application/json", of: "h" },
              { assert: "jsonType", path: "ok", type: "boolean", of: "h" },
            ],
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

      // Surface failure detail if anything went wrong, before the summary asserts.
      if (report.summary.pass !== 3) {
        const detail = report.results
          .map((r) => `${r.id}: ${r.status} — ${r.observed}${r.failures.length ? ` [${r.failures.join("; ")}]` : ""}`)
          .join("\n");
        throw new Error(`expected 3 passing cases, got summary=${JSON.stringify(report.summary)}\n${detail}`);
      }

      expect(report.summary.total).toBe(3);
      expect(report.summary.pass).toBe(3);
      expect(report.summary.fail).toBe(0);

      const ui = report.results.find((r) => r.id === "ui-home-renders");
      const api = report.results.find((r) => r.id === "api-health-ok");
      const reqMode = report.results.find((r) => r.id === "api-request-mode");
      expect(ui?.status).toBe("pass");
      expect(api?.status).toBe("pass");
      expect(reqMode?.status).toBe("pass");
      expect(ui?.driver).toBe("cdp");
    },
    60_000,
  );
});

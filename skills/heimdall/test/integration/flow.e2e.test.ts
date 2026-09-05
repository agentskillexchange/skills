/**
 * REAL end-to-end test for the stateful/async flow features on the cdp lane.
 *
 * It exercises the synthetes-style forge lifecycle that previously could not be
 * expressed in a plan and had to be hand-driven:
 *
 *   request POST /start (redirect:'manual')  -> 303 with readable headers;
 *     capture the run id out of the x-run-id header into ${runId};
 *     oracles: status === 303 and location header contains "/done".
 *   pollUntil /poll?id=${runId}              -> templated url uses the captured id;
 *     poll-oracle: jsonPath ready === true (passes on the first iteration);
 *     stored under "p", then a case oracle asserts jsonPath id === "r123" of "p".
 *
 * A real Chromium is launched via Heimdall's public runPlan API and driven
 * against the node:http fixture server. We assert summary.pass === 1.
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
  outDir = await mkdtemp(join(tmpdir(), "heimdall-flow-e2e-"));
});

afterAll(async () => {
  await fixture?.stop();
  if (outDir) {
    await rm(outDir, { recursive: true, force: true }).catch(() => {});
  }
});

describe("stateful flow (capture + manual redirect + pollUntil) end-to-end", () => {
  it(
    "captures an id from a redirect header, templates it into a poll, and passes",
    async () => {
      const plan: Plan = {
        name: "flow-e2e",
        defaultDriver: "cdp",
        cases: [
          {
            id: "forge-lifecycle",
            title: "POST /start -> capture run id -> poll until ready -> assert",
            steps: [
              {
                action: "request",
                url: "/start",
                method: "POST",
                redirect: "manual",
                capture: { runId: { header: "x-run-id" } },
                as: "start",
              },
              {
                action: "pollUntil",
                url: "/poll?id=${runId}",
                oracle: [{ assert: "jsonPath", path: "ready", equals: true }],
                timeoutMs: 5000,
                as: "p",
              },
            ],
            oracle: [
              { assert: "status", equals: 303, of: "start" },
              { assert: "header", name: "location", contains: "/done", of: "start" },
              { assert: "jsonPath", path: "id", equals: "r123", of: "p" },
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
        concurrency: 1,
        driverOverride: "cdp",
      };

      const report = await runPlan(plan, opts);

      if (report.summary.pass !== 1) {
        const detail = report.results
          .map((r) => `${r.id}: ${r.status} — ${r.observed}${r.failures.length ? ` [${r.failures.join("; ")}]` : ""}`)
          .join("\n");
        throw new Error(`expected 1 passing case, got summary=${JSON.stringify(report.summary)}\n${detail}`);
      }

      expect(report.summary.total).toBe(1);
      expect(report.summary.pass).toBe(1);
      expect(report.summary.fail).toBe(0);

      const r = report.results.find((x) => x.id === "forge-lifecycle");
      expect(r?.status).toBe("pass");
      expect(r?.driver).toBe("cdp");
    },
    60_000,
  );
});

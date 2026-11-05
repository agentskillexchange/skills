/**
 * REAL end-to-end test for ROADMAP #7 — setup/teardown fixtures & hooks.
 *
 * Drives actual Chromium through Heimdall's public `runPlan` API against the
 * node:http fixture's in-memory resource CRUD, exercising the three contracts:
 *
 *   1. Per-case lifecycle — a case `setup` creates a resource and captures its id;
 *      the case `steps` verify it exists (oracle status 200 / exists true); the
 *      case `teardown` deletes it. We then ask the server `/resources` and assert
 *      the store is empty, proving BOTH setup AND teardown ran on the same page,
 *      sharing the captured ${rid}.
 *
 *   2. Teardown is best-effort — a PASSING case whose teardown step throws must
 *      stay `pass` (teardown never flips the verdict), with the trouble surfaced
 *      in `notes`.
 *
 *   3. Plan setup failure blocks — when `plan.setup` fails, every runnable case is
 *      marked `blocked` (nothing silently passes) and the exit code stays non-zero.
 */
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterAll, beforeAll, describe, expect, it } from "vitest";

import { runPlan, exitCodeFor, type Plan, type RunOptions } from "../../src/index.js";
import { startFixtureServer, type FixtureServer } from "../fixtures/server.js";

let fixture: FixtureServer;
let outDir: string;

beforeAll(async () => {
  fixture = await startFixtureServer();
  outDir = await mkdtemp(join(tmpdir(), "heimdall-fixtures-e2e-"));
});

afterAll(async () => {
  await fixture?.stop();
  if (outDir) {
    await rm(outDir, { recursive: true, force: true }).catch(() => {});
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

describe("setup/teardown hooks end-to-end", () => {
  it(
    "runs a per-case create-then-delete lifecycle that shares captured ids",
    async () => {
      const plan: Plan = {
        name: "case-lifecycle",
        defaultDriver: "cdp",
        cases: [
          {
            id: "resource-lifecycle",
            title: "setup creates a resource, steps verify it, teardown deletes it",
            setup: [
              { action: "request", url: "/resource", method: "POST", capture: { rid: { jsonPath: "id" } }, as: "made" },
            ],
            steps: [{ action: "request", url: "/resource?id=${rid}", as: "check" }],
            teardown: [{ action: "request", url: "/resource?id=${rid}", method: "DELETE" }],
            oracle: [
              { assert: "status", equals: 200, of: "check" },
              { assert: "jsonPath", path: "exists", equals: true, of: "check" },
            ],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, baseOpts());

      const r = report.results.find((x) => x.id === "resource-lifecycle");
      if (r?.status !== "pass") {
        throw new Error(`expected resource-lifecycle to pass, got ${JSON.stringify(r)}`);
      }
      expect(report.summary.pass).toBe(1);

      // Teardown ran: the resource setup created was deleted, so the store is empty.
      const remaining = (await (await fetch(`${fixture.baseUrl}/resources`)).json()) as { count: number };
      expect(remaining.count).toBe(0);
    },
    60_000,
  );

  it(
    "keeps a passing case green when its teardown step fails (best-effort)",
    async () => {
      const plan: Plan = {
        name: "teardown-best-effort",
        defaultDriver: "cdp",
        cases: [
          {
            id: "teardown-throws",
            title: "case passes; teardown throws and is noted, not fatal",
            steps: [{ action: "request", url: "/api/health", as: "h" }],
            teardown: [{ action: "waitFor", selector: "#this-never-appears", timeoutMs: 250 }],
            oracle: [{ assert: "status", equals: 200, of: "h" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, baseOpts());

      const r = report.results.find((x) => x.id === "teardown-throws");
      expect(r?.status).toBe("pass");
      expect(report.summary.fail).toBe(0);
      // The teardown failure is surfaced honestly without flipping the verdict.
      expect(r?.notes ?? "").toContain("teardown");
      expect(r?.failures ?? []).toHaveLength(0);
    },
    60_000,
  );

  it(
    "runs teardown even after the case FAILS, cleaning up what setup created",
    async () => {
      const plan: Plan = {
        name: "teardown-after-failure",
        defaultDriver: "cdp",
        cases: [
          {
            id: "failing-case-still-tears-down",
            title: "setup creates a resource; the oracle fails; teardown must still delete it",
            setup: [
              { action: "request", url: "/resource", method: "POST", capture: { rid: { jsonPath: "id" } }, as: "made" },
            ],
            steps: [{ action: "request", url: "/resource?id=${rid}", as: "check" }],
            teardown: [{ action: "request", url: "/resource?id=${rid}", method: "DELETE" }],
            // Deliberately wrong: the resource exists, but we assert it does NOT.
            oracle: [{ assert: "jsonPath", path: "exists", equals: false, of: "check" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, baseOpts());

      const r = report.results.find((x) => x.id === "failing-case-still-tears-down");
      // The oracle failed, so the case is fail (not error, not silently passed).
      expect(r?.status).toBe("fail");
      expect(report.summary.fail).toBe(1);
      // Teardown ran despite the failure: the created resource was deleted.
      const remaining = (await (await fetch(`${fixture.baseUrl}/resources`)).json()) as { count: number };
      expect(remaining.count).toBe(0);
    },
    60_000,
  );

  it(
    "skips the oracles when a per-case setup step fails (the case is fail, not a false pass)",
    async () => {
      const plan: Plan = {
        name: "setup-skips-oracles",
        defaultDriver: "cdp",
        cases: [
          {
            id: "setup-fails-skip-oracles",
            title: "a failing setup step short-circuits steps + oracles",
            // This setup step cannot succeed (no such element on about:blank).
            setup: [{ action: "waitFor", selector: "#never", timeoutMs: 250 }],
            steps: [{ action: "request", url: "/api/health", as: "h" }],
            // If the oracles RAN, this would add a "no response captured" failure,
            // because the steps (which capture `h`) never executed. Its absence
            // proves the oracles were skipped — only the setup failure is reported.
            oracle: [{ assert: "status", equals: 200, of: "h" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, baseOpts());

      const r = report.results.find((x) => x.id === "setup-fails-skip-oracles");
      expect(r?.status).toBe("fail");
      // Exactly one failure: the setup error. The oracle was never evaluated.
      expect(r?.failures).toHaveLength(1);
      expect(r?.failures[0]).toContain("setup step");
      expect(r?.failures.join(" ")).not.toContain("no response captured");
    },
    60_000,
  );

  it(
    "runs plan setup/teardown UNGATED — write/delete hooks execute without --allow-risk",
    async () => {
      // Plan-level hooks are trusted, author-controlled fixtures and run UNGATED:
      // they are NOT subject to the risk/--allow-risk gate that protects cases. Here
      // the hooks perform write (POST) and delete (DELETE) operations that, at CASE
      // level with risk:"destructive", would be `blocked` without --allow-risk. We
      // run with allowRisk:false and prove the hooks still executed.
      const plan: Plan = {
        name: "plan-hooks-ungated",
        defaultDriver: "cdp",
        setup: [{ action: "request", url: "/resource", method: "POST" }],
        teardown: [
          // Best-effort cleanup that runs ungated AND leaves an observable effect:
          // a bulk DELETE that empties the store, so the test below can prove the
          // plan-level teardown actually executed (not just plan.setup).
          { action: "request", url: "/resources", method: "DELETE" },
        ],
        cases: [
          {
            id: "observes-hook-write",
            // A read-only case: the WRITE was done by the ungated plan.setup hook.
            steps: [{ action: "request", url: "/resources", as: "list" }],
            oracle: [
              { assert: "status", equals: 200, of: "list" },
              // setup created at least one resource — so the hook ran without the gate.
              { assert: "jsonPath", path: "count", equals: 1, of: "list" },
            ],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, baseOpts());

      const r = report.results.find((x) => x.id === "observes-hook-write");
      if (r?.status !== "pass") {
        throw new Error(`expected the case to pass (proving the ungated setup hook ran), got ${JSON.stringify(r)}`);
      }
      expect(report.summary.pass).toBe(1);
      expect(report.summary.blocked).toBe(0);

      // Prove the ungated plan-level TEARDOWN also ran: it bulk-deleted the store,
      // so after the run the resource setup created is gone.
      const after = (await (await fetch(`${fixture.baseUrl}/resources`)).json()) as { count: number };
      expect(after.count).toBe(0);
    },
    60_000,
  );

  it(
    "blocks every runnable case when plan.setup fails",
    async () => {
      const plan: Plan = {
        name: "plan-setup-fails",
        defaultDriver: "cdp",
        // A plan-level setup step that cannot succeed (no such element on about:blank).
        setup: [{ action: "waitFor", selector: "#never", timeoutMs: 250 }],
        cases: [
          {
            id: "case-a",
            steps: [{ action: "request", url: "/api/health", as: "h" }],
            oracle: [{ assert: "status", equals: 200, of: "h" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "case-b",
            steps: [{ action: "request", url: "/api/health", as: "h" }],
            oracle: [{ assert: "status", equals: 200, of: "h" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, baseOpts());

      expect(report.summary.total).toBe(2);
      expect(report.summary.blocked).toBe(2);
      expect(report.summary.pass).toBe(0);
      for (const r of report.results) {
        expect(r.status).toBe("blocked");
        expect(r.notes ?? "").toContain("plan setup failed");
      }
      // Honesty gate: a plan that ran nothing must not exit zero.
      expect(exitCodeFor(report)).toBe(1);
    },
    60_000,
  );
});

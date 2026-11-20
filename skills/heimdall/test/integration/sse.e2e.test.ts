/**
 * REAL end-to-end test for the `sse` step + eventCount oracle.
 *
 * Launches actual Chromium through Heimdall's public `runPlan` API and opens an
 * EventSource against the fixture's `/events` route, which emits exactly three
 * `data:` frames and then closes the stream. The `sse` step collects the message
 * events into an aggregate (events array under json, newline-joined data under
 * bodyText); the eventCount/bodyContains oracles decide pass/fail against it.
 *
 *   pass case -> sse /events (expect 3); assert eventCount equals 3 and that the
 *                aggregate body carries the streamed payload.
 *   fail case -> same stream; assert eventCount min 5 (it isn't) -> the oracle
 *                must honestly fail, proving the count reflects the real stream.
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
  outDir = await mkdtemp(join(tmpdir(), "heimdall-sse-e2e-"));
});

afterAll(async () => {
  await fixture?.stop();
  if (outDir) {
    await rm(outDir, { recursive: true, force: true }).catch(() => {});
  }
});

describe("sse step end-to-end", () => {
  it(
    "opens an EventSource, collects events, and evaluates eventCount oracles honestly",
    async () => {
      const sseStep = { action: "sse" as const, url: "/events", events: 3, timeoutMs: 8000, as: "stream" };
      const plan: Plan = {
        name: "sse-e2e",
        defaultDriver: "cdp",
        cases: [
          {
            id: "sse-three-events",
            title: "collects the three streamed events and asserts on them",
            steps: [sseStep],
            oracle: [
              { assert: "eventCount", equals: 3, of: "stream" },
              { assert: "eventCount", min: 1, of: "stream" },
              { assert: "bodyContains", value: '"n":1', of: "stream" },
              { assert: "jsonPath", path: "2.id", exists: true, of: "stream" },
            ],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "sse-demands-too-many",
            title: "demanding more events than the stream emits must fail honestly",
            steps: [sseStep],
            oracle: [{ assert: "eventCount", min: 5, of: "stream" }],
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

      const pass = report.results.find((r) => r.id === "sse-three-events");
      const fail = report.results.find((r) => r.id === "sse-demands-too-many");

      // Surface detail if the happy case did not pass as expected.
      if (pass?.status !== "pass") {
        throw new Error(`expected sse-three-events to pass, got ${JSON.stringify(pass)}`);
      }

      expect(report.summary.total).toBe(2);
      expect(report.summary.pass).toBe(1);
      expect(report.summary.fail).toBe(1);

      expect(pass.status).toBe("pass");
      expect(pass.driver).toBe("cdp");

      expect(fail?.status).toBe("fail");
      // The count reflected the real stream (3 events, not the demanded 5).
      expect(fail?.failures.join(" ")).toContain("eventCount");
      expect(fail?.failures.join(" ")).toContain("got 3");
    },
    60_000,
  );

  it(
    "collects fewer events than requested then times out, recording what arrived (status 200)",
    async () => {
      // /events-one emits a single event then holds the stream open; asking for 3
      // with a short budget must resolve with the one event collected, not hang.
      const plan: Plan = {
        name: "sse-partial",
        defaultDriver: "cdp",
        cases: [
          {
            id: "sse-partial-collect",
            steps: [{ action: "sse", url: "/events-one", events: 3, timeoutMs: 2000, as: "stream" }],
            oracle: [
              { assert: "eventCount", equals: 1, of: "stream" },
              { assert: "bodyContains", value: '"n":1', of: "stream" },
            ],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "sse-partial-demands-three",
            steps: [{ action: "sse", url: "/events-one", events: 3, timeoutMs: 2000, as: "stream" }],
            oracle: [{ assert: "eventCount", min: 3, of: "stream" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, {
        outDir,
        baseUrl: fixture.baseUrl,
        allowRisk: false,
        headed: false,
        concurrency: 2,
        driverOverride: "cdp",
      });

      const got = report.results.find((r) => r.id === "sse-partial-collect");
      if (got?.status !== "pass") {
        throw new Error(`expected sse-partial-collect to pass, got ${JSON.stringify(got)}`);
      }
      // The one collected event has data, so the stream recorded an OK (200) response.
      const captured = got.evidence.responses.find((x) => x.name === "stream");
      expect(captured?.status).toBe(200);

      const demanded = report.results.find((r) => r.id === "sse-partial-demands-three");
      expect(demanded?.status).toBe("fail");
      expect(demanded?.failures.join(" ")).toContain("expected at least 3, got 1");
    },
    60_000,
  );

  it(
    "times out with zero events and records a status-0 (no-data) stream response",
    async () => {
      // /events-hang opens the stream but sends nothing; the client collects no
      // events and times out. The sse step records status 0 (no data ever arrived).
      const plan: Plan = {
        name: "sse-empty",
        defaultDriver: "cdp",
        cases: [
          {
            id: "sse-zero-events",
            steps: [{ action: "sse", url: "/events-hang", events: 2, timeoutMs: 1500, as: "stream" }],
            // Demanding even one event must fail honestly against an empty stream.
            oracle: [{ assert: "eventCount", min: 1, of: "stream" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, {
        outDir,
        baseUrl: fixture.baseUrl,
        allowRisk: false,
        headed: false,
        concurrency: 1,
        driverOverride: "cdp",
      });

      const r = report.results.find((x) => x.id === "sse-zero-events");
      expect(r?.status).toBe("fail");
      expect(r?.failures.join(" ")).toContain("expected at least 1, got 0");
      // Zero events -> the recorded stream response carries status 0 (captured honestly).
      const captured = r?.evidence.responses.find((x) => x.name === "stream");
      expect(captured?.status).toBe(0);
    },
    60_000,
  );
});

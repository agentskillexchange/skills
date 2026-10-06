import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { describe, it, expect, beforeEach, afterEach } from "vitest";
import { PNG } from "pngjs";
import { evaluateOracles, getByPath, type Observation, type ObservedResponse } from "../src/oracle.js";
import { applyVars } from "../src/execute.js";
import type { AxeResultLike } from "../src/a11y.js";
import type { Oracle } from "../src/schema.js";

function mockObs(over: Partial<Observation> & { responses?: Record<string, ObservedResponse> } = {}): Observation {
  const responses = over.responses ?? {};
  return {
    url: over.url ?? (() => "http://localhost/app/dashboard"),
    title: over.title ?? (async () => "Dashboard · MyApp"),
    isVisible: over.isVisible ?? (async () => true),
    textOf: over.textOf ?? (async () => "Welcome back"),
    count: over.count ?? (async () => 1),
    attribute: over.attribute ?? (async () => null),
    consoleErrors: over.consoleErrors ?? (() => []),
    response: over.response ?? ((name) => (name ? responses[name] : Object.values(responses).at(-1))),
    evaluate: over.evaluate ?? (async () => true),
    axe: over.axe ?? (async () => ({ violations: [] })),
    screenshot: over.screenshot ?? (async () => solidPng(2, 2, [0, 0, 0, 255])),
  };
}

/** Encode a `width`×`height` PNG filled with a single RGBA colour. */
function solidPng(width: number, height: number, rgba: [number, number, number, number]): Buffer {
  const png = new PNG({ width, height });
  for (let i = 0; i < width * height; i++) {
    png.data[i * 4] = rgba[0];
    png.data[i * 4 + 1] = rgba[1];
    png.data[i * 4 + 2] = rgba[2];
    png.data[i * 4 + 3] = rgba[3];
  }
  return PNG.sync.write(png);
}

const resp = (over: Partial<ObservedResponse>): ObservedResponse => ({
  url: "http://localhost/api/health",
  method: "GET",
  status: 200,
  ok: true,
  headers: { "content-type": "application/json; charset=utf-8" },
  bodyText: "{}",
  json: {},
  ...over,
});

describe("getByPath", () => {
  it("resolves dot paths and $-prefixed paths", () => {
    const obj = { data: { user: { id: 7 } }, ok: true };
    expect(getByPath(obj, "data.user.id")).toBe(7);
    expect(getByPath(obj, "$.ok")).toBe(true);
    expect(getByPath(obj, "$")).toEqual(obj);
    expect(getByPath(obj, "missing.path")).toBeUndefined();
  });
});

describe("applyVars", () => {
  it("substitutes known tokens and leaves unknown ones verbatim", () => {
    const vars = { runId: "r123", name: "alice" };
    expect(applyVars("/poll?id=${runId}", vars)).toBe("/poll?id=r123");
    expect(applyVars("hi ${name}, run ${runId}", vars)).toBe("hi alice, run r123");
    // Unknown token is left as-is, not blanked.
    expect(applyVars("/x/${missing}/y", vars)).toBe("/x/${missing}/y");
  });

  it("is a no-op when there is no token", () => {
    const vars = { runId: "r123" };
    expect(applyVars("/static/path", vars)).toBe("/static/path");
    expect(applyVars("", vars)).toBe("");
  });

  it("resolves ${env.X} from process.env, blanks unknown env vars, leaves capture vars alone", () => {
    const KEY = "HEIMDALL_TEST_TOKEN_X";
    delete process.env[KEY];
    process.env[KEY] = "s3cr3t";
    try {
      // Set env var is interpolated from process.env, not the capture bag.
      expect(applyVars("Bearer ${env.HEIMDALL_TEST_TOKEN_X}", {})).toBe("Bearer s3cr3t");
      // Unset env var resolves to an empty string (does not crash, does not leave the token).
      expect(applyVars("Bearer ${env.HEIMDALL_TEST_MISSING}", {})).toBe("Bearer ");
      // Capture vars still win for non-env tokens; env. prefix never reads the bag.
      expect(applyVars("${runId} ${env.HEIMDALL_TEST_TOKEN_X}", { runId: "r1" })).toBe("r1 s3cr3t");
    } finally {
      delete process.env[KEY];
    }
  });
});

describe("evaluateOracles", () => {
  it("passes when every oracle holds", async () => {
    const oracles: Oracle[] = [
      { assert: "visible", selector: ".dashboard" },
      { assert: "urlContains", value: "/app" },
      { assert: "noConsoleErrors" },
    ];
    const out = await evaluateOracles(oracles, mockObs());
    expect(out.passed).toBe(true);
    expect(out.failures).toHaveLength(0);
  });

  it("fails visible when the element is not visible", async () => {
    const out = await evaluateOracles([{ assert: "visible", selector: "#x" }], mockObs({ isVisible: async () => false }));
    expect(out.passed).toBe(false);
    expect(out.failures[0]).toContain("not visible");
  });

  it("checks status and jsonPath against a named response", async () => {
    const obs = mockObs({ responses: { health: resp({ status: 200, json: { ok: true, n: 3 } }) } });
    const ok = await evaluateOracles(
      [
        { assert: "status", equals: 200, of: "health" },
        { assert: "jsonPath", path: "ok", equals: true, of: "health" },
        { assert: "jsonPath", path: "n", equals: 3, of: "health" },
      ],
      obs,
    );
    expect(ok.passed).toBe(true);

    const bad = await evaluateOracles([{ assert: "status", equals: 201, of: "health" }], obs);
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("expected 201, got 200");
  });

  it("reports a missing response instead of throwing", async () => {
    const out = await evaluateOracles([{ assert: "status", equals: 200, of: "nope" }], mockObs());
    expect(out.passed).toBe(false);
    expect(out.failures[0]).toContain("no response captured");
  });

  it("flags console errors", async () => {
    const out = await evaluateOracles(
      [{ assert: "noConsoleErrors" }],
      mockObs({ consoleErrors: () => ["TypeError: x is undefined"] }),
    );
    expect(out.passed).toBe(false);
    expect(out.failures[0]).toContain("console error");
  });

  it("checks titleContains", async () => {
    const ok = await evaluateOracles([{ assert: "titleContains", value: "Dashboard" }], mockObs());
    expect(ok.passed).toBe(true);
    const bad = await evaluateOracles([{ assert: "titleContains", value: "Login" }], mockObs());
    expect(bad.passed).toBe(false);
  });

  it("checks count", async () => {
    const obs = mockObs({ count: async () => 3 });
    expect((await evaluateOracles([{ assert: "count", selector: ".row", equals: 3 }], obs)).passed).toBe(true);
    const bad = await evaluateOracles([{ assert: "count", selector: ".row", equals: 5 }], obs);
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("expected 5, got 3");
  });

  it("checks attribute equals and contains, and missing attribute", async () => {
    const obs = mockObs({ attribute: async () => "/app/home?x=1" });
    expect((await evaluateOracles([{ assert: "attribute", selector: "a", name: "href", contains: "/app" }], obs)).passed).toBe(true);
    expect((await evaluateOracles([{ assert: "attribute", selector: "a", name: "href", equals: "/app/home?x=1" }], obs)).passed).toBe(true);
    const missing = await evaluateOracles([{ assert: "attribute", selector: "a", name: "href" }], mockObs());
    expect(missing.passed).toBe(false);
    expect(missing.failures[0]).toContain("no \"href\"");
  });

  it("checks statusIn for a member and a non-member status", async () => {
    const obs = mockObs({ responses: { r: resp({ status: 204 }) } });
    expect(
      (await evaluateOracles([{ assert: "statusIn", values: [200, 201, 204], of: "r" }], obs)).passed,
    ).toBe(true);
    const bad = await evaluateOracles([{ assert: "statusIn", values: [200, 201], of: "r" }], obs);
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("expected one of [200, 201], got 204");
    const missing = await evaluateOracles([{ assert: "statusIn", values: [200], of: "nope" }], mockObs());
    expect(missing.passed).toBe(false);
    expect(missing.failures[0]).toContain("no response captured");
  });

  it("checks statusRange inclusively (in and out of range)", async () => {
    const inRange = mockObs({ responses: { r: resp({ status: 404 }) } });
    expect(
      (await evaluateOracles([{ assert: "statusRange", min: 200, max: 499, of: "r" }], inRange)).passed,
    ).toBe(true);
    const outRange = mockObs({ responses: { r: resp({ status: 500 }) } });
    const bad = await evaluateOracles([{ assert: "statusRange", min: 200, max: 499, of: "r" }], outRange);
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("expected 200..499, got 500");
  });

  it("checks attribute exists (present and absent)", async () => {
    const present = mockObs({ attribute: async () => "" });
    expect(
      (await evaluateOracles([{ assert: "attribute", selector: "input", name: "required", exists: true }], present)).passed,
    ).toBe(true);
    const absent = mockObs({ attribute: async () => null });
    expect(
      (await evaluateOracles([{ assert: "attribute", selector: "input", name: "required", exists: false }], absent)).passed,
    ).toBe(true);
    // exists:true fails when absent
    const wantPresent = await evaluateOracles(
      [{ assert: "attribute", selector: "input", name: "required", exists: true }],
      absent,
    );
    expect(wantPresent.passed).toBe(false);
    expect(wantPresent.failures[0]).toContain("expected exists=true, got false");
    // exists:false fails when present
    const wantAbsent = await evaluateOracles(
      [{ assert: "attribute", selector: "input", name: "required", exists: false }],
      present,
    );
    expect(wantAbsent.passed).toBe(false);
  });

  it("checks attribute matches (match and non-match, plus absent)", async () => {
    const obs = mockObs({ attribute: async () => "aria-expanded-true" });
    expect(
      (await evaluateOracles([{ assert: "attribute", selector: "div", name: "class", matches: "expanded" }], obs)).passed,
    ).toBe(true);
    const bad = await evaluateOracles([{ assert: "attribute", selector: "div", name: "class", matches: "^collapsed$" }], obs);
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("did not match");
    const missing = await evaluateOracles(
      [{ assert: "attribute", selector: "div", name: "class", matches: "x" }],
      mockObs({ attribute: async () => null }),
    );
    expect(missing.passed).toBe(false);
    expect(missing.failures[0]).toContain('has no "class"');
  });

  it("checks titleMatches against a RegExp pattern", async () => {
    expect((await evaluateOracles([{ assert: "titleMatches", pattern: "·\\s*MyApp$" }], mockObs())).passed).toBe(true);
    const bad = await evaluateOracles([{ assert: "titleMatches", pattern: "^Login" }], mockObs());
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("did not match");
  });

  it("checks urlMatches against a RegExp pattern", async () => {
    expect((await evaluateOracles([{ assert: "urlMatches", pattern: "/app/\\w+$" }], mockObs())).passed).toBe(true);
    const bad = await evaluateOracles([{ assert: "urlMatches", pattern: "/login$" }], mockObs());
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("did not match");
  });

  it("checks responseTime against a captured response", async () => {
    const fast = mockObs({ responses: { api: resp({ durationMs: 120 }) } });
    expect((await evaluateOracles([{ assert: "responseTime", maxMs: 500, of: "api" }], fast)).passed).toBe(true);
    const slow = mockObs({ responses: { api: resp({ durationMs: 900 }) } });
    const bad = await evaluateOracles([{ assert: "responseTime", maxMs: 500, of: "api" }], slow);
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("exceeded 500ms");
  });

  it("checks header equals, contains, and a missing header", async () => {
    const obs = mockObs({
      responses: {
        h: resp({ headers: { "content-type": "application/json; charset=utf-8", "x-token": "abc" } }),
      },
    });
    expect(
      (await evaluateOracles([{ assert: "header", name: "Content-Type", contains: "application/json", of: "h" }], obs))
        .passed,
    ).toBe(true);
    expect(
      (await evaluateOracles([{ assert: "header", name: "x-token", equals: "abc", of: "h" }], obs)).passed,
    ).toBe(true);
    const missing = await evaluateOracles([{ assert: "header", name: "x-absent", of: "h" }], obs);
    expect(missing.passed).toBe(false);
    expect(missing.failures[0]).toContain("absent");
    const wrong = await evaluateOracles([{ assert: "header", name: "x-token", equals: "nope", of: "h" }], obs);
    expect(wrong.passed).toBe(false);
  });

  it("checks jsonType for every type and reports mismatches", async () => {
    const obs = mockObs({
      responses: {
        r: resp({
          json: { s: "hi", n: 3, b: true, arr: [1, 2], obj: { a: 1 }, nul: null },
        }),
      },
    });
    const cases: [string, string][] = [
      ["s", "string"],
      ["n", "number"],
      ["b", "boolean"],
      ["arr", "array"],
      ["obj", "object"],
      ["nul", "null"],
    ];
    for (const [path, type] of cases) {
      const out = await evaluateOracles(
        [{ assert: "jsonType", path, type: type as never, of: "r" }],
        obs,
      );
      expect(out.passed, `${path} should be ${type}`).toBe(true);
    }
    const bad = await evaluateOracles([{ assert: "jsonType", path: "n", type: "string", of: "r" }], obs);
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("expected string, got number");
  });

  it("checks nonEmpty for a path (string/array) and for the raw body", async () => {
    const obs = mockObs({
      responses: {
        r: resp({ bodyText: '{"s":"x","arr":[1],"empty":"","none":[]}', json: { s: "x", arr: [1], empty: "", none: [] } }),
      },
    });
    expect((await evaluateOracles([{ assert: "nonEmpty", path: "s", of: "r" }], obs)).passed).toBe(true);
    expect((await evaluateOracles([{ assert: "nonEmpty", path: "arr", of: "r" }], obs)).passed).toBe(true);
    expect((await evaluateOracles([{ assert: "nonEmpty", of: "r" }], obs)).passed).toBe(true);
    const emptyStr = await evaluateOracles([{ assert: "nonEmpty", path: "empty", of: "r" }], obs);
    expect(emptyStr.passed).toBe(false);
    const emptyArr = await evaluateOracles([{ assert: "nonEmpty", path: "none", of: "r" }], obs);
    expect(emptyArr.passed).toBe(false);
    const emptyBody = mockObs({ responses: { r: resp({ bodyText: "" }) } });
    expect((await evaluateOracles([{ assert: "nonEmpty", of: "r" }], emptyBody)).passed).toBe(false);
  });

  it("checks bodyContains", async () => {
    const obs = mockObs({ responses: { r: resp({ bodyText: '{"hello":"world"}' }) } });
    expect((await evaluateOracles([{ assert: "bodyContains", value: "world", of: "r" }], obs)).passed).toBe(true);
    const bad = await evaluateOracles([{ assert: "bodyContains", value: "nope", of: "r" }], obs);
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain('did not contain "nope"');
  });

  it("checks jsonMatch against a RegExp pattern", async () => {
    const obs = mockObs({ responses: { r: resp({ json: { email: "a@b.com", n: 5 } }) } });
    expect(
      (await evaluateOracles([{ assert: "jsonMatch", path: "email", pattern: "^[^@]+@[^@]+$", of: "r" }], obs)).passed,
    ).toBe(true);
    const bad = await evaluateOracles([{ assert: "jsonMatch", path: "email", pattern: "^\\d+$", of: "r" }], obs);
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("did not match");
    const notString = await evaluateOracles([{ assert: "jsonMatch", path: "n", pattern: ".", of: "r" }], obs);
    expect(notString.passed).toBe(false);
    expect(notString.failures[0]).toContain("expected a string");
  });

  it("evaluates evalTruthy", async () => {
    const truthy = await evaluateOracles([{ assert: "evalTruthy", expression: "1" }], mockObs({ evaluate: async () => 1 }));
    expect(truthy.passed).toBe(true);
    const falsy = await evaluateOracles(
      [{ assert: "evalTruthy", expression: "0" }],
      mockObs({ evaluate: async () => 0 }),
    );
    expect(falsy.passed).toBe(false);
  });

  it("checks errorRate against a load aggregate", async () => {
    const load = { count: 10, errors: 2, errorRate: 0.2, minMs: 1, p50: 5, p95: 9, p99: 10, maxMs: 10 };
    const obs = mockObs({ responses: { lt: resp({ load }) } });
    expect((await evaluateOracles([{ assert: "errorRate", max: 0.25, of: "lt" }], obs)).passed).toBe(true);
    // boundary: <= is inclusive
    expect((await evaluateOracles([{ assert: "errorRate", max: 0.2, of: "lt" }], obs)).passed).toBe(true);
    const bad = await evaluateOracles([{ assert: "errorRate", max: 0.1, of: "lt" }], obs);
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("20.0% (2/10) exceeded 10.0%");
    // a non-load response has no aggregate
    const noLoad = await evaluateOracles([{ assert: "errorRate", max: 0.1 }], mockObs({ responses: { r: resp({}) } }));
    expect(noLoad.passed).toBe(false);
    expect(noLoad.failures[0]).toContain("no load stats");
  });

  it("fails errorRate when the real rate is the smallest amount over the bound", async () => {
    const load = { count: 1000, errors: 201, errorRate: 0.201, minMs: 1, p50: 5, p95: 9, p99: 10, maxMs: 10 };
    const obs = mockObs({ responses: { lt: resp({ load }) } });
    // 0.201 > 0.20 -> must fail; the boundary is a strict <=, not a rounded compare.
    const bad = await evaluateOracles([{ assert: "errorRate", max: 0.2, of: "lt" }], obs);
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("(201/1000)");
    // Exactly at the bound passes (inclusive).
    expect((await evaluateOracles([{ assert: "errorRate", max: 0.201, of: "lt" }], obs)).passed).toBe(true);
  });

  it("passes percentile at the exact boundary and reports no load stats for a plain response", async () => {
    const load = { count: 5, errors: 0, errorRate: 0, minMs: 1, p50: 5, p95: 30, p99: 48, maxMs: 60 };
    const obs = mockObs({ responses: { lt: resp({ load }) } });
    // maxMs === the percentile value is inclusive.
    expect((await evaluateOracles([{ assert: "percentile", p: 95, maxMs: 30, of: "lt" }], obs)).passed).toBe(true);
    expect((await evaluateOracles([{ assert: "percentile", p: "max", maxMs: 60, of: "lt" }], obs)).passed).toBe(true);
    // A captured-but-non-load response cannot satisfy a percentile oracle.
    const noLoad = await evaluateOracles(
      [{ assert: "percentile", p: 95, maxMs: 10, of: "plain" }],
      mockObs({ responses: { plain: resp({}) } }),
    );
    expect(noLoad.passed).toBe(false);
    expect(noLoad.failures[0]).toContain("no load stats");
  });

  it("checks percentile (p50/p95/p99/max) against a load aggregate", async () => {
    const load = { count: 10, errors: 0, errorRate: 0, minMs: 1, p50: 5, p95: 30, p99: 48, maxMs: 60 };
    const obs = mockObs({ responses: { lt: resp({ load }) } });
    expect((await evaluateOracles([{ assert: "percentile", p: 95, maxMs: 30, of: "lt" }], obs)).passed).toBe(true);
    expect((await evaluateOracles([{ assert: "percentile", p: 50, maxMs: 10, of: "lt" }], obs)).passed).toBe(true);
    expect((await evaluateOracles([{ assert: "percentile", p: 99, maxMs: 50, of: "lt" }], obs)).passed).toBe(true);
    expect((await evaluateOracles([{ assert: "percentile", p: "max", maxMs: 60, of: "lt" }], obs)).passed).toBe(true);
    const bad = await evaluateOracles([{ assert: "percentile", p: 95, maxMs: 20, of: "lt" }], obs);
    expect(bad.passed).toBe(false);
    expect(bad.failures[0]).toContain("p95: 30ms exceeded 20ms");
    const missing = await evaluateOracles([{ assert: "percentile", p: 95, maxMs: 10, of: "nope" }], obs);
    expect(missing.passed).toBe(false);
    expect(missing.failures[0]).toContain("no response captured");
  });

  it("checks eventCount against an sse aggregate", async () => {
    const events = [
      { event: "message", data: '{"n":1}', id: "1" },
      { event: "message", data: '{"n":2}', id: "2" },
      { event: "message", data: '{"n":3}', id: "3" },
    ];
    const obs = mockObs({ responses: { stream: resp({ events, json: events, bodyText: events.map((e) => e.data).join("\n") }) } });
    expect((await evaluateOracles([{ assert: "eventCount", min: 1, of: "stream" }], obs)).passed).toBe(true);
    expect((await evaluateOracles([{ assert: "eventCount", equals: 3, of: "stream" }], obs)).passed).toBe(true);
    expect((await evaluateOracles([{ assert: "eventCount", min: 3, equals: 3, of: "stream" }], obs)).passed).toBe(true);
    // bodyContains / jsonPath work over the sse aggregate (events array under json).
    expect((await evaluateOracles([{ assert: "bodyContains", value: '"n":2', of: "stream" }], obs)).passed).toBe(true);
    expect((await evaluateOracles([{ assert: "jsonPath", path: "0.id", equals: "1", of: "stream" }], obs)).passed).toBe(true);

    const tooFew = await evaluateOracles([{ assert: "eventCount", min: 5, of: "stream" }], obs);
    expect(tooFew.passed).toBe(false);
    expect(tooFew.failures[0]).toContain("expected at least 5, got 3");

    const wrongExact = await evaluateOracles([{ assert: "eventCount", equals: 2, of: "stream" }], obs);
    expect(wrongExact.passed).toBe(false);
    expect(wrongExact.failures[0]).toContain("expected exactly 2, got 3");

    // min is satisfied (>=1) but the exact equals is not — equals is checked first,
    // so the single failure cites the equals mismatch, proving both clauses are ANDed.
    const minOkEqualsBad = await evaluateOracles([{ assert: "eventCount", min: 1, equals: 5, of: "stream" }], obs);
    expect(minOkEqualsBad.passed).toBe(false);
    expect(minOkEqualsBad.failures).toHaveLength(1);
    expect(minOkEqualsBad.failures[0]).toContain("expected exactly 5, got 3");

    // Zero collected events: eventCount min 1 must fail honestly (the sse-timeout case).
    const empty = mockObs({ responses: { s: resp({ events: [], json: [], bodyText: "" }) } });
    const zero = await evaluateOracles([{ assert: "eventCount", min: 1, of: "s" }], empty);
    expect(zero.passed).toBe(false);
    expect(zero.failures[0]).toContain("expected at least 1, got 0");

    // A response that isn't an sse aggregate carries no events.
    const noEvents = await evaluateOracles([{ assert: "eventCount", min: 1 }], mockObs({ responses: { r: resp({}) } }));
    expect(noEvents.passed).toBe(false);
    expect(noEvents.failures[0]).toContain("no events");

    const missing = await evaluateOracles([{ assert: "eventCount", min: 1, of: "nope" }], obs);
    expect(missing.passed).toBe(false);
    expect(missing.failures[0]).toContain("no response captured");
  });

  it("fails a bounds-less eventCount (defence-in-depth past parse) instead of passing vacuously", async () => {
    // The schema rejects this at parse time; but a hand-built oracle could bypass
    // parsing, so evalOne must FAIL it rather than fall through to a (falsy) PASS.
    const events = [{ event: "message", data: "{}", id: "1" }];
    const obs = mockObs({ responses: { stream: resp({ events, json: events }) } });
    const vacuous = await evaluateOracles(
      // Cast: this shape is unconstructable through the schema, which is the point.
      [{ assert: "eventCount", of: "stream" } as unknown as Parameters<typeof evaluateOracles>[0][number]],
      obs,
    );
    expect(vacuous.passed).toBe(false);
    expect(vacuous.failures[0]).toContain("at least one of min/equals");
  });

  it("returns a per-oracle record for every oracle, mirroring failures over mixed pass/fail", async () => {
    const obs = mockObs({
      isVisible: async () => true,
      count: async () => 2,
      responses: { health: resp({ status: 500 }) },
    });
    const oracles: Oracle[] = [
      { assert: "visible", selector: ".dashboard" }, // pass
      { assert: "status", equals: 200, of: "health" }, // fail
      { assert: "count", selector: ".row", equals: 2 }, // pass
      { assert: "status", equals: 200, of: "nope" }, // fail (missing response)
    ];
    const out = await evaluateOracles(oracles, obs);

    // The legacy { passed, failures } view is unchanged.
    expect(out.passed).toBe(false);
    expect(out.failures).toEqual([
      "status: expected 200, got 500",
      'status: no response captured named "nope"',
    ]);

    // records: one per oracle, in order, with the right kind and pass flag.
    expect(out.records).toHaveLength(4);
    expect(out.records.map((r) => r.kind)).toEqual(["visible", "status", "count", "status"]);
    expect(out.records.map((r) => r.passed)).toEqual([true, false, true, false]);

    // The failing records' details are exactly `failures`, in the same order.
    expect(out.records.filter((r) => !r.passed).map((r) => r.detail)).toEqual(out.failures);

    // Passing records carry a CONCRETE detail (the observed value/selector), not a vacuous "passed".
    const visibleRec = out.records[0];
    expect(visibleRec.detail).toContain(".dashboard");
    expect(visibleRec.detail).toContain("is visible");
    const countRec = out.records[2];
    expect(countRec.detail).toContain(".row");
    expect(countRec.detail).toContain("2");
  });

  it("records a passing detail even when every oracle holds", async () => {
    const out = await evaluateOracles(
      [{ assert: "urlContains", value: "/app" }],
      mockObs(),
    );
    expect(out.passed).toBe(true);
    expect(out.failures).toHaveLength(0);
    expect(out.records).toHaveLength(1);
    expect(out.records[0]).toMatchObject({ kind: "urlContains", passed: true });
    expect(out.records[0].detail).toContain("/app");
  });
});

describe("a11y oracle", () => {
  const violation = (impact: "minor" | "moderate" | "serious" | "critical") => ({
    id: `rule-${impact}`,
    impact,
  });

  it("passes when no violation reaches maxImpact (below threshold)", async () => {
    const result: AxeResultLike = { violations: [violation("minor"), violation("moderate")] };
    const obs = mockObs({ axe: async () => result });
    const out = await evaluateOracles([{ assert: "a11y", maxImpact: "serious" }], obs);
    expect(out.passed).toBe(true);
    expect(out.records).toHaveLength(1);
    expect(out.records[0]).toMatchObject({ kind: "a11y", passed: true });
    expect(out.records[0].detail).toContain("No accessibility violations");
  });

  it("fails on a violation at the threshold and reports a summary in the detail", async () => {
    const result: AxeResultLike = { violations: [violation("serious")] };
    const obs = mockObs({ axe: async () => result });
    const out = await evaluateOracles([{ assert: "a11y", maxImpact: "serious" }], obs);
    expect(out.passed).toBe(false);
    expect(out.failures[0]).toContain("1 accessibility violation");
    expect(out.failures[0]).toContain("rule-serious");
    // The failing record's detail mirrors the failure summary.
    expect(out.records[0]).toMatchObject({ kind: "a11y", passed: false });
    expect(out.records[0].detail).toBe(out.failures[0]);
  });

  it("fails on a violation above the threshold", async () => {
    const result: AxeResultLike = { violations: [violation("critical")] };
    const obs = mockObs({ axe: async () => result });
    const out = await evaluateOracles([{ assert: "a11y", maxImpact: "serious" }], obs);
    expect(out.passed).toBe(false);
    expect(out.failures[0]).toContain("critical");
  });

  it("forwards include/exclude selectors to the driver's axe scan", async () => {
    let seen: { include?: string[]; exclude?: string[] } | undefined;
    const obs = mockObs({
      axe: async (opts) => {
        seen = opts;
        return { violations: [] };
      },
    });
    await evaluateOracles([{ assert: "a11y", maxImpact: "serious", include: ["main"], exclude: ["#ad"] }], obs);
    expect(seen).toEqual({ include: ["main"], exclude: ["#ad"] });
  });
});

describe("screenshotMatches oracle", () => {
  let dir: string;
  beforeEach(() => {
    dir = mkdtempSync(join(tmpdir(), "heimdall-shot-"));
  });
  afterEach(() => {
    rmSync(dir, { recursive: true, force: true });
  });

  it("passes when the capture is identical to the baseline (ratio 0)", async () => {
    const baseline = join(dir, "home.png");
    const img = solidPng(4, 4, [10, 20, 30, 255]);
    writeFileSync(baseline, img);
    const obs = mockObs({ screenshot: async () => img });
    const out = await evaluateOracles([{ assert: "screenshotMatches", baseline, maxDiffRatio: 0.01 }], obs);
    expect(out.passed).toBe(true);
    expect(out.records[0]).toMatchObject({ kind: "screenshotMatches", passed: true });
    expect(out.records[0].detail).toContain("0.0000");
    expect(out.records[0].detail).toContain(baseline);
  });

  it("fails when the diff ratio exceeds maxDiffRatio", async () => {
    const baseline = join(dir, "home.png");
    writeFileSync(baseline, solidPng(4, 4, [0, 0, 0, 255]));
    // A fully white capture against a fully black baseline => ratio 1.0.
    const obs = mockObs({ screenshot: async () => solidPng(4, 4, [255, 255, 255, 255]) });
    const out = await evaluateOracles([{ assert: "screenshotMatches", baseline, maxDiffRatio: 0.01 }], obs);
    expect(out.passed).toBe(false);
    expect(out.failures[0]).toContain("exceeded 0.01");
    expect(out.failures[0]).toContain("1.0000");
    expect(out.records[0]).toMatchObject({ kind: "screenshotMatches", passed: false });
    expect(out.records[0].detail).toBe(out.failures[0]);
  });

  it("passes with a first-run note when the baseline is missing", async () => {
    const baseline = join(dir, "missing.png");
    let captured = false;
    const obs = mockObs({
      screenshot: async () => {
        captured = true;
        return solidPng(2, 2, [1, 2, 3, 255]);
      },
    });
    const out = await evaluateOracles([{ assert: "screenshotMatches", baseline, maxDiffRatio: 0.01 }], obs);
    expect(out.passed).toBe(true);
    expect(captured).toBe(true); // the capture still happens (the driver persists it as the baseline)
    expect(out.records[0]).toMatchObject({ kind: "screenshotMatches", passed: true });
    expect(out.records[0].detail).toContain("first run");
    expect(out.records[0].detail).toContain(baseline);
  });
});

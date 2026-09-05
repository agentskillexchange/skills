import { describe, it, expect } from "vitest";
import { parsePlan, fidelityForDriver, Result, Plan } from "../src/schema.js";
import { SAMPLE_PLAN } from "../src/commands/init.js";

describe("parsePlan", () => {
  it("accepts the sample plan and applies defaults", () => {
    const plan = parsePlan(JSON.parse(JSON.stringify(SAMPLE_PLAN)));
    expect(plan.defaultDriver).toBe("cdp");
    expect(plan.cases[0]!.risk).toBe("read-only");
    expect(plan.cases[0]!.priority).toBe("p0");
    // method defaults to "ui" when omitted on a parsed-from-minimal case
  });

  it("rejects a case with no oracle", () => {
    expect(() =>
      parsePlan({
        cases: [{ id: "x", steps: [{ action: "goto", url: "/" }], oracle: [] }],
      }),
    ).toThrow();
  });

  it("rejects an unknown step action", () => {
    expect(() =>
      parsePlan({
        cases: [{ id: "x", steps: [{ action: "teleport", url: "/" }], oracle: [{ assert: "noConsoleErrors" }] }],
      }),
    ).toThrow();
  });

  it("rejects unknown keys (strict)", () => {
    expect(() =>
      parsePlan({
        cases: [{ id: "x", oracle: [{ assert: "noConsoleErrors" }], bogus: 1 }],
      }),
    ).toThrow();
  });

  it("requires at least one case", () => {
    expect(() => parsePlan({ cases: [] })).toThrow();
  });

  it("accepts a load step plus errorRate/percentile oracles", () => {
    const plan = parsePlan({
      cases: [
        {
          id: "load-x",
          steps: [{ action: "load", url: "/slow", times: 20, concurrency: 5, as: "lt" }],
          oracle: [
            { assert: "errorRate", max: 0.3, of: "lt" },
            { assert: "percentile", p: 95, maxMs: 500, of: "lt" },
            { assert: "percentile", p: "max", maxMs: 2000, of: "lt" },
          ],
        },
      ],
    });
    const step = plan.cases[0]!.steps[0]!;
    expect(step.action).toBe("load");
    if (step.action === "load") {
      expect(step.times).toBe(20);
      expect(step.concurrency).toBe(5);
    }
  });

  it("rejects a load step with non-positive times", () => {
    expect(() =>
      parsePlan({
        cases: [
          {
            id: "bad-load",
            steps: [{ action: "load", url: "/x", times: 0 }],
            oracle: [{ assert: "errorRate", max: 0.1 }],
          },
        ],
      }),
    ).toThrow();
  });

  it("rejects an errorRate oracle outside 0..1 and a bad percentile literal", () => {
    expect(() =>
      parsePlan({ cases: [{ id: "x", oracle: [{ assert: "errorRate", max: 1.5 }] }] }),
    ).toThrow();
    expect(() =>
      parsePlan({ cases: [{ id: "x", oracle: [{ assert: "percentile", p: 90, maxMs: 100 }] }] }),
    ).toThrow();
  });

  it("accepts an sse step plus an eventCount oracle", () => {
    const plan = parsePlan({
      cases: [
        {
          id: "sse-x",
          steps: [{ action: "sse", url: "/events", events: 3, timeoutMs: 5000, closeAfterMs: 4000, as: "stream" }],
          oracle: [
            { assert: "eventCount", min: 1, of: "stream" },
            { assert: "eventCount", equals: 3, of: "stream" },
            { assert: "bodyContains", value: "n", of: "stream" },
          ],
        },
      ],
    });
    const step = plan.cases[0]!.steps[0]!;
    expect(step.action).toBe("sse");
    if (step.action === "sse") {
      expect(step.url).toBe("/events");
      expect(step.events).toBe(3);
      expect(step.timeoutMs).toBe(5000);
      expect(step.closeAfterMs).toBe(4000);
    }
  });

  it("accepts setup/teardown hooks on both the case and the plan", () => {
    const plan = parsePlan({
      setup: [{ action: "request", url: "/seed", method: "POST" }],
      teardown: [{ action: "request", url: "/unseed", method: "POST" }],
      cases: [
        {
          id: "lifecycle",
          setup: [{ action: "request", url: "/resource", method: "POST", capture: { rid: { jsonPath: "id" } } }],
          steps: [{ action: "request", url: "/resource?id=${rid}", as: "check" }],
          teardown: [{ action: "request", url: "/resource?id=${rid}", method: "DELETE" }],
          oracle: [{ assert: "status", equals: 200, of: "check" }],
        },
      ],
    });
    expect(plan.setup).toHaveLength(1);
    expect(plan.teardown).toHaveLength(1);
    const c = plan.cases[0]!;
    expect(c.setup).toHaveLength(1);
    expect(c.teardown).toHaveLength(1);
    // Hooks are plain Steps: an unknown action inside a hook is still rejected.
    expect(() =>
      parsePlan({
        cases: [
          {
            id: "bad-hook",
            setup: [{ action: "teleport", url: "/" }],
            oracle: [{ assert: "noConsoleErrors" }],
          },
        ],
      }),
    ).toThrow();
  });

  it("rejects a vacuous eventCount oracle (no min and no equals)", () => {
    // An unbounded eventCount asserts nothing (any count, including zero, "passes"),
    // which would let a case meet its mandatory >=1-oracle rule while proving nothing.
    expect(() =>
      parsePlan({
        cases: [
          {
            id: "vacuous-eventcount",
            steps: [{ action: "sse", url: "/events", as: "stream" }],
            oracle: [{ assert: "eventCount", of: "stream" }],
          },
        ],
      }),
    ).toThrow(/min\/equals/);
    // The same oracle WITH a bound is accepted.
    expect(() =>
      parsePlan({
        cases: [
          {
            id: "ok-eventcount",
            steps: [{ action: "sse", url: "/events", as: "stream" }],
            oracle: [{ assert: "eventCount", min: 1, of: "stream" }],
          },
        ],
      }),
    ).not.toThrow();
  });

  it("rejects an sse step with non-positive events and an unknown key", () => {
    expect(() =>
      parsePlan({
        cases: [
          {
            id: "bad-sse",
            steps: [{ action: "sse", url: "/events", events: 0 }],
            oracle: [{ assert: "eventCount", min: 1 }],
          },
        ],
      }),
    ).toThrow();
    expect(() =>
      parsePlan({
        cases: [
          {
            id: "bad-sse-key",
            steps: [{ action: "sse", url: "/events", bogus: true }],
            oracle: [{ assert: "eventCount", min: 1 }],
          },
        ],
      }),
    ).toThrow();
  });

  it("accepts a route step in each interception mode", () => {
    for (const mode of ["block", "abort", "fulfill", "delay"] as const) {
      const plan = parsePlan({
        cases: [
          {
            id: `route-${mode}`,
            steps: [
              {
                action: "route",
                urlContains: "/api/flaky",
                mode,
                status: 503,
                body: "{}",
                headers: { "content-type": "application/json" },
                delayMs: 250,
              },
              { action: "goto", url: "/" },
            ],
            oracle: [{ assert: "noConsoleErrors" }],
          },
        ],
      });
      const step = plan.cases[0]!.steps[0]!;
      expect(step.action).toBe("route");
      if (step.action === "route") {
        expect(step.mode).toBe(mode);
        expect(step.urlContains).toBe("/api/flaky");
      }
    }
  });

  it("rejects a route step with an unknown mode or extra key", () => {
    expect(() =>
      parsePlan({
        cases: [
          {
            id: "bad-route-mode",
            steps: [{ action: "route", urlContains: "/x", mode: "rewrite" }],
            oracle: [{ assert: "noConsoleErrors" }],
          },
        ],
      }),
    ).toThrow();
    expect(() =>
      parsePlan({
        cases: [
          {
            id: "bad-route-key",
            steps: [{ action: "route", urlContains: "/x", mode: "block", bogus: 1 }],
            oracle: [{ assert: "noConsoleErrors" }],
          },
        ],
      }),
    ).toThrow();
  });

  it("accepts a race step whose nested steps are request/fetch/load", () => {
    const plan = parsePlan({
      cases: [
        {
          id: "race-ok",
          steps: [
            {
              action: "race",
              steps: [
                { action: "request", url: "/a", as: "a" },
                { action: "fetch", url: "/b", as: "b" },
                { action: "load", url: "/c", times: 5, as: "c" },
              ],
            },
          ],
          oracle: [{ assert: "responseOk" }],
        },
      ],
    });
    const step = plan.cases[0]!.steps[0]!;
    expect(step.action).toBe("race");
    if (step.action === "race") {
      expect(step.steps).toHaveLength(3);
      expect(step.steps.map((s) => s.action)).toEqual(["request", "fetch", "load"]);
    }
  });

  it("rejects a race step that nests a non-network action (goto)", () => {
    expect(() =>
      parsePlan({
        cases: [
          {
            id: "race-goto",
            steps: [
              {
                action: "race",
                steps: [
                  { action: "request", url: "/a" },
                  { action: "goto", url: "/" },
                ],
              },
            ],
            oracle: [{ assert: "responseOk" }],
          },
        ],
      }),
    ).toThrow();
  });

  it("accepts an a11y oracle and defaults maxImpact to serious", () => {
    const plan = parsePlan({
      cases: [
        {
          id: "a11y-x",
          steps: [{ action: "goto", url: "/" }],
          oracle: [{ assert: "a11y", include: ["main"], exclude: [".ads"] }],
        },
      ],
    });
    const oracle = plan.cases[0]!.oracle[0]!;
    expect(oracle.assert).toBe("a11y");
    if (oracle.assert === "a11y") {
      expect(oracle.maxImpact).toBe("serious");
      expect(oracle.include).toEqual(["main"]);
      expect(oracle.exclude).toEqual([".ads"]);
    }
  });

  it("accepts a screenshotMatches oracle and defaults maxDiffRatio to 0.01", () => {
    const plan = parsePlan({
      cases: [
        {
          id: "pixel-x",
          steps: [{ action: "goto", url: "/" }],
          oracle: [{ assert: "screenshotMatches", baseline: "home.png", selector: "main" }],
        },
      ],
    });
    const oracle = plan.cases[0]!.oracle[0]!;
    expect(oracle.assert).toBe("screenshotMatches");
    if (oracle.assert === "screenshotMatches") {
      expect(oracle.baseline).toBe("home.png");
      expect(oracle.maxDiffRatio).toBe(0.01);
      expect(oracle.selector).toBe("main");
    }
  });

  it("rejects a screenshotMatches oracle without a baseline", () => {
    expect(() =>
      parsePlan({
        cases: [
          {
            id: "pixel-no-baseline",
            steps: [{ action: "goto", url: "/" }],
            oracle: [{ assert: "screenshotMatches", maxDiffRatio: 0.05 }],
          },
        ],
      }),
    ).toThrow();
  });

  it("accepts an optional plan-level redaction spec", () => {
    const plan = parsePlan({
      redaction: { headers: ["authorization", "cookie"], patterns: ["sk-[a-z0-9]+"] },
      cases: [
        {
          id: "redact-x",
          steps: [{ action: "goto", url: "/" }],
          oracle: [{ assert: "noConsoleErrors" }],
        },
      ],
    });
    expect(plan.redaction).toEqual({ headers: ["authorization", "cookie"], patterns: ["sk-[a-z0-9]+"] });
  });

  it("omits redaction when absent — a no-new-fields plan parses byte-equivalently", () => {
    const minimal = {
      cases: [
        {
          id: "plain",
          steps: [{ action: "goto", url: "/" }],
          oracle: [{ assert: "noConsoleErrors" }],
        },
      ],
    };
    const plan = parsePlan(minimal) as Record<string, unknown>;
    expect("redaction" in plan).toBe(false);
    // Re-parsing the parsed output is a fixpoint (no new fields leak in).
    expect(JSON.stringify(Plan.parse(plan))).toBe(JSON.stringify(plan));
  });
});

describe("Result.oracleResults", () => {
  const base = {
    id: "r1",
    status: "pass" as const,
    driver: "cdp" as const,
    fidelityTier: "medium" as const,
    observed: "ok",
    durationMs: 12,
  };

  it("parses a Result without oracleResults (backward compatible)", () => {
    const r = Result.parse(base);
    expect(r.oracleResults).toBeUndefined();
  });

  it("parses a Result carrying per-oracle results", () => {
    const r = Result.parse({
      ...base,
      oracleResults: [
        { kind: "status", passed: true, detail: "200 == 200" },
        { kind: "a11y", passed: false, detail: "1 serious violation" },
      ],
    });
    expect(r.oracleResults).toHaveLength(2);
    expect(r.oracleResults![1]!.passed).toBe(false);
    expect(r.oracleResults![1]!.kind).toBe("a11y");
  });
});

describe("fidelityForDriver", () => {
  it("maps drivers to tiers", () => {
    expect(fidelityForDriver("extension")).toBe("high");
    expect(fidelityForDriver("cdp")).toBe("medium");
    expect(fidelityForDriver("container")).toBe("medium-linux");
  });
});

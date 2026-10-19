import { describe, it, expect } from "vitest";
import {
  filterViolations,
  runAxe,
  type AxeBridge,
  type AxeResultLike,
  type AxeViolation,
} from "../src/a11y.js";

const violation = (id: string, impact: AxeViolation["impact"]): AxeViolation => ({
  id,
  impact,
  help: `help for ${id}`,
  description: `desc for ${id}`,
  helpUrl: `https://example.test/${id}`,
  nodes: [{ html: `<div id="${id}">`, target: [`#${id}`], failureSummary: "fix it" }],
});

const result = (...violations: AxeViolation[]): AxeResultLike => ({ violations });

describe("filterViolations", () => {
  it("ignores violations below the threshold", () => {
    const out = filterViolations(result(violation("color-contrast", "minor")), "serious");
    expect(out.violations).toHaveLength(0);
    expect(out.passed).toBe(true);
    expect(out.summary).toContain("No accessibility violations");
  });

  it("flips passed=false for violations at the threshold", () => {
    const out = filterViolations(result(violation("label", "serious")), "serious");
    expect(out.passed).toBe(false);
    expect(out.violations.map((v) => v.id)).toEqual(["label"]);
  });

  it("flips passed=false for violations above the threshold", () => {
    const out = filterViolations(result(violation("aria-required", "critical")), "serious");
    expect(out.passed).toBe(false);
    expect(out.violations.map((v) => v.id)).toEqual(["aria-required"]);
  });

  it("lists offending rule ids and impacts in the summary", () => {
    const out = filterViolations(
      result(violation("label", "serious"), violation("aria-required", "critical")),
      "moderate",
    );
    expect(out.summary).toContain("label");
    expect(out.summary).toContain("aria-required");
    expect(out.summary).toContain("serious");
    expect(out.summary).toContain("critical");
  });

  it("applies the threshold ordering minor<moderate<serious<critical", () => {
    const all = result(
      violation("v-minor", "minor"),
      violation("v-moderate", "moderate"),
      violation("v-serious", "serious"),
      violation("v-critical", "critical"),
    );
    expect(filterViolations(all, "minor").violations.map((v) => v.id)).toEqual([
      "v-minor",
      "v-moderate",
      "v-serious",
      "v-critical",
    ]);
    expect(filterViolations(all, "moderate").violations.map((v) => v.id)).toEqual([
      "v-moderate",
      "v-serious",
      "v-critical",
    ]);
    expect(filterViolations(all, "serious").violations.map((v) => v.id)).toEqual([
      "v-serious",
      "v-critical",
    ]);
    expect(filterViolations(all, "critical").violations.map((v) => v.id)).toEqual(["v-critical"]);
  });

  it("ignores violations with null/unknown impact", () => {
    const out = filterViolations(result(violation("unknown", null)), "minor");
    expect(out.violations).toHaveLength(0);
    expect(out.passed).toBe(true);
  });

  it("treats a missing violations array as empty", () => {
    const out = filterViolations({} as AxeResultLike, "minor");
    expect(out.passed).toBe(true);
    expect(out.violations).toHaveLength(0);
  });
});

describe("runAxe", () => {
  type Call = { pageFunction: unknown; arg: unknown };

  function mockBridge(canned: AxeResultLike) {
    const calls: Call[] = [];
    const bridge: AxeBridge = {
      evaluate: ((pageFunction: unknown, arg?: unknown) => {
        calls.push({ pageFunction, arg });
        // First call injects the axe source; the run call returns the result.
        return Promise.resolve(calls.length >= 2 ? canned : undefined);
      }) as AxeBridge["evaluate"],
    };
    return { bridge, calls };
  }

  it("injects the axe source before running and returns the raw result", async () => {
    const canned = result(violation("label", "serious"));
    const { bridge, calls } = mockBridge(canned);
    const raw = await runAxe(bridge);
    expect(raw).toBe(canned);
    expect(calls).toHaveLength(2);
    // The injection call passes the axe-core source as a string.
    expect(typeof calls[0]?.pageFunction).toBe("string");
    expect(calls[0]?.pageFunction as string).toContain("axe");
  });

  it("forwards include/exclude as the run context", async () => {
    const { bridge, calls } = mockBridge(result());
    await runAxe(bridge, { include: [["#main"]], exclude: [[".ads"]] });
    expect(calls[1]?.arg).toEqual({ include: [["#main"]], exclude: [[".ads"]] });
  });

  it("forwards only include when exclude is omitted", async () => {
    const { bridge, calls } = mockBridge(result());
    await runAxe(bridge, { include: [["#main"]] });
    expect(calls[1]?.arg).toEqual({ include: [["#main"]] });
  });

  it("passes no context when neither include nor exclude is given", async () => {
    const { bridge, calls } = mockBridge(result());
    await runAxe(bridge);
    expect(calls[1]?.arg).toBeUndefined();
  });
});

import { describe, it, expect } from "vitest";
import { collectPlanErrors, validateCasesIndividually } from "../src/commands/validate.js";
import { SAMPLE_PLAN } from "../src/commands/init.js";

describe("collectPlanErrors", () => {
  it("returns [] for a valid plan", () => {
    const plan = JSON.parse(JSON.stringify(SAMPLE_PLAN));
    expect(collectPlanErrors(plan)).toEqual([]);
  });

  it("reports EVERY problem across several bad cases, not just the first", () => {
    const errors = collectPlanErrors({
      cases: [
        // valid
        { id: "ok", oracle: [{ assert: "noConsoleErrors" }] },
        // unknown oracle key (strict)
        { id: "bad-key", oracle: [{ assert: "visible", selector: "body", exists: true }] },
        // unknown step action
        { id: "bad-step", steps: [{ action: "teleport" }], oracle: [{ assert: "noConsoleErrors" }] },
        // missing required id + no oracle
        { steps: [] },
      ],
    });
    // At least one line per bad case — proves we did NOT stop at the first.
    expect(errors.length).toBeGreaterThanOrEqual(3);
    const joined = errors.join("\n");
    // Case attribution: index + derived id where available.
    expect(joined).toContain("cases[1] (id=bad-key)");
    expect(joined).toContain("cases[2] (id=bad-step)");
    // The fourth case has no id, so it is named by index only.
    expect(joined).toContain("cases[3]");
    // Readable reason text.
    expect(joined).toMatch(/Unrecognized key/);
  });

  it("formats an unrecognized oracle key with the in-case path and reason", () => {
    const errors = collectPlanErrors({
      cases: [{ id: "foo", oracle: [{ assert: "noConsoleErrors", exists: true }] }],
    });
    expect(errors.some((e) => /cases\[0\] \(id=foo\): oracle\.0 — Unrecognized key: exists/.test(e))).toBe(true);
  });

  it("reports plan-level problems too", () => {
    const errors = collectPlanErrors({ defaultDriver: "rocket", cases: [] });
    expect(errors.length).toBeGreaterThanOrEqual(1);
    const joined = errors.join("\n");
    // not attributed to any case
    expect(joined).not.toContain("cases[");
  });
});

describe("validateCasesIndividually (lenient path)", () => {
  it("separates valid from invalid cases and explains each invalid one", () => {
    const checked = validateCasesIndividually({
      cases: [
        { id: "good", oracle: [{ assert: "noConsoleErrors" }] },
        { id: "no-oracle", oracle: [] },
        { id: "bad-key", oracle: [{ assert: "visible", selector: "x", exists: 1 }] },
      ],
    });
    expect(checked).toHaveLength(3);
    expect(checked[0]!.errors).toEqual([]);
    expect(checked[0]!.id).toBe("good");
    expect(checked[1]!.errors.length).toBeGreaterThanOrEqual(1);
    expect(checked[2]!.errors.length).toBeGreaterThanOrEqual(1);
    // valid cases are runnable; invalid ones are not
    expect(checked.filter((c) => c.errors.length === 0)).toHaveLength(1);
  });

  it("returns [] when there are no cases", () => {
    expect(validateCasesIndividually({})).toEqual([]);
    expect(validateCasesIndividually(null)).toEqual([]);
  });
});

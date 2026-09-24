import { describe, it, expect } from "vitest";
import { toJUnitXml } from "../src/reporters/junit.js";
import { buildHtml } from "../src/reporters/html.js";
import { formatReport, exitCodeFor, groupResults, type CaseMeta } from "../src/reporter.js";
import { diffReports, formatDiff, isCleanDiff } from "../src/reporters/diff.js";
import type { Result, RunReport } from "../src/schema.js";

function mkResult(over: Partial<Result>): Result {
  return {
    id: "case-1",
    status: "pass",
    driver: "cdp",
    fidelityTier: "medium",
    observed: "ok",
    failures: [],
    evidence: { screenshots: [], consoleErrors: [], responses: [] },
    durationMs: 100,
    ...over,
  };
}

const report: RunReport = {
  plan: "demo & <plan>",
  heimdallVersion: "0.1.0",
  startedAt: "2026-01-01T00:00:00.000Z",
  finishedAt: "2026-01-01T00:00:01.000Z",
  durationMs: 1000,
  summary: { total: 3, pass: 1, fail: 1, blocked: 1, skipped: 0, error: 0 },
  results: [
    mkResult({ id: "ok-case", status: "pass" }),
    mkResult({ id: "bad-case", status: "fail", observed: "oracle x failed", failures: ["visible: #y not visible"] }),
    mkResult({ id: "blocked-case", status: "blocked", driver: "extension", fidelityTier: "high", observed: "agent-driven" }),
  ],
};

describe("toJUnitXml", () => {
  it("emits a valid-looking testsuite with counts", () => {
    const xml = toJUnitXml(report);
    expect(xml).toContain('<?xml version="1.0"');
    expect(xml).toContain('tests="3"');
    expect(xml).toContain('failures="1"');
    expect(xml).toContain('skipped="1"'); // blocked maps to skipped
    expect(xml).toContain('name="ok-case"');
    expect(xml).toContain("<failure");
    expect(xml).toContain("<skipped");
  });

  it("escapes XML-special chars in the plan name", () => {
    const xml = toJUnitXml(report);
    expect(xml).toContain("demo &amp; &lt;plan&gt;");
    expect(xml).not.toContain("demo & <plan>");
  });
});

describe("buildHtml", () => {
  it("renders a self-contained document with each case", async () => {
    const html = await buildHtml(report);
    expect(html.startsWith("<!doctype html>")).toBe(true);
    expect(html).toContain("ok-case");
    expect(html).toContain("bad-case");
    expect(html).toContain("visible: #y not visible");
    expect(html).toContain("1 pass");
  });

  it("escapes HTML-special chars", async () => {
    const html = await buildHtml(report);
    expect(html).toContain("demo &amp; &lt;plan&gt;");
  });
});

const meta: Record<string, CaseMeta> = {
  "ok-case": { tags: ["smoke"], dimension: "functional" },
  "bad-case": { tags: ["smoke", "auth"], dimension: "security" },
  "blocked-case": { tags: [], dimension: "functional" },
};

describe("formatReport grouping & blocked section", () => {
  it("is byte-identical to the legacy 2-arg call when no options are passed", () => {
    const a = formatReport(report, "/out");
    const b = formatReport(report, "/out", undefined);
    expect(a).toBe(b);
    // The legacy layout has no grouping headers or blocked section.
    expect(a).not.toContain("▸");
    expect(a).not.toContain("Blocked (");
  });

  it("groups case rows under tag headers with per-group tallies", () => {
    const out = formatReport(report, "/out", { groupBy: "tag", meta });
    expect(out).toContain("▸ tag · smoke");
    expect(out).toContain("▸ tag · auth");
    expect(out).toContain("▸ tag · (untagged)"); // blocked-case has no tags
    // smoke holds ok-case (pass) + bad-case (fail)
    expect(out).toContain("▸ tag · smoke  (1 pass, 1 fail / 2)");
  });

  it("groups by dimension, bucketing cases by their dimension value", () => {
    const out = formatReport(report, "/out", { groupBy: "dimension", meta });
    expect(out).toContain("▸ dimension · functional");
    expect(out).toContain("▸ dimension · security");
    expect(out).toContain("▸ dimension · functional  (1 pass, 0 fail / 2)");
  });

  it("falls back to (no dimension) when meta is absent", () => {
    const out = formatReport(report, "/out", { groupBy: "dimension" });
    expect(out).toContain("▸ dimension · (no dimension)");
  });

  it("renders a dedicated Blocked section with id + reason when options are passed", () => {
    const out = formatReport(report, "/out", { groupBy: "tag", meta });
    expect(out).toContain("Blocked (1)");
    expect(out).toContain("blocked-case");
    expect(out).toContain("agent-driven"); // the observed reason
  });

  it("suppresses the blocked section when blocked:false", () => {
    const out = formatReport(report, "/out", { blocked: false });
    expect(out).not.toContain("Blocked (");
  });
});

describe("groupResults", () => {
  it("places multi-tag cases under each tag and preserves order", () => {
    const groups = groupResults(report.results, "tag", meta);
    const labels = groups.map(([l]) => l);
    expect(labels).toEqual(["smoke", "auth", "(untagged)"]);
    const auth = groups.find(([l]) => l === "auth")![1];
    expect(auth.map((r) => r.id)).toEqual(["bad-case"]);
  });

  it("returns no groups for an empty result set", () => {
    expect(groupResults([], "tag", meta)).toEqual([]);
    expect(groupResults([], "dimension")).toEqual([]);
  });

  it("buckets cases entirely absent from meta into the catch-all", () => {
    const orphan = mkResult({ id: "no-meta-case", status: "pass" });
    const byTag = groupResults([orphan], "tag", meta);
    expect(byTag.map(([l]) => l)).toEqual(["(untagged)"]);
    const byDim = groupResults([orphan], "dimension", meta);
    expect(byDim.map(([l]) => l)).toEqual(["(no dimension)"]);
  });
});

describe("exitCodeFor (CI honesty gate)", () => {
  const withSummary = (over: Partial<RunReport["summary"]>): RunReport => ({
    ...report,
    results: [],
    summary: { total: 0, pass: 0, fail: 0, blocked: 0, skipped: 0, error: 0, ...over },
  });

  it("is non-zero when anything failed or errored", () => {
    expect(exitCodeFor(withSummary({ total: 2, pass: 1, fail: 1 }))).toBe(1);
    expect(exitCodeFor(withSummary({ total: 2, pass: 1, error: 1 }))).toBe(1);
  });

  it("is non-zero when cases existed but NOTHING ran (all blocked/skipped)", () => {
    expect(exitCodeFor(withSummary({ total: 3, blocked: 3 }))).toBe(1);
    expect(exitCodeFor(withSummary({ total: 2, skipped: 2 }))).toBe(1);
    expect(exitCodeFor(withSummary({ total: 2, blocked: 1, skipped: 1 }))).toBe(1);
  });

  it("is zero when at least one case passed, even alongside blocked/skipped", () => {
    expect(exitCodeFor(withSummary({ total: 3, pass: 1, blocked: 2 }))).toBe(0);
    expect(exitCodeFor(withSummary({ total: 2, pass: 2 }))).toBe(0);
  });

  it("is zero for a genuinely empty plan (no cases at all)", () => {
    expect(exitCodeFor(withSummary({ total: 0 }))).toBe(0);
  });
});

describe("buildHtml grouping & blocked panel", () => {
  it("is unchanged when no options are passed (no extra CSS or panels)", async () => {
    const a = await buildHtml(report);
    const b = await buildHtml(report, undefined);
    expect(a).toBe(b);
    expect(a).not.toContain("blocked-panel");
    expect(a).not.toContain("class=\"group\"");
  });

  it("emits grouped sections and a blocked panel when grouping is requested", async () => {
    const html = await buildHtml(report, { groupBy: "dimension", meta });
    expect(html).toContain('class="group"');
    expect(html).toContain("dimension: functional");
    expect(html).toContain("dimension: security");
    expect(html).toContain("blocked-panel");
    expect(html).toContain("Blocked (1)");
    expect(html).toContain("blocked-case");
  });
});

describe("toJUnitXml classname grouping", () => {
  it("uses driver classname by default (unchanged)", () => {
    expect(toJUnitXml(report)).toContain('classname="heimdall.cdp"');
  });

  it("uses the dimension as classname when classnameBy:dimension", () => {
    const xml = toJUnitXml(report, { classnameBy: "dimension", meta });
    expect(xml).toContain('classname="heimdall.functional"');
    expect(xml).toContain('classname="heimdall.security"');
  });
});

describe("diffReports", () => {
  const prev: RunReport = {
    ...report,
    results: [
      mkResult({ id: "a", status: "pass" }),
      mkResult({ id: "b", status: "fail" }),
      mkResult({ id: "c", status: "fail" }),
      mkResult({ id: "gone", status: "pass" }),
    ],
  };
  const curr: RunReport = {
    ...report,
    results: [
      mkResult({ id: "a", status: "fail" }), // regression
      mkResult({ id: "b", status: "pass" }), // fixed
      mkResult({ id: "c", status: "error" }), // still failing (error counts)
      mkResult({ id: "new", status: "fail" }), // added
    ],
  };

  it("classifies newly-failing / newly-passing / still-failing / added / removed by id", () => {
    const d = diffReports(prev, curr);
    expect(d.newlyFailing.map((x) => x.id)).toEqual(["a"]);
    expect(d.newlyFailing[0].status).toBe("fail");
    expect(d.newlyPassing.map((x) => x.id)).toEqual(["b"]);
    expect(d.stillFailing.map((x) => x.id)).toEqual(["c"]);
    expect(d.stillFailing[0].status).toBe("error");
    expect(d.added.map((x) => x.id)).toEqual(["new"]);
    expect(d.removed).toEqual([{ id: "gone", status: "pass" }]);
    expect(isCleanDiff(d)).toBe(false);
  });

  it("reports a clean diff when an all-passing run is unchanged", () => {
    const allPass: RunReport = {
      ...report,
      results: [mkResult({ id: "a", status: "pass" }), mkResult({ id: "b", status: "pass" })],
    };
    const d = diffReports(allPass, allPass);
    expect(isCleanDiff(d)).toBe(true);
    expect(d.newlyFailing).toEqual([]);
    expect(formatDiff(d)).toContain("no changes since the previous run");
  });

  it("still surfaces cases failing in both runs as stillFailing (not clean)", () => {
    const d = diffReports(prev, prev);
    expect(d.stillFailing.map((x) => x.id)).toEqual(["b", "c"]);
    expect(isCleanDiff(d)).toBe(false);
  });

  it("formatDiff surfaces every populated bucket", () => {
    const text = formatDiff(diffReports(prev, curr));
    expect(text).toContain("Newly failing (1)");
    expect(text).toContain("a [fail]");
    expect(text).toContain("Newly passing (1)");
    expect(text).toContain("Added (1)");
    expect(text).toContain("Removed (1)");
  });

  it("never counts a pass->blocked non-run as a regression", () => {
    const before: RunReport = { ...report, results: [mkResult({ id: "a", status: "pass" })] };
    const after: RunReport = { ...report, results: [mkResult({ id: "a", status: "blocked" })] };
    const d = diffReports(before, after);
    // A case that stopped running (blocked) is NOT a newly-failing regression.
    expect(d.newlyFailing).toEqual([]);
    expect(d.newlyPassing).toEqual([]);
    expect(d.stillFailing).toEqual([]);
  });

  it("never counts a blocked->pass transition as a fix, nor blocked-in-both as failing", () => {
    const before: RunReport = {
      ...report,
      results: [mkResult({ id: "a", status: "blocked" }), mkResult({ id: "b", status: "blocked" })],
    };
    const after: RunReport = {
      ...report,
      results: [mkResult({ id: "a", status: "pass" }), mkResult({ id: "b", status: "blocked" })],
    };
    const d = diffReports(before, after);
    // blocked->pass is not a regression-fix (it was never a failure); blocked->blocked
    // is a non-run in both and belongs to no bucket -> the diff reads clean.
    expect(d.newlyPassing).toEqual([]);
    expect(d.stillFailing).toEqual([]);
    expect(isCleanDiff(d)).toBe(true);
  });

  it("counts a brand-new case by its current status regardless of pass/fail", () => {
    const before: RunReport = { ...report, results: [mkResult({ id: "old", status: "pass" })] };
    const after: RunReport = {
      ...report,
      results: [mkResult({ id: "old", status: "pass" }), mkResult({ id: "fresh", status: "fail" })],
    };
    const d = diffReports(before, after);
    expect(d.added).toEqual([{ id: "fresh", status: "fail" }]);
    // An added case is reported as `added`, not double-counted as newlyFailing.
    expect(d.newlyFailing).toEqual([]);
  });
});

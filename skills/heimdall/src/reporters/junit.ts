/** JUnit XML report for CI test reporters. */
import { writeFile } from "node:fs/promises";
import type { Result, RunReport } from "../schema.js";
import type { CaseMeta } from "../reporter.js";

const esc = (s: string): string =>
  s.replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&apos;" })[ch]!);

/** Optional grouping for CI dashboards: surface tag/dimension via the JUnit `classname`. */
export interface JUnitOptions {
  /** Build `classname` from a case's dimension or first tag instead of the driver. */
  classnameBy?: "dimension" | "tag";
  /** Per-case tags/dimension keyed by case id (the report does not carry them). */
  meta?: Record<string, CaseMeta>;
}

function classnameFor(r: Result, opts?: JUnitOptions): string {
  if (opts?.classnameBy) {
    const m = opts.meta?.[r.id];
    const group =
      opts.classnameBy === "dimension" ? m?.dimension : (m?.tags && m.tags[0]) || undefined;
    if (group) return `heimdall.${group}`;
  }
  return `heimdall.${r.driver}`;
}

function renderCase(r: Result, opts?: JUnitOptions): string {
  const time = (r.durationMs / 1000).toFixed(3);
  const name = esc(r.id);
  const cls = esc(classnameFor(r, opts));
  const open = `  <testcase classname="${cls}" name="${name}" time="${time}">`;
  if (r.status === "fail") {
    return `${open}\n    <failure message="${esc(r.observed)}">${esc(r.failures.join("\n"))}</failure>\n  </testcase>`;
  }
  if (r.status === "error") {
    return `${open}\n    <error message="${esc(r.observed)}">${esc(r.failures.join("\n"))}</error>\n  </testcase>`;
  }
  if (r.status === "blocked" || r.status === "skipped") {
    return `${open}\n    <skipped message="${esc(r.observed)}"/>\n  </testcase>`;
  }
  return `${open}</testcase>`;
}

export function toJUnitXml(report: RunReport, opts?: JUnitOptions): string {
  const s = report.summary;
  const failures = s.fail;
  const errors = s.error;
  const skipped = s.blocked + s.skipped;
  const time = (report.durationMs / 1000).toFixed(3);
  const cases = report.results.map((r) => renderCase(r, opts)).join("\n");
  return `<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="heimdall" tests="${s.total}" failures="${failures}" errors="${errors}" skipped="${skipped}" time="${time}">
  <testsuite name="${esc(report.plan)}" tests="${s.total}" failures="${failures}" errors="${errors}" skipped="${skipped}" time="${time}">
${cases}
  </testsuite>
</testsuites>
`;
}

export async function writeJUnitReport(report: RunReport, path: string, opts?: JUnitOptions): Promise<void> {
  await writeFile(path, toJUnitXml(report, opts), "utf8");
}

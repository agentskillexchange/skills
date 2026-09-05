/** Human-readable terminal rendering of a RunReport. */
import { join } from "node:path";
import type { Result, RunReport } from "./schema.js";
import { c } from "./log.js";

function statusBadge(s: Result["status"]): string {
  switch (s) {
    case "pass":
      return c.green("PASS");
    case "fail":
      return c.red("FAIL");
    case "error":
      return c.red("ERROR");
    case "blocked":
      return c.yellow("BLOCKED");
    case "skipped":
      return c.dim("SKIPPED");
  }
}

/**
 * Per-case metadata the report itself does not carry. `Result` records only
 * `id`/`status`/`driver`/…, so a caller that wants to group by tag or dimension
 * (which live on the plan's `TestCase`) supplies them here, keyed by case id.
 */
export interface CaseMeta {
  tags?: string[];
  dimension?: string;
}

/** Optional rendering controls for {@link formatReport} / {@link buildHtml}. */
export interface ReportFormatOptions {
  /** Group case rows under tag-value or dimension headers (with a per-group tally). */
  groupBy?: "tag" | "dimension";
  /** Per-case tags/dimension keyed by case id; required for `groupBy` to do anything. */
  meta?: Record<string, CaseMeta>;
  /** Render the dedicated "Blocked (N)" section. Defaults to true when options are passed. */
  blocked?: boolean;
}

interface Tally {
  pass: number;
  fail: number;
  total: number;
}

function tallyOf(results: Result[]): Tally {
  let pass = 0;
  let fail = 0;
  for (const r of results) {
    if (r.status === "pass") pass++;
    else if (r.status === "fail" || r.status === "error") fail++;
  }
  return { pass, fail, total: results.length };
}

/**
 * Bucket results by tag value or dimension, preserving first-appearance order of
 * both groups and the cases within them. A case with multiple tags appears under
 * each of its tags; a case with no tag/dimension lands in an explicit catch-all
 * bucket (`(untagged)` / `(no dimension)`). Pure.
 */
export function groupResults(
  results: Result[],
  groupBy: "tag" | "dimension",
  meta?: Record<string, CaseMeta>,
): Array<[string, Result[]]> {
  const order: string[] = [];
  const buckets = new Map<string, Result[]>();
  const add = (label: string, r: Result): void => {
    let arr = buckets.get(label);
    if (!arr) {
      arr = [];
      buckets.set(label, arr);
      order.push(label);
    }
    arr.push(r);
  };
  for (const r of results) {
    const m = meta?.[r.id];
    if (groupBy === "tag") {
      const tags = m?.tags ?? [];
      if (tags.length === 0) add("(untagged)", r);
      else for (const t of tags) add(t, r);
    } else {
      add(m?.dimension ?? "(no dimension)", r);
    }
  }
  return order.map((label) => [label, buckets.get(label)!]);
}

/** The lines for one case row, including failure/blocked sub-lines (matches the legacy layout). */
function caseLines(r: Result): string[] {
  const tier = c.dim(`[${r.fidelityTier}]`);
  const out = [`${statusBadge(r.status)}  ${c.bold(r.id)} ${c.dim(r.driver)} ${tier}`];
  if (r.status === "fail" || r.status === "error") {
    for (const f of r.failures.slice(0, 5)) out.push(c.red("      ↳ ") + f);
    if (r.evidence.screenshots.length) {
      out.push(c.dim(`      shot: ${r.evidence.screenshots[r.evidence.screenshots.length - 1]}`));
    }
  } else if (r.status === "blocked") {
    out.push(c.yellow("      ↳ ") + r.observed);
  }
  return out;
}

export function formatReport(report: RunReport, outDir: string, opts?: ReportFormatOptions): string {
  const lines: string[] = [];
  const s = report.summary;

  lines.push("");
  lines.push(c.bold(`Heimdall — ${report.plan}`) + c.dim(`  (${report.durationMs}ms, v${report.heimdallVersion})`));
  lines.push(c.dim("─".repeat(60)));

  if (opts?.groupBy) {
    for (const [label, results] of groupResults(report.results, opts.groupBy, opts.meta)) {
      const t = tallyOf(results);
      lines.push(
        c.bold(`▸ ${opts.groupBy} · ${label}`) + c.dim(`  (${t.pass} pass, ${t.fail} fail / ${t.total})`),
      );
      for (const r of results) for (const ln of caseLines(r)) lines.push(`  ${ln}`);
    }
  } else {
    for (const r of report.results) for (const ln of caseLines(r)) lines.push(ln);
  }

  // Dedicated, prominent rundown of everything that did NOT run — only when the
  // caller opts in, so the default 2-arg output stays byte-for-byte unchanged.
  const showBlocked = opts ? opts.blocked !== false : false;
  const deferred = report.results.filter((r) => r.status === "blocked" || r.status === "skipped");
  if (showBlocked && deferred.length) {
    lines.push("");
    lines.push(c.yellow(c.bold(`Blocked (${deferred.length})`)));
    for (const r of deferred) {
      const reason = r.observed || r.notes || "(no reason given)";
      lines.push(`${c.yellow("   • ")}${c.bold(r.id)}${c.dim(` [${r.status}] `)}${reason}`);
    }
  }

  lines.push(c.dim("─".repeat(60)));
  const parts = [
    c.green(`${s.pass} pass`),
    s.fail ? c.red(`${s.fail} fail`) : c.dim("0 fail"),
    s.error ? c.red(`${s.error} error`) : c.dim("0 error"),
    s.blocked ? c.yellow(`${s.blocked} blocked`) : c.dim("0 blocked"),
    s.skipped ? c.dim(`${s.skipped} skipped`) : c.dim("0 skipped"),
  ];
  lines.push(`${parts.join("  ")}   ${c.dim(`of ${s.total}`)}`);
  lines.push(c.dim(`report: ${join(outDir, "report.json")}`));
  lines.push("");
  return lines.join("\n");
}

/**
 * Process exit code. Non-zero if anything failed or errored, OR if cases existed
 * but nothing actually executed (all blocked/skipped) — a CI gate must not pass
 * green on a non-run. Blocked/skipped alongside at least one pass do not fail.
 */
export function exitCodeFor(report: RunReport): number {
  const s = report.summary;
  if (s.fail + s.error > 0) return 1;
  if (s.total > 0 && s.pass + s.fail + s.error === 0) return 1;
  return 0;
}

/**
 * Regression diff between two Heimdall runs — what changed since last time.
 *
 * Compares two {@link RunReport}s by case id and classifies every case into a
 * transition bucket so a CI gate (or a human) can see regressions at a glance,
 * without re-reading both reports. Pure: no I/O except the explicit writer.
 */
import { writeFile } from "node:fs/promises";
import type { ResultStatus, RunReport } from "../schema.js";

/** A case id paired with its status in the run that classified it. */
export interface DiffCase {
  id: string;
  status: ResultStatus;
}

/** The set of transitions between a previous run (`prev`) and the current run (`curr`). */
export interface RegressionDiff {
  /** Passed before, now failing/errored — the regressions a gate cares about. `status` is current. */
  newlyFailing: DiffCase[];
  /** Failed/errored before, now passing — fixes. `status` is current. */
  newlyPassing: DiffCase[];
  /** Failing/errored in both runs. `status` is current. */
  stillFailing: DiffCase[];
  /** Present in `curr` but not in `prev`. `status` is current. */
  added: DiffCase[];
  /** Present in `prev` but not in `curr`. `status` is the previous one. */
  removed: DiffCase[];
}

const isFail = (s: ResultStatus): boolean => s === "fail" || s === "error";
const isPass = (s: ResultStatus): boolean => s === "pass";

/**
 * Classify every case by its transition from `prev` to `curr`, comparing by id.
 * A case must be a pass→fail flip to count as `newlyFailing` (and the reverse for
 * `newlyPassing`); blocked/skipped non-runs never count as a regression or a fix.
 */
export function diffReports(prev: RunReport, curr: RunReport): RegressionDiff {
  const prevById = new Map(prev.results.map((r) => [r.id, r.status]));
  const currById = new Map(curr.results.map((r) => [r.id, r.status]));

  const diff: RegressionDiff = {
    newlyFailing: [],
    newlyPassing: [],
    stillFailing: [],
    added: [],
    removed: [],
  };

  for (const r of curr.results) {
    const before = prevById.get(r.id);
    if (before === undefined) {
      diff.added.push({ id: r.id, status: r.status });
      continue;
    }
    if (isFail(r.status)) {
      if (isPass(before)) diff.newlyFailing.push({ id: r.id, status: r.status });
      else if (isFail(before)) diff.stillFailing.push({ id: r.id, status: r.status });
    } else if (isPass(r.status) && isFail(before)) {
      diff.newlyPassing.push({ id: r.id, status: r.status });
    }
  }

  for (const r of prev.results) {
    if (!currById.has(r.id)) diff.removed.push({ id: r.id, status: r.status });
  }

  return diff;
}

/** True when nothing changed between the two runs (every bucket empty). */
export function isCleanDiff(diff: RegressionDiff): boolean {
  return (
    diff.newlyFailing.length === 0 &&
    diff.newlyPassing.length === 0 &&
    diff.stillFailing.length === 0 &&
    diff.added.length === 0 &&
    diff.removed.length === 0
  );
}

/** Human-readable terminal rendering of a {@link RegressionDiff}. Pure. */
export function formatDiff(diff: RegressionDiff): string {
  const lines: string[] = [];
  const section = (title: string, cases: DiffCase[]): void => {
    if (!cases.length) return;
    lines.push(`${title} (${cases.length})`);
    for (const c of cases) lines.push(`   • ${c.id} [${c.status}]`);
  };

  lines.push("Regression diff vs previous run");
  section("✗ Newly failing", diff.newlyFailing);
  section("✓ Newly passing", diff.newlyPassing);
  section("• Still failing", diff.stillFailing);
  section("+ Added", diff.added);
  section("- Removed", diff.removed);
  if (isCleanDiff(diff)) lines.push("   no changes since the previous run");
  return lines.join("\n");
}

/** Persist a {@link RegressionDiff} as pretty JSON. */
export async function writeDiffReport(diff: RegressionDiff, path: string): Promise<void> {
  await writeFile(path, `${JSON.stringify(diff, null, 2)}\n`, "utf8");
}

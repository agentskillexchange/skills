import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import type { ZodIssue } from "zod";
import { Plan, TestCase } from "../schema.js";
import { log, c } from "../log.js";

/**
 * Plan validation UX. Agents author Heimdall plans, so a failed plan must report
 * EVERY problem (not just the first batch), with the offending case index/id and
 * the in-case path made legible. Two extra affordances live here too: a
 * standalone `validate` command (dry-run; executes nothing) and the `--lenient`
 * helper that lets the run command salvage the valid cases.
 */

/** True when this issue's path begins `cases[<n>]`, i.e. it belongs to a case. */
function caseIndexOf(issue: ZodIssue): number | undefined {
  const [head, idx] = issue.path;
  if (head === "cases" && typeof idx === "number") return idx;
  return undefined;
}

/** Best-effort id lookup for `cases[n]` so messages name the case, not just an index. */
function caseIdAt(parsedJson: unknown, index: number): string | undefined {
  if (parsedJson === null || typeof parsedJson !== "object") return undefined;
  const cases = (parsedJson as { cases?: unknown }).cases;
  if (!Array.isArray(cases)) return undefined;
  const tc = cases[index];
  if (tc === null || typeof tc !== "object") return undefined;
  const id = (tc as { id?: unknown }).id;
  return typeof id === "string" && id.length > 0 ? id : undefined;
}

/** Render the part of the path INSIDE a case (or the whole path at plan level). */
function pathTail(path: ReadonlyArray<string | number>): string {
  return (
    path
      .map((seg) => (typeof seg === "number" ? String(seg) : seg))
      .join(".") || "<root>"
  );
}

/** A human-readable, single-line reason for one zod issue. */
function reasonFor(issue: ZodIssue): string {
  switch (issue.code) {
    case "unrecognized_keys":
      return `Unrecognized key: ${issue.keys.join(", ")}`;
    case "invalid_union_discriminator":
      return `Unknown discriminator (expected ${issue.options.map((o) => JSON.stringify(o)).join(" | ")})`;
    default:
      return issue.message;
  }
}

/**
 * Format a single zod issue as one readable line, attributing it to a case when
 * the path allows it — e.g. `cases[3] (id=foo): oracle.0 — Unrecognized key: exists`.
 */
function formatIssue(issue: ZodIssue, parsedJson: unknown): string {
  const idx = caseIndexOf(issue);
  const reason = reasonFor(issue);
  if (idx === undefined) {
    // Plan-level issue (e.g. bad defaultDriver, missing cases, top-level key).
    return `${pathTail(issue.path)} — ${reason}`;
  }
  const id = caseIdAt(parsedJson, idx);
  const where = id ? `cases[${idx}] (id=${id})` : `cases[${idx}]`;
  // Drop the leading `cases`, `<idx>` so the tail is the in-case path.
  const tail = pathTail(issue.path.slice(2));
  return `${where}: ${tail} — ${reason}`;
}

/**
 * Validate a parsed-JSON value against the Plan schema and return EVERY problem
 * as a readable line. Returns `[]` when the plan is valid. Never throws.
 */
export function collectPlanErrors(parsedJson: unknown): string[] {
  const result = Plan.safeParse(parsedJson);
  if (result.success) return [];
  // Stable order: by case index (plan-level issues first), then by path depth.
  const issues = [...result.error.issues].sort((a, b) => {
    const ai = caseIndexOf(a) ?? -1;
    const bi = caseIndexOf(b) ?? -1;
    if (ai !== bi) return ai - bi;
    return a.path.length - b.path.length;
  });
  return issues.map((issue) => formatIssue(issue, parsedJson));
}

/** One raw case from the parsed JSON, validated on its own (for --lenient). */
export interface CaseValidation {
  index: number;
  id?: string;
  raw: unknown;
  errors: string[];
}

/**
 * Validate each raw case of a parsed plan independently (for `run --lenient`).
 * The plan wrapper itself need not be valid; we read `cases` defensively. Each
 * entry reports the per-case zod errors (empty ⇒ that case is runnable).
 */
export function validateCasesIndividually(parsedJson: unknown): CaseValidation[] {
  const cases =
    parsedJson !== null && typeof parsedJson === "object" && Array.isArray((parsedJson as { cases?: unknown }).cases)
      ? ((parsedJson as { cases: unknown[] }).cases)
      : [];
  return cases.map((raw, index) => {
    const id = caseIdAt(parsedJson, index);
    const result = TestCase.safeParse(raw);
    if (result.success) return { index, id, raw, errors: [] };
    const errors = result.error.issues.map((issue) => {
      const tail = pathTail(issue.path);
      return `${tail} — ${reasonFor(issue)}`;
    });
    return { index, id, raw, errors };
  });
}

/**
 * `heimdall validate <plan>` — a dry-run plan check that executes nothing.
 * Prints a clear OK line when valid (exit 0), or every error (exit 2).
 */
export async function validateCommand(planPath: string): Promise<void> {
  const path = resolve(planPath);
  let raw: string;
  try {
    raw = await readFile(path, "utf8");
  } catch (e) {
    log.err(`could not read plan: ${e instanceof Error ? e.message : String(e)}`);
    process.exitCode = 2;
    return;
  }

  let parsedJson: unknown;
  try {
    parsedJson = JSON.parse(raw);
  } catch (e) {
    log.err(`could not parse plan JSON: ${e instanceof Error ? e.message : String(e)}`);
    process.exitCode = 2;
    return;
  }

  const errors = collectPlanErrors(parsedJson);
  if (errors.length === 0) {
    const count = Array.isArray((parsedJson as { cases?: unknown }).cases)
      ? (parsedJson as { cases: unknown[] }).cases.length
      : 0;
    log.ok(`valid: ${count} case${count === 1 ? "" : "s"}`);
    process.exitCode = 0;
    return;
  }

  log.err(`invalid plan — ${errors.length} problem${errors.length === 1 ? "" : "s"}:`);
  for (const line of errors) log.info(c.red("  • ") + line);
  process.exitCode = 2;
}

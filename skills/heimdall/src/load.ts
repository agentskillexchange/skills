/**
 * Load / concurrency primitive — the pure engine behind the `load` step.
 *
 * Kept browser-agnostic and side-effect-free (the caller supplies the per-call
 * request issuer) so the percentile/error-rate maths is unit-testable without a
 * Chromium. `runConcurrent` is a bounded worker pool; `summarizeLoad` reduces the
 * sampled outcomes to the {@link LoadStats} aggregate the oracles read.
 */
import type { LoadStats } from "./schema.js";

/** One sampled request outcome from a load step. */
export interface LoadSample {
  /** HTTP status (0 when the request threw before a response). */
  status: number;
  durationMs: number;
  /** True when the request threw or returned a non-2xx status. */
  error: boolean;
}

/**
 * Run `times` async tasks bounded by `concurrency` workers. Results are collected
 * in completion order (load samples are aggregated, so per-call order is moot).
 */
export async function runConcurrent<T>(
  times: number,
  concurrency: number,
  task: (i: number) => Promise<T>,
): Promise<T[]> {
  const results: T[] = [];
  const limit = Math.max(1, Math.min(concurrency, times));
  let next = 0;
  const worker = async (): Promise<void> => {
    for (let i = next++; i < times; i = next++) {
      results.push(await task(i));
    }
  };
  await Promise.all(Array.from({ length: limit }, () => worker()));
  return results;
}

/** Nearest-rank percentile of an ascending-sorted numeric array; `[]` ⇒ 0. */
export function percentile(sortedAsc: number[], p: number): number {
  if (sortedAsc.length === 0) return 0;
  if (p <= 0) return sortedAsc[0]!;
  if (p >= 100) return sortedAsc[sortedAsc.length - 1]!;
  const rank = Math.ceil((p / 100) * sortedAsc.length);
  const idx = Math.min(sortedAsc.length - 1, Math.max(0, rank - 1));
  return sortedAsc[idx]!;
}

/** Reduce sampled per-call outcomes to the load aggregate. */
export function summarizeLoad(samples: LoadSample[]): LoadStats {
  const count = samples.length;
  const errors = samples.reduce((n, s) => n + (s.error ? 1 : 0), 0);
  const errorRate = count === 0 ? 0 : errors / count;
  const durations = samples.map((s) => s.durationMs).sort((a, b) => a - b);
  return {
    count,
    errors,
    errorRate,
    minMs: durations[0] ?? 0,
    p50: percentile(durations, 50),
    p95: percentile(durations, 95),
    p99: percentile(durations, 99),
    maxMs: durations[durations.length - 1] ?? 0,
  };
}

/** The most frequently observed status (ties broken by the last seen); 0 when empty. */
export function modalStatus(samples: LoadSample[]): number {
  const counts = new Map<number, number>();
  let best = 0;
  let bestN = 0;
  for (const s of samples) {
    const n = (counts.get(s.status) ?? 0) + 1;
    counts.set(s.status, n);
    if (n >= bestN) {
      best = s.status;
      bestN = n;
    }
  }
  return best;
}

/** A one-line, human-readable summary of a load aggregate (used as `bodyText`). */
export function formatLoadStats(stats: LoadStats): string {
  const pct = (stats.errorRate * 100).toFixed(1);
  return (
    `load ${stats.count} req: ${stats.errors} error(s) (${pct}%), ` +
    `min ${stats.minMs}ms p50 ${stats.p50}ms p95 ${stats.p95}ms p99 ${stats.p99}ms max ${stats.maxMs}ms`
  );
}

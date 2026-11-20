import { describe, it, expect } from "vitest";
import {
  formatLoadStats,
  modalStatus,
  percentile,
  runConcurrent,
  summarizeLoad,
  type LoadSample,
} from "../src/load.js";

const sample = (status: number, durationMs: number, error = status >= 300 || status === 0): LoadSample => ({
  status,
  durationMs,
  error,
});

describe("percentile (nearest-rank)", () => {
  it("returns 0 for an empty set", () => {
    expect(percentile([], 95)).toBe(0);
  });

  it("computes p50/p95/p99/min/max over a sorted set", () => {
    const xs = Array.from({ length: 100 }, (_, i) => i + 1); // 1..100 ascending
    expect(percentile(xs, 50)).toBe(50);
    expect(percentile(xs, 95)).toBe(95);
    expect(percentile(xs, 99)).toBe(99);
    expect(percentile(xs, 0)).toBe(1);
    expect(percentile(xs, 100)).toBe(100);
  });

  it("clamps the rank into range for small sets", () => {
    expect(percentile([5], 95)).toBe(5);
    expect(percentile([1, 2], 99)).toBe(2);
  });

  it("picks the nearest-rank member of an irregular distribution (not interpolated)", () => {
    // 20 values: nineteen fast (10ms) and one slow tail (1000ms). Nearest-rank p95
    // of 20 samples is rank ceil(0.95*20)=19 -> index 18 -> still a 10ms value; only
    // p100/max surfaces the 1000ms tail. This guards against an interpolating impl.
    const xs = [...Array.from({ length: 19 }, () => 10), 1000].sort((a, b) => a - b);
    expect(percentile(xs, 95)).toBe(10); // ceil(0.95*20)=19 -> idx 18 -> 10
    expect(percentile(xs, 96)).toBe(1000); // ceil(0.96*20)=20 -> idx 19 -> 1000 (the tail)
    expect(percentile(xs, 100)).toBe(1000);
  });

  it("is monotonically non-decreasing across ascending p for a fixed set", () => {
    const xs = Array.from({ length: 50 }, (_, i) => (i + 1) * 3); // 3..150
    let prev = -Infinity;
    for (const p of [0, 25, 50, 75, 90, 95, 99, 100]) {
      const v = percentile(xs, p);
      expect(v).toBeGreaterThanOrEqual(prev);
      prev = v;
    }
  });
});

describe("summarizeLoad", () => {
  it("reduces samples to count / errors / errorRate / latency percentiles", () => {
    // 10 samples, 2 errors -> 20% error rate; durations 1..10ms.
    const samples: LoadSample[] = [
      sample(200, 1),
      sample(200, 2),
      sample(200, 3),
      sample(200, 4),
      sample(500, 5),
      sample(200, 6),
      sample(200, 7),
      sample(200, 8),
      sample(200, 9),
      sample(500, 10),
    ];
    const s = summarizeLoad(samples);
    expect(s.count).toBe(10);
    expect(s.errors).toBe(2);
    expect(s.errorRate).toBeCloseTo(0.2, 10);
    expect(s.minMs).toBe(1);
    expect(s.maxMs).toBe(10);
    expect(s.p50).toBe(5);
    expect(s.p95).toBe(10);
    expect(s.p99).toBe(10);
  });

  it("handles the empty case without dividing by zero", () => {
    const s = summarizeLoad([]);
    expect(s).toEqual({ count: 0, errors: 0, errorRate: 0, minMs: 0, p50: 0, p95: 0, p99: 0, maxMs: 0 });
  });

  it("reports a 100% error rate when every sample failed (incl. thrown status-0)", () => {
    const s = summarizeLoad([sample(500, 3), sample(0, 7), sample(503, 5)]);
    expect(s.count).toBe(3);
    expect(s.errors).toBe(3);
    expect(s.errorRate).toBe(1);
    // A thrown request (status 0) still contributes its latency to the percentiles.
    expect(s.minMs).toBe(3);
    expect(s.maxMs).toBe(7);
  });

  it("collapses every percentile onto the lone value for a single sample", () => {
    const s = summarizeLoad([sample(200, 42)]);
    expect(s).toMatchObject({ count: 1, errors: 0, errorRate: 0, minMs: 42, p50: 42, p95: 42, p99: 42, maxMs: 42 });
  });

  it("does not let sample arrival order corrupt the sorted percentiles", () => {
    // Same multiset, shuffled — summarize sorts internally, so stats are identical.
    const ordered = [sample(200, 1), sample(200, 2), sample(200, 3), sample(200, 4)];
    const shuffled = [sample(200, 3), sample(200, 1), sample(200, 4), sample(200, 2)];
    expect(summarizeLoad(shuffled)).toEqual(summarizeLoad(ordered));
  });
});

describe("modalStatus", () => {
  it("returns the most frequent status", () => {
    expect(modalStatus([sample(200, 1), sample(200, 2), sample(500, 3)])).toBe(200);
  });
  it("returns 0 for an empty set", () => {
    expect(modalStatus([])).toBe(0);
  });

  it("breaks an exact tie in favour of the last-seen status", () => {
    // 200 and 500 each appear once; the `>=` comparison keeps the later one.
    expect(modalStatus([sample(200, 1), sample(500, 2)])).toBe(500);
    expect(modalStatus([sample(500, 1), sample(200, 2)])).toBe(200);
  });
});

describe("runConcurrent", () => {
  it("runs exactly `times` tasks and never exceeds `concurrency` in flight", async () => {
    let inFlight = 0;
    let maxInFlight = 0;
    const seen: number[] = [];
    await runConcurrent(20, 4, async (i) => {
      inFlight++;
      maxInFlight = Math.max(maxInFlight, inFlight);
      await new Promise((r) => setTimeout(r, 2));
      seen.push(i);
      inFlight--;
    });
    expect(seen.length).toBe(20);
    expect(new Set(seen).size).toBe(20); // every index exactly once
    expect(maxInFlight).toBeLessThanOrEqual(4);
  });

  it("clamps concurrency to `times` and always runs at least one worker", async () => {
    let runs = 0;
    await runConcurrent(3, 50, async () => {
      runs++;
    });
    expect(runs).toBe(3);
  });

  it("runs strictly serially when concurrency is 1 (max in-flight never exceeds 1)", async () => {
    let inFlight = 0;
    let maxInFlight = 0;
    await runConcurrent(8, 1, async () => {
      inFlight++;
      maxInFlight = Math.max(maxInFlight, inFlight);
      await new Promise((r) => setTimeout(r, 1));
      inFlight--;
    });
    expect(maxInFlight).toBe(1);
  });

  it("treats a non-positive concurrency as a single worker rather than stalling", async () => {
    let runs = 0;
    // Math.max(1, ...) inside runConcurrent guards against a 0 worker count.
    await runConcurrent(4, 0, async () => {
      runs++;
    });
    expect(runs).toBe(4);
  });
});

describe("formatLoadStats", () => {
  it("renders a one-line human summary", () => {
    const s = summarizeLoad([sample(200, 4), sample(500, 8)]);
    const line = formatLoadStats(s);
    expect(line).toContain("load 2 req");
    expect(line).toContain("1 error(s) (50.0%)");
    expect(line).toContain("p95");
  });
});

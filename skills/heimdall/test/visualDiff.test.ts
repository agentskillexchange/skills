import { describe, it, expect } from "vitest";
import { PNG } from "pngjs";
import { comparePng, DimensionMismatchError } from "../src/visualDiff.js";

/** Build an in-memory PNG buffer of the given size, coloring each pixel via `fill`. */
function makePng(
  width: number,
  height: number,
  fill: (x: number, y: number) => [number, number, number, number],
): Buffer {
  const png = new PNG({ width, height });
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const idx = (width * y + x) << 2;
      const [r, g, b, a] = fill(x, y);
      png.data[idx] = r;
      png.data[idx + 1] = g;
      png.data[idx + 2] = b;
      png.data[idx + 3] = a;
    }
  }
  return PNG.sync.write(png);
}

const BLACK = (): [number, number, number, number] => [0, 0, 0, 255];
const WHITE = (): [number, number, number, number] => [255, 255, 255, 255];

describe("comparePng", () => {
  it("reports ratio 0 for identical images", () => {
    const a = makePng(8, 8, BLACK);
    const b = makePng(8, 8, BLACK);
    const res = comparePng(a, b);
    expect(res.ratio).toBe(0);
    expect(res.width).toBe(8);
    expect(res.height).toBe(8);
  });

  it("reports ratio ~1 for fully different images", () => {
    const a = makePng(8, 8, BLACK);
    const b = makePng(8, 8, WHITE);
    const res = comparePng(a, b);
    expect(res.ratio).toBe(1);
  });

  it("reports the expected fraction for a partial change", () => {
    // 10x10 = 100 px; flip the bottom half (rows 5..9) → 50 changed px.
    const a = makePng(10, 10, BLACK);
    const b = makePng(10, 10, (_x, y) => (y >= 5 ? [255, 255, 255, 255] : [0, 0, 0, 255]));
    const res = comparePng(a, b);
    expect(res.ratio).toBeCloseTo(0.5, 5);
  });

  it("returns a diffBuffer that decodes to the current dimensions", () => {
    const a = makePng(12, 7, BLACK);
    const b = makePng(12, 7, WHITE);
    const res = comparePng(a, b);
    const decoded = PNG.sync.read(res.diffBuffer);
    expect(decoded.width).toBe(12);
    expect(decoded.height).toBe(7);
  });

  it("throws DimensionMismatchError when sizes differ", () => {
    const a = makePng(8, 8, BLACK);
    const b = makePng(10, 8, BLACK);
    expect(() => comparePng(a, b)).toThrow(DimensionMismatchError);
    try {
      comparePng(a, b);
    } catch (err) {
      expect((err as Error).message).toContain("8x8");
      expect((err as Error).message).toContain("10x8");
    }
  });
});

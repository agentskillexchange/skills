/**
 * Pure PNG pixel comparison — the math behind visual regression, with no I/O.
 *
 * Decodes two PNG buffers, requires they share dimensions, and runs a
 * perceptual pixel diff. Returns the changed-pixel `ratio` (0 = identical,
 * 1 = every pixel differs), the image size, and an encoded diff PNG. Knows
 * nothing about the filesystem, Playwright, or the Plan schema — callers feed
 * it bytes and get bytes back.
 */
import pixelmatch from "pixelmatch";
import { PNG } from "pngjs";

/** Outcome of comparing two equally sized PNGs. */
export interface PngCompareResult {
  /** Fraction of pixels that changed, in `[0, 1]` (`changed / total`). */
  ratio: number;
  /** Shared width of both images, in pixels. */
  width: number;
  /** Shared height of both images, in pixels. */
  height: number;
  /** Encoded PNG highlighting the differing pixels, sized to the inputs. */
  diffBuffer: Buffer;
}

/** Knobs for {@link comparePng}; defaults match pixelmatch. */
export interface PngCompareOptions {
  /** Per-pixel matching threshold (0 strict … 1 lax). Defaults to `0.1`. */
  threshold?: number;
}

/**
 * Thrown by {@link comparePng} when the two PNGs do not share dimensions.
 * A pixel-by-pixel diff is undefined across different sizes, so rather than
 * silently scoring it `1` we fail loudly with both dimensions in the message.
 */
export class DimensionMismatchError extends Error {
  constructor(
    readonly baselineWidth: number,
    readonly baselineHeight: number,
    readonly currentWidth: number,
    readonly currentHeight: number,
  ) {
    super(
      `PNG dimension mismatch: baseline is ${baselineWidth}x${baselineHeight}, current is ${currentWidth}x${currentHeight}`,
    );
    this.name = "DimensionMismatchError";
  }
}

/**
 * Compare two PNG buffers pixel by pixel.
 *
 * Both images must share dimensions; otherwise a {@link DimensionMismatchError}
 * is thrown. On success the changed-pixel `ratio` is `changed / total`
 * (`0` when the images are empty), and `diffBuffer` is a freshly encoded PNG of
 * the same size with the differing pixels highlighted.
 */
export function comparePng(
  baseline: Buffer,
  current: Buffer,
  options: PngCompareOptions = {},
): PngCompareResult {
  const base = PNG.sync.read(baseline);
  const curr = PNG.sync.read(current);

  if (base.width !== curr.width || base.height !== curr.height) {
    throw new DimensionMismatchError(base.width, base.height, curr.width, curr.height);
  }

  const { width, height } = curr;
  const diff = new PNG({ width, height });
  const changed = pixelmatch(base.data, curr.data, diff.data, width, height, {
    threshold: options.threshold ?? 0.1,
  });

  const total = width * height;
  const ratio = total === 0 ? 0 : changed / total;
  const diffBuffer = PNG.sync.write(diff);

  return { ratio, width, height, diffBuffer };
}

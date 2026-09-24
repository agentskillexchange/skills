/** Minimal dependency-free logger with ANSI colour (auto-disabled when not a TTY). */
const useColor = process.stdout.isTTY && process.env.NO_COLOR === undefined;

const paint = (code: number, s: string) => (useColor ? `\x1b[${code}m${s}\x1b[0m` : s);

export const c = {
  dim: (s: string) => paint(2, s),
  red: (s: string) => paint(31, s),
  green: (s: string) => paint(32, s),
  yellow: (s: string) => paint(33, s),
  blue: (s: string) => paint(34, s),
  cyan: (s: string) => paint(36, s),
  bold: (s: string) => paint(1, s),
};

let verbose = false;
export const setVerbose = (v: boolean) => {
  verbose = v;
};

export const log = {
  info: (msg: string) => console.error(msg),
  step: (msg: string) => console.error(c.dim("  · " + msg)),
  ok: (msg: string) => console.error(c.green("✓ ") + msg),
  warn: (msg: string) => console.error(c.yellow("! ") + msg),
  err: (msg: string) => console.error(c.red("✗ ") + msg),
  debug: (msg: string) => {
    if (verbose) console.error(c.dim("[debug] " + msg));
  },
};

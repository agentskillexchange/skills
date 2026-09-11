import { describe, it, expect, afterEach } from "vitest";
import { mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { loadConfig } from "../src/config.js";
import { resolveRunNumber } from "../src/commands/run.js";

const cleanups: Array<() => void> = [];
afterEach(() => {
  while (cleanups.length) cleanups.pop()!();
});

function writeConfig(contents: string): string {
  const dir = mkdtempSync(join(tmpdir(), "heimdall-cfg-"));
  const path = join(dir, "heimdall.config.json");
  writeFileSync(path, contents, "utf8");
  cleanups.push(() => rmSync(dir, { recursive: true, force: true }));
  return path;
}

describe("loadConfig", () => {
  it("returns an empty config (never throws) when the file is missing", () => {
    expect(loadConfig(join(tmpdir(), "definitely-not-here-heimdall.config.json"))).toEqual({});
  });

  it("parses a valid config and returns typed fields", () => {
    const path = writeConfig(
      JSON.stringify({ baseUrl: "https://app.example", defaultDriver: "container", concurrency: 3, retries: 1 }),
    );
    const cfg = loadConfig(path);
    expect(cfg.baseUrl).toBe("https://app.example");
    expect(cfg.defaultDriver).toBe("container");
    expect(cfg.concurrency).toBe(3);
    expect(cfg.retries).toBe(1);
  });

  it("seeds process.env from env, without clobbering already-set keys", () => {
    const FRESH = "HEIMDALL_CFG_FRESH";
    const EXISTING = "HEIMDALL_CFG_EXISTING";
    delete process.env[FRESH];
    process.env[EXISTING] = "real-value";
    cleanups.push(() => {
      delete process.env[FRESH];
      delete process.env[EXISTING];
    });

    const path = writeConfig(
      JSON.stringify({ env: { [FRESH]: "from-config", [EXISTING]: "from-config" } }),
    );
    loadConfig(path);

    // Unset key gets seeded from config.
    expect(process.env[FRESH]).toBe("from-config");
    // Already-set key is preserved — real env always wins.
    expect(process.env[EXISTING]).toBe("real-value");
  });

  it("throws on malformed config (unknown key) rather than silently ignoring it", () => {
    const path = writeConfig(JSON.stringify({ bogus: true }));
    expect(() => loadConfig(path)).toThrow();
  });
});

describe("resolveRunNumber (CLI > config > builtin precedence)", () => {
  it("lets config fill in only when the CLI flag is still at its commander default", () => {
    // concurrency: default "4" not user-supplied → config wins.
    expect(resolveRunNumber("4", true, 8, 1)).toBe(8);
    // …but no config value → keep the CLI default.
    expect(resolveRunNumber("4", true, undefined, 1)).toBe(4);
  });

  it("honours an EXPLICITLY-passed flag equal to the default over config (the bug)", () => {
    // `--concurrency 4` explicitly: source is "cli", not "default" → CLI must win.
    expect(resolveRunNumber("4", false, 8, 1)).toBe(4);
    // `--retries 0` explicitly must beat a config retries:3 (the cross-corroborated edge).
    expect(resolveRunNumber("0", false, 3, 0)).toBe(0);
  });

  it("falls back to the floor on a non-default explicit but garbage value", () => {
    expect(resolveRunNumber("not-a-number", false, undefined, 1)).toBe(1);
    expect(resolveRunNumber(undefined, false, undefined, 0)).toBe(0);
  });

  it("clamps below-floor values up to the minimum", () => {
    expect(resolveRunNumber("0", false, undefined, 1)).toBe(1); // concurrency floor is 1
    expect(resolveRunNumber("-5", false, undefined, 0)).toBe(0);
  });
});

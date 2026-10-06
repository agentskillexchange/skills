/**
 * Optional `heimdall.config.json` loader.
 *
 * The config provides run-level defaults (baseUrl, driver, concurrency, retries,
 * storageState) and — crucially — an `env` map that seeds `process.env` for THIS
 * process. Seeding lets a plan reference `${env.API_TOKEN}` (see {@link applyVars})
 * without the secret living inside the plan JSON. Real environment values always
 * win: an `env` entry is only applied when the key is not already set, so the CLI
 * caller's environment overrides the config file.
 *
 * This module is intentionally dependency-light (only Zod) and side-effect-free
 * apart from the explicit, documented `process.env` seeding in {@link loadConfig}.
 */
import { readFileSync } from "node:fs";
import { z } from "zod";
import { Driver, Redaction } from "./schema.js";

/** Shape of `heimdall.config.json`. Every field is optional; unknown keys are rejected. */
export const HeimdallConfig = z
  .object({
    baseUrl: z.string().optional(),
    defaultDriver: Driver.optional(),
    concurrency: z.number().int().positive().optional(),
    retries: z.number().int().nonnegative().optional(),
    storageState: z.string().optional().describe("path to a Playwright storageState for injected auth"),
    /**
     * Extra redaction applied on top of the per-run `${env.X}` secrets: response-header
     * names whose values are blanked and regex patterns scrubbed from the report and the
     * raw HAR evidence. Reuses the plan-level {@link Redaction} shape.
     */
    redaction: Redaction.optional(),
    /**
     * Environment seed. Each entry is written to `process.env` only when the key
     * is not already present, so a real environment variable always takes priority.
     */
    env: z.record(z.string()).optional(),
  })
  .strict();
export type HeimdallConfig = z.infer<typeof HeimdallConfig>;

const DEFAULT_CONFIG_PATH = "heimdall.config.json";

/**
 * Load and validate `heimdall.config.json` (or an explicit path).
 *
 * A missing file yields an empty config and never throws — config is optional. A
 * present-but-malformed file (bad JSON or failing the schema) DOES throw, so a
 * typo in real config is surfaced loudly rather than silently ignored.
 *
 * Side effect: when `env` is present, its entries seed `process.env` for keys that
 * are not already set (real env wins). Returns the validated, typed config.
 */
export function loadConfig(path: string = DEFAULT_CONFIG_PATH): HeimdallConfig {
  let raw: string;
  try {
    raw = readFileSync(path, "utf8");
  } catch {
    // No file (ENOENT) or unreadable → treat as "no config", the common case.
    return {};
  }

  const parsed = HeimdallConfig.parse(JSON.parse(raw));

  if (parsed.env) {
    for (const [key, value] of Object.entries(parsed.env)) {
      // Only seed keys the real environment hasn't already provided.
      if (process.env[key] === undefined) process.env[key] = value;
    }
  }

  return parsed;
}

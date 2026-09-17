/**
 * `heimdall gc` — prune orphaned Playwright browser revisions.
 *
 * Playwright keeps every browser revision it ever downloaded in its cache; old
 * ones accrete (e.g. chromium-1148/1217/1223/1228 = ~2 GB). This keeps the
 * newest revision of each browser family and removes the rest. Dry-run by
 * default; pass `--yes` to actually delete.
 */
import { execFile } from "node:child_process";
import { readdir, rm, stat } from "node:fs/promises";
import { homedir } from "node:os";
import { join } from "node:path";
import { promisify } from "node:util";
import { c, log } from "../log.js";

const pexecFile = promisify(execFile);

function cacheDir(): string {
  if (process.env.PLAYWRIGHT_BROWSERS_PATH && process.env.PLAYWRIGHT_BROWSERS_PATH !== "0") {
    return process.env.PLAYWRIGHT_BROWSERS_PATH;
  }
  switch (process.platform) {
    case "darwin":
      return join(homedir(), "Library", "Caches", "ms-playwright");
    case "win32":
      return join(process.env.LOCALAPPDATA ?? homedir(), "ms-playwright");
    default:
      return join(homedir(), ".cache", "ms-playwright");
  }
}

/** Parse "chromium-1228" -> { family: "chromium", rev: 1228 }. */
function parseEntry(name: string): { family: string; rev: number } | undefined {
  const m = /^([a-z_]+)-(\d+)$/.exec(name);
  if (!m) return undefined;
  return { family: m[1]!, rev: Number.parseInt(m[2]!, 10) };
}

async function dirSizeMB(path: string): Promise<number> {
  try {
    const { stdout } = await pexecFile("du", ["-sk", path], { maxBuffer: 16 * 1024 * 1024 });
    const kb = Number.parseInt(stdout.split(/\s+/)[0] ?? "0", 10);
    return Math.round(kb / 1024);
  } catch {
    return 0;
  }
}

export interface GcOpts {
  yes?: boolean;
}

export async function gcCommand(opts: GcOpts): Promise<void> {
  const dir = cacheDir();
  let entries: string[];
  try {
    entries = await readdir(dir);
  } catch {
    log.warn(`no Playwright cache at ${dir} — nothing to do`);
    return;
  }

  // Group revisioned dirs by family.
  const byFamily = new Map<string, { name: string; rev: number }[]>();
  for (const name of entries) {
    const parsed = parseEntry(name);
    if (!parsed) continue;
    const full = join(dir, name);
    if (!(await stat(full)).isDirectory()) continue;
    (byFamily.get(parsed.family) ?? byFamily.set(parsed.family, []).get(parsed.family)!).push({
      name,
      rev: parsed.rev,
    });
  }

  const toRemove: string[] = [];
  for (const [family, revs] of byFamily) {
    revs.sort((a, b) => b.rev - a.rev);
    const keep = revs[0]!;
    log.info(`${c.cyan(family)}: keep ${c.green(keep.name)}` + (revs.length > 1 ? c.dim(`, prune ${revs.length - 1}`) : ""));
    for (const r of revs.slice(1)) toRemove.push(join(dir, r.name));
  }

  if (toRemove.length === 0) {
    log.ok("cache is already clean — no orphaned revisions");
    return;
  }

  let freedMB = 0;
  for (const path of toRemove) freedMB += await dirSizeMB(path);

  log.info(c.dim("─".repeat(50)));
  log.info(`${toRemove.length} orphaned revision(s), ~${c.bold(`${freedMB} MB`)}`);
  for (const p of toRemove) log.info(c.dim(`  ${p}`));

  if (!opts.yes) {
    log.warn(`dry-run. Re-run with ${c.bold("--yes")} to delete.`);
    return;
  }

  for (const p of toRemove) {
    await rm(p, { recursive: true, force: true });
    log.step(`removed ${p}`);
  }
  log.ok(`freed ~${freedMB} MB`);
}

import { existsSync } from "node:fs";
import { chromium } from "playwright";
import { dockerAvailable, imageExists, IMAGE_TAG } from "../drivers/container.js";
import { c, log } from "../log.js";
import { VERSION } from "../version.js";

export interface Check {
  name: string;
  ok: boolean;
  detail: string;
  fix?: string;
}

/** Gather toolchain checks (shared by the `doctor` command and the MCP server). */
export async function collectDoctorChecks(): Promise<Check[]> {
  const checks: Check[] = [];

  // Node
  const major = Number.parseInt(process.versions.node.split(".")[0] ?? "0", 10);
  checks.push({
    name: "Node.js >= 20",
    ok: major >= 20,
    detail: `v${process.versions.node}`,
    fix: "install Node 20+",
  });

  // Playwright Chromium (the cdp driver)
  let chromiumPath = "";
  try {
    chromiumPath = chromium.executablePath();
  } catch {
    /* not installed */
  }
  const chromiumOk = Boolean(chromiumPath) && existsSync(chromiumPath);
  checks.push({
    name: "Playwright Chromium (cdp driver)",
    ok: chromiumOk,
    detail: chromiumOk ? chromiumPath : "not installed",
    fix: "npx playwright install chromium",
  });

  // Docker (the container driver)
  const docker = await dockerAvailable();
  checks.push({
    name: "Docker (container driver)",
    ok: docker,
    detail: docker ? "running" : "not available",
    fix: "start Docker Desktop / install docker — only needed for --driver container",
  });

  // Heimdall image
  const img = docker ? await imageExists() : false;
  checks.push({
    name: `Container image (${IMAGE_TAG})`,
    ok: img,
    detail: img ? "built" : "not built",
    fix: "heimdall build-image — or it auto-builds on first container run",
  });

  return checks;
}

/** True when the cdp lane (the floor) is usable. */
export function cdpReady(checks: Check[]): boolean {
  return Boolean(checks[0]?.ok && checks[1]?.ok);
}

export async function doctorCommand(): Promise<void> {
  const checks = await collectDoctorChecks();

  log.info(c.bold(`Heimdall doctor`) + c.dim(`  v${VERSION}`));
  log.info(c.dim("─".repeat(60)));
  for (const ck of checks) {
    const mark = ck.ok ? c.green("✓") : c.yellow("✗");
    log.info(`${mark} ${ck.name.padEnd(36)} ${c.dim(ck.detail)}`);
    if (!ck.ok && ck.fix) log.info(c.dim(`    fix: ${ck.fix}`));
  }
  log.info(c.dim("─".repeat(60)));

  // The cdp lane is the floor; container is optional.
  const ready = cdpReady(checks);
  if (ready) log.ok("cdp lane ready");
  else log.warn("cdp lane not ready — fix the checks above");
  process.exitCode = ready ? 0 : 1;
}

import { writeFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import { resolve } from "node:path";
import type { Plan } from "../schema.js";
import { log, c } from "../log.js";

export const SAMPLE_PLAN: Plan = {
  name: "example-plan",
  baseUrl: "http://localhost:3000",
  defaultDriver: "cdp",
  cases: [
    {
      id: "home-loads",
      title: "Home page renders without console errors",
      dimension: "functional",
      steps: [{ action: "goto", url: "/" }],
      oracle: [{ assert: "noConsoleErrors" }, { assert: "visible", selector: "body" }],
      risk: "read-only",
      priority: "p0",
      tags: ["smoke"],
    },
    {
      id: "health-endpoint",
      title: "Health endpoint returns 200 and ok:true",
      dimension: "api",
      steps: [{ action: "fetch", url: "/api/health", method: "GET", as: "health" }],
      oracle: [
        { assert: "status", equals: 200, of: "health" },
        { assert: "jsonPath", path: "ok", equals: true, of: "health" },
      ],
      risk: "read-only",
      priority: "p1",
      tags: ["api", "smoke"],
    },
  ],
};

export async function initCommand(out: string): Promise<void> {
  const path = resolve(out);
  if (existsSync(path)) {
    log.err(`${path} already exists — refusing to overwrite`);
    process.exitCode = 1;
    return;
  }
  await writeFile(path, JSON.stringify(SAMPLE_PLAN, null, 2) + "\n", "utf8");
  log.ok(`wrote sample plan to ${c.bold(path)}`);
  log.info(c.dim(`  edit baseUrl + cases, then: heimdall run ${out}`));
}

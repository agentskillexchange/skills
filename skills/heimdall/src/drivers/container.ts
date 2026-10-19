/**
 * Container driver — runs a case via the `cdp` path inside a disposable Docker
 * sandbox whose Playwright base image bundles Chromium + Xvfb.
 *
 * Each case gets its own throwaway container (its own Xvfb display → its own OS
 * input focus), which is why this regime can run isolated *headed* sessions in
 * parallel and is the safe home for destructive/untrusted SUTs. It needs Docker;
 * on macOS that is Docker Desktop's Linux VM, so the browser is *Linux* Chrome
 * (fidelity tier `medium-linux`).
 */
import { execFile } from "node:child_process";
import { mkdtemp, readFile, writeFile, cp, mkdir, chmod, rm } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { promisify } from "node:util";
import type { Plan, Result, Step, TestCase } from "../schema.js";
import { fidelityForDriver } from "../schema.js";
import { ensureCaseDir } from "../execute.js";
import type { CaseDriver, RunContext } from "./types.js";
import { log } from "../log.js";

const pexecFile = promisify(execFile);
const here = dirname(fileURLToPath(import.meta.url));
// dist/drivers/container.js -> package root is two levels up.
const packageRoot = join(here, "..", "..");

export const IMAGE_TAG = "heimdall:local";

async function docker(args: string[], opts: { timeoutMs?: number } = {}): Promise<string> {
  const { stdout } = await pexecFile("docker", args, {
    timeout: opts.timeoutMs ?? 0,
    maxBuffer: 64 * 1024 * 1024,
  });
  return stdout;
}

export async function dockerAvailable(): Promise<boolean> {
  try {
    await docker(["version", "--format", "{{.Server.Version}}"], { timeoutMs: 10_000 });
    return true;
  } catch {
    return false;
  }
}

export async function imageExists(tag = IMAGE_TAG): Promise<boolean> {
  try {
    const out = await docker(["images", "-q", tag]);
    return out.trim().length > 0;
  } catch {
    return false;
  }
}

/** Build the Heimdall runner image from the packaged Dockerfile. */
export async function buildImage(tag = IMAGE_TAG): Promise<void> {
  const dockerfile = join(packageRoot, "docker", "Dockerfile");
  log.info(`Building ${tag} from ${dockerfile} …`);
  await docker(["build", "-f", dockerfile, "-t", tag, packageRoot]);
  log.ok(`Built ${tag}`);
}

/** Rewrite a host-local URL so a container can reach the host's SUT. */
function toHostUrl(url: string): string {
  return url.replace(/\/\/(localhost|127\.0\.0\.1)(:|\/|$)/, "//host.docker.internal$2");
}

function containerBaseUrl(baseUrl: string | undefined): string | undefined {
  return baseUrl ? toHostUrl(baseUrl) : baseUrl;
}

/**
 * Rewrite every URL-bearing step so an absolute `localhost`/`127.0.0.1` target
 * reaches the host's SUT via `host.docker.internal`. Covers EVERY network action
 * with a `url` (goto/fetch/request/pollUntil/load/sse) — not just goto/fetch — and
 * is applied to a case's `steps`, `setup` AND `teardown`, so a hook/load/sse step
 * pointed at the host doesn't silently hit the container's own loopback. Relative
 * URLs (resolved against the rewritten baseUrl) pass through untouched.
 */
function rewriteHostUrls(steps: Step[]): Step[] {
  return steps.map((s) => {
    switch (s.action) {
      case "goto":
      case "fetch":
      case "request":
      case "pollUntil":
      case "load":
      case "sse":
        return { ...s, url: toHostUrl(s.url) };
      default:
        return s;
    }
  });
}

/**
 * Collect the distinct `${env.NAME}` variable names a case references across its
 * steps/setup/teardown (URLs, bodies, headers). Used to forward those env vars into
 * the container via `docker run -e NAME` so `${env.NAME}` interpolation — which runs
 * INSIDE the container (a process that does not inherit the host's env otherwise) —
 * resolves to the host's value. The `-e NAME` form (no `=value`) forwards the host's
 * current value WITHOUT writing it to the on-disk sub-plan.
 */
function collectEnvRefs(tc: TestCase): string[] {
  const names = new Set<string>();
  const re = /\$\{env\.([\w.]+)\}/g;
  const hay = JSON.stringify(tc);
  let m: RegExpExecArray | null;
  while ((m = re.exec(hay)) !== null) names.add(m[1]!);
  return [...names];
}

const WORK_OUT_CASES = "/work/out/cases";

/** Remap an in-container evidence path to where we copied it on the host. */
function remapEvidencePath(p: string, caseDir: string): string {
  if (!p.startsWith(WORK_OUT_CASES)) return p;
  const rel = p.slice(WORK_OUT_CASES.length).replace(/^\//, "");
  return join(caseDir, "container", rel);
}

export class ContainerDriver implements CaseDriver {
  readonly name = "container" as const;

  async setup(): Promise<void> {
    if (!(await dockerAvailable())) {
      throw new Error("Docker is not available — `container` driver needs Docker running. Run `heimdall doctor`.");
    }
    if (!(await imageExists())) {
      log.warn(`Image ${IMAGE_TAG} not found; building it once (this can take a few minutes).`);
      await buildImage();
    }
  }

  async runCase(tc: TestCase, ctx: RunContext): Promise<Result> {
    const started = Date.now();
    const fidelityTier = fidelityForDriver("container");
    const caseDir = await ensureCaseDir(ctx.outDir, tc.id);

    // Sandbox under outDir (not the OS tmpdir): on macOS, colima/Lima does not
    // mount /var/folders into its VM, so a tmpdir bind mount would be empty inside
    // the container. outDir lives in the project tree, which the VM does mount.
    const work = await mkdtemp(join(ctx.outDir, ".sandbox-"));
    const inDir = join(work, "in");
    const outDir = join(work, "out");
    await mkdir(inDir, { recursive: true });
    await mkdir(outDir, { recursive: true });

    // Absolute localhost URLs in steps/setup/teardown must also reach the host,
    // like baseUrl does — across every URL-bearing action, not just goto/fetch.
    const subCase: TestCase = {
      ...tc,
      driver: "cdp",
      steps: rewriteHostUrls(tc.steps),
      ...(tc.setup ? { setup: rewriteHostUrls(tc.setup) } : {}),
      ...(tc.teardown ? { teardown: rewriteHostUrls(tc.teardown) } : {}),
    };

    // A single-case plan, forced onto the in-container cdp path. The redaction spec
    // (header NAMES + regex SOURCES — never secret values) is threaded in so the inner
    // cdp run scrubs its OWN network.har via scrubHar BEFORE we copy it out; otherwise
    // the container lane would leak the exact header values/PII the #16 redaction
    // feature exists to blank (the cdp lane already scrubs in its own driver).
    const subPlan: Plan = {
      name: `case-${tc.id}`,
      baseUrl: containerBaseUrl(tc.baseUrl ?? ctx.baseUrl),
      defaultDriver: "cdp",
      ...(ctx.redaction ? { redaction: ctx.redaction } : {}),
      cases: [subCase],
    };
    // The sub-plan keeps `${env.NAME}` tokens VERBATIM — never the resolved secret
    // values — so nothing sensitive is written to disk; the values are forwarded
    // separately via `docker run -e NAME` below and resolved inside the container.
    await writeFile(join(inDir, "plan.json"), JSON.stringify(subPlan, null, 2), "utf8");
    if (ctx.storageState) {
      const dest = join(inDir, "storageState.json");
      await cp(ctx.storageState, dest);
      await chmod(dest, 0o600); // it holds live cookies/tokens
    }

    // Forward the host env vars the case references via `${env.NAME}` so the
    // in-container interpolation resolves them. `-e NAME` (no value) passes the
    // host's current value through Docker WITHOUT it touching the on-disk sub-plan.
    const envArgs = collectEnvRefs(tc)
      .filter((name) => process.env[name] !== undefined)
      .flatMap((name) => ["-e", name]);

    const args = [
      "run",
      "--rm",
      "--add-host=host.docker.internal:host-gateway",
      ...envArgs,
      "-v",
      `${inDir}:/work/in:ro`,
      "-v",
      `${outDir}:/work/out`,
      IMAGE_TAG,
      "run",
      "/work/in/plan.json",
      "--driver",
      "cdp",
      "--out",
      "/work/out",
      ...(ctx.storageState ? ["--storage-state", "/work/in/storageState.json"] : []),
      ...(ctx.allowRisk ? ["--allow-risk"] : []),
      ...(ctx.trace !== "off" ? ["--trace", ctx.trace] : []),
      ...(ctx.video !== "off" ? ["--video", ctx.video] : []),
    ];

    try {
      await docker(args, { timeoutMs: 5 * 60_000 });
      const reportRaw = await readFile(join(outDir, "report.json"), "utf8");
      const report = JSON.parse(reportRaw) as { results: Result[] };
      const inner = report.results[0];
      if (!inner) throw new Error("container produced no result");

      // Copy evidence out of the throwaway mount into our run's case dir.
      await cp(join(outDir, "cases"), join(caseDir, "container"), { recursive: true }).catch(() => {});

      return {
        ...inner,
        id: tc.id,
        driver: "container",
        fidelityTier,
        // Remap in-container paths (/work/out/...) to where we copied them on the host.
        evidence: {
          ...inner.evidence,
          screenshots: inner.evidence.screenshots.map((p) => remapEvidencePath(p, caseDir)),
          har: inner.evidence.har ? remapEvidencePath(inner.evidence.har, caseDir) : undefined,
          trace: inner.evidence.trace ? remapEvidencePath(inner.evidence.trace, caseDir) : undefined,
          video: inner.evidence.video ? remapEvidencePath(inner.evidence.video, caseDir) : undefined,
        },
        notes: `ran in ${IMAGE_TAG} (Linux Chrome)`,
        durationMs: Date.now() - started,
      };
    } catch (e) {
      return {
        id: tc.id,
        status: "error",
        driver: "container",
        fidelityTier,
        observed: `container error: ${e instanceof Error ? e.message : String(e)}`,
        failures: [e instanceof Error ? e.message : String(e)],
        evidence: { screenshots: [], consoleErrors: [], responses: [] },
        durationMs: Date.now() - started,
      };
    } finally {
      // The temp dir held a cleartext copy of the injected session — always remove it.
      await rm(work, { recursive: true, force: true }).catch(() => {});
    }
  }

  async teardown(): Promise<void> {
    // Containers are --rm; nothing persistent to clean up.
  }
}

/**
 * Container-driver end-to-end test.
 *
 * Skipped automatically unless Docker is running AND the heimdall:local image is
 * built (CI without Docker, or before `heimdall build-image`, just skips it). It
 * proves the `container` lane: a case runs inside a disposable Docker + Xvfb
 * sandbox, reaches the host's fixture via host.docker.internal, and passes.
 */
import { afterAll, beforeAll, describe, expect, it } from "vitest";
import { mkdtemp, mkdir, rm, readFile } from "node:fs/promises";
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from "node:fs";
import { join } from "node:path";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import { runPlan, type Plan } from "../../src/index.js";
import { dockerAvailable, imageExists, IMAGE_TAG } from "../../src/drivers/container.js";
import { startFixtureServer, type FixtureServer } from "../fixtures/server.js";

const pexecFile = promisify(execFile);

/**
 * Probe a real bind-mount round-trip. colima/Lima (macOS Docker backends) only mount
 * SPECIFIC host paths into the VM; when the repo lives outside them (e.g. under
 * /tmp), a `-v` bind mount is EMPTY inside the container and every container case
 * errors with ENOENT — an environment limitation, not a driver bug. Gate the e2e on
 * an actual mount working (mirroring the dockerAvailable/imageExists guards) so it
 * skips cleanly where the mount is unusable and runs where it is.
 */
async function bindMountWorks(): Promise<boolean> {
  let dir: string | undefined;
  try {
    const base = join(process.cwd(), "heimdall-runs");
    mkdirSync(base, { recursive: true });
    dir = mkdtempSync(join(base, "mountprobe-"));
    writeFileSync(join(dir, "marker"), "mounted", "utf8");
    const { stdout } = await pexecFile(
      "docker",
      ["run", "--rm", "-v", `${dir}:/probe:ro`, "--entrypoint", "cat", IMAGE_TAG, "/probe/marker"],
      { timeout: 30_000 },
    );
    return stdout.trim() === "mounted";
  } catch {
    return false;
  } finally {
    if (dir) rmSync(dir, { recursive: true, force: true });
  }
}

const ready = (await dockerAvailable()) && (await imageExists()) && (await bindMountWorks());

describe.skipIf(!ready)("container driver end-to-end", () => {
  let fixture: FixtureServer;
  let outDir: string;

  beforeAll(async () => {
    // Bind to 0.0.0.0 so the container can reach it via host.docker.internal.
    fixture = await startFixtureServer("0.0.0.0");
    // outDir must be in the project tree (mounted into the colima/Lima VM), not the
    // OS tmpdir which macOS Docker backends don't share.
    const base = join(process.cwd(), "heimdall-runs");
    await mkdir(base, { recursive: true });
    outDir = await mkdtemp(join(base, "ctr-e2e-"));
  });

  afterAll(async () => {
    await fixture?.stop();
    await rm(outDir, { recursive: true, force: true }).catch(() => {});
  });

  it(
    "runs a ui case inside a disposable container and passes",
    async () => {
      const plan: Plan = {
        name: "container-e2e",
        baseUrl: fixture.baseUrl, // localhost -> rewritten to host.docker.internal by the driver
        defaultDriver: "container",
        cases: [
          {
            id: "ctr-home-renders",
            steps: [{ action: "goto", url: "/" }],
            oracle: [
              { assert: "visible", selector: "#app" },
              { assert: "textContains", selector: "#app", value: "Heimdall OK" },
            ],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, {
        outDir,
        allowRisk: false,
        headed: false,
        concurrency: 1,
      });

      const r = report.results[0];
      expect(r?.driver).toBe("container");
      expect(r?.fidelityTier).toBe("medium-linux");
      expect(report.summary.pass).toBe(1);
      expect(report.summary.fail + report.summary.error).toBe(0);
    },
    180_000,
  );

  it(
    "scrubs a configured redaction pattern from the container's copied-out network.har",
    async () => {
      // The container lane copies the inner HAR out to the host. The redaction spec is
      // threaded into the sub-plan so the INNER cdp run scrubs the HAR before copy-out;
      // without that, the spec-targeted secret would leak verbatim in the host's copy.
      const SECRET = "sk-live-ctrhar00112233445566";
      const plan: Plan = {
        name: "container-redaction",
        baseUrl: fixture.baseUrl,
        defaultDriver: "container",
        redaction: { patterns: ["sk-live-[A-Za-z0-9]+"] },
        cases: [
          {
            id: "ctr-har-redaction",
            // The secret rides in the request URL, so it lands in the HAR's request entry.
            steps: [{ action: "request", url: `/echo-secret?probe=${SECRET}`, as: "s" }],
            oracle: [{ assert: "status", equals: 200, of: "s" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, { outDir, allowRisk: false, headed: false, concurrency: 1 });
      const r = report.results[0];
      expect(r?.status).toBe("pass");
      // The report is scrubbed...
      expect(JSON.stringify(report)).not.toContain(SECRET);
      // ...AND the copied-out container HAR is scrubbed (the inner run applied scrubHar).
      expect(r?.evidence.har, "container case should have a HAR").toBeTruthy();
      const har = await readFile(r!.evidence.har!, "utf8");
      expect(har).not.toContain(SECRET);
      expect(har).toContain("[redacted]");
    },
    180_000,
  );

  it(
    "rewrites ABSOLUTE host URLs in setup/load/sse steps so hooks and aggregates reach the host SUT",
    async () => {
      // Every URL here is an ABSOLUTE localhost URL (not relative-to-baseUrl), so it
      // only reaches the host if the driver rewrote it to host.docker.internal across
      // setup, load AND sse — the gap this exercises. If any rewrite were missing the
      // step would hit the container's own loopback: all-error load / zero events.
      const abs = (p: string) => `${fixture.baseUrl}${p}`;
      const plan: Plan = {
        name: "container-hosturl-e2e",
        defaultDriver: "container",
        cases: [
          {
            id: "ctr-hooks-load-sse",
            setup: [{ action: "request", url: abs("/resource"), method: "POST", capture: { rid: { jsonPath: "id" } }, as: "made" }],
            steps: [
              { action: "load", url: abs("/slow"), times: 10, concurrency: 4, as: "lt" },
              { action: "sse", url: abs("/events"), events: 3, timeoutMs: 5000, as: "stream" },
            ],
            teardown: [{ action: "request", url: abs("/resource?id=${rid}"), method: "DELETE" }],
            oracle: [
              { assert: "errorRate", max: 0.5, of: "lt" },
              { assert: "eventCount", min: 1, of: "stream" },
            ],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const report = await runPlan(plan, { outDir, allowRisk: false, headed: false, concurrency: 1 });
      const r = report.results[0];
      if (r?.status !== "pass") {
        throw new Error(`expected pass (host URLs rewritten in hooks/load/sse), got ${JSON.stringify(r)}`);
      }
      expect(r?.driver).toBe("container");
      expect(report.summary.pass).toBe(1);
    },
    180_000,
  );

  it(
    "forwards a referenced ${env.X} secret into the container so it reaches the SUT",
    async () => {
      const KEY = "HEIMDALL_CTR_E2E_TOKEN";
      const SECRET = "Bearer ctr-secret-from-host";
      process.env[KEY] = SECRET;
      try {
        const plan: Plan = {
          name: "container-env-e2e",
          baseUrl: fixture.baseUrl,
          defaultDriver: "container",
          cases: [
            {
              id: "ctr-env-reaches-sut",
              // ${env.X} resolves INSIDE the container; it only works if the driver
              // forwarded the host env var via `docker run -e KEY` (value never on disk).
              steps: [{ action: "request", url: "/echo-auth", headers: { authorization: "${env.HEIMDALL_CTR_E2E_TOKEN}" }, as: "echo" }],
              oracle: [
                { assert: "status", equals: 200, of: "echo" },
                { assert: "jsonPath", path: "authorization", equals: SECRET, of: "echo" },
              ],
              risk: "read-only",
              priority: "p0",
              tags: [],
            },
          ],
        };

        const report = await runPlan(plan, { outDir, allowRisk: false, headed: false, concurrency: 1 });
        const r = report.results[0];
        if (r?.status !== "pass") {
          throw new Error(`expected the forwarded env secret to reach the SUT, got ${JSON.stringify(r)}`);
        }
        expect(report.summary.pass).toBe(1);
        // The forwarded secret must not be serialized into the report.
        expect(JSON.stringify(report)).not.toContain("ctr-secret-from-host");
      } finally {
        delete process.env[KEY];
      }
    },
    180_000,
  );
});

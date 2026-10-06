/**
 * REAL end-to-end test for env-secret interpolation (ROADMAP #9) and its honest
 * redaction scope.
 *
 * Confirms that a secret injected via the environment — `${env.NAME}` — is resolved
 * at runtime by {@link applyVars} and actually reaches the SUT inside a request
 * header AND a request URL, end-to-end through the public `runPlan` API + a real
 * Chromium browser. Then it pins the security contract precisely:
 *
 *   - the resolved secret is SCRUBBED from the report (both the returned object and
 *     the on-disk report.json), even when spliced into a URL → `responses[].url`;
 *   - the resolved secret is NOT scrubbed from the binary Playwright EVIDENCE file
 *     (`network.har`), which retains request headers/URLs on the wire — so the test
 *     is honest about what the run output directory contains.
 *
 * A real fixture endpoint (`GET /echo-auth`) reflects the request's Authorization
 * header back in its body, so we can assert the resolved secret landed on the wire.
 */
import { mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterAll, beforeAll, describe, expect, it, vi } from "vitest";

import { runPlan, type Plan, type RunOptions } from "../../src/index.js";
import { startFixtureServer, type FixtureServer } from "../fixtures/server.js";

let fixture: FixtureServer;
let outDir: string;
const TOKEN_KEY = "HEIMDALL_E2E_TOKEN";
const URL_TOKEN_KEY = "HEIMDALL_E2E_URLTOKEN";
const HEADER_SECRET = "Bearer s3cr3t-from-env";
// A URL-safe secret (no spaces): it must survive into a request URL verbatim so the
// redaction match is exact (Playwright would percent-encode a space in the URL).
const URL_SECRET = "urlsecret-abc123def";

beforeAll(async () => {
  fixture = await startFixtureServer();
  outDir = await mkdtemp(join(tmpdir(), "heimdall-cfg-e2e-"));
  process.env[TOKEN_KEY] = HEADER_SECRET;
  process.env[URL_TOKEN_KEY] = URL_SECRET;
});

afterAll(async () => {
  delete process.env[TOKEN_KEY];
  delete process.env[URL_TOKEN_KEY];
  await fixture?.stop();
  if (outDir) {
    await rm(outDir, { recursive: true, force: true }).catch(() => {});
  }
});

describe("env-secret interpolation end-to-end", () => {
  it(
    "resolves ${env.X} into a request header that reaches the SUT, and blanks unset env vars",
    async () => {
      const plan: Plan = {
        name: "config-e2e",
        defaultDriver: "cdp",
        cases: [
          {
            id: "env-secret-reaches-sut",
            title: "an ${env.X} secret is interpolated into the Authorization header",
            // No goto: the request step uses the browser-context APIRequestContext.
            steps: [
              {
                action: "request",
                url: "/echo-auth",
                headers: { authorization: "${env.HEIMDALL_E2E_TOKEN}" },
                as: "echo",
              },
            ],
            oracle: [
              { assert: "status", equals: 200, of: "echo" },
              // The server reflected exactly the env-resolved header value back.
              { assert: "jsonPath", path: "authorization", equals: HEADER_SECRET, of: "echo" },
            ],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
          {
            id: "unset-env-blanks",
            title: "an unset ${env.X} resolves to empty, not the literal token",
            steps: [
              {
                action: "request",
                url: "/echo-auth",
                headers: { authorization: "${env.HEIMDALL_E2E_MISSING}" },
                as: "echo",
              },
            ],
            oracle: [
              { assert: "status", equals: 200, of: "echo" },
              { assert: "jsonPath", path: "authorization", equals: "", of: "echo" },
            ],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const opts: RunOptions = {
        outDir,
        baseUrl: fixture.baseUrl,
        allowRisk: false,
        headed: false,
        concurrency: 2,
        driverOverride: "cdp",
      };

      const report = await runPlan(plan, opts);

      if (report.summary.pass !== 2) {
        const detail = report.results
          .map((r) => `${r.id}: ${r.status} — ${r.observed}${r.failures.length ? ` [${r.failures.join("; ")}]` : ""}`)
          .join("\n");
        throw new Error(`expected 2 passing cases, got summary=${JSON.stringify(report.summary)}\n${detail}`);
      }

      expect(report.summary.total).toBe(2);
      expect(report.summary.pass).toBe(2);
      expect(report.summary.fail).toBe(0);

      // Security: the resolved secret must not be serialized into the report. The
      // SUT echoed it back in a body we deliberately do NOT capture, so the secret
      // value should appear nowhere in the report JSON (returned or on disk).
      expect(JSON.stringify(report)).not.toContain("s3cr3t-from-env");
      const onDisk = await readFile(join(outDir, "report.json"), "utf8");
      expect(onDisk).not.toContain("s3cr3t-from-env");

      // Honest scope: the per-case network.har is a secret-bearing evidence file.
      // recordHar keeps request headers (only response BODIES are omitted), so the
      // injected Authorization secret is present in the HAR on the wire — exactly as
      // an injected storageState holds live cookies. We assert that reality so the
      // "secrets stay out of the report" guarantee is not silently overclaimed.
      const har = await readFile(join(outDir, "cases", "env-secret-reaches-sut", "network.har"), "utf8");
      expect(har).toContain("s3cr3t-from-env");
    },
    60_000,
  );

  it(
    "scrubs a ${env.X} secret spliced into a request URL out of report.json (responses[].url)",
    async () => {
      const plan: Plan = {
        name: "config-url-secret",
        defaultDriver: "cdp",
        cases: [
          {
            id: "url-secret-redacted",
            title: "a secret in the URL query is redacted from the serialized report",
            // The resolved token lands in responses[].url — the deterministic leak.
            steps: [{ action: "request", url: "/api/health?token=${env.HEIMDALL_E2E_URLTOKEN}", as: "h" }],
            oracle: [{ assert: "status", equals: 200, of: "h" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const opts: RunOptions = {
        outDir,
        baseUrl: fixture.baseUrl,
        allowRisk: false,
        headed: false,
        concurrency: 1,
        driverOverride: "cdp",
      };

      const report = await runPlan(plan, opts);

      const r = report.results.find((x) => x.id === "url-secret-redacted");
      expect(r?.status).toBe("pass");

      // The captured response URL carried the secret; it must be redacted, not raw.
      const urls = r?.evidence.responses.map((x) => x.url) ?? [];
      expect(urls.some((u) => u.includes("token="))).toBe(true);
      expect(urls.some((u) => u.includes(URL_SECRET))).toBe(false);
      expect(urls.some((u) => u.includes("[redacted]"))).toBe(true);

      // The whole report (returned + on-disk) is free of the raw secret.
      expect(JSON.stringify(report)).not.toContain(URL_SECRET);
      const onDisk = await readFile(join(outDir, "report.json"), "utf8");
      expect(onDisk).not.toContain(URL_SECRET);
    },
    60_000,
  );

  it(
    "scrubs a ${env.X} secret from STDERR when a plan-setup hook fails quoting the URL",
    async () => {
      // A plan-setup step whose templated URL embeds the secret and then ERRORS
      // (connection refused at an unroutable port) — Playwright's error message
      // quotes the full URL, so the secret would reach stderr verbatim via log.err
      // unless the runner redacts hook-error strings. This pins that terminal-scrub
      // promise on the failure path, complementing the report.json redaction above.
      const plan: Plan = {
        name: "config-setup-stderr-secret",
        defaultDriver: "cdp",
        setup: [{ action: "goto", url: "http://127.0.0.1:1/${env.HEIMDALL_E2E_URLTOKEN}" }],
        cases: [
          {
            id: "never-runs",
            title: "blocked because plan setup failed",
            steps: [{ action: "request", url: "/api/health", as: "h" }],
            oracle: [{ assert: "status", equals: 200, of: "h" }],
            risk: "read-only",
            priority: "p0",
            tags: [],
          },
        ],
      };

      const errSpy = vi.spyOn(console, "error").mockImplementation(() => {});
      let report;
      try {
        report = await runPlan(plan, {
          outDir,
          baseUrl: fixture.baseUrl,
          allowRisk: false,
          headed: false,
          concurrency: 1,
          driverOverride: "cdp",
        });
      } finally {
        errSpy.mockRestore();
      }

      // The setup failure blocked the case (honesty invariant: no false green).
      const r = report.results.find((x) => x.id === "never-runs");
      expect(r?.status).toBe("blocked");

      // The secret must appear in NONE of the captured stderr lines...
      const stderr = errSpy.mock.calls.map((c) => c.join(" ")).join("\n");
      expect(stderr).not.toContain(URL_SECRET);
      // ...nor in the blocked reason stored in the report.
      expect(JSON.stringify(report)).not.toContain(URL_SECRET);
      // Sanity: the run genuinely failed setup (so the assertion above is not vacuous).
      expect(r?.observed ?? "").toMatch(/plan setup failed/);
    },
    60_000,
  );
});

/**
 * REAL end-to-end test for two related guarantees:
 *
 *  1. PER-ORACLE PASS DETAILS ARE VALUE-FREE. A passing oracle records WHICH
 *     assertion fired and what it targeted, but NOT the raw observed value — so a
 *     secret/PII returned by the SUT in a response body never lands in report.json
 *     by default (the body is not serialized either). This shrinks the default
 *     secret-exposure surface that the `redaction` feature exists to protect.
 *  2. `heimdall.config.json` `redaction` THREADING. For a secret that DOES reach a
 *     serialized channel (a token spliced into a request URL → `responses[].url` in
 *     the report and the request URL in the raw HAR), a `config.redaction.patterns`
 *     entry scrubs it from BOTH report.json and the on-disk network.har — which only
 *     holds if `runCommand` threads `config.redaction` through to runPlan + scrubHar.
 *
 * Driven through the REAL `run` command against the `/echo-secret` fixture, which
 * reflects a fixed token + PII in its body.
 */
import { mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterAll, afterEach, beforeAll, describe, expect, it } from "vitest";

import { runCommand, type RunCmdOpts } from "../../src/commands/run.js";
import { startFixtureServer, type FixtureServer } from "../fixtures/server.js";

// Secrets the /echo-secret fixture returns in its BODY (never the URL):
const BODY_TOKEN = "sk-live-deadbeefcafebabe0123456789";
const BODY_EMAIL = "user@example.com";
const BODY_SSN = "123-45-6789";
// A DISTINCT secret we splice into the request URL — it reaches responses[].url + HAR:
const URL_SECRET = "sk-live-urlcafe99887766aabbccdd";

let fixture: FixtureServer;
let workDir: string;
let savedExitCode: typeof process.exitCode;

beforeAll(async () => {
  fixture = await startFixtureServer();
  workDir = await mkdtemp(join(tmpdir(), "heimdall-cfg-redact-"));
  savedExitCode = process.exitCode;
});

afterEach(() => {
  // runCommand sets process.exitCode; don't let it leak into the vitest process.
  process.exitCode = savedExitCode;
});

afterAll(async () => {
  await fixture?.stop();
  if (workDir) await rm(workDir, { recursive: true, force: true }).catch(() => {});
});

const PLAN = {
  name: "cfg-redaction",
  defaultDriver: "cdp",
  cases: [
    {
      id: "echo-secret",
      title: "a passing case whose response carries secrets in body + URL",
      // The URL_SECRET in the query string lands in responses[].url and the HAR.
      steps: [{ action: "request", url: `/echo-secret?probe=${URL_SECRET}`, as: "secret" }],
      // A PASSING jsonPath on the body token: its record must NOT echo the token.
      oracle: [
        { assert: "status", equals: 200, of: "secret" },
        { assert: "jsonPath", path: "token", of: "secret" },
        { assert: "jsonType", path: "email", type: "string", of: "secret" },
      ],
      risk: "read-only",
      priority: "p0",
      tags: [],
    },
  ],
};

async function runWithConfig(
  name: string,
  redaction?: { patterns?: string[]; headers?: string[] },
): Promise<{ report: string; har: string }> {
  const outDir = join(workDir, name);
  const planPath = join(workDir, `${name}.plan.json`);
  const configPath = join(workDir, `${name}.config.json`);
  await writeFile(planPath, JSON.stringify(PLAN), "utf8");
  await writeFile(
    configPath,
    JSON.stringify({ baseUrl: fixture.baseUrl, ...(redaction ? { redaction } : {}) }),
    "utf8",
  );
  const opts: RunCmdOpts = { out: outDir, concurrency: "1", driver: "cdp", config: configPath };
  await runCommand(planPath, opts);
  const report = await readFile(join(outDir, "report.json"), "utf8");
  const har = await readFile(join(outDir, "cases", "echo-secret", "network.har"), "utf8").catch(() => "");
  return { report, har };
}

describe("report redaction (run command, cdp)", () => {
  it(
    "keeps passing-oracle records value-free: SUT body secrets never reach report.json by default",
    async () => {
      const { report } = await runWithConfig("plain");
      // The case passed (so the oracleResults are present)...
      expect(report).toContain("oracleResults");
      expect(report).toContain('"passed": true');
      // ...yet NONE of the body-returned secrets/PII appear, with NO redaction configured.
      expect(report).not.toContain(BODY_TOKEN);
      expect(report).not.toContain(BODY_EMAIL);
      expect(report).not.toContain(BODY_SSN);
    },
    120_000,
  );

  it(
    "config.redaction scrubs a URL-borne secret from BOTH report.json and the raw HAR",
    async () => {
      // Control: a secret in the request URL DOES reach the report (responses[].url) + HAR.
      const plain = await runWithConfig("url-plain");
      expect(plain.report).toContain(URL_SECRET);
      expect(plain.har).toContain(URL_SECRET);

      // Fix under test: a config-level pattern scrubs the SAME secret from report AND HAR.
      const scrubbed = await runWithConfig("url-scrubbed", { patterns: ["sk-live-[A-Za-z0-9]+"] });
      expect(scrubbed.report).not.toContain(URL_SECRET);
      expect(scrubbed.report).toContain("[redacted]");
      expect(scrubbed.har).not.toContain(URL_SECRET);
    },
    120_000,
  );
});

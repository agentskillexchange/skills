/**
 * MCP server end-to-end test: spawn `heimdall mcp` (via tsx) and drive it with
 * the official MCP client — list tools, call schema/doctor, and run a real plan
 * against a fixture server through the cdp lane.
 */
import { afterAll, beforeAll, describe, expect, it } from "vitest";
import { mkdir, mkdtemp, rm } from "node:fs/promises";
import { join } from "node:path";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { startFixtureServer, type FixtureServer } from "../fixtures/server.js";

function parsed(res: { content: Array<{ type: string; text?: string }> }): any {
  const block = res.content.find((c) => c.type === "text");
  return JSON.parse(block?.text ?? "{}");
}

describe("mcp server end-to-end", () => {
  let client: Client;
  let transport: StdioClientTransport;
  let fixture: FixtureServer;
  let outDir: string;

  beforeAll(async () => {
    fixture = await startFixtureServer();
    const base = join(process.cwd(), "heimdall-runs");
    await mkdir(base, { recursive: true });
    outDir = await mkdtemp(join(base, "mcp-e2e-"));

    transport = new StdioClientTransport({
      command: "npx",
      args: ["tsx", "src/cli.ts", "mcp"],
      cwd: process.cwd(),
    });
    client = new Client({ name: "heimdall-test", version: "0.0.0" });
    await client.connect(transport);
  }, 60_000);

  afterAll(async () => {
    await client?.close().catch(() => {});
    await fixture?.stop().catch(() => {});
    await rm(outDir, { recursive: true, force: true }).catch(() => {});
  });

  it("exposes run/doctor/schema tools", async () => {
    const { tools } = await client.listTools();
    const names = tools.map((t) => t.name).sort();
    expect(names).toEqual(["doctor", "run", "schema"]);
  });

  it("returns the plan JSON schema", async () => {
    const res = await client.callTool({ name: "schema", arguments: {} });
    const schema = parsed(res as any);
    expect(JSON.stringify(schema)).toContain("HeimdallPlan");
  });

  it("reports toolchain status via doctor", async () => {
    const res = await client.callTool({ name: "doctor", arguments: {} });
    const out = parsed(res as any);
    expect(Array.isArray(out.checks)).toBe(true);
    expect(typeof out.cdpReady).toBe("boolean");
  });

  it(
    "runs a plan against the fixture and reports a pass",
    async () => {
      const res = await client.callTool({
        name: "run",
        arguments: {
          plan: {
            name: "mcp-run",
            cases: [
              {
                id: "mcp-home",
                steps: [{ action: "goto", url: "/" }],
                oracle: [
                  { assert: "visible", selector: "#app" },
                  { assert: "textContains", selector: "#app", value: "Heimdall OK" },
                ],
              },
            ],
          },
          baseUrl: fixture.baseUrl,
          outDir,
        },
      });
      const report = parsed(res as any);
      expect(report.summary.pass).toBe(1);
      expect(report.summary.fail + report.summary.error).toBe(0);
      expect(report.results[0].driver).toBe("cdp");
    },
    60_000,
  );

  it("rejects an invalid plan with isError", async () => {
    const res: any = await client.callTool({ name: "run", arguments: { plan: { cases: [] } } });
    expect(res.isError).toBe(true);
  });
});

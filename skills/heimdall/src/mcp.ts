/**
 * Heimdall MCP server — exposes Heimdall to Claude Code (and any MCP client) as
 * native tools, so an agent calls `heimdall_run` instead of shelling out.
 *
 * Run it with `heimdall mcp` (stdio transport). Register in Claude Code with:
 *   claude mcp add heimdall -- heimdall mcp
 *
 * Tools:
 *   run     — validate + execute a plan, return the RunReport (summary + results)
 *   doctor  — toolchain status (Node, Playwright Chromium, Docker, image)
 *   schema  — the JSON Schema for a plan
 */
import { resolve } from "node:path";
import { z } from "zod";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { parsePlan, planJsonSchema } from "./schema.js";
import { runPlan } from "./runner.js";
import { collectDoctorChecks, cdpReady } from "./commands/doctor.js";
import { VERSION } from "./version.js";

const CAPTURE = z.enum(["off", "on", "on-failure"]);

function text(obj: unknown) {
  return { content: [{ type: "text" as const, text: JSON.stringify(obj, null, 2) }] };
}

export async function mcpCommand(): Promise<void> {
  const server = new McpServer({ name: "heimdall", version: VERSION });

  server.registerTool(
    "run",
    {
      description:
        "Run a Heimdall browser test plan (drivers cdp/container) and return the report. " +
        "extension-driver cases are reported blocked (they need an agent's own browser tools).",
      inputSchema: {
        plan: z.record(z.string(), z.unknown()).describe("A Heimdall plan object; see the `schema` tool for its shape"),
        baseUrl: z.string().optional().describe("base URL for relative step/fetch URLs (overrides plan)"),
        driver: z.enum(["cdp", "container"]).optional().describe("force a driver for every case"),
        outDir: z.string().optional().describe("evidence/report dir (default heimdall-runs/mcp)"),
        concurrency: z.number().int().positive().optional(),
        retries: z.number().int().nonnegative().optional(),
        timeoutMs: z.number().int().positive().optional(),
        allowRisk: z.boolean().optional().describe("permit destructive/paid/prod cases"),
        storageState: z.string().optional().describe("path to a Playwright storageState for injected auth"),
        trace: CAPTURE.optional(),
        video: CAPTURE.optional(),
        filter: z.array(z.string()).optional(),
      },
    },
    async (args) => {
      let plan;
      try {
        plan = parsePlan(args.plan);
      } catch (e) {
        return {
          isError: true,
          content: [{ type: "text" as const, text: `invalid plan: ${e instanceof Error ? e.message : String(e)}` }],
        };
      }
      const report = await runPlan(plan, {
        outDir: resolve(args.outDir ?? "heimdall-runs/mcp"),
        baseUrl: args.baseUrl,
        driverOverride: args.driver,
        concurrency: args.concurrency ?? 4,
        retries: args.retries ?? 0,
        timeoutMs: args.timeoutMs,
        allowRisk: Boolean(args.allowRisk),
        headed: false,
        storageState: args.storageState ? resolve(args.storageState) : undefined,
        trace: args.trace ?? "off",
        video: args.video ?? "off",
        filter: args.filter,
      });
      return text(report);
    },
  );

  server.registerTool(
    "doctor",
    { description: "Check the Heimdall toolchain (Node, Playwright Chromium, Docker, container image).", inputSchema: {} },
    async () => {
      const checks = await collectDoctorChecks();
      return text({ checks, cdpReady: cdpReady(checks) });
    },
  );

  server.registerTool(
    "schema",
    { description: "Return the JSON Schema for a Heimdall plan.", inputSchema: {} },
    async () => text(planJsonSchema()),
  );

  const transport = new StdioServerTransport();
  await server.connect(transport);
  // Stay alive on stdio until the client disconnects.
}

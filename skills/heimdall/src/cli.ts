#!/usr/bin/env node
import { Command, Option } from "commander";
import { VERSION } from "./version.js";
import { runCommand } from "./commands/run.js";
import { validateCommand } from "./commands/validate.js";
import { doctorCommand } from "./commands/doctor.js";
import { gcCommand } from "./commands/gc.js";
import { initCommand } from "./commands/init.js";
import { authSaveCommand } from "./commands/auth.js";
import { schemaCommand } from "./commands/schema.js";
import { buildImageCommand } from "./commands/buildImage.js";
import { extensionsCommand, loadExternalResults } from "./commands/extensions.js";
import { mcpCommand } from "./mcp.js";
import { log } from "./log.js";

const program = new Command();

program
  .name("heimdall")
  .description("Multi-driver browser test runner for agentic development")
  .version(VERSION, "-V, --version");

const collect = (val: string, prev: string[]) => [...prev, val];

program
  .command("run")
  .description("Run a test plan through its drivers (cdp/container) and report")
  .argument("<plan>", "path to a plan JSON file")
  .addOption(
    new Option("-d, --driver <driver>", "force a driver for every case").choices(["cdp", "container"]),
  )
  .option("-o, --out <dir>", "output dir for evidence + report", "heimdall-runs/latest")
  .option("-b, --base-url <url>", "base URL for relative step/fetch URLs (overrides plan)")
  .option("-s, --storage-state <file>", "Playwright storageState for injected auth")
  .option("-c, --concurrency <n>", "max parallel cases per driver", "4")
  .option("-r, --retries <n>", "retry a failed/errored case up to n times", "0")
  .option("--timeout <ms>", "overall per-case wall-clock budget in ms (per-case timeoutMs wins)")
  .option("--allow-risk", "permit cases marked destructive/paid/prod to run", false)
  .option("--headed", "run with a visible browser window (cdp only)", false)
  .option("--insecure", "disable TLS validation (ignored when --storage-state is set)", false)
  .addOption(
    new Option("--trace [mode]", "record a Playwright trace.zip per case")
      .choices(["off", "on", "on-failure"])
      .default("off")
      .preset("on-failure"),
  )
  .addOption(
    new Option("--video [mode]", "record a Playwright video per case")
      .choices(["off", "on", "on-failure"])
      .default("off")
      .preset("on-failure"),
  )
  .option("--html [file]", "also write a self-contained HTML report (default <out>/report.html)")
  .option("--junit <file>", "also write a JUnit XML report for CI")
  .addOption(
    new Option("--group-by <key>", "group report rows by case tag or dimension").choices(["tag", "dimension"]),
  )
  .option("--diff <prevReport.json>", "compare against a previous report.json and print a regression diff")
  .option("-C, --config <file>", "load run defaults + env seed from a heimdall.config.json")
  .option("-f, --filter <idOrTag>", "only run cases matching id substring or tag (repeatable)", collect, [])
  .option("--json", "print the full JSON report to stdout", false)
  .option("--lenient", "skip invalid cases (with a warning) instead of aborting the whole run", false)
  .option(
    "--merge-results <file>",
    "fold externally-produced Result[] (e.g. extension cases run via the agent's browser) into the report; a matching blocked id is replaced verbatim",
  )
  .option("-v, --verbose", "verbose debug logging", false)
  .action(async (planPath, opts, command) => {
    // Load --merge-results here (CLI layer) so runCommand receives a validated
    // Result[] to hand the runner; the runner replaces matching (blocked) ids
    // with these verbatim — never fabricating a passing verdict.
    const externalResults = opts.mergeResults ? await loadExternalResults(opts.mergeResults) : undefined;
    await runCommand(planPath, { ...opts, externalResults }, command);
  });

program
  .command("extensions")
  .description("Emit a manifest of the plan's driver:extension cases for the agent to drive in real Chrome")
  .argument("<plan>", "path to a plan JSON file")
  .option("-o, --out <file>", "write the manifest to a file instead of stdout")
  .action((planPath, opts) => extensionsCommand(planPath, { out: opts.out }));

program
  .command("validate")
  .description("Validate a plan and report ALL problems (a dry run — executes nothing)")
  .argument("<plan>", "path to a plan JSON file")
  .action(validateCommand);

program
  .command("doctor")
  .description("Check the toolchain: Node, Playwright Chromium, Docker, image")
  .action(doctorCommand);

program
  .command("gc")
  .description("Prune orphaned Playwright browser revisions from the cache")
  .option("-y, --yes", "actually delete (default is a dry run)", false)
  .action((opts) => gcCommand(opts));

program
  .command("init")
  .description("Write a sample plan you can edit")
  .option("-o, --out <file>", "where to write the sample plan", "heimdall.plan.json")
  .action((opts) => initCommand(opts.out));

program
  .command("schema")
  .description("Emit the JSON Schema for a plan (for editors / other tools)")
  .option("-o, --out <file>", "write to a file instead of stdout")
  .action((opts) => schemaCommand(opts.out));

program
  .command("build-image")
  .description("Build the Docker image used by the container driver")
  .option("-t, --tag <tag>", "image tag")
  .action((opts) => buildImageCommand(opts.tag));

program
  .command("mcp")
  .description("Run Heimdall as an MCP server over stdio (for Claude Code & other agents)")
  .action(mcpCommand);

const auth = program.command("auth").description("Manage injected auth sessions");
auth
  .command("save")
  .description("Open a browser, log in manually, and save the session to a file")
  .requiredOption("-u, --url <url>", "login URL to open")
  .option("-o, --out <file>", "where to save the storageState", "auth/session.storageState.json")
  .action((opts) => authSaveCommand({ url: opts.url, out: opts.out }));

program.parseAsync(process.argv).catch((e) => {
  log.err(e instanceof Error ? e.message : String(e));
  process.exit(1);
});

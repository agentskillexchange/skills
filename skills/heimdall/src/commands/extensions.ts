import { readFile, writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { z } from "zod";
import { Result, parsePlan, type Oracle, type Plan, type Step, type TestCase } from "../schema.js";
import { collectPlanErrors } from "./validate.js";
import { log, c } from "../log.js";

export interface ExtensionManifestCase {
  id: string;
  title?: string;
  steps: Step[];
  oracle: Oracle[];
  tapHint: string;
}

export interface ExtensionManifest {
  plan: string;
  driver: "extension";
  cases: ExtensionManifestCase[];
}

function resolvedDriver(tc: TestCase, plan: Plan): string {
  return tc.driver ?? plan.defaultDriver;
}

function tapHintFor(tc: TestCase): string {
  const goto = tc.steps.find((s): s is Extract<Step, { action: "goto" }> => s.action === "goto");
  const start = goto?.url ?? tc.baseUrl;
  const what = tc.title ?? tc.id;
  const counts = `${tc.steps.length} step(s) + ${tc.oracle.length} oracle(s)`;
  return start
    ? `Drive "${what}" in real Chrome starting at ${start}, then verify ${counts}.`
    : `Drive "${what}" in real Chrome, then verify ${counts}.`;
}

export function buildExtensionManifest(plan: Plan): ExtensionManifest {
  const cases: ExtensionManifestCase[] = plan.cases
    .filter((tc) => resolvedDriver(tc, plan) === "extension")
    .map((tc) => ({
      id: tc.id,
      ...(tc.title !== undefined ? { title: tc.title } : {}),
      steps: tc.steps,
      oracle: tc.oracle,
      tapHint: tapHintFor(tc),
    }));
  return { plan: plan.name, driver: "extension", cases };
}

export async function loadExternalResults(file: string): Promise<Result[]> {
  const raw = await readFile(resolve(file), "utf8");
  const json = JSON.parse(raw) as unknown;
  const candidate =
    json !== null && typeof json === "object" && !Array.isArray(json) && Array.isArray((json as { results?: unknown }).results)
      ? (json as { results: unknown[] }).results
      : json;
  return z.array(Result).parse(candidate);
}

export async function extensionsCommand(planPath: string, opts: { out?: string }): Promise<void> {
  const raw = await readFile(resolve(planPath), "utf8");
  let json: unknown;
  try {
    json = JSON.parse(raw);
  } catch (e) {
    log.err(`could not parse plan JSON: ${e instanceof Error ? e.message : String(e)}`);
    process.exitCode = 2;
    return;
  }

  const errors = collectPlanErrors(json);
  if (errors.length > 0) {
    log.err(`invalid plan — ${errors.length} problem${errors.length === 1 ? "" : "s"}:`);
    for (const line of errors) log.info(c.red("  • ") + line);
    process.exitCode = 2;
    return;
  }

  const manifest = buildExtensionManifest(parsePlan(json));
  const text = JSON.stringify(manifest, null, 2);
  if (opts.out) {
    const path = resolve(opts.out);
    await writeFile(path, text + "\n", "utf8");
    log.ok(`wrote ${manifest.cases.length} extension case(s) to ${c.bold(path)}`);
  } else {
    process.stdout.write(text + "\n");
  }
}

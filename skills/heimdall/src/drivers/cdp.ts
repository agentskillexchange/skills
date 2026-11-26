/**
 * CDP driver — drives Chromium via Playwright (Chrome DevTools Protocol).
 *
 * Input is dispatched per-target, so many contexts run genuinely in parallel
 * with no shared OS focus — this is the focus fix that the extension regime
 * cannot offer. Each case gets its own isolated BrowserContext.
 */
import { readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { chromium, type Browser, type BrowserContext, type Video } from "playwright";
import type { Redaction, Result, TestCase } from "../schema.js";
import { fidelityForDriver } from "../schema.js";
import { ensureCaseDir, executeCase } from "../execute.js";
import { scrubHar } from "../redact.js";
import type { CaseDriver, RunContext } from "./types.js";
import { log } from "../log.js";

export class CdpDriver implements CaseDriver {
  readonly name = "cdp" as const;
  private browser: Browser | undefined;

  async setup(ctx: RunContext): Promise<void> {
    this.browser = await chromium.launch({ headless: !ctx.headed });
    log.debug(`cdp: launched chromium (headless=${!ctx.headed})`);
  }

  async runCase(tc: TestCase, ctx: RunContext): Promise<Result> {
    if (!this.browser) throw new Error("CdpDriver.setup() was not called");
    const started = Date.now();
    const fidelityTier = fidelityForDriver("cdp");
    const baseUrl = tc.baseUrl ?? ctx.baseUrl;
    let context: BrowserContext | undefined;
    let video: Video | undefined;
    let failed = true;
    let result!: Result;

    try {
      // Inside the try so a bad outDir / storageState fails this CASE, not the run.
      const caseDir = await ensureCaseDir(ctx.outDir, tc.id);
      const harPath = join(caseDir, "network.har");
      context = await this.browser.newContext({
        baseURL: baseUrl,
        storageState: ctx.storageState,
        recordHar: { path: harPath, content: "omit" },
        recordVideo: ctx.video !== "off" ? { dir: caseDir } : undefined,
        ignoreHTTPSErrors: ctx.insecureTLS ?? false,
      });
      if (ctx.trace !== "off") await context.tracing.start({ screenshots: true, snapshots: true });

      const page = await context.newPage();
      video = ctx.video !== "off" ? page.video() ?? undefined : undefined;
      const outcome = await executeCase(tc, page, { caseDir, baseUrl });
      failed = outcome.status !== "pass";

      // Stop tracing while the context is still open; keep the zip only if wanted.
      let tracePath: string | undefined;
      if (ctx.trace !== "off") {
        if (ctx.trace === "on" || failed) {
          tracePath = join(caseDir, "trace.zip");
          await context.tracing.stop({ path: tracePath });
        } else {
          await context.tracing.stop();
        }
      }

      result = {
        id: tc.id,
        status: outcome.status,
        driver: "cdp",
        fidelityTier,
        observed: outcome.observed,
        failures: outcome.failures,
        evidence: {
          screenshots: outcome.screenshots,
          har: harPath,
          trace: tracePath,
          consoleErrors: outcome.consoleErrors,
          responses: outcome.responses,
        },
        // Carry the per-oracle pass/fail breakdown so even a PASSING case is auditable
        // down to each oracle (the container path forwards this field verbatim).
        oracleResults: outcome.oracleResults,
        notes: outcome.notes,
        durationMs: Date.now() - started,
      };
    } catch (e) {
      result = {
        id: tc.id,
        status: "error",
        driver: "cdp",
        fidelityTier,
        observed: `driver error: ${e instanceof Error ? e.message : String(e)}`,
        failures: [e instanceof Error ? e.message : String(e)],
        evidence: { screenshots: [], consoleErrors: [], responses: [] },
        durationMs: Date.now() - started,
      };
    } finally {
      await context?.close().catch(() => {}); // flushes HAR + finalizes video; never throws
    }

    // The HAR is flushed only on context.close() above, and (unlike the report) is raw
    // Playwright evidence. When the runner supplies a redaction spec, scrub the file in
    // place: blank configured header values + regex matches in URLs/bodies. Best-effort —
    // a missing or unparsable HAR must never turn a passing case into an error.
    const redaction = (ctx as RunContext & { redaction?: Redaction }).redaction;
    if (redaction && (redaction.headers?.length || redaction.patterns?.length) && result.evidence.har) {
      try {
        const raw = await readFile(result.evidence.har, "utf8");
        await writeFile(result.evidence.har, JSON.stringify(scrubHar(JSON.parse(raw), redaction)));
      } catch {
        /* HAR absent/unparsable — evidence scrubbing is non-fatal */
      }
    }

    // Video path resolves only after the context closes; keep or discard by mode.
    if (video) {
      try {
        if (ctx.video === "on" || (ctx.video === "on-failure" && failed)) {
          result.evidence.video = await video.path();
        } else {
          await video.delete();
        }
      } catch {
        /* video unavailable */
      }
    }
    return result;
  }

  async teardown(): Promise<void> {
    await this.browser?.close();
  }
}

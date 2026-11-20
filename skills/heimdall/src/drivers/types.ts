import type { Redaction, Result, TestCase } from "../schema.js";

/** When to keep a trace/video artifact. */
export type CaptureMode = "off" | "on" | "on-failure";

/** Shared run options threaded from the CLI into every driver. */
export interface RunContext {
  /** Root output directory for evidence + report. */
  outDir: string;
  /** Base URL for resolving relative step/fetch URLs. */
  baseUrl?: string;
  /** Path to a Playwright storageState (injected auth session). */
  storageState?: string;
  /** Allow cases marked destructive/paid/prod to actually run. */
  allowRisk: boolean;
  /** Run with a visible browser window (cdp only). */
  headed: boolean;
  /** Disable TLS validation (opt-in; forced off when a session is injected). */
  insecureTLS: boolean;
  /** When to keep a Playwright trace.zip per case. */
  trace: CaptureMode;
  /** When to keep a Playwright video per case. */
  video: CaptureMode;
  /** Resolved redaction spec (header names + regex sources) scrubbed from the report and the HAR. */
  redaction?: Redaction;
}

/**
 * A driver knows how to execute cases for one regime. `setup`/`teardown` bracket
 * a run so expensive resources (a browser, a container image) are created once.
 */
export interface CaseDriver {
  readonly name: "cdp" | "container";
  setup(ctx: RunContext): Promise<void>;
  runCase(tc: TestCase, ctx: RunContext): Promise<Result>;
  teardown(): Promise<void>;
}

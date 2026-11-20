/**
 * Secret redaction for serialized output.
 *
 * `${env.*}` tokens (see {@link import("./execute.js").applyVars}) splice secret
 * values into request URLs / bodies / headers. Those resolved values can then
 * deterministically surface in machine-readable output Heimdall controls:
 *   - `report.json` — `results[].evidence.responses[].url`, plus `observed` /
 *     `failures[]` strings that may embed a Playwright error message carrying the
 *     full request URL;
 *   - the terminal/HTML/JUnit reports rendered from that same report;
 *
 * so a `${env.TOKEN}` placed in a URL would otherwise be persisted verbatim. This
 * module tracks the set of env-resolved secret values and scrubs them from any
 * string Heimdall serializes, BEFORE the report is written or printed.
 *
 * Scope (and its honest limits): redaction covers the report object Heimdall
 * builds. It does NOT rewrite the binary-ish Playwright EVIDENCE FILES — the HAR
 * (`network.har`, which retains request headers + URLs even with `content:"omit"`)
 * and the trace (`trace.zip`). Those, like an injected `storageState`, can contain
 * the secret on the wire; treat a run's output directory as secret-bearing.
 *
 * On top of the per-run `${env.*}` secrets, a plan/config may declare a
 * {@link Redaction} spec — extra response-header NAMES (whose values are blanked)
 * and regex SOURCES (whose matches are blanked). {@link redactWithSpec} folds that
 * spec into the same deep-walk used for the report, and {@link scrubHar} applies it
 * to the raw Playwright HAR evidence the report path otherwise leaves untouched.
 */
import type { Redaction } from "./schema.js";

/**
 * Process-wide registry of secret values resolved from `${env.*}` tokens. A Set is
 * fine: registration is idempotent and the values are only ever used as scrub
 * targets. `runPlan` calls {@link clearSecrets} at the start of every run, so the
 * registry is scoped to one run and never grows unbounded across runs.
 *
 * Redaction is plain substring replacement, so a short or common env value (the
 * {@link MIN_SECRET_LEN} floor only rejects trivially short ones) CAN over-scrub an
 * unrelated occurrence within the same run's report. That is a deliberate fail-safe:
 * over-redaction is acceptable; leaking a declared secret is not.
 */
const secrets = new Set<string>();

/** Minimum length for a value to be treated as a redactable secret (rejects trivial values). */
const MIN_SECRET_LEN = 4;

/** Record an env-resolved value so it can be scrubbed from serialized output. */
export function registerSecret(value: string): void {
  if (value.length >= MIN_SECRET_LEN) secrets.add(value);
}

/** Replace every registered secret in a string with `[redacted]`. */
export function redactString(input: string): string {
  if (secrets.size === 0) return input;
  let out = input;
  for (const s of secrets) {
    if (out.includes(s)) out = out.split(s).join("[redacted]");
  }
  return out;
}

/** Deep-redact every string in a JSON-serializable value, returning a new value. */
export function redactDeep<T>(value: T): T {
  if (secrets.size === 0) return value;
  if (typeof value === "string") return redactString(value) as unknown as T;
  if (Array.isArray(value)) return value.map((v) => redactDeep(v)) as unknown as T;
  if (value && typeof value === "object") {
    const out: Record<string, unknown> = {};
    for (const [k, v] of Object.entries(value as Record<string, unknown>)) out[k] = redactDeep(v);
    return out as T;
  }
  return value;
}

/** Test/scope helper: forget all registered secrets (used to isolate test runs). */
export function clearSecrets(): void {
  secrets.clear();
}

/** Compile a spec's regex sources to global RegExps; an invalid source is skipped, never thrown. */
function compilePatterns(patterns?: string[]): RegExp[] {
  if (!patterns || patterns.length === 0) return [];
  const out: RegExp[] = [];
  for (const p of patterns) {
    try {
      out.push(new RegExp(p, "g"));
    } catch {
      // A malformed pattern is ignored rather than aborting redaction (fail-safe, never fail-open loudly).
    }
  }
  return out;
}

/** Apply the registered env secrets and the spec's regex patterns to one string. */
function scrubStringWithSpec(input: string, regexes: RegExp[]): string {
  let out = redactString(input);
  for (const re of regexes) {
    re.lastIndex = 0;
    out = out.replace(re, "[redacted]");
  }
  return out;
}

/**
 * Deep-redact like {@link redactDeep}, additionally honouring a {@link Redaction} spec:
 * an object entry whose KEY matches one of `spec.headers` (case-insensitive) has its
 * string value blanked, and every string is scrubbed of `spec.patterns` matches on top
 * of the env secrets. With no spec (or an empty one) this delegates straight to
 * {@link redactDeep}, so legacy output is byte-identical.
 */
export function redactWithSpec<T>(value: T, spec?: Redaction): T {
  const headers = spec?.headers ?? [];
  const patterns = spec?.patterns ?? [];
  if (headers.length === 0 && patterns.length === 0) return redactDeep(value);

  const headerSet = new Set(headers.map((h) => h.toLowerCase()));
  const regexes = compilePatterns(patterns);
  const walk = (v: unknown): unknown => {
    if (typeof v === "string") return scrubStringWithSpec(v, regexes);
    if (Array.isArray(v)) return v.map(walk);
    if (v && typeof v === "object") {
      const out: Record<string, unknown> = {};
      for (const [k, val] of Object.entries(v as Record<string, unknown>)) {
        out[k] = headerSet.has(k.toLowerCase()) && typeof val === "string" ? "[redacted]" : walk(val);
      }
      return out;
    }
    return v;
  };
  return walk(value) as T;
}

/**
 * Pure scrubber for a parsed Playwright HAR object. Blanks the values of headers named
 * in `spec.headers` (case-insensitive) on every request/response, and scrubs env secrets
 * + `spec.patterns` matches from request URLs and request/response bodies. Operates on a
 * structural clone so the input is never mutated, always returns a JSON-serializable value,
 * and never throws on missing/odd fields.
 */
export function scrubHar(harJson: unknown, spec?: Redaction): unknown {
  let root: unknown;
  try {
    root = structuredClone(harJson);
  } catch {
    root = harJson;
  }

  const headerSet = new Set((spec?.headers ?? []).map((h) => h.toLowerCase()));
  const regexes = compilePatterns(spec?.patterns);
  const scrub = (s: unknown): unknown => (typeof s === "string" ? scrubStringWithSpec(s, regexes) : s);

  const scrubHeaders = (headers: unknown): void => {
    if (!Array.isArray(headers)) return;
    for (const h of headers) {
      if (!h || typeof h !== "object") continue;
      const rec = h as Record<string, unknown>;
      const name = typeof rec.name === "string" ? rec.name.toLowerCase() : "";
      if (headerSet.has(name)) rec.value = "[redacted]";
      else rec.value = scrub(rec.value);
    }
  };

  const entries = (root as { log?: { entries?: unknown } } | null | undefined)?.log?.entries;
  if (Array.isArray(entries)) {
    for (const entry of entries) {
      if (!entry || typeof entry !== "object") continue;
      const e = entry as { request?: Record<string, unknown>; response?: Record<string, unknown> };
      const req = e.request;
      if (req && typeof req === "object") {
        req.url = scrub(req.url);
        scrubHeaders(req.headers);
        scrubHeaders(req.queryString);
        const postData = req.postData as Record<string, unknown> | undefined;
        if (postData && typeof postData === "object") postData.text = scrub(postData.text);
      }
      const res = e.response;
      if (res && typeof res === "object") {
        res.redirectURL = scrub(res.redirectURL);
        scrubHeaders(res.headers);
        const content = res.content as Record<string, unknown> | undefined;
        if (content && typeof content === "object") content.text = scrub(content.text);
      }
    }
  }
  return root;
}

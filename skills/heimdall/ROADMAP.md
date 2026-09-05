# Heimdall roadmap

Priorities distilled from dogfooding Heimdall against a real app (the synthetes
forge) via an exhaustive, expert-designed live-test. Each item names the concrete
evidence that motivated it. Ordered by impact.

## Done (validated by real use)
- **Per-oracle fault isolation** — a throwing oracle (e.g. bad `evalTruthy`) used to
  crash the whole case as `error`, masking its other oracles (23 cases errored in one
  run). Now each oracle is fault-isolated → fails only itself.
- **`fetch` from `about:blank`** — a fetch-only case (no prior `goto`) ran with a null
  origin, so API fetches were cross-origin/CORS-blocked. Now we land on the target
  origin first.
- Multi-driver (extension/cdp/container), per-case evidence (screenshot/HAR/trace/video),
  honest `blocked`/non-zero-on-non-run semantics, MCP server — all validated; unchanged.

## P0 — biggest gaps

### 1. Response-aware oracles + API request mode — ✅ DONE (#4, commit 13392a9)
Was the #1 gap: `evalTruthy` runs in the page and couldn't see captured responses;
no header capture (~65 oracles deferred in the synthetes run). Delivered + verified
live against synthetes:
- `request` step (Playwright `APIRequestContext`) — status + **headers** + body, no
  page/`goto`, not subject to page CORS;
- response **header capture** (lower-cased) on `fetch` + `waitForResponse`;
- new oracles: `header`, `jsonType`, `nonEmpty`, `bodyContains`, `jsonMatch`.

### 2. Stateful / async flows: variable capture + redirect + pollUntil — ✅ DONE (#5, commit 0223eff)
The forge lifecycle (POST → grab `run_id` from a redirect header → poll until done →
assert) could not be expressed; now it can. Delivered + verified (real-Chromium flow.e2e):
- **`capture`** (jsonPath/header → per-case `${var}`) + `${var}` templating in later
  step url/body/headers + `waitForResponse.urlContains`;
- request **`redirect: 'manual'`** — returns the 3xx with readable `location`/`hx-redirect`;
- **`pollUntil`** — re-issue a request until its response-oracles pass or timeout.

## P1 — expressiveness & authoring

### 3. Oracle expressiveness — ✅ DONE (#6)
Experts repeatedly wanted: `statusIn`/ranges/`not` (e.g. `status ∈ {404,405}`,
`≠ 500`); `attribute` `exists`/`matches` (couldn't assert `required`/`aria-*` presence —
case A004); `titleMatches`.

### 4. Plan validation UX — ✅ DONE (#7)
Agents author plans, so validation must be kind: one bad key aborted the whole plan with
exit 2 and only the **first** zod error. Deliver: validate **all** cases and report
every error with case id + path; a `--validate`/dry-run; a `--lenient` mode that skips
invalid cases with warnings instead of failing the run.

### 5. Load / concurrency primitive — ✅ DONE (#8)
The perf lens had to hand-roll `Promise.all` inside `evalTruthy`. Now a first-class
`load` step fires the same request `times` times via the browser-context
`APIRequestContext`, bounded by `concurrency` (default `min(times, 10)`), and stores an
aggregate `LoadStats` (count/errors/`errorRate` + `minMs`/`p50`/`p95`/`p99`/`maxMs`). The
pure engine lives in `src/load.ts` (`runConcurrent` + `summarizeLoad`, unit-tested in
`test/load.test.ts`). New oracles `errorRate {max}` and `percentile {p: 50|95|99|max,
maxMs}` read the aggregate (vs `responseTime`, which is per-call only). Delivered +
verified (real-Chromium load.e2e against a slow/flaky fixture route).

## P2 — coverage & polish

### 6. SSE / streaming — ✅ DONE (#6)
synthetes streams `/run/{id}/events`; Heimdall couldn't assert on event streams. Now an
`sse` step opens an in-page `EventSource` (same about:blank origin guard as `fetch`),
collects message events `{event,data,id}` until `events` are reached or
`timeoutMs`/`closeAfterMs` elapse, and stores an aggregate (events array under `json`,
newline-joined `data` under `bodyText`). New `eventCount` `{min?,equals?}` oracle plus the
existing `bodyContains`/`jsonPath` read the aggregate. Delivered + verified (real-Chromium
sse.e2e against a `/events` fixture).

### 7. Setup/teardown & fixtures — ✅ DONE (#7)
Idempotent create-then-delete; plan/per-case setup hooks (the live-test guardrail wants
tests to clean up after themselves). Now `TestCase` and `Plan` each take optional
`setup`/`teardown` step arrays. Per-case hooks run on the case's own page sharing its
captured `${vars}`: a failing `setup` step fails the case and skips its steps/oracles; a
`teardown` always runs (even on failure) as best-effort cleanup, surfaced in `notes` and
never flipping the verdict. Plan-level hooks run once in a throwaway context — a failing
`plan.setup` blocks every runnable case (honesty preserved), `plan.teardown` is best-effort
and logged. All hooks reuse the existing `runStep` interpreter. Delivered + verified
(real-Chromium fixtures.e2e: create-then-delete lifecycle, best-effort teardown-on-pass,
plan-setup-failure-blocks).

### 8. Reporting — ✅ DONE (#8)
Group results by `tag`/dimension; surface `blocked`/deferred reasons prominently; a
regression diff vs the previous run. Delivered: `--group-by tag|dimension` threads a
`ReportFormatOptions` (with a per-case tags/dimension `meta` map) into `formatReport`,
`buildHtml`, and the JUnit `classname`; an always-on "Blocked (N)" panel surfaces every
deferred case with its reason. `src/reporters/diff.ts` (`diffReports`/`formatDiff`/
`isCleanDiff`/`writeDiffReport`) classifies cases into newly-failing/newly-passing/
still-failing/added/removed by id; `--diff <prevReport.json>` prints the regression diff
after a run. The legacy 2-arg report output stays byte-identical (options are opt-in).

### 9. Config / secrets — ✅ DONE (#9)
`heimdall.config.json` loaded via `--config` (or the cwd default); supplies run-level
defaults (`baseUrl`/`defaultDriver`/`concurrency`/`retries`/`storageState`) folded under
CLI > plan > config precedence, and an `env` map that seeds `process.env` (never
clobbering already-set keys — real env wins). Plans reference secrets via `${env.NAME}`
templating (resolved from `process.env` in `applyVars`), so tokens live in the
environment, never inline in the plan JSON. `src/config.ts` (`loadConfig` +
`HeimdallConfig` Zod schema) is unit-tested in `test/config.test.ts`; the env-templating
path is covered by `test/integration/config.e2e.test.ts`.

## P3 — cross-derived from the live-test skill

Distilled from reading the **`live-test`** skill (the primary embedder) against Heimdall's
current surface: each item names the live-test expert lens or guardrail it would
unblock, and would let MORE cases move off the un-self-drivable `extension` lane
onto the parallel `cdp`/`container` lanes. Ordered by leverage.

### 10. Per-oracle results in the `Result` — ✅ DONE
A passing case used to report only `observed: "all N oracle(s) satisfied"`; the
live-test verifier had to guess whether an oracle *actually* fired or passed
vacuously. Delivered: an optional `oracleResults[]` on each `Result` — per assert,
its `kind`, `passed`, and a human-readable `detail` of what it checked — so the
Phase-4 skeptic detects a hollow green from the report alone, no re-run. Older
reports omit the field (optional). Highest leverage: every consumer's pass is now
auditable.

### 11. Accessibility oracle — ✅ DONE
The a11y lens could only hack at WCAG via `evalTruthy`. Delivered: an `a11y` oracle
that injects axe-core into the page and fails on any violation at/above a severity
(`{ maxImpact: "serious", include?: [...], exclude?: [...] }`, default `serious`),
with the violation list captured as evidence. Self-drivable on `cdp`/`container`.

### 12. Fault-injection step — ✅ DONE
The chaos lens could not express "does the UI recover when `/api/x` 500s / is slow?"
as a plan. Delivered: a `route` step (Playwright route interception) keyed on
`urlContains` with `mode` ∈ `block`/`abort`/`fulfill`/`delay` — fail matching
requests, return a synthetic `status`/`body`/`headers`, or add `delayMs` latency for
the rest of the case — so failure-recovery is a case, not hand-driving.

### 13. Visual baseline-diff oracle — ✅ DONE
Delivered: a `screenshotMatches` oracle that pixel-compares the case's screenshot
(full page or a `selector` clip) to a committed `baseline` PNG via pixelmatch and
passes when the differing-pixel fraction ≤ `maxDiffRatio` (default `0.01`), writing
the diff image as evidence. Lets the `cdp`/`container` lanes catch visual
regressions without the human committee for the deterministic cases.

### 14. Extension-case manifest + external-results merge — ✅ DONE
Heimdall `block`s `extension` cases; the orchestrator re-derived them and the final
report was split across two artifacts. Delivered: (a) `heimdall extensions <plan>`
extracts the `extension` cases as an actionable manifest (steps + oracle + `tapHint`),
and (b) `runPlan(plan, { externalResults })` / `run --merge-results <file>` folds
externally-produced `Result[]` into one `RunReport` — a matching (blocked) id is
replaced verbatim, extras are appended, never fabricating a passing verdict — so a
live test ends with a single, honest, whole-plan report.

### 15. Concurrent-distinct-ops (race) step — ✅ DONE
`load` fires N *identical* requests; the concurrency lens needed N *distinct* steps
fired at once (two writers racing one resource, optimistic-lock contention).
Delivered: a `race` step that runs its nested `steps` concurrently and resolves when
the first settles, capturing every response for cross-assertion. Only network steps
(`request`/`fetch`/`load`) may nest — racing page-mutating actions has no honest
meaning on a single-threaded page, so it is rejected at parse time.

### 16. Evidence redaction config — ✅ DONE
`${env.*}` values are scrubbed from `report.json`, but the report could still carry
SUT-returned PII or sensitive headers. Delivered: a plan-level `redaction` block
(`{ headers?: string[], patterns?: string[] }`) — response-header names plus RegExp
sources — folded with the env secrets and applied to the serialized report so a run's
evidence is shareable, directly serving live-test's "never paste real secrets into
evidence". Embedders can supply the same spec via `runPlan(plan, { redaction })`. The
binary HAR/trace stay raw (an injected `storageState` already carries live cookies);
treat the output dir as secret-bearing.

---

**Build order:** 1 → 2 → 4 → 3 → 5, then P2 (all ✅). P3 (cross-derived from the
live-test embedder) shipped in the order 10 → 11 → 12 → 14 → 13 → 15 → 16 — per-oracle
results first, since it makes every other lane's greens auditable — and is now all ✅.

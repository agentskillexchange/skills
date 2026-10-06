# Heimdall — Repository MAP

> Generated cartography of `@antreas/heimdall@0.1.0` — a multi-driver browser/API test runner. One JSON **Plan** is executed through real-Chrome (extension), headless Playwright/CDP, or an isolated Docker+Xvfb container, producing a unified, honest `RunReport` (with real `blocked`/non-run semantics) plus rich evidence.

## Overview / Architecture

Heimdall takes a declarative **Plan** (cases → steps + oracles + risk/priority) and runs each case through a pluggable **driver**, then renders results in multiple formats.

The codebase is organized as a clean pipeline with a strict separation between **pure/browser-agnostic logic** and **driver/IO concerns**:

```
            ┌────────────┐
   argv ───▶│  src/cli.ts │  Commander entrypoint (bin: heimdall)
            └─────┬──────┘
                  │ dispatches to
        ┌─────────┴───────────────────────────────┐
        ▼                                          ▼
  src/commands/*  (run, validate, doctor,    src/mcp.ts  (MCP stdio server:
   gc, init, auth, schema, buildImage)         run/doctor/schema tools)
        │
        ▼
  src/runner.ts  ── resolves & gates drivers, blocks non-runnable
        │             cases, runs via bounded concurrency pool
        ▼
  src/drivers/{cdp,container}.ts  (implement CaseDriver)
        │
        ▼
  src/execute.ts  ── shared step interpreter: drives Playwright Page,
        │             builds an Observation, runs oracles
        ▼
  src/oracle.ts   ── pure pass/fail layer over the Observation contract
        │
        ▼
  src/schema.ts   ── Zod single source of truth (Plan/Step/Oracle/Result/Report)
        │
        ▼
  RunReport ──▶ src/reporter.ts (+ reporters/{html,junit,diff}.ts)
```

**Design pillars:**
- **Single source of truth:** `src/schema.ts` is the only place the plan/report shape lives. Zod schemas derive both the TS types and the published JSON Schema (`heimdall.schema.json`).
- **Purity at the core:** `oracle.ts`, `load.ts`, `redact.ts`, and the reporters are browser-agnostic and unit-testable. The only Playwright-touching modules are `execute.ts` and the drivers.
- **Driver contract:** `src/drivers/types.ts` defines `CaseDriver` (`setup`/`runCase`/`teardown`); both the CDP and container drivers implement it, so the runner is driver-agnostic.
- **Honest results:** non-runnable cases are `blocked` (not silently passed); `exitCodeFor` is a CI-honesty gate that fails on any fail/error/non-run.
- **Secrets discipline:** `${env.X}` values reach the SUT but are scrubbed from `report.json`/stderr via `redact.ts` (retained only in the raw HAR).

## Entry Points

- **`src/cli.ts`** — the `heimdall` binary (`#!/usr/bin/env node`). Registers every subcommand and the full `run` flag surface.
- **`src/index.ts`** — public API barrel for embedding Heimdall as a library (used by the `live-test` skill): re-exports `parsePlan`, `runPlan`, `evaluateOracles`, the reporters, `loadConfig`, `VERSION`, and all types.
- **`src/mcp.ts`** — MCP stdio server (`heimdall mcp`) exposing `run`/`doctor`/`schema` as native agent tools.
- **`docker/Dockerfile`** — `ENTRYPOINT node dist/cli.js`; the container driver shells back into the CLI inside the image.

## Per-Directory File Reference

### `src/` — core

| File | Role | Key symbols |
|------|------|-------------|
| `cli.ts` | Commander CLI entrypoint (bin `heimdall`); parses argv, registers all subcommands + `run` flags | `program` (root Command), `collect` (repeatable `--filter` accumulator); commands: `run`, `validate`, `doctor`, `gc`, `init`, `schema`, `build-image`, `mcp`, `auth save` |
| `index.ts` | Public API barrel for library embedding | re-exports from `schema`, `runner`, `oracle`, `reporter`, `reporters/diff`, `config`, `version` |
| `schema.ts` | **Single source of truth** — Zod schemas + derived TS types; emits JSON Schema | `Driver` enum (extension/cdp/container), `fidelityForDriver`, `Step` (discriminated union, 19 actions), `Oracle`/`OracleUnion` (25 asserts), `Risk`, `Priority`, `TestCase`, `Plan`, `Result`, `RunReport`, `parsePlan`, `planJsonSchema` |
| `execute.ts` | Shared step interpreter — drives one case's steps against a Playwright `Page`, builds `Observation`, runs oracles | `executeCase`, `runStep` (big action switch), `applyVars` (`${name}`/`${env.*}` templating), `runHookSteps`, `ensureCaseDir`, `writeJson`, `ExecOutcome` |
| `oracle.ts` | Pure browser-agnostic pass/fail layer over an `Observation` | `evaluateOracles`, `evalOne` (total switch over 25 asserts), `getByPath`; interfaces `Observation`, `ObservedResponse`, `OracleOutcome` |
| `load.ts` | Pure load/concurrency engine for the `load` step (percentile + error-rate maths) | `runConcurrent` (bounded pool), `percentile` (nearest-rank), `summarizeLoad`, `modalStatus`, `formatLoadStats`, `LoadSample` |
| `runner.ts` | Core orchestrator — resolve/gate drivers, block non-runnable cases, run via concurrency pool, emit `RunReport` | `runPlan`, `filterMatchedNothing`, `resolveDriver`, `pool`, `runOnce` (timeout race), `runWithRetries`, `runPlanHook`, `RunOptions` |
| `config.ts` | Optional `heimdall.config.json` loader — run defaults + env seed for `${env.*}` | `loadConfig` (missing⇒`{}`, malformed⇒throws, real env wins), `HeimdallConfig` (strict) |
| `redact.ts` | Secret redaction — scrubs env-resolved `${env.*}` values from report output | `registerSecret`, `redactString`, `redactDeep`, `clearSecrets` (per-run scope) |
| `reporter.ts` | Terminal rendering + exit-code policy + grouping | `formatReport`, `exitCodeFor` (CI honesty gate), `groupResults` (pure), `CaseMeta`, `ReportFormatOptions` |
| `log.ts` | Dependency-free ANSI colour logger (auto-disabled off-TTY; all to stderr) | `c` (colour fns), `log` (info/step/ok/warn/err/debug), `setVerbose` |
| `version.ts` | Reads `package.json` at runtime → version constant (falls back to `0.0.0`) | `readVersion`, `VERSION` |

### `src/drivers/` — execution lanes

| File | Role | Key symbols |
|------|------|-------------|
| `types.ts` | Driver contracts shared by cdp + container | `CaseDriver` (`name`/`setup`/`runCase`/`teardown`), `RunContext`, `CaptureMode` (`off`/`on`/`on-failure`) |
| `cdp.ts` | Playwright/CDP driver (default lane) — isolated `BrowserContext` per case, genuine parallelism | `CdpDriver` (`setup`=`chromium.launch`, `runCase`=newContext+HAR/trace/video+`executeCase`, `teardown`=`browser.close`) |
| `container.ts` | Docker+Xvfb sandbox driver — runs each case via in-image cdp path; safe home for destructive/untrusted SUTs | `ContainerDriver`, `dockerAvailable`, `imageExists`, `buildImage`, `rewriteHostUrls` (localhost→host.docker.internal), `collectEnvRefs`, `IMAGE_TAG`=`heimdall:local` |

### `src/reporters/` — output formats

| File | Role | Key symbols |
|------|------|-------------|
| `html.ts` | Self-contained HTML report with inlined base64 screenshots | `buildHtml`, `writeHtmlReport`, `renderCase` |
| `junit.ts` | JUnit XML for CI test reporters | `toJUnitXml` (skipped = blocked+skipped), `writeJUnitReport`, `JUnitOptions` |
| `diff.ts` | Regression diff between two `RunReport`s — pass↔fail buckets | `diffReports` (pure), `isCleanDiff`, `formatDiff`, `writeDiffReport`, `RegressionDiff`, `DiffCase` |

### `src/commands/` — CLI subcommand implementations

| File | Role | Key symbols |
|------|------|-------------|
| `run.ts` | `heimdall run <plan>` — config/plan loading, CLI>config precedence, `runPlan`, report fan-out, exit code | `runCommand`, `resolveRunNumber` (precedence), `metaFor`, `RunCmdOpts` |
| `validate.ts` | Plan validation UX (every problem with case attribution) + `--lenient` | `collectPlanErrors`, `validateCasesIndividually`, `validateCommand`, `CaseValidation` |
| `doctor.ts` | Toolchain checks (Node/Chromium/Docker/image), shared by command + MCP | `collectDoctorChecks`, `cdpReady`, `doctorCommand`, `Check` |
| `gc.ts` | `heimdall gc` — prune orphaned Playwright browser revisions | `gcCommand` (dry-run unless `--yes`), `GcOpts` |
| `init.ts` | `heimdall init` — write sample plan; refuses to overwrite | `initCommand`, `SAMPLE_PLAN` (2-case sample) |
| `auth.ts` | `heimdall auth save` — interactive headed-browser storageState capture (passwords never touch Heimdall) | `authSaveCommand`, `AuthSaveOpts` |
| `schema.ts` | `heimdall schema` — emit plan JSON Schema to file/stdout | `schemaCommand` |
| `buildImage.ts` | `heimdall build-image` — build the container-driver Docker image | `buildImageCommand` (Docker guard → `buildImage`) |

### `test/` — Vitest suite

| File | Role |
|------|------|
| `fixtures/server.ts` | Dependency-free `node:http` fixture server (HTML/health/redirect/poll/slow/SSE/resource-CRUD/echo-auth) that all integration e2es drive against |
| `integration/cdp.e2e.test.ts` | Real Chromium e2e through `runPlan` on cdp: ui render, in-page fetch, request-mode |
| `integration/config.e2e.test.ts` | `${env.X}` interpolation + redaction contract (reaches SUT, scrubbed from report/stderr, retained in HAR) |
| `integration/container.e2e.test.ts` | Container-driver e2e (skipped unless Docker + image + working bind mount) |
| `integration/fixtures.e2e.test.ts` | setup/teardown hook lifecycle (per-case + plan-level, failure semantics) |
| `integration/flow.e2e.test.ts` | Stateful flow: capture `x-run-id` from redirect, then templated `pollUntil` |
| `integration/load.e2e.test.ts` | `load` step + errorRate/percentile oracles against flaky `/slow` |
| `integration/mcp.e2e.test.ts` | Spawns `heimdall mcp`, drives via official MCP client (tools list/schema/doctor/run/invalid) |
| `integration/sse.e2e.test.ts` | `sse` step + `eventCount` oracle (three events / partial / hang) |
| `config.test.ts` | Unit: `loadConfig` + `resolveRunNumber` precedence |
| `load.test.ts` | Unit: load engine (percentile/summarize/modalStatus/runConcurrent/format) |
| `oracle.test.ts` | Unit: `getByPath`, `applyVars`, `evaluateOracles` across full vocabulary |
| `redact.test.ts` | Unit: secret redactor + applyVars-registers-env wiring |
| `reporters.test.ts` | Unit: JUnit/HTML/terminal reporters, `groupResults`, `exitCodeFor`, diff |
| `schema.test.ts` | Unit: `parsePlan` defaults/rejections, `fidelityForDriver` |
| `validate.test.ts` | Unit: `collectPlanErrors`, `validateCasesIndividually` |

### Root / config / assets

| File | Role |
|------|------|
| `docker/Dockerfile` | Container-driver image — `FROM mcr.microsoft.com/playwright:v1.61.0-jammy` (must match pinned playwright dep); `ENTRYPOINT node dist/cli.js` |
| `package.json` | NPM manifest — ESM, `bin heimdall→dist/cli.js`; deps playwright 1.61.0 (pinned), zod, commander, `@modelcontextprotocol/sdk`, zod-to-json-schema, axe-core, pixelmatch, pngjs; scripts build/dev/schema/test/typecheck |
| `tsconfig.json` | TS config — ES2022/ESNext, Bundler resolution, strict + noUncheckedIndexedAccess; emits to `dist` from `src`; excludes test |
| `heimdall.schema.json` | Generated JSON Schema of a Plan (emitted from `src/schema.ts`) |
| `examples/plan.example.json` | Example plan mirroring `SAMPLE_PLAN` |
| `MAP.md` / `README.md` / `ROADMAP.md` | Engineering map / agent playbook / roadmap (feeds `improve-heimdall`) |
| `.claude/skills/heimdall/SKILL.md` | Heimdall skill — author/run plans through the three drivers |
| `.claude/skills/live-test/{SKILL,roster}.md` | Live-test skill + expert persona roster (composes agent-orchestra + visual-qa + Heimdall) |
| `.claude/workflows/improve-heimdall.js` | Orchestration workflow — 2 implementers → arbiter → adversary → applyable diff |
| `LICENSE` / `.gitignore` | MIT license / ignore rules (auth storageState, heimdall-runs evidence) |

## Plan Model (the domain vocabulary)

- **19 step actions:** `goto`, `click`, `fill`, `select`, `hover`, `check`, `uncheck`, `setViewport`, `waitForResponse`, `press`, `waitFor`, `wait`, `fetch`, `request`, `pollUntil`, `load`, `sse`, `eval`, `screenshot`.
- **25 oracle asserts:** `status`, `responseOk`, `statusIn`, `statusRange`, `jsonPath`, `visible`, `hidden`, `textContains`, `urlContains`, `titleContains`, `count`, `attribute`, `responseTime`, `header`, `jsonType`, `nonEmpty`, `bodyContains`, `jsonMatch`, `titleMatches`, `urlMatches`, `noConsoleErrors`, `evalTruthy`, `errorRate`, `eventCount`, `percentile`. (`Oracle.superRefine` rejects unbounded `eventCount`.)
- **Drivers → fidelity:** `extension`→`high`, `cdp`→`medium`, `container`→`medium-linux`.
- **Risk gate:** `read-only` (default) / `writes` / `destructive` / `paid` / `prod`; the runner blocks cases above the allowed risk.
- **Result status:** `pass` / `fail` / `blocked` / `skipped` / `error`.

## Dependency Sketch

```
cli.ts ──▶ commands/* ──▶ runner.ts ──▶ drivers/{cdp,container}.ts ──▶ execute.ts ──▶ oracle.ts ──▶ schema.ts
   │            │              │                                          │              ▲
   │            │              └─▶ reporter.ts ─▶ reporters/{html,junit,diff}.ts         │
   │            └─▶ config.ts ─────────────────────────────────────────────────────────┘
   ├──▶ mcp.ts ──▶ runner.ts + commands/doctor.ts + schema.ts
   └──▶ log.ts, version.ts (leaf utilities, no internal deps)

execute.ts ──▶ load.ts + redact.ts        (pure helpers)
schema.ts  ──▶ zod, zod-to-json-schema     (only external schema deps)
drivers/container.ts ──▶ docker/Dockerfile (builds & runs the image)
index.ts (library barrel) ──▶ schema + runner + oracle + reporter + reporters/diff + config + version
```

**External dependencies:** `playwright` (1.61.0 pinned, must match the Dockerfile base image), `commander` (CLI), `zod` + `zod-to-json-schema` (schema), `@modelcontextprotocol/sdk` (MCP), `axe-core`/`pixelmatch`/`pngjs` (a11y/visual tooling). Reporters and pure-logic modules use only Node built-ins.

**Cross-cutting invariants:**
- All schema/report shapes flow from `schema.ts`; nothing else defines them.
- `oracle.ts` only knows the `Observation` interface — never Playwright directly.
- `redact.ts` secrets are per-run scoped (`clearSecrets` between runs); secrets survive only in raw HAR, never in `report.json`/stderr.
- `exitCodeFor` is the CI honesty gate: any non-run (`blocked`) counts against a clean exit.

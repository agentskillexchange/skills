# Heimdall

A browser and API test runner that turns an agent's claim of “it works” into repeatable checks and inspectable evidence.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

You describe the actions and the result that must be true in a JSON plan. Heimdall executes the self-driven cases, evaluates their assertions, and records outcomes with screenshots, network evidence, and per-assertion results. Cases requiring your real logged-in browser remain explicit handoffs; Heimdall does not pretend it drove them.

## Why Heimdall exists

Clicking through an app is useful exploration, but it is hard to repeat, compare, or audit unless the expected outcomes are written down. And checks that depend on a person's current browser session should not be confused with checks run in a fresh automated browser.

Heimdall gives those checks a common contract. A case needs at least one **oracle**—an explicit pass/fail assertion—so a sequence of clicks alone cannot count as a test. The driver records where it ran; the report separates `pass`, `fail`, `error`, `blocked`, and `skipped`.

For example, after changing a search flow you can check that submitting a query reaches the results page, displays the expected text, and produces no console errors. An API case can check status and response fields, or start an asynchronous job, capture its ID, and poll until it is ready. Save the plan and run it again after the next change.

## Skill and runtime

This repository ships both:

- [An Agent Skill](SKILL.md) that teaches an agent to author meaningful plans, choose drivers, respect risk boundaries, and report partial runs accurately.
- A TypeScript runtime available as a CLI, an MCP server, and a library. It validates and executes plans and produces the evidence and reports.

Installing the skill alone does not install the CLI or a browser. Conversely, you can use the CLI without an agent. The model helps decide what to test; the runner performs the specified actions and checks.

## Choose where a case runs

| Driver | What actually runs | Use and limit |
| --- | --- | --- |
| `cdp` (default) | Playwright launches Chromium; each case gets a fresh browser context. Cases run in parallel without sharing foreground input focus. | Repeatable browser/API checks, headless or headed. Injected auth is available, but this is not your existing Chrome session. Report tier: `medium`. |
| `container` | The same execution path in a disposable Docker container per case, using a Linux Playwright image. | Separates the browser process from your desktop. Requires Docker and a built image; it does not isolate the remote application or undo server-side changes. Report tier: `medium-linux`. |
| `extension` | No self-driven execution. The runner records `blocked`; an external human or browser-capable agent must perform the case. | Checks that need the real logged-in browser. Export the handoff and merge independently collected results. Report tier: `high`, a driver label—not proof that the check ran. |

The plan format is shared, but the environments are not interchangeable. Choose for the claim you need to support and report any missing evidence.

## What a pass means—and does not mean

A pass means the authored assertions succeeded, not that the application is comprehensively correct. Weak assertions still make weak tests. Blocked/skipped cases can coexist with a successful process exit if at least one case passed and none failed or errored; inspect the summary before calling a whole plan complete.

Heimdall can run axe-core checks and compare screenshots against baselines. Those are executable checks, not accessibility certification or design judgment. [Visual QA](https://github.com/AntreasAntoniou/visual-qa) is the complementary screenshot-review protocol for hierarchy, readability, affordances, and visible edge states; it does not replace these functional tests. No automatic integration is assumed.

Plans execute real actions. Review targets, credentials, fixtures, and side effects before running them; [risk labels are coordination controls, not a sandbox](SECURITY.md).

---

## Install

Requires **Node.js >= 20**.

```bash
# CLI, directly from the public source release
npm install -g git+https://github.com/AntreasAntoniou/heimdall.git

# Agent Skill (Claude Code, Codex, and compatible clients)
npx skills add AntreasAntoniou/heimdall
```

The package is not currently published to the npm registry. The GitHub install above is
the supported installation path for this release.

The `cdp` (default) driver needs Playwright's Chromium:

```bash
npx playwright install chromium
```

Check your toolchain at any time:

```bash
heimdall doctor
```

`doctor` verifies Node >= 20, Playwright Chromium (the `cdp` lane — the floor), Docker (only needed for `container`), and whether the container image is built. It exits non-zero only if the `cdp` lane isn't ready.

---

## Quickstart

```bash
# 1. Scaffold a sample plan (refuses to overwrite an existing file)
heimdall init                       # writes ./heimdall.plan.json
heimdall init -o smoke.plan.json    # custom path

# 2. Edit baseUrl + cases for an app you are authorized to test
heimdall validate heimdall.plan.json  # checks the plan without executing it

# 3. Run and read the report
heimdall run heimdall.plan.json
```

A run prints a human-readable report to stderr and writes the collected evidence to disk. Example output:

```
Heimdall — example-plan  (1843ms, v0.1.0)
────────────────────────────────────────────────────────────
PASS  home-loads cdp [medium]
PASS  health-endpoint cdp [medium]
────────────────────────────────────────────────────────────
2 pass  0 fail  0 error  0 blocked  0 skipped   of 2
report: heimdall-runs/latest/report.json
```

Run reports and captured evidence land under the output dir (default `heimdall-runs/latest`). A typical CDP case produces:

```
heimdall-runs/latest/
  report.json                       # the full machine-readable RunReport
  cases/<case-id>/
    final.png                       # final-state screenshot, when capture succeeds
    network.har                     # per-case HAR; response bodies omitted, may contain secrets
```

The JSON report also contains console errors, captured responses, and per-oracle results when available. Optional HTML/JUnit reports support review and CI; traces, videos, and visual diffs provide additional evidence when requested or applicable. Evidence can be missing after a driver/capture error. Use a distinct `--out` directory when you need to preserve earlier runs, and treat output directories as sensitive.

The process **exits non-zero if any case failed or errored** — and also if cases existed but *nothing actually ran* (everything blocked/skipped, or a `--filter` that matched no cases), so a CI gate can never pass green on a non-run. Blocked/skipped alongside at least one pass do not fail the run.

---

## The plan format

A plan is a single JSON file validated by a Zod schema (`src/schema.ts` is the source of truth). Emit the JSON Schema for your editor or other tools with `heimdall schema`.

### Plan

| Field | Type | Default | Notes |
| --- | --- | --- | --- |
| `name` | string | `"heimdall-plan"` | Shown in the report |
| `baseUrl` | string | — | Base for relative step/fetch URLs |
| `defaultDriver` | `extension` \| `cdp` \| `container` | `cdp` | Per-case `driver` overrides this |
| `storageState` | string | — | Path to a Playwright storageState for injected auth |
| `redaction` | `{ headers?: string[], patterns?: string[] }` | — | Extra response-**header** names and regex **patterns** scrubbed from the report on top of the per-run `${env.X}` secrets (see [Config & secrets](#config--secrets)) |
| `setup` | Step[] | — | Steps run **once** before any case (throwaway context) to seed shared state; if any fails, every runnable case is `blocked` (honesty preserved). **Trusted, ungated fixture** — see note below |
| `teardown` | Step[] | — | Best-effort steps run **once** after all cases to clean up shared state; failures are logged, never fatal. **Trusted, ungated fixture** — see note below |
| `cases` | TestCase[] | — | At least one required |

> **Plan hooks run UNGATED.** Unlike cases, `plan.setup`/`plan.teardown` are **not** subject to the `risk`/`--allow-risk` gate (a hook has no per-step risk field). They are treated as trusted, author-controlled fixtures and run unconditionally whenever any case is runnable. Keep destructive operations out of plan hooks unless you intend them to run without the gate; put risk-gated destructive work in a case (with `risk: "destructive"`) instead.

### TestCase

| Field | Type | Default | Notes |
| --- | --- | --- | --- |
| `id` | string | — | Required, non-empty; used for evidence dirs + filtering |
| `title` | string | — | Optional human label |
| `dimension` | string | — | Which expert/lens authored this case |
| `driver` | `extension` \| `cdp` \| `container` | inherits plan | Per-case override |
| `baseUrl` | string | — | Per-case override of the plan `baseUrl` |
| `setup` | Step[] | — | Steps run on the case's own page **before** `steps` (share its `${vars}`); a failing setup step fails the case and skips its steps/oracles |
| `steps` | Step[] | `[]` | Actions to perform before oracles run |
| `teardown` | Step[] | — | Best-effort cleanup steps run **after** oracles regardless of pass/fail (share the case's page + captured `${vars}`); a teardown failure is noted in `notes`, never flips the verdict |
| `oracle` | Oracle[] | — | **At least one required** — "otherwise it is a click, not a test" |
| `risk` | `read-only` \| `writes` \| `destructive` \| `paid` \| `prod` | `read-only` | `destructive`/`paid`/`prod` are gated (see Risk gating) |
| `priority` | `p0` \| `p1` \| `p2` \| `p3` | `p2` | |
| `tags` | string[] | `[]` | Used by `--filter` |

### Steps

A step's shape is selected by its `action`:

| Action | Fields |
| --- | --- |
| `goto` | `url` (absolute or resolved against baseUrl); `waitUntil?` (`load` \| `domcontentloaded` \| `networkidle` \| `commit`) |
| `click` | `selector` |
| `fill` | `selector`, `value` |
| `select` | `selector`, `value` (string or string[] of option values) |
| `hover` | `selector` |
| `check` | `selector` |
| `uncheck` | `selector` |
| `setViewport` | `width`, `height` |
| `press` | `key` (e.g. `"Enter"`, `"Control+A"`); `selector?` (else dispatched to the keyboard) |
| `waitFor` | `selector?`, `state?` (`visible` \| `hidden` \| `attached` \| `detached`), `timeoutMs?` (no selector ⇒ waits for `networkidle`) |
| `waitForResponse` | `urlContains`, `timeoutMs?`, `as?` (capture a response — already-arrived or future — for oracles incl. `responseTime`); `capture?` |
| `wait` | `ms` |
| `fetch` | `url`, `method?`, `headers?`, `body?`, `as?` (name to store the response under for oracles); `capture?`. Runs in-page with `credentials: "include"`. |
| `request` | `url`, `method?`, `headers?`, `body?`, `as?`, `capture?`; `redirect?` (`follow` \| `manual`, default `follow`) — a browser-context API request via Playwright's `APIRequestContext`. **No page/`goto` needed and not subject to page CORS.** With `redirect: "manual"` a 3xx is returned with **readable** headers (`location` / `hx-redirect` / …) instead of being auto-followed — this is **`request`-step only**, since an in-page `fetch` can't read an `opaqueredirect`. Captures status, headers, body + parsed JSON like `fetch`. |
| `pollUntil` | `url`, `method?`, `headers?`, `body?`, `oracle` (array of response-based oracles), `intervalMs?` (default `1000`), `timeoutMs?` (default `30000`), `as?` — issue the request via the browser-context `APIRequestContext` and re-evaluate `oracle` each poll until **all** pass (then stored as last + `as`), or **throw** when `timeoutMs` elapses (so the case fails honestly). |
| `sse` | `url`, `events?` (resolve after collecting N events), `timeoutMs?` (default `10000`), `closeAfterMs?` (hard stop), `as?` — open an in-page `EventSource` (same about:blank origin guard as `fetch`), collect message events `{event,data,id}` until `events` is reached or `timeoutMs`/`closeAfterMs` elapses (or the server closes the stream), and store an aggregate: the events array under `json`, the newline-joined `data` under `bodyText`, status `200` if any events arrived else `0`. Read it with the `eventCount` / `bodyContains` / `jsonPath` oracles. |
| `load` | `url`, `method?`, `headers?`, `body?`, `times` (total iterations), `concurrency?` (max in-flight; default `min(times, 10)`), `as?` — fire the same request `times` times via the browser-context `APIRequestContext` (bounded by `concurrency`) and store an aggregate (`errorRate` plus latency percentiles `p50`/`p95`/`p99`/`max`). Read it with the `errorRate` / `percentile` oracles. |
| `route` | `urlContains` (substring matched against request URLs), `mode` (`block` \| `abort` \| `fulfill` \| `delay`), `status?`/`body?`/`headers?` (for `fulfill`), `delayMs?` (added latency for `delay`, also usable with `fulfill`) — install a network interception for the rest of the case: `block`/`abort` fail matching requests, `fulfill` returns a synthetic status/body/headers, `delay` slows them. Fault injection / stubbing so failure-recovery is a case, not hand-driving. **Intercepts PAGE-originated requests only** (`goto` + in-page `fetch`/`eval`); it does **not** affect the `request`/`load`/`pollUntil` steps (those use Playwright's APIRequestContext, which bypasses `page.route`) — drive those flows through an in-page `fetch` step if you need them faulted. |
| `race` | `steps` (array of **network** steps — only `request`/`fetch`/`load` are allowed, enforced at parse time) — run the nested steps concurrently and wait for **all** of them to settle, capturing every response for cross-assertion (two writers racing one resource, optimistic-lock contention). Unlike `load` (which fires N *identical* requests), `race` fires N *distinct* steps at once. |
| `eval` | `expression` (JS evaluated in the page, for side effects) |
| `screenshot` | `name?` |

#### Variable capture + `${...}` templating

`fetch`, `request`, and `waitForResponse` accept an optional **`capture`** map that pulls values out of the step's response into a per-case variable bag:

```jsonc
"capture": {
  "runId": { "header": "x-run-id" },     // from a response header (case-insensitive)
  "userId": { "jsonPath": "data.user.id" } // or a JSON path into the parsed body
}
```

Captured values are then substitutable as `${name}` in later steps' `url`, `body`, `headers` values (`goto`/`fetch`/`request`/`pollUntil`/`load`/`sse`) and in `waitForResponse`'s `urlContains`. A token beginning `env.` (e.g. `${env.API_TOKEN}`) resolves from `process.env` at runtime instead of the capture bag — this is how a plan injects secrets via the environment rather than inlining them (see [Config & secrets](#config--secrets)). Unknown `${tokens}` are left verbatim. Together with `request` `redirect: "manual"` and `pollUntil`, this expresses a full async lifecycle — **POST → capture an id from a redirect header → poll until ready → assert** — entirely within a plan:

```jsonc
{ "action": "request", "url": "/start", "method": "POST", "redirect": "manual",
  "capture": { "runId": { "header": "x-run-id" } }, "as": "start" },
{ "action": "pollUntil", "url": "/poll?id=${runId}", "timeoutMs": 5000, "as": "p",
  "oracle": [{ "assert": "jsonPath", "path": "ready", "equals": true }] }
```

### Oracles

The pass/fail layer. A case passes only if **every** oracle passes.

| Assert | Fields | Checks |
| --- | --- | --- |
| `status` | `equals`, `of?` (named fetch response; defaults to last) | HTTP status equals |
| `statusIn` | `values` (non-empty int[]), `of?` | Captured response status is one of `values` |
| `statusRange` | `min`, `max`, `of?` | `min <= status <= max` (inclusive; e.g. `200..499` for "not 5xx") |
| `responseOk` | `of?` | Response was 2xx |
| `jsonPath` | `path` (e.g. `"data.user.id"` or `"$.ok"`), `equals?`, `exists?`, `of?` | JSON body at path equals / exists |
| `visible` | `selector` | Element is visible |
| `hidden` | `selector` | Element is not visible |
| `textContains` | `selector`, `value` | Element text contains substring |
| `urlContains` | `value` | Current URL contains substring |
| `titleContains` | `value` | Page `<title>` contains substring |
| `count` | `selector`, `equals` | Number of matching elements equals |
| `attribute` | `selector`, `name`, `equals?`, `contains?`, `exists?`, `matches?` | Element attribute equals / contains / matches `RegExp`; `exists:true` asserts presence (any value), `exists:false` asserts absence |
| `responseTime` | `maxMs`, `of?` | Captured response's duration is within budget |
| `header` | `name` (case-insensitive), `equals?`, `contains?`, `of?` | Captured response header equals / contains (fails clearly if absent) |
| `jsonType` | `path`, `type` (`string` \| `number` \| `boolean` \| `array` \| `object` \| `null`), `of?` | JSON value at path has the given type |
| `nonEmpty` | `path?`, `of?` | JSON value at path is a non-empty string/array; with no `path`, the response body is non-empty |
| `bodyContains` | `value`, `of?` | Response body text includes `value` |
| `jsonMatch` | `path`, `pattern`, `of?` | String at path matches `RegExp(pattern)` |
| `titleMatches` | `pattern` | Page `<title>` matches `RegExp(pattern)` |
| `urlMatches` | `pattern` | Current URL matches `RegExp(pattern)` |
| `eventCount` | `min?`, `equals?`, `of?` | Number of events collected by an `sse` step is at least `min` and/or exactly `equals` |
| `errorRate` | `max` (0..1), `of?` | A `load` step aggregate's error rate (non-2xx or thrown) is `<= max` |
| `percentile` | `p` (`50` \| `95` \| `99` \| `"max"`), `maxMs`, `of?` | A `load` step aggregate's chosen latency percentile is `<= maxMs` |
| `noConsoleErrors` | — | No `console.error` / page errors during the case |
| `evalTruthy` | `expression` | JS evaluated in the page is truthy |
| `a11y` | `maxImpact?` (`minor` \| `moderate` \| `serious` \| `critical`, default `serious`), `include?`/`exclude?` (CSS selectors) | Runs an axe-core accessibility audit over the page and fails on any violation **at or above** `maxImpact`; the violation list is captured as evidence. Self-drivable on `cdp`/`container`. |
| `screenshotMatches` | `baseline` (path to a baseline PNG), `maxDiffRatio?` (0..1, default `0.01`), `selector?` (clip to an element instead of the viewport) | Pixel-compares the viewport (or `selector`) against a baseline via pixelmatch and fails when the fraction of differing pixels exceeds `maxDiffRatio`; the driver attempts to write a diff image as evidence. A missing baseline passes with a first-run note and is seeded from the current capture; this is not regression evidence until the baseline is reviewed. |

### A concrete plan

```json
{
  "name": "example-plan",
  "baseUrl": "http://localhost:3000",
  "defaultDriver": "cdp",
  "storageState": "auth/session.storageState.json",
  "cases": [
    {
      "id": "home-loads",
      "title": "Home page renders without console errors",
      "dimension": "functional",
      "steps": [{ "action": "goto", "url": "/" }],
      "oracle": [
        { "assert": "noConsoleErrors" },
        { "assert": "visible", "selector": "body" }
      ],
      "risk": "read-only",
      "priority": "p0",
      "tags": ["smoke"]
    },
    {
      "id": "search-flow",
      "title": "Searching navigates to results",
      "steps": [
        { "action": "goto", "url": "/" },
        { "action": "fill", "selector": "#q", "value": "heimdall" },
        { "action": "press", "key": "Enter" },
        { "action": "waitFor", "selector": "[data-testid=results]", "state": "visible" },
        { "action": "screenshot", "name": "results" }
      ],
      "oracle": [
        { "assert": "urlContains", "value": "/search" },
        { "assert": "textContains", "selector": "[data-testid=results]", "value": "heimdall" }
      ],
      "risk": "read-only",
      "priority": "p1",
      "tags": ["search"]
    },
    {
      "id": "health-endpoint",
      "title": "Health endpoint returns 200 and ok:true",
      "dimension": "api",
      "steps": [
        { "action": "fetch", "url": "/api/health", "method": "GET", "as": "health" }
      ],
      "oracle": [
        { "assert": "status", "equals": 200, "of": "health" },
        { "assert": "responseOk", "of": "health" },
        { "assert": "jsonPath", "path": "ok", "equals": true, "of": "health" }
      ],
      "risk": "read-only",
      "priority": "p1",
      "tags": ["api", "smoke"]
    }
  ]
}
```

---

## CLI commands

### `heimdall run <plan>`

Run a plan through its drivers (`cdp`/`container`) and report.

| Flag | Default | Meaning |
| --- | --- | --- |
| `-d, --driver <driver>` | — | Force a driver for every case: `cdp` \| `container` |
| `-o, --out <dir>` | `heimdall-runs/latest` | Output dir for evidence + report |
| `-b, --base-url <url>` | — | Base URL for relative step/fetch URLs (overrides plan) |
| `-s, --storage-state <file>` | — | Playwright storageState for injected auth |
| `-c, --concurrency <n>` | `4` | Max parallel cases **per driver** |
| `-r, --retries <n>` | `0` | Retry a failed/errored case up to n times (helps with flake) |
| `--timeout <ms>` | — | Overall wall-clock budget per case (per-case `timeoutMs` wins) |
| `--allow-risk` | `false` | Permit cases marked `destructive`/`paid`/`prod` to run |
| `--headed` | `false` | Visible browser window (`cdp` only) |
| `--insecure` | `false` | Disable TLS validation (ignored when `--storage-state` is set) |
| `--trace [mode]` | `off` | Record a Playwright `trace.zip` per case: `off`/`on`/`on-failure` (bare `--trace` ⇒ `on-failure`) |
| `--video [mode]` | `off` | Record a video per case: `off`/`on`/`on-failure` (bare `--video` ⇒ `on-failure`) |
| `--html [file]` | — | Also write a self-contained HTML report (default `<out>/report.html`) |
| `--junit <file>` | — | Also write a JUnit XML report for CI |
| `--group-by <key>` | — | Group report rows (terminal + HTML) and the JUnit `classname` by case `tag` or `dimension`; also surfaces a prominent "Blocked (N)" panel |
| `--diff <prevReport.json>` | — | Compare against a previous run's `report.json` and print a regression diff (newly-failing / newly-passing / still-failing / added / removed) after the run |
| `-C, --config <file>` | `heimdall.config.json` | Load run defaults + an `env` seed from a config file before parsing the plan (see [Config & secrets](#config--secrets)) |
| `-f, --filter <idOrTag>` | — | Only run cases matching an id substring or exact tag (repeatable) |
| `--merge-results <file>` | — | Fold an externally-produced `Result[]` (or a `{ results: [...] }` report) into the run. Matching `blocked`/`skipped` entries are replaced; actual executed verdicts are not overwritten; unknown ids are appended. External evidence remains the producer's responsibility—see [`heimdall extensions`](#heimdall-extensions-plan). |
| `--json` | `false` | Print the full JSON report to stdout |
| `-v, --verbose` | `false` | Verbose debug logging |

```bash
heimdall run plan.json
heimdall run plan.json -d container --allow-risk        # isolated, risky SUT
heimdall run plan.json -f smoke -f search -c 8          # filter + more parallelism
heimdall run plan.json --retries 2 --timeout 30000      # tolerate flake, cap each case
heimdall run plan.json --html --junit results.xml       # shareable + CI reports
heimdall run plan.json --group-by dimension             # group rows by authoring lens
heimdall run plan.json --diff prev/report.json          # regression diff vs last run
heimdall run plan.json --config heimdall.config.json    # defaults + env-seeded secrets
heimdall run plan.json --trace on-failure --video on-failure  # capture failures for replay
heimdall run plan.json --headed                         # watch the cdp browser
heimdall run plan.json --json > report.json             # machine-readable to stdout
```

A captured trace is replayable with `npx playwright show-trace <out>/cases/<id>/trace.zip`.

### `heimdall doctor`

Check the toolchain: Node, Playwright Chromium, Docker, and the container image. Exits non-zero only if the `cdp` lane isn't ready.

### `heimdall validate <plan>`

Check JSON and plan-schema validity without executing actions. Reports validation errors with their case and field paths; exits `0` for a valid plan or `2` for invalid/unreadable input. This checks structure, not whether the assertions are meaningful or the target is safe.

### `heimdall gc`

Prune orphaned Playwright browser revisions from the cache (Playwright hoards every revision it ever downloaded). Keeps the newest revision per browser family.

| Flag | Default | Meaning |
| --- | --- | --- |
| `-y, --yes` | `false` | Actually delete (default is a dry run) |

### `heimdall init`

Write a sample plan you can edit. Refuses to overwrite an existing file.

| Flag | Default | Meaning |
| --- | --- | --- |
| `-o, --out <file>` | `heimdall.plan.json` | Where to write the sample plan |

### `heimdall schema`

Emit the JSON Schema for a plan (for editors / other tools).

| Flag | Default | Meaning |
| --- | --- | --- |
| `-o, --out <file>` | stdout | Write to a file instead of stdout |

### `heimdall extensions <plan>`

Emit a manifest of the plan's `driver: extension` cases for an agent to drive in real Chrome. Heimdall cannot self-drive your logged-in browser, so it `block`s those cases; this command extracts them as an actionable manifest — each case's `steps` + `oracle` plus a human `tapHint` ("Drive X in real Chrome starting at …, then verify N step(s) + M oracle(s).").

| Flag | Default | Meaning |
| --- | --- | --- |
| `-o, --out <file>` | stdout | Write the manifest to a file instead of stdout |

The two-lane workflow closes with `--merge-results`: run the self-drivable lanes, drive the extension cases via the agent's real-Chrome tools, write their outcomes as a `Result[]`, then fold them into one report. Importing a result does not independently verify that its claimed actions happened; review its producer and evidence:

```bash
heimdall extensions plan.json -o ext-manifest.json   # what the agent must drive
# … agent drives those cases in real Chrome, writes ext-results.json …
heimdall run plan.json --merge-results ext-results.json   # one unified RunReport
```

### `heimdall build-image`

Build the Docker image used by the `container` driver (`heimdall:local`). It also auto-builds on first container run.

| Flag | Default | Meaning |
| --- | --- | --- |
| `-t, --tag <tag>` | `heimdall:local` | Image tag |

### `heimdall auth save`

Open a Playwright browser, log in manually, and save its session to a file. The CLI does not ask for your password or MFA code; the saved cookies/localStorage can still grant account access.

| Flag | Default | Meaning |
| --- | --- | --- |
| `-u, --url <url>` | *(required)* | Login URL to open |
| `-o, --out <file>` | `auth/session.storageState.json` | Where to save the storageState |

### `heimdall mcp`

Run Heimdall as an [MCP](https://modelcontextprotocol.io) server over stdio, so Claude Code (or any MCP client) calls it as a **native tool** instead of shelling out.

```bash
# register once with Claude Code
claude mcp add heimdall -- heimdall mcp
```

It exposes three tools:

| Tool | Input | Returns |
| --- | --- | --- |
| `run` | `plan` (object) + optional `baseUrl`/`driver`/`concurrency`/`retries`/`timeoutMs`/`allowRisk`/`storageState`/`trace`/`video`/`filter`/`outDir` | the full `RunReport` (summary + per-case results + evidence paths) |
| `doctor` | — | toolchain checks + `cdpReady` |
| `schema` | — | the JSON Schema for a plan |

The agent builds a plan, calls `run`, and reads the structured report back — no CLI parsing, no temp files. An invalid plan comes back as an MCP error with the validation message.

---

## Risk gating

Every case carries a `risk`. Cases marked `destructive`, `paid`, or `prod` are **blocked unless you pass `--allow-risk`**. Obtain human authorization before using that flag: it permits all such selected cases, and the runtime cannot verify the authorization itself. `read-only` and `writes` are not gated. The labels are author-supplied; Heimdall does not infer the real consequences of a request. Blocked cases appear with their reason.

Plan-level setup/teardown is trusted and ungated, and runs through a host Playwright browser even when the cases use containers. A container isolates the case's browser process, not the system under test, network side effects, or plan-level hooks. Use disposable test data and review cleanup/recovery independently; best-effort teardown failures do not flip a passing verdict.

`extension` cases are always blocked too: Heimdall cannot self-drive your real Chrome, so it records them as `blocked` with a pointer to run them through an agent's browser tools.

---

## Auth via `storageState`

Brittle, scripted logins are a classic test-suite tax. Heimdall sidesteps them with Playwright's **storageState** — a snapshot of cookies + localStorage you capture once and inject into every run.

```bash
# 1. Capture a session interactively (real headed browser; you sign in by hand)
heimdall auth save -u https://app.example.com/login -o auth/session.storageState.json

# 2. Inject it into a run
heimdall run plan.json --storage-state auth/session.storageState.json
#    …or set "storageState" in the plan, or per the cdp/container context.
```

The `cdp` driver loads the storageState into every `BrowserContext`; the `container` driver copies it into the sandbox and reuses it inside. **The session file holds live cookies/tokens — keep it gitignored and never share it.**

---

## Config & secrets

An optional `heimdall.config.json` (loaded from the cwd, or an explicit `--config <file>`) supplies run-level defaults and — crucially — an `env` map that **seeds `process.env` for this run** so a plan can reference secrets via `${env.NAME}` templating instead of inlining them:

```jsonc
{
  "baseUrl": "https://staging.example.com",
  "defaultDriver": "cdp",
  "concurrency": 6,
  "retries": 1,
  "storageState": "auth/session.storageState.json",
  "env": {
    "API_BASE": "https://api.staging.example.com"
  }
}
```

- **Defaults precedence is CLI > plan > config.** A config value only fills a hole the CLI flag (and, for `baseUrl`/`defaultDriver`/`storageState`, the plan) left open.
- **`env` never clobbers a real environment variable** — an entry is applied only when the key is unset, so a CI-provided `API_TOKEN` always wins over the config file. Put non-secret defaults here; keep actual secrets in the real environment.
- In a plan, `${env.API_TOKEN}` resolves from `process.env` at runtime (unknown env ⇒ empty string), so tokens live in the environment, never in the committed plan JSON. The `container` driver forwards the env vars a case references into the sandbox via `docker run -e NAME` (the value is pulled from the host environment at run time — the on-disk sub-plan keeps the `${env.NAME}` token, never the resolved secret), so `${env.*}` resolves identically on the `cdp` and `container` lanes.

**Secret hygiene — what is and isn't scrubbed.** The runtime tracks env-resolved values of at least four characters and replaces registered values in `report.json` and reports derived from it. This is literal-value redaction, not general secret detection. Short, transformed, unregistered, or externally supplied secrets need separate scrutiny. Without extra redaction configuration, the per-case `network.har` retains headers and URLs even though response bodies are omitted; traces, screenshots, and video can also expose sensitive data. **Treat a run's output directory as secret-bearing**—keep it gitignored and review it before any sharing.

**Extra redaction config.** Beyond the per-run `${env.X}` secrets, a plan can declare a `redaction` block to scrub SUT-returned PII or sensitive headers from the report:

```jsonc
{
  "name": "my-plan",
  "redaction": {
    "headers": ["authorization", "set-cookie"],   // response header values blanked (case-insensitive)
    "patterns": ["[0-9]{16}", "\\b\\w+@\\w+\\.\\w+\\b"]  // RegExp sources; any match in report strings is blanked
  },
  "cases": [ /* … */ ]
}
```

The spec is folded with the registered env values and applied to the serialized report (`report.json` + terminal/HTML/JUnit). A non-empty spec also enables best-effort scrubbing of the on-disk `network.har` in the CDP driver; the container driver passes the spec to its inner run. HAR scrubbing failures do not fail the case, and screenshots, `trace.zip`, and video are not scrubbed. Embedders can supply the same spec via `runPlan(plan, { redaction })`, merged with `plan.redaction`. Invalid regex patterns are silently ignored, so verify your patterns and inspect outputs rather than treating configuration as proof that redaction succeeded.

A malformed config (bad JSON or an unknown key) fails loudly; a missing config is simply ignored.

---

## How it pairs with agent test workflows

Heimdall is designed to be embedded, not just run by hand. The public API (`src/index.ts`) exports the schemas, the runner, the oracle evaluator, and the reporter:

```ts
import { runPlan, parsePlan, evaluateOracles, formatReport, exitCodeFor } from "@antreas/heimdall";

const plan = parsePlan(JSON.parse(rawPlanJson));
const report = await runPlan(plan, {
  outDir: "heimdall-runs/latest",
  allowRisk: false,
  headed: false,
  concurrency: 4,
});
process.exit(exitCodeFor(report));
```

An agent workflow can author a thorough plan and then execute it through the most faithful available browser lane. The division of labour is clean:

- The skill authors plans against the schema (`heimdall schema` gives it the contract), assigning each case a `dimension`, `risk`, `priority`, and the right `driver`.
- Heimdall runs the **self-drivable lanes** (`cdp`, `container`) in parallel and emits a structured `RunReport` with screenshots, HAR, console errors, and captured responses as evidence.
- Cases that demand the highest fidelity — your real logged-in session — are tagged `driver: extension`. Heimdall blocks those honestly, the calling workflow extracts them with [`heimdall extensions`](#heimdall-extensions-plan), drives them through real-Chrome browser tools, and folds the outcomes back in.

**Per-oracle results — auditable greens.** Each `Result` carries an optional `oracleResults[]` — one entry per oracle with its `kind` (the `assert` discriminant), `passed`, and a human-readable `detail`. A passing case no longer reports only `observed: "all N oracle(s) satisfied"`; the verifier can see *which* oracle fired and on what, detecting a hollow green from the report alone without a re-run. (Older reports omit the field, so it is optional.)

**Merging the two lanes into one report.** Embedders pass externally driven outcomes to `runPlan(plan, { externalResults })` (the CLI equivalent is `--merge-results`). The runner replaces matching `blocked`/`skipped` placeholders, refuses to overwrite an executed verdict, and appends extra IDs before recomputing the summary. `exitCodeFor` then reflects that merged report, whose imported evidence still depends on the external producer:

```ts
const report = await runPlan(plan, {
  outDir: "heimdall-runs/latest",
  externalResults,   // Result[] the agent produced for the extension cases
  redaction: { headers: ["set-cookie"] },  // optional extra scrubbing, merged with plan.redaction
});
```

The result is one plan format and one evidence model, with execution and handoffs kept visible. It makes a verification claim inspectable; it does not remove the need to assess the tests or trustworthiness of their evidence.

## Development

From a source checkout:

```bash
npm ci
npm test
npm run build
```

See [CONTRIBUTING.md](CONTRIBUTING.md). Browser/container integration tests need the corresponding runtime dependencies; passing schema or unit tests alone does not verify those lanes.

---

## License

MIT © Antreas Antoniou

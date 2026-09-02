---
name: "Author and Run Regression Tests with Agent QA"
slug: "author-and-run-regression-tests-with-agent-qa"
description: "Use Agent QA's CLI and MCP server to author, validate, run, debug, and triage natural-language web and mobile regression tests with persistent test memory and reviewable run evidence."
github_stars: 897
verification: "listed"
source: "https://github.com/vostride/agent-qa"
author: "vostride"
category: "Browser Automation"
framework: "Codex"
tool_ecosystem:
  github_repo: "vostride/agent-qa"
  github_stars: 897
---

# Author and Run Regression Tests with Agent QA

Use Agent QA when a coding task needs an application flow verified in a real browser or mobile environment. Agent QA stores tests as reviewable project files, accepts natural-language actions and assertions, and can retain scoped observations from earlier runs. Prefer its MCP tools when available: discover the workspace, inspect configuration, generate canonical IDs, validate test or suite definitions, and enqueue the run. Use the CLI as a fallback. When execution fails, inspect the recorded steps and evidence before changing the test; distinguish an application regression from an outdated instruction or an infrastructure failure. Agent QA can re-observe the interface and try another path during a run, but successful self-healing should still be reviewed before the learned path is trusted for later runs.

Agent QA is currently source-available under FSL-1.1-ALv2. Each release converts to Apache-2.0 after two years. Configured model, browser, or device providers may have separate costs.

## Prerequisites

Install Agent QA in the project and initialize its workspace:

```bash
npm install -D agent-qa
npx agent-qa init
npx agent-qa install-browsers --chromium
```

For Android or iOS projects, install the required mobile drivers:

```bash
npx agent-qa install-mobile-drivers --all
```

## Workflow

1. Discover the Agent QA workspace and inspect its active targets, devices, and providers.
2. Generate IDs with Agent QA tooling; never invent test, suite, hook, run, or observation IDs.
3. Create or update the natural-language test, then validate its definition before saving or running it.
4. Enqueue the test or suite through MCP. If MCP is unavailable, run a validated file with `npx agent-qa run <test-file>`.
5. Review step evidence, healing attempts, and retained observations before deciding whether to fix the application, revise the test, or retry infrastructure.

## Installation

Install or set up from the source-backed instructions:

Install with npm install -D agent-qa, then run npx agent-qa init and install the runtime support you need such as npx agent-qa install-browsers --chromium.

- Source: https://github.com/vostride/agent-qa

## Documentation

- [Agent QA quickstart](https://vostride.com/docs/agent-qa/quickstart)
- [Agent QA CLI reference](https://vostride.com/docs/agent-qa/cli)
- [Agent QA source and license](https://github.com/vostride/agent-qa)

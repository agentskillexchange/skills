---
name: "Playwright Test Recorder"
description: "Playwright Test Recorder is built around Playwright browser automation framework. The underlying ecosystem is represented by microsoft/playwright (84,874+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like browser contexts, locators, page actions, tracing, screenshots, test runner and preserving […]"
category: "Code Quality & Review"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/playwright-test-recorder/"
---
# Playwright Test Recorder

Playwright Test Recorder is built around Playwright browser automation framework. The underlying ecosystem is represented by microsoft/playwright (84,874+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like browser contexts, locators, page actions, tracing, screenshots, test runner and preserving […]

## Overview

Playwright Test Recorder is built around Playwright browser automation framework. The underlying ecosystem is represented by `microsoft/playwright` (84,874+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like browser contexts, locators, page actions, tracing, screenshots, test runner and preserving the operational context that matters for real tasks.

For testing and review work, the skill wraps the normal playwright commands into a repeatable analysis loop that can produce summaries, prioritized findings, and CI-friendly output instead of a wall of raw logs. The implementation typically relies on browser contexts, locators, page actions, tracing, screenshots, test runner, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses browser contexts, locators, page actions, tracing, screenshots, test runner instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as web testing, scraping, login automation, and UI validation.

Key integration points include web testing, scraping, login automation, and UI validation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-test-recorder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-test-recorder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-test-recorder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-test-recorder -a codex
```

### OpenClaw

```bash
clawhub install playwright-test-recorder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-test-recorder/)

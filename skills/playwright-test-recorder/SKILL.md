---
title: "Playwright Test Recorder"
description: "Playwright Test Recorder is built around Playwright browser automation framework. The underlying ecosystem is represented by microsoft/playwright (84,874+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like browser contexts, locators, page actions, tracing, screenshots, test runner and preserving the operational context that matters for real tasks.\nFor testing and review work, the skill wraps the normal playwright commands into a repeatable analysis loop that can produce summaries, prioritized findings, and CI-friendly output instead of a wall of raw logs. The implementation typically relies on browser contexts, locators, page actions, tracing, screenshots, test runner, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.\n\nAccesses browser contexts, locators, page actions, tracing, screenshots, test runner instead of scraping a UI, which makes runs easier to audit and retry.\nSupports structured inputs and outputs so another tool, agent, or CI step can consume the result.\nCan be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.\nFits into broader integration points such as web testing, scraping, login automation, and UI validation.\n\n Key integration points include web testing, scraping, login automation, and UI validation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations."
verification: security_reviewed
source: "https://github.com/microsoft/playwright"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86378
  ase_npm_package: "playwright"
  npm_weekly_downloads: 46839239
---

# Playwright Test Recorder

Playwright Test Recorder is built around Playwright browser automation framework. The underlying ecosystem is represented by microsoft/playwright (84,874+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like browser contexts, locators, page actions, tracing, screenshots, test runner and preserving the operational context that matters for real tasks.
For testing and review work, the skill wraps the normal playwright commands into a repeatable analysis loop that can produce summaries, prioritized findings, and CI-friendly output instead of a wall of raw logs. The implementation typically relies on browser contexts, locators, page actions, tracing, screenshots, test runner, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses browser contexts, locators, page actions, tracing, screenshots, test runner instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as web testing, scraping, login automation, and UI validation.

 Key integration points include web testing, scraping, login automation, and UI validation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/playwright-test-recorder
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/playwright-test-recorder` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-test-recorder/)

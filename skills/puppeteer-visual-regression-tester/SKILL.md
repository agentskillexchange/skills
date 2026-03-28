---
name: "Puppeteer Visual Regression Tester"
description: "Automates visual regression testing using Puppeteer page.screenshot() with pixelmatch diffing. Captures full-page screenshots at multiple viewport sizes and generates HTML diff reports with highlighted change regions."
category: "Browser Automation"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
tool_ecosystem:
  tool: puppeteer
  github_stars: 93932
  npm_weekly_downloads: 8696130
  github_repo: puppeteer/puppeteer
  license: Apache-2.0
  maintained: true
---

# Puppeteer Visual Regression Tester

Automates visual regression testing using Puppeteer page.screenshot() with pixelmatch diffing. Captures full-page screenshots at multiple viewport sizes and generates HTML diff reports with highlighted change regions.

## Overview

**Puppeteer Visual Regression Tester** is built around Puppeteer Chrome automation library. The underlying ecosystem is represented by `puppeteer/puppeteer` (93,912+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like page.screenshot, tracing, DevTools protocol, PDF, viewport control and preserving the operational context that matters for real tasks.

For testing and review work, the skill wraps the normal puppeteer commands into a repeatable analysis loop that can produce summaries, prioritized findings, and CI-friendly output instead of a wall of raw logs. The original use case is clear: Automates visual regression testing using Puppeteer page.screenshot() with pixelmatch diffing. Captures full-page screenshots at multiple viewport sizes and generates HTML diff reports with highlighted change regions. The implementation typically relies on page.screenshot, tracing, DevTools protocol, PDF, viewport control, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses page.screenshot, tracing, DevTools protocol, PDF, viewport control instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as browser automation, screenshots, and visual regression testing.

Key integration points include browser automation, screenshots, and visual regression testing. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-visual-regression-tester
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-visual-regression-tester -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-visual-regression-tester -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-visual-regression-tester -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-visual-regression-tester
```

## Source

- Marketplace: https://agentskillexchange.com/skills/puppeteer-visual-regression-tester/

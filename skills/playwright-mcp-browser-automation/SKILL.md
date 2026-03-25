---
name: "Playwright MCP Browser Automation"
description: "Official Playwright-powered browser control for agent workflows."
category: "Browser Automation"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/playwright-mcp-browser-automation/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84938  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Playwright MCP Browser Automation

Official Playwright-powered browser control for agent workflows.

## Overview

**Playwright MCP Browser Automation** is built around Playwright browser automation framework. The underlying ecosystem is represented by `microsoft/playwright` (84,874+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like browser contexts, locators, page actions, tracing, screenshots, test runner and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to playwright so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Official Playwright-powered browser control for agent workflows. The implementation typically relies on browser contexts, locators, page actions, tracing, screenshots, test runner, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses browser contexts, locators, page actions, tracing, screenshots, test runner instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as web testing, scraping, login automation, and UI validation.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include web testing, scraping, login automation, and UI validation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-mcp-browser-automation
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-mcp-browser-automation -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-mcp-browser-automation -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-mcp-browser-automation -a codex
```

### OpenClaw

```bash
clawhub install playwright-mcp-browser-automation
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-mcp-browser-automation/

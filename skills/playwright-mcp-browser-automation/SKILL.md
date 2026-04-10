---
name: Playwright MCP Browser Automation
description: Official Playwright-powered browser control for agent workflows.
verification: security_reviewed
source: https://github.com/microsoft/playwright-mcp
category:
- Browser Automation
framework:
- Claude Code
- Cursor
- MCP
- OpenClaw
tool_ecosystem:
  github_repo: microsoft/playwright-mcp
  github_stars: 30509
  ase_npm_package: '@playwright/mcp'
  npm_weekly_downloads: 3140002
---
# Playwright MCP Browser Automation

Playwright MCP Browser Automation is built around Playwright browser automation framework. The underlying ecosystem is represented by microsoft/playwright (84,874+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like browser contexts, locators, page actions, tracing, screenshots, test runner and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to playwright so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Official Playwright-powered browser control for agent workflows. The implementation typically relies on browser contexts, locators, page actions, tracing, screenshots, test runner, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses browser contexts, locators, page actions, tracing, screenshots, test runner instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as web testing, scraping, login automation, and UI validation.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include web testing, scraping, login automation, and UI validation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-mcp-browser-automation/)

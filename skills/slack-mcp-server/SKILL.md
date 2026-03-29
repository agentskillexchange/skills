---
name: "Slack MCP Server"
description: "Agent access to Slack conversations and workspace workflows."
category: "Calendar, Email & Productivity"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/modelcontextprotocol/servers"
tool_ecosystem:
  tool: slack
  github_stars: 2899
  npm_weekly_downloads: 2433529
  github_repo: slackapi/bolt-js
  license: MIT
  maintained: true
---
# Slack MCP Server

Agent access to Slack conversations and workspace workflows.

## Overview

**Slack MCP Server** is built around Slack messaging and workspace APIs. The underlying ecosystem is represented by `slackapi/bolt-js` (2,900+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like conversations.history, chat.postMessage, users.info, block kit, files and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to slack so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Agent access to Slack conversations and workspace workflows. The implementation typically relies on conversations.history, chat.postMessage, users.info, block kit, files, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses conversations.history, chat.postMessage, users.info, block kit, files instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as chat triage, digests, alerts, and collaborative automation.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include chat triage, digests, alerts, and collaborative automation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install slack-mcp-server
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-mcp-server/)

---
title: "Slack MCP Server"
description: "Agent access to Slack conversations and workspace workflows."
verification: security_reviewed
source: "https://github.com/modelcontextprotocol/servers"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Claude Code"
  - "Cursor"
  - "MCP"
  - "OpenClaw"
tool_ecosystem:
  github_repo: "modelcontextprotocol/servers"
  github_stars: 83947
---

# Slack MCP Server

Slack MCP Server is built around Slack messaging and workspace APIs. The underlying ecosystem is represented by slackapi/bolt-js (2,900+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like conversations.history, chat.postMessage, users.info, block kit, files and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to slack so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Agent access to Slack conversations and workspace workflows. The implementation typically relies on conversations.history, chat.postMessage, users.info, block kit, files, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses conversations.history, chat.postMessage, users.info, block kit, files instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as chat triage, digests, alerts, and collaborative automation.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include chat triage, digests, alerts, and collaborative automation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/slack-mcp-server
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/slack-mcp-server` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-mcp-server/)

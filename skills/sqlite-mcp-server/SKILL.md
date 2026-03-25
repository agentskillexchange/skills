---
name: "SQLite MCP Server"
description: "Lightweight local database access for agent tasks."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sqlite-mcp-server/"
tool_ecosystem:
  tool: "sqlite"
  github_stars: 7043
  npm_weekly_downloads: 4960915
  github_repo: "WiseLibs/better-sqlite3"
  license: "MIT"
  maintained: true
---

# SQLite MCP Server

Lightweight local database access for agent tasks.

## Overview

**SQLite MCP Server** is built around SQLite embedded database. The underlying ecosystem is represented by `WiseLibs/better-sqlite3` (7,041+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like local .db files, SQL queries, schema inspection, FTS, WAL, query plans and preserving the operational context that matters for real tasks.

The skill is especially useful when an agent needs to translate a natural-language request into concrete sqlite-level queries, run them safely, and then explain the result in operational terms rather than returning raw output. The original use case is clear: Lightweight local database access for agent tasks. The implementation typically relies on local .db files, SQL queries, schema inspection, FTS, WAL, query plans, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses local .db files, SQL queries, schema inspection, FTS, WAL, query plans instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as lightweight analytics, app data inspection, and local tooling.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include lightweight analytics, app data inspection, and local tooling. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sqlite-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sqlite-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sqlite-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sqlite-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install sqlite-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sqlite-mcp-server/

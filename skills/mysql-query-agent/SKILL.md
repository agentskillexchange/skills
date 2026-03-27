---
name: "MySQL Query Agent"
description: "MySQL Query Agent is built around MySQL relational database. The underlying ecosystem is represented by sidorares/node-mysql2 (4,348+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SQL queries, INFORMATION_SCHEMA, EXPLAIN, indexes, transactions, replication basics and preserving the operational […]"
category: "Developer Tools"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/mysql-query-agent/"
tool_ecosystem:
  tool: mysql
  github_stars: 4348
  npm_weekly_downloads: 8743089
  github_repo: sidorares/node-mysql2
  license: MIT
  maintained: true
---

# MySQL Query Agent

MySQL Query Agent is built around MySQL relational database. The underlying ecosystem is represented by sidorares/node-mysql2 (4,348+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SQL queries, INFORMATION_SCHEMA, EXPLAIN, indexes, transactions, replication basics and preserving the operational […]

## Overview

**MySQL Query Agent** is built around MySQL relational database. The underlying ecosystem is represented by `sidorares/node-mysql2` (4,348+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SQL queries, INFORMATION_SCHEMA, EXPLAIN, indexes, transactions, replication basics and preserving the operational context that matters for real tasks.

The skill is especially useful when an agent needs to translate a natural-language request into concrete mysql-level queries, run them safely, and then explain the result in operational terms rather than returning raw output. The implementation typically relies on SQL queries, INFORMATION_SCHEMA, EXPLAIN, indexes, transactions, replication basics, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses SQL queries, INFORMATION_SCHEMA, EXPLAIN, indexes, transactions, replication basics instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as application data access, diagnostics, and reporting queries.

Key integration points include application data access, diagnostics, and reporting queries. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mysql-query-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mysql-query-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mysql-query-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mysql-query-agent -a codex
```

### OpenClaw

```bash
clawhub install mysql-query-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/mysql-query-agent/

---
name: "Notion Database Sync & Page Generator"
description: "Reads from and writes to Notion databases using the official Notion API v1, supporting filtered queries, property mapping, and bulk page creation from structured JSON input. Resolves relation and rollup properties automatically when generating linked records."
category: "Integrations &amp; Connectors"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/makenotion/notion-sdk-js"
tool_ecosystem:
  tool: notion
  github_repo: makenotion/notion-sdk-js
  github_stars: 5566
  license: MIT
  maintained: true
---
# Notion Database Sync & Page Generator

Reads from and writes to Notion databases using the official Notion API v1, supporting filtered queries, property mapping, and bulk page creation from structured JSON input. Resolves relation and rollup properties automatically when generating linked records.

## Overview

Notion Database Sync & Page Generator is built around Notion workspace and database platform. The underlying ecosystem is represented by makenotion/notion-sdk-js (5,562+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like pages, databases.query, blocks.children, properties, relations, pagination and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to notion so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Reads from and writes to Notion databases using the official Notion API v1, supporting filtered queries, property mapping, and bulk page creation from structured JSON input. Resolves relation and rollup properties automatically when generating linked records. The implementation typically relies on pages, databases.query, blocks.children, properties, relations, pagination, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses pages, databases.query, blocks.children, properties, relations, pagination instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as knowledge bases, task tracking, content sync, and structured note workflows.

For generator-style use cases, the skill turns a vague request into repeatable scaffolding with defaults that match the upstream toolchain rather than inventing ad hoc files. Key integration points include knowledge bases, task tracking, content sync, and structured note workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill notion-database-sync-page-generator-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill notion-database-sync-page-generator-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill notion-database-sync-page-generator-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill notion-database-sync-page-generator-2 -a codex
```

### OpenClaw

```bash
clawhub install notion-database-sync-page-generator-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-database-sync-page-generator-2/)

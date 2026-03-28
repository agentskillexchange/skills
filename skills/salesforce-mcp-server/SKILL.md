---
name: "Salesforce MCP Server"
description: "Salesforce MCP Server is built around Salesforce CRM platform. The underlying ecosystem is represented by jsforce/jsforce (1,452+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SOQL, REST API, objects, workflows, envelopes, records, sync and preserving the operational […]"
category: "Integrations & Connectors"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/jsforce/jsforce"
tool_ecosystem:
  tool: salesforce
  github_stars: 1452
  npm_weekly_downloads: 804753
  github_repo: jsforce/jsforce
  license: MIT
  maintained: true
---

# Salesforce MCP Server

Salesforce MCP Server is built around Salesforce CRM platform. The underlying ecosystem is represented by jsforce/jsforce (1,452+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SOQL, REST API, objects, workflows, envelopes, records, sync and preserving the operational […]

## Overview

**Salesforce MCP Server** is built around Salesforce CRM platform. The underlying ecosystem is represented by `jsforce/jsforce` (1,452+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SOQL, REST API, objects, workflows, envelopes, records, sync and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to salesforce so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on SOQL, REST API, objects, workflows, envelopes, records, sync, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses SOQL, REST API, objects, workflows, envelopes, records, sync instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as CRM integration, contract routing, and sales operations automation.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include CRM integration, contract routing, and sales operations automation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill salesforce-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill salesforce-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill salesforce-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill salesforce-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install salesforce-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/salesforce-mcp-server/

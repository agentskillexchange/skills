---
name: "HubSpot MCP Server"
description: "HubSpot MCP Server is built around HubSpot CRM and marketing APIs. The underlying ecosystem is represented by HubSpot/hubspot-api-nodejs (391+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like contacts, companies, deals, forms, workflows, search API, associations and preserving […]"
category: "Integrations & Connectors"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/HubSpot/hubspot-api-nodejs"
tool_ecosystem:
  github_repo: "HubSpot/hubspot-api-nodejs"
  github_stars: 392
  npm_package: "@hubspot/api-client"
---
# HubSpot MCP Server

HubSpot MCP Server is built around HubSpot CRM and marketing APIs. The underlying ecosystem is represented by HubSpot/hubspot-api-nodejs (391+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like contacts, companies, deals, forms, workflows, search API, associations and preserving […]

HubSpot MCP Server is built around HubSpot CRM and marketing APIs. The underlying ecosystem is represented by HubSpot/hubspot-api-nodejs (391+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like contacts, companies, deals, forms, workflows, search API, associations and preserving the operational context that matters for real tasks.



In practice, the skill gives an agent a stable interface to hubspot so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on contacts, companies, deals, forms, workflows, search API, associations, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.



- Accesses contacts, companies, deals, forms, workflows, search API, associations instead of scraping a UI, which makes runs easier to audit and retry.



- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.



- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.



- Fits into broader integration points such as sales automation, CRM sync, lead enrichment, and lifecycle tracking.



Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include sales automation, CRM sync, lead enrichment, and lifecycle tracking. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill hubspot-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill hubspot-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill hubspot-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill hubspot-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install hubspot-mcp-server
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hubspot-mcp-server/)

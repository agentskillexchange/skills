---
name: "OpsGenie MCP Server"
description: "OpsGenie MCP Server is built around Opsgenie incident and on-call platform. The underlying ecosystem is represented by opsgenie/opsgenie-nodejs-sdk (24+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like alerts, schedules, teams, escalation policies, notes, integrations and preserving the […]"
category: "Monitoring & Alerts"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/opsgenie-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "opsgenie"  # from ase_tool_match
  github_stars: 24  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9107  # from ase_npm_downloads
  github_repo: "opsgenie/opsgenie-nodejs-sdk"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# OpsGenie MCP Server

OpsGenie MCP Server is built around Opsgenie incident and on-call platform. The underlying ecosystem is represented by opsgenie/opsgenie-nodejs-sdk (24+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like alerts, schedules, teams, escalation policies, notes, integrations and preserving the […]

## Overview

**OpsGenie MCP Server** is built around Opsgenie incident and on-call platform. The underlying ecosystem is represented by `opsgenie/opsgenie-nodejs-sdk` (24+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like alerts, schedules, teams, escalation policies, notes, integrations and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to opsgenie so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on alerts, schedules, teams, escalation policies, notes, integrations, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses alerts, schedules, teams, escalation policies, notes, integrations instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as alert triage, on-call auditing, and incident coordination.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include alert triage, on-call auditing, and incident coordination. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill opsgenie-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill opsgenie-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill opsgenie-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill opsgenie-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install opsgenie-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/opsgenie-mcp-server/

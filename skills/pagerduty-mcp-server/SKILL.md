---
name: "PagerDuty MCP Server"
description: "PagerDuty MCP Server is built around PagerDuty incident response platform. The underlying ecosystem is represented by PagerDuty/pdjs (69+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like incidents, escalation policies, schedules, services, responders, analytics and preserving the operational […]"
category: "Monitoring & Alerts"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pagerduty-mcp-server/"
---
# PagerDuty MCP Server

PagerDuty MCP Server is built around PagerDuty incident response platform. The underlying ecosystem is represented by PagerDuty/pdjs (69+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like incidents, escalation policies, schedules, services, responders, analytics and preserving the operational […]

## Overview

PagerDuty MCP Server is built around PagerDuty incident response platform. The underlying ecosystem is represented by `PagerDuty/pdjs` (69+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like incidents, escalation policies, schedules, services, responders, analytics and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to pagerduty so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on incidents, escalation policies, schedules, services, responders, analytics, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses incidents, escalation policies, schedules, services, responders, analytics instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as on-call checks, incident routing, and response coordination.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include on-call checks, incident routing, and response coordination. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pagerduty-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagerduty-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagerduty-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install pagerduty-mcp-server
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-mcp-server/)

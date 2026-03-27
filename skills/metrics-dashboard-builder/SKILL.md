---
name: "Metrics Dashboard Builder"
description: "Metrics Dashboard Builder is built around Datadog observability platform. The underlying ecosystem is represented by DataDog/dd-trace-js (787+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like metrics API, monitors, logs, dashboards, traces, incidents and preserving the operational context […]"
category: "Monitoring & Alerts"
framework: "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/metrics-dashboard-builder/"
tool_ecosystem:
  tool: datadog
  github_stars: 789
  npm_weekly_downloads: 6043057
  github_repo: DataDog/dd-trace-js
  maintained: true
---

# Metrics Dashboard Builder

Metrics Dashboard Builder is built around Datadog observability platform. The underlying ecosystem is represented by DataDog/dd-trace-js (787+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like metrics API, monitors, logs, dashboards, traces, incidents and preserving the operational context […]

## Overview

**Metrics Dashboard Builder** is built around Datadog observability platform. The underlying ecosystem is represented by `DataDog/dd-trace-js` (787+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like metrics API, monitors, logs, dashboards, traces, incidents and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to datadog so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on metrics API, monitors, logs, dashboards, traces, incidents, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses metrics API, monitors, logs, dashboards, traces, incidents instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as incident response, APM, alerting, and operational dashboards.

For generator-style use cases, the skill turns a vague request into repeatable scaffolding with defaults that match the upstream toolchain rather than inventing ad hoc files. Key integration points include incident response, APM, alerting, and operational dashboards. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill metrics-dashboard-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill metrics-dashboard-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill metrics-dashboard-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill metrics-dashboard-builder -a codex
```

### OpenClaw

```bash
clawhub install metrics-dashboard-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/metrics-dashboard-builder/

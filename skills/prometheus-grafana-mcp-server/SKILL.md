---
title: "Prometheus / Grafana MCP Server"
description: "Prometheus / Grafana MCP Server is built around Grafana visualization and alerting platform. The underlying ecosystem is represented by grafana/grafana (72,784+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like dashboards API, panels, Loki/Prometheus datasources, alerting, rendered images […]"
verification: "security_reviewed"
source: "https://github.com/grafana/grafana"
category:
  - "Monitoring & Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73414
---

# Prometheus / Grafana MCP Server

Prometheus / Grafana MCP Server is built around Grafana visualization and alerting platform. The underlying ecosystem is represented by grafana/grafana (72,784+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like dashboards API, panels, Loki/Prometheus datasources, alerting, rendered images and preserving the operational context that matters for real tasks. In practice, the skill gives an agent a stable interface to grafana so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on dashboards API, panels, Loki/Prometheus datasources, alerting, rendered images, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform. Accesses dashboards API, panels, Loki/Prometheus datasources, alerting, rendered images instead of scraping a UI, which makes runs easier to audit and retry. Supports structured inputs and outputs so another tool, agent, or CI step can consume the result. Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format. Fits into broader integration points such as metrics dashboards, alert routing, and observability investigations. Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include metrics dashboards, alert routing, and observability investigations. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prometheus-grafana-mcp-server/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-grafana-mcp-server
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prometheus-grafana-mcp-server`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-grafana-mcp-server/)

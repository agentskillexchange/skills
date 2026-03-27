---
name: "Loki Log Query Agent"
description: "Loki Log Query Agent is built around Grafana Loki log aggregation system. The underlying ecosystem is represented by grafana/loki (27,858+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like LogQL, labels, streams, tailing, retention, query frontend and preserving […]"
category: "Monitoring & Alerts"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/loki-log-query-agent/"
tool_ecosystem:
  tool: loki
  github_stars: 27858
  github_repo: grafana/loki
  license: AGPL-3.0
  maintained: true
---

# Loki Log Query Agent

Loki Log Query Agent is built around Grafana Loki log aggregation system. The underlying ecosystem is represented by grafana/loki (27,858+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like LogQL, labels, streams, tailing, retention, query frontend and preserving […]

## Overview

**Loki Log Query Agent** is built around Grafana Loki log aggregation system. The underlying ecosystem is represented by `grafana/loki` (27,858+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like LogQL, labels, streams, tailing, retention, query frontend and preserving the operational context that matters for real tasks.

The skill is especially useful when an agent needs to translate a natural-language request into concrete loki-level queries, run them safely, and then explain the result in operational terms rather than returning raw output. The implementation typically relies on LogQL, labels, streams, tailing, retention, query frontend, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses LogQL, labels, streams, tailing, retention, query frontend instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as log search, correlation with metrics, and troubleshooting workflows.

Key integration points include log search, correlation with metrics, and troubleshooting workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill loki-log-query-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill loki-log-query-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill loki-log-query-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill loki-log-query-agent -a codex
```

### OpenClaw

```bash
clawhub install loki-log-query-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/loki-log-query-agent/

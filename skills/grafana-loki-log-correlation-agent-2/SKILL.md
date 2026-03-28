---
name: "Grafana Loki Log Correlation Agent"
description: "Queries Grafana Loki via the LogQL API to correlate log streams across services. Builds cross-service trace-to-log mappings using Tempo integration and generates alert rule suggestions."
category: "Monitoring & Alerts"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://github.com/grafana/loki"
tool_ecosystem:
  tool: loki
  github_stars: 27858
  github_repo: grafana/loki
  license: AGPL-3.0
  maintained: true
---

# Grafana Loki Log Correlation Agent

Queries Grafana Loki via the LogQL API to correlate log streams across services. Builds cross-service trace-to-log mappings using Tempo integration and generates alert rule suggestions.

## Overview

The Grafana Loki Log Correlation Agent skill queries distributed log data through the Loki HTTP API using LogQL expressions. It performs multi-stream correlation by joining log lines across services using shared trace IDs, request IDs, and timestamp windows. The skill leverages the Loki Series API to discover active label combinations and builds LogQL pipeline expressions with line_format, json, and regexp parsers for structured field extraction. It integrates with the Grafana Tempo API to create trace-to-log links, enabling seamless navigation between distributed traces and corresponding log entries. The agent analyzes log volume patterns using the Loki Stats API to identify unusual error rate spikes, generates Grafana alerting rule YAML for Cortex/Mimir ruler compatible alert definitions, and configures recording rules for frequently queried aggregations. Output includes correlated log summaries, suggested dashboard panels in JSON format, and LogQL query templates for common debugging scenarios.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-loki-log-correlation-agent-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-loki-log-correlation-agent-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-loki-log-correlation-agent-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-loki-log-correlation-agent-2 -a codex
```

### OpenClaw

```bash
clawhub install grafana-loki-log-correlation-agent-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/grafana-loki-log-correlation-agent-2/

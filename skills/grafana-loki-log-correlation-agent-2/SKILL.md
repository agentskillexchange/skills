---
title: "Grafana Loki Log Correlation Agent"
description: "Queries Grafana Loki via the LogQL API to correlate log streams across services. Builds cross-service trace-to-log mappings using Tempo integration and generates alert rule suggestions."
verification: "security_reviewed"
source: "https://github.com/grafana/loki"
category:
  - "Monitoring & Alerts"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "grafana/loki"
  github_stars: 27993
---

# Grafana Loki Log Correlation Agent

The Grafana Loki Log Correlation Agent skill queries distributed log data through the Loki HTTP API using LogQL expressions. It performs multi-stream correlation by joining log lines across services using shared trace IDs, request IDs, and timestamp windows. The skill leverages the Loki Series API to discover active label combinations and builds LogQL pipeline expressions with line_format, json, and regexp parsers for structured field extraction. It integrates with the Grafana Tempo API to create trace-to-log links, enabling seamless navigation between distributed traces and corresponding log entries. The agent analyzes log volume patterns using the Loki Stats API to identify unusual error rate spikes, generates Grafana alerting rule YAML for Cortex/Mimir ruler compatible alert definitions, and configures recording rules for frequently queried aggregations. Output includes correlated log summaries, suggested dashboard panels in JSON format, and LogQL query templates for common debugging scenarios.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/grafana-loki-log-correlation-agent-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grafana-loki-log-correlation-agent-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/grafana-loki-log-correlation-agent-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-correlation-agent-2/)

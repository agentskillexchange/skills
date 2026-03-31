---
name: "Grafana Loki Log Query Agent"
description: "Queries Grafana Loki log aggregation system using LogQL via the Loki HTTP API. Filters log streams by labels, parses structured JSON logs, and correlates log entries with Grafana dashboard panels."
category: "Monitoring &amp; Alerts"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/grafana/grafana"
tool_ecosystem:
  tool: grafana
  github_repo: grafana/grafana
  github_stars: 72840
  license: AGPL-3.0
  maintained: true
---
# Grafana Loki Log Query Agent

Queries Grafana Loki log aggregation system using LogQL via the Loki HTTP API. Filters log streams by labels, parses structured JSON logs, and correlates log entries with Grafana dashboard panels.

## Overview

The Grafana Loki Log Query Agent skill enables Claude to search and analyze logs stored in Grafana Loki through its HTTP API. It constructs LogQL queries from natural language descriptions, handling both log stream selectors and log pipeline stages for filtering, parsing, and formatting.

The skill supports label-based stream selection ({job="api-server", level="error"}), line filter expressions for text matching, and parser stages for extracting structured fields from JSON, logfmt, and regex-patterned logs. It handles the Loki query range endpoint with configurable time windows and result limits.

For incident investigation, the skill correlates log entries with Grafana dashboard panels by querying the Grafana API for dashboard JSON models and matching datasource references. This lets Claude explain which logs correspond to which visual anomalies on dashboards.

Rate and volume queries using LogQL metric expressions (rate, count_over_time, bytes_over_time) enable log-based alerting analysis without Prometheus. The skill manages Loki's query timeout and chunk limits, splitting large time ranges into smaller windows for reliable retrieval. Authentication supports both API key and OAuth token methods. Built for DevOps teams running the Grafana/Loki/Promtail stack.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-loki-log-query-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-loki-log-query-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-loki-log-query-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-loki-log-query-agent -a codex
```

### OpenClaw

```bash
clawhub install grafana-loki-log-query-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-query-agent/)

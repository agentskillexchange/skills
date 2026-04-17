---
title: "Grafana Loki Log Query Agent"
description: "Queries Grafana Loki log aggregation system using LogQL via the Loki HTTP API. Filters log streams by labels, parses structured JSON logs, and correlates log entries with Grafana dashboard panels."
verification: security_reviewed
source: "https://github.com/grafana/loki"
category:
  - "Monitoring & Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "grafana/loki"
  github_stars: 27993
  license: "AGPL-3.0"
---

# Grafana Loki Log Query Agent

The Grafana Loki Log Query Agent skill enables Claude to search and analyze logs stored in Grafana Loki through its HTTP API. It constructs LogQL queries from natural language descriptions, handling both log stream selectors and log pipeline stages for filtering, parsing, and formatting.

The skill supports label-based stream selection ({job=”api-server”, level=”error”}), line filter expressions for text matching, and parser stages for extracting structured fields from JSON, logfmt, and regex-patterned logs. It handles the Loki query range endpoint with configurable time windows and result limits.

For incident investigation, the skill correlates log entries with Grafana dashboard panels by querying the Grafana API for dashboard JSON models and matching datasource references. This lets Claude explain which logs correspond to which visual anomalies on dashboards.

Rate and volume queries using LogQL metric expressions (rate, count_over_time, bytes_over_time) enable log-based alerting analysis without Prometheus. The skill manages Loki’s query timeout and chunk limits, splitting large time ranges into smaller windows for reliable retrieval. Authentication supports both API key and OAuth token methods. Built for DevOps teams running the Grafana/Loki/Promtail stack.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grafana-loki-log-query-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/grafana-loki-log-query-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-query-agent/)

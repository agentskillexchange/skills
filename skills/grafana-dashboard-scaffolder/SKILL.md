---
title: "Grafana Dashboard Scaffolder"
description: "Generates Grafana dashboard JSON using the Grafana HTTP API /api/dashboards/db endpoint. Creates panels with Prometheus, InfluxDB, and Elasticsearch datasource queries pre-configured for common infrastructure metrics."
verification: "security_reviewed"
source: "https://github.com/grafana/grafana"
category:
  - "Monitoring & Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Dashboard Scaffolder

The Grafana Dashboard Scaffolder skill generates complete Grafana dashboard definitions as JSON and deploys them via the Grafana HTTP API. Dashboards are created through POST /api/dashboards/db with the full dashboard model including panels, variables, and annotations. The skill generates panel configurations for all major visualization types: time series, stat, gauge, table, heatmap, and logs panels. Each panel includes pre-built queries for common datasources: Prometheus with PromQL using rate and histogram_quantile, InfluxDB with Flux queries using range filter and aggregateWindow, and Elasticsearch with Lucene query syntax and date histogram aggregations. Template variables are generated using datasource query for label_values and query_result variable types enabling dynamic dashboard filtering. Row-based layouts organize panels into collapsible sections for CPU, memory, disk, network, and application-specific metrics. The skill queries /api/datasources to auto-discover available datasources and match them to appropriate panel queries. Alert rules are embedded in panels using Grafana unified alerting format with configurable evaluation intervals. Dashboard versioning uses the versions endpoint for safe rollback. Folder organization via /api/folders keeps generated dashboards categorized by service or team.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/grafana-dashboard-scaffolder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grafana-dashboard-scaffolder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/grafana-dashboard-scaffolder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-scaffolder/)

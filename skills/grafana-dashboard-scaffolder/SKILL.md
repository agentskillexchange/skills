---
name: "Grafana Dashboard Scaffolder"
description: "Generates Grafana dashboard JSON using the Grafana HTTP API /api/dashboards/db endpoint. Creates panels with Prometheus, InfluxDB, and Elasticsearch datasource queries pre-configured for common infrastructure metrics."
category: "Monitoring & Alerts"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/grafana/grafana"
tool_ecosystem:
  tool: grafana
  github_stars: 72796
  github_repo: grafana/grafana
  license: AGPL-3.0
  maintained: true
---

# Grafana Dashboard Scaffolder

Generates Grafana dashboard JSON using the Grafana HTTP API /api/dashboards/db endpoint. Creates panels with Prometheus, InfluxDB, and Elasticsearch datasource queries pre-configured for common infrastructure metrics.

## Overview

The Grafana Dashboard Scaffolder skill generates complete Grafana dashboard definitions as JSON and deploys them via the Grafana HTTP API. Dashboards are created through POST /api/dashboards/db with the full dashboard model including panels, variables, and annotations. The skill generates panel configurations for all major visualization types: time series, stat, gauge, table, heatmap, and logs panels. Each panel includes pre-built queries for common datasources: Prometheus with PromQL using rate and histogram_quantile, InfluxDB with Flux queries using range filter and aggregateWindow, and Elasticsearch with Lucene query syntax and date histogram aggregations. Template variables are generated using datasource query for label_values and query_result variable types enabling dynamic dashboard filtering. Row-based layouts organize panels into collapsible sections for CPU, memory, disk, network, and application-specific metrics. The skill queries /api/datasources to auto-discover available datasources and match them to appropriate panel queries. Alert rules are embedded in panels using Grafana unified alerting format with configurable evaluation intervals. Dashboard versioning uses the versions endpoint for safe rollback. Folder organization via /api/folders keeps generated dashboards categorized by service or team.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-scaffolder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-scaffolder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-scaffolder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-scaffolder -a codex
```

### OpenClaw

```bash
clawhub install grafana-dashboard-scaffolder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/grafana-dashboard-scaffolder/

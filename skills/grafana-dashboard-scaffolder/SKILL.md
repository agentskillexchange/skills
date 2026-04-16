---
title: "Grafana Dashboard Scaffolder"
description: "Generates Grafana dashboard JSON using the Grafana HTTP API /api/dashboards/db endpoint. Creates panels with Prometheus, InfluxDB, and Elasticsearch datasource queries pre-configured for common infrastructure metrics."
verification: "security_reviewed"
source: "https://github.com/grafana/grafana"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
  license: "AGPL-3.0"
---

# Grafana Dashboard Scaffolder

The Grafana Dashboard Scaffolder skill generates complete Grafana dashboard definitions as JSON and deploys them via the Grafana HTTP API. Dashboards are created through POST /api/dashboards/db with the full dashboard model including panels, variables, and annotations. The skill generates panel configurations for all major visualization types: time series, stat, gauge, table, heatmap, and logs panels. Each panel includes pre-built queries for common datasources: Prometheus with PromQL using rate and histogram_quantile, InfluxDB with Flux queries using range filter and aggregateWindow, and Elasticsearch with Lucene query syntax and date histogram aggregations. Template variables are generated using datasource query for label_values and query_result variable types enabling dynamic dashboard filtering. Row-based layouts organize panels into collapsible sections for CPU, memory, disk, network, and application-specific metrics. The skill queries /api/datasources to auto-discover available datasources and match them to appropriate panel queries. Alert rules are embedded in panels using Grafana unified alerting format with configurable evaluation intervals. Dashboard versioning uses the versions endpoint for safe rollback. Folder organization via /api/folders keeps generated dashboards categorized by service or team.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-scaffolder/)

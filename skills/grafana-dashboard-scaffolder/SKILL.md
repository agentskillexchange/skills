---
title: Grafana Dashboard Scaffolder
description: 'The Grafana Dashboard Scaffolder skill generates complete Grafana dashboard
  definitions as JSON and deploys them via the Grafana HTTP API. Dashboards are created
  through POST /api/dashboards/db with the full dashboard model including panels,
  variables, and annotations. The skill generates panel configurations for all major
  visualization types: time series, stat, gauge, table, heatmap, and logs panels.
  Each panel includes pre-built queries for common datasources: Prometheus with PromQL
  using rate and histogram_quantile, InfluxDB with Flux queries using range filter
  and aggregateWindow, and Elasticsearch with Lucene query syntax and date histogram
  aggregations. Template variables are generated using datasource query for label_values
  and query_result variable types enabling dynamic dashboard filtering. Row-based
  layouts organize panels into collapsible sections for CPU, memory, disk, network,
  and application-specific metrics. The skill queries /api/datasources to auto-discover
  available datasources and match them to appropriate panel queries. Alert rules are
  embedded in panels using Grafana unified alerting format with configurable evaluation
  intervals. Dashboard versioning uses the versions endpoint for safe rollback. Folder
  organization via /api/folders keeps generated dashboards categorized by service
  or team.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/grafana-dashboard-scaffolder/
category:
- Monitoring &amp; Alerts
framework:
- Cursor
---

# Grafana Dashboard Scaffolder

The Grafana Dashboard Scaffolder skill generates complete Grafana dashboard definitions as JSON and deploys them via the Grafana HTTP API. Dashboards are created through POST /api/dashboards/db with the full dashboard model including panels, variables, and annotations. The skill generates panel configurations for all major visualization types: time series, stat, gauge, table, heatmap, and logs panels. Each panel includes pre-built queries for common datasources: Prometheus with PromQL using rate and histogram_quantile, InfluxDB with Flux queries using range filter and aggregateWindow, and Elasticsearch with Lucene query syntax and date histogram aggregations. Template variables are generated using datasource query for label_values and query_result variable types enabling dynamic dashboard filtering. Row-based layouts organize panels into collapsible sections for CPU, memory, disk, network, and application-specific metrics. The skill queries /api/datasources to auto-discover available datasources and match them to appropriate panel queries. Alert rules are embedded in panels using Grafana unified alerting format with configurable evaluation intervals. Dashboard versioning uses the versions endpoint for safe rollback. Folder organization via /api/folders keeps generated dashboards categorized by service or team.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-scaffolder/)

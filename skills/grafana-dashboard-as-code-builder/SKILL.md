---
title: "Grafana Dashboard as Code Builder"
description: "Builds Grafana dashboards programmatically using grafonnet-lib (Jsonnet) and the Grafana HTTP API. Generates panel JSON for time series, stat, table, and heatmap visualizations with PromQL/LogQL queries."
verification: "security_reviewed"
source: "https://github.com/grafana/grafana"
category:
  - "Monitoring & Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Dashboard as Code Builder

The Grafana Dashboard as Code Builder skill creates Grafana dashboards programmatically using grafonnet-lib Jsonnet library and the Grafana HTTP API for provisioning. It generates panel definitions for time series visualizations with PromQL queries and legend formatting, stat panels with value mappings and threshold coloring, table panels with field override configurations, and heatmap panels for distribution visualization using histogram_quantile expressions. The skill produces complete dashboard JSON models with template variable definitions (query, custom, datasource types), annotation configurations for deployment event overlay from GitHub webhook data, and row-based panel organization with collapse state management. It generates grafonnet Jsonnet code using grafana.dashboard.new(), grafana.graphPanel.new(), and grafana.template.datasource() functions for version-controlled dashboard definitions. Advanced features include Grafana provisioning YAML for dashboards-as-code file-based loading, library panel creation for cross-dashboard component reuse via the Library Elements API, and alert rule migration from legacy dashboard alerts to Grafana Unified Alerting with folder-based rule group organization. The skill configures data source provisioning for Prometheus, Loki, Tempo, and Elasticsearch with proper authentication and TLS settings, and generates Grafana Terraform provider resources using grafana_dashboard and grafana_folder for infrastructure-as-code deployment.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/grafana-dashboard-as-code-builder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grafana-dashboard-as-code-builder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/grafana-dashboard-as-code-builder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-as-code-builder/)

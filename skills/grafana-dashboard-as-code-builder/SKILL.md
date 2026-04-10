---
title: "Grafana Dashboard as Code Builder"
description: "Builds Grafana dashboards programmatically using grafonnet-lib (Jsonnet) and the Grafana HTTP API. Generates panel JSON for time series, stat, table, and heatmap visualizations with PromQL/LogQL queries."
slug: "grafana-dashboard-as-code-builder"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/grafana-dashboard-as-code-builder/"
---

# Grafana Dashboard as Code Builder

Builds Grafana dashboards programmatically using grafonnet-lib (Jsonnet) and the Grafana HTTP API. Generates panel JSON for time series, stat, table, and heatmap visualizations with PromQL/LogQL queries.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install grafana-dashboard-as-code-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Grafana Dashboard as Code Builder skill creates Grafana dashboards programmatically using grafonnet-lib Jsonnet library and the Grafana HTTP API for provisioning. It generates panel definitions for time series visualizations with PromQL queries and legend formatting, stat panels with value mappings and threshold coloring, table panels with field override configurations, and heatmap panels for distribution visualization using histogram_quantile expressions.
The skill produces complete dashboard JSON models with template variable definitions (query, custom, datasource types), annotation configurations for deployment event overlay from GitHub webhook data, and row-based panel organization with collapse state management. It generates grafonnet Jsonnet code using grafana.dashboard.new(), grafana.graphPanel.new(), and grafana.template.datasource() functions for version-controlled dashboard definitions.
Advanced features include Grafana provisioning YAML for dashboards-as-code file-based loading, library panel creation for cross-dashboard component reuse via the Library Elements API, and alert rule migration from legacy dashboard alerts to Grafana Unified Alerting with folder-based rule group organization. The skill configures data source provisioning for Prometheus, Loki, Tempo, and Elasticsearch with proper authentication and TLS settings, and generates Grafana Terraform provider resources using grafana_dashboard and grafana_folder for infrastructure-as-code deployment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-as-code-builder/)

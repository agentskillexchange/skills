---
title: "Grafana Dashboard JSON Assembler"
description: "Assembles Grafana dashboard JSON models using panel types like timeseries, stat, table, and heatmap. Configures datasource references, template variables, and annotation queries for operational dashboards."
slug: "grafana-dashboard-json-assembler"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/grafana-dashboard-json-assembler/"
---

# Grafana Dashboard JSON Assembler

Assembles Grafana dashboard JSON models using panel types like timeseries, stat, table, and heatmap. Configures datasource references, template variables, and annotation queries for operational dashboards.

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
clawhub install grafana-dashboard-json-assembler
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Grafana Dashboard JSON Assembler constructs complete dashboard models following the Grafana JSON schema specification. It generates panel configurations for all major visualization types including timeseries with multiple y-axes, stat panels with value mappings and thresholds, table panels with field overrides and column filtering, and heatmap panels with bucket aggregation. The skill handles datasource provisioning references using UID-based selectors compatible with Grafana provisioning workflows. Template variables are configured with proper query types—label_values for Prometheus, tag queries for InfluxDB, and dimension values for CloudWatch. Row-based layouts use gridPos calculations for responsive panel positioning. Annotation queries overlay deployment events and alert state changes on time-series panels. The assembler supports library panel references for reusable components, dashboard links for drill-down navigation, and JSON-based provisioning compatible with Kubernetes ConfigMap mounting.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-json-assembler/)

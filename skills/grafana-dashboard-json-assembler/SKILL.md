---
title: "Grafana Dashboard JSON Assembler"
description: "The Grafana Dashboard JSON Assembler constructs complete dashboard models following the Grafana JSON schema specification. It generates panel configurations for all major visualization types including timeseries with multiple y-axes, stat panels with value mappings and thresholds, table panels with field overrides and column filtering, and heatmap panels with bucket aggregation. The skill handles datasource provisioning references using UID-based selectors compatible with Grafana provisioning workflows. Template variables are configured with proper query types—label_values for Prometheus, tag queries for InfluxDB, and dimension values for CloudWatch. Row-based layouts use gridPos calculations for responsive panel positioning. Annotation queries overlay deployment events and alert state changes on time-series panels. The assembler supports library panel references for reusable components, dashboard links for drill-down navigation, and JSON-based provisioning compatible with Kubernetes ConfigMap mounting."
source: "https://github.com/grafana/grafana"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Dashboard JSON Assembler

The Grafana Dashboard JSON Assembler constructs complete dashboard models following the Grafana JSON schema specification. It generates panel configurations for all major visualization types including timeseries with multiple y-axes, stat panels with value mappings and thresholds, table panels with field overrides and column filtering, and heatmap panels with bucket aggregation. The skill handles datasource provisioning references using UID-based selectors compatible with Grafana provisioning workflows. Template variables are configured with proper query types—label_values for Prometheus, tag queries for InfluxDB, and dimension values for CloudWatch. Row-based layouts use gridPos calculations for responsive panel positioning. Annotation queries overlay deployment events and alert state changes on time-series panels. The assembler supports library panel references for reusable components, dashboard links for drill-down navigation, and JSON-based provisioning compatible with Kubernetes ConfigMap mounting.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-json-assembler/)

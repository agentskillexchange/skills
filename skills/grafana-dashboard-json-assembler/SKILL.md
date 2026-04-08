---
title: Grafana Dashboard JSON Assembler
description: The Grafana Dashboard JSON Assembler constructs complete dashboard models
  following the Grafana JSON schema specification. It generates panel configurations
  for all major visualization types including timeseries with multiple y-axes, stat
  panels with value mappings and thresholds, table panels with field overrides and
  column filtering, and heatmap panels with bucket aggregation. The skill handles
  datasource provisioning references using UID-based selectors compatible with Grafana
  provisioning workflows. Template variables are configured with proper query types—label_values
  for Prometheus, tag queries for InfluxDB, and dimension values for CloudWatch. Row-based
  layouts use gridPos calculations for responsive panel positioning. Annotation queries
  overlay deployment events and alert state changes on time-series panels. The assembler
  supports library panel references for reusable components, dashboard links for drill-down
  navigation, and JSON-based provisioning compatible with Kubernetes ConfigMap mounting.
verification: security_reviewed
source: https://agentskillexchange.com/skills/grafana-dashboard-json-assembler/
category:
- Monitoring &amp; Alerts
framework:
- Cursor
---

# Grafana Dashboard JSON Assembler

The Grafana Dashboard JSON Assembler constructs complete dashboard models following the Grafana JSON schema specification. It generates panel configurations for all major visualization types including timeseries with multiple y-axes, stat panels with value mappings and thresholds, table panels with field overrides and column filtering, and heatmap panels with bucket aggregation. The skill handles datasource provisioning references using UID-based selectors compatible with Grafana provisioning workflows. Template variables are configured with proper query types—label_values for Prometheus, tag queries for InfluxDB, and dimension values for CloudWatch. Row-based layouts use gridPos calculations for responsive panel positioning. Annotation queries overlay deployment events and alert state changes on time-series panels. The assembler supports library panel references for reusable components, dashboard links for drill-down navigation, and JSON-based provisioning compatible with Kubernetes ConfigMap mounting.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-json-assembler/)

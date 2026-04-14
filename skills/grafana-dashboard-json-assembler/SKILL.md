---
title: "Grafana Dashboard JSON Assembler"
description: "Assembles Grafana dashboard JSON models using panel types like timeseries, stat, table, and heatmap. Configures datasource references, template variables, and annotation queries for operational dashboards."
verification: security_reviewed
source: "https://github.com/grafana/grafana"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-json-assembler/)

---
title: "Grafana Dashboard as Code Generator"
description: "The Grafana Dashboard as Code Generator creates production-quality Grafana dashboards using Grafonnet, the official Jsonnet library for Grafana dashboard generation. It produces version-controlled dashboard definitions that compile to Grafana JSON model format, supporting all panel types including time series, stat, gauge, table, heatmap, and geomap visualizations. The skill interfaces with the Grafana HTTP API for dashboard provisioning, folder management, and datasource configuration. It generates multi-datasource panels combining Prometheus metrics queries, Loki log queries with LogQL, and Tempo trace queries for unified observability dashboards. The generator uses grafana-toolkit for dashboard linting and validation, ensuring compliance with organizational standards for variable naming, panel sizing, and annotation configurations. It supports dashboard templating with Grafana variables for environment, cluster, and service selection, and implements row-level repeating for dynamic dashboard sections. The tool also configures alert rules using Grafana Alerting with proper notification policies and contact point routing."
source: "https://github.com/grafana/grafonnet"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafonnet"
  github_stars: 528
---

# Grafana Dashboard as Code Generator

The Grafana Dashboard as Code Generator creates production-quality Grafana dashboards using Grafonnet, the official Jsonnet library for Grafana dashboard generation. It produces version-controlled dashboard definitions that compile to Grafana JSON model format, supporting all panel types including time series, stat, gauge, table, heatmap, and geomap visualizations. The skill interfaces with the Grafana HTTP API for dashboard provisioning, folder management, and datasource configuration. It generates multi-datasource panels combining Prometheus metrics queries, Loki log queries with LogQL, and Tempo trace queries for unified observability dashboards. The generator uses grafana-toolkit for dashboard linting and validation, ensuring compliance with organizational standards for variable naming, panel sizing, and annotation configurations. It supports dashboard templating with Grafana variables for environment, cluster, and service selection, and implements row-level repeating for dynamic dashboard sections. The tool also configures alert rules using Grafana Alerting with proper notification policies and contact point routing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-as-code-generator/)

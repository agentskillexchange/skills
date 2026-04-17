---
title: "Grafana Dashboard as Code Generator"
description: "The Grafana Dashboard as Code Generator creates production-quality Grafana dashboards using Grafonnet, the official Jsonnet library for Grafana dashboard generation. It produces version-controlled dashboard definitions that compile to Grafana JSON model format, supporting all panel types including time series, stat, gauge, table, heatmap, and geomap visualizations. The skill interfaces with the Grafana HTTP API for dashboard provisioning, folder management, and datasource configuration. It generates multi-datasource panels combining Prometheus metrics queries, Loki log queries with LogQL, and Tempo trace queries for unified observability dashboards. The generator uses grafana-toolkit for dashboard linting and validation, ensuring compliance with organizational standards for variable naming, panel sizing, and annotation configurations. It supports dashboard templating with Grafana variables for environment, cluster, and service selection, and implements row-level repeating for dynamic dashboard sections. The tool also configures alert rules using Grafana Alerting with proper notification policies and contact point routing."
verification: security_reviewed
source: "https://github.com/grafana/grafonnet"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafonnet"
  github_stars: 528
---

# Grafana Dashboard as Code Generator

The Grafana Dashboard as Code Generator creates production-quality Grafana dashboards using Grafonnet, the official Jsonnet library for Grafana dashboard generation. It produces version-controlled dashboard definitions that compile to Grafana JSON model format, supporting all panel types including time series, stat, gauge, table, heatmap, and geomap visualizations. The skill interfaces with the Grafana HTTP API for dashboard provisioning, folder management, and datasource configuration. It generates multi-datasource panels combining Prometheus metrics queries, Loki log queries with LogQL, and Tempo trace queries for unified observability dashboards. The generator uses grafana-toolkit for dashboard linting and validation, ensuring compliance with organizational standards for variable naming, panel sizing, and annotation configurations. It supports dashboard templating with Grafana variables for environment, cluster, and service selection, and implements row-level repeating for dynamic dashboard sections. The tool also configures alert rules using Grafana Alerting with proper notification policies and contact point routing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grafana-dashboard-as-code-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/grafana-dashboard-as-code-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-as-code-generator/)

---
title: "Grafana Dashboard as Code Generator"
description: "Generates Grafana dashboards programmatically using Grafonnet (jsonnet), the Grafana HTTP API, and grafana-toolkit. Supports multi-datasource panels with Prometheus, Loki, and Tempo queries."
verification: "security_reviewed"
source: "https://github.com/grafana/grafonnet"
category:
  - "Monitoring & Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafonnet"
  github_stars: 528
---

# Grafana Dashboard as Code Generator

The Grafana Dashboard as Code Generator creates production-quality Grafana dashboards using Grafonnet, the official Jsonnet library for Grafana dashboard generation. It produces version-controlled dashboard definitions that compile to Grafana JSON model format, supporting all panel types including time series, stat, gauge, table, heatmap, and geomap visualizations. The skill interfaces with the Grafana HTTP API for dashboard provisioning, folder management, and datasource configuration. It generates multi-datasource panels combining Prometheus metrics queries, Loki log queries with LogQL, and Tempo trace queries for unified observability dashboards. The generator uses grafana-toolkit for dashboard linting and validation, ensuring compliance with organizational standards for variable naming, panel sizing, and annotation configurations. It supports dashboard templating with Grafana variables for environment, cluster, and service selection, and implements row-level repeating for dynamic dashboard sections. The tool also configures alert rules using Grafana Alerting with proper notification policies and contact point routing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/grafana-dashboard-as-code-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grafana-dashboard-as-code-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/grafana-dashboard-as-code-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-as-code-generator/)

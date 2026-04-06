---
name: "Grafana Dashboard as Code Generator"
description: "Generates Grafana dashboards programmatically using Grafonnet (jsonnet), the Grafana HTTP API, and grafana-toolkit. Supports multi-datasource panels with Prometheus, Loki, and Tempo queries."
category: "Monitoring &amp; Alerts"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/grafana-dashboard-as-code-generator/"
---
# Grafana Dashboard as Code Generator

Generates Grafana dashboards programmatically using Grafonnet (jsonnet), the Grafana HTTP API, and grafana-toolkit. Supports multi-datasource panels with Prometheus, Loki, and Tempo queries.

The Grafana Dashboard as Code Generator creates production-quality Grafana dashboards using Grafonnet, the official Jsonnet library for Grafana dashboard generation. It produces version-controlled dashboard definitions that compile to Grafana JSON model format, supporting all panel types including time series, stat, gauge, table, heatmap, and geomap visualizations. The skill interfaces with the Grafana HTTP API for dashboard provisioning, folder management, and datasource configuration. It generates multi-datasource panels combining Prometheus metrics queries, Loki log queries with LogQL, and Tempo trace queries for unified observability dashboards. The generator uses grafana-toolkit for dashboard linting and validation, ensuring compliance with organizational standards for variable naming, panel sizing, and annotation configurations. It supports dashboard templating with Grafana variables for environment, cluster, and service selection, and implements row-level repeating for dynamic dashboard sections. The tool also configures alert rules using Grafana Alerting with proper notification policies and contact point routing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-as-code-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-as-code-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-as-code-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-as-code-generator -a codex
```

### OpenClaw

```bash
clawhub install grafana-dashboard-as-code-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-as-code-generator/)

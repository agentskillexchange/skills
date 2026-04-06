---
name: "Grafana Dashboard Template Generator"
description: "Programmatically creates Grafana dashboard JSON models using the Grafana HTTP API and grafonnet-lib. Supports templated variables, panel linking, and multi-datasource layouts for Prometheus, Loki, and Tempo."
category: "Monitoring &amp; Alerts"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/grafana-dashboard-template-generator/"
---
# Grafana Dashboard Template Generator

Programmatically creates Grafana dashboard JSON models using the Grafana HTTP API and grafonnet-lib. Supports templated variables, panel linking, and multi-datasource layouts for Prometheus, Loki, and Tempo.

The Grafana Dashboard Template Generator automates dashboard creation by producing Grafana-compatible JSON models through the Grafana HTTP API (v9+). It leverages grafonnet-lib patterns to construct panels, rows, and templating variables programmatically, supporting Prometheus, Loki, Tempo, and Elasticsearch datasources in a single dashboard.

Given a service name and its metrics schema, the agent generates a comprehensive dashboard with: RED metrics panels (Rate, Errors, Duration) using PromQL, log volume histograms from Loki LogQL queries, trace duration distributions from Tempo TraceQL, and resource utilization gauges. All panels include proper unit formatting, threshold coloring, and drill-down links.

The generator supports Grafana folder organization, provisioning-compatible YAML output for gitops workflows, and annotation queries for deployment markers. It can also produce reusable library panels and dashboard variables with custom regex filters. Output dashboards are validated against Grafana’s JSON schema before deployment via the Dashboard API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-template-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-template-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-template-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-template-generator -a codex
```

### OpenClaw

```bash
clawhub install grafana-dashboard-template-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-template-generator/)

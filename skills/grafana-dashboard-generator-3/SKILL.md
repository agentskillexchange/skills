---
name: "Grafana Dashboard Generator"
description: "Programmatically generates Grafana dashboards from service definitions using the Grafana HTTP API /api/dashboards/db endpoint. Creates panels for RED metrics, SLO tracking, and infrastructure views."
category: "Monitoring & Alerts"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/grafana-dashboard-generator-3/"
tool_ecosystem:
  tool: "grafana"
  github_stars: 72796
  github_repo: "grafana/grafana"
  license: "AGPL-3.0"
  maintained: true
---

# Grafana Dashboard Generator

Programmatically generates Grafana dashboards from service definitions using the Grafana HTTP API /api/dashboards/db endpoint. Creates panels for RED metrics, SLO tracking, and infrastructure views.

## Overview

The Grafana Dashboard Generator creates standardized monitoring dashboards by querying service registries and generating Grafana dashboard JSON models. It uses the Grafana HTTP API with token-based authentication to push dashboards via the /api/dashboards/db endpoint.

For each service definition, the skill generates RED metrics panels (Rate, Errors, Duration) using PromQL query templates, SLO tracking panels with error budget burn rate calculations, and infrastructure overview panels pulling from node_exporter and kube-state-metrics. All panels use Grafana variable templating for environment and namespace selection.

The skill supports multiple data source types including Prometheus, InfluxDB, and Elasticsearch, automatically configuring panel queries for each backend. It manages dashboard versioning via the Grafana API, supports folder organization, and can generate alerting rules embedded in dashboard panels. Library panel support allows sharing common visualizations across dashboards, and the skill includes a CI integration mode that validates dashboard JSON against the Grafana schema before deployment.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-generator-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-generator-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-generator-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-generator-3 -a codex
```

### OpenClaw

```bash
clawhub install grafana-dashboard-generator-3
```

## Source

- Marketplace: https://agentskillexchange.com/skills/grafana-dashboard-generator-3/

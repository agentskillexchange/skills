---
title: "Grafana Dashboard Generator"
description: "Programmatically generates Grafana dashboards from service definitions using the Grafana HTTP API /api/dashboards/db endpoint. Creates panels for RED metrics, SLO tracking, and infrastructure views."
verification: "security_reviewed"
source: "https://github.com/grafana/grafana"
category:
  - "Monitoring & Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Dashboard Generator

The Grafana Dashboard Generator creates standardized monitoring dashboards by querying service registries and generating Grafana dashboard JSON models. It uses the Grafana HTTP API with token-based authentication to push dashboards via the /api/dashboards/db endpoint. For each service definition, the skill generates RED metrics panels (Rate, Errors, Duration) using PromQL query templates, SLO tracking panels with error budget burn rate calculations, and infrastructure overview panels pulling from node_exporter and kube-state-metrics. All panels use Grafana variable templating for environment and namespace selection. The skill supports multiple data source types including Prometheus, InfluxDB, and Elasticsearch, automatically configuring panel queries for each backend. It manages dashboard versioning via the Grafana API, supports folder organization, and can generate alerting rules embedded in dashboard panels. Library panel support allows sharing common visualizations across dashboards, and the skill includes a CI integration mode that validates dashboard JSON against the Grafana schema before deployment.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/grafana-dashboard-generator-3/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grafana-dashboard-generator-3
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/grafana-dashboard-generator-3`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-generator-3/)

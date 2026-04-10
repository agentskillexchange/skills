---
title: "Grafana Dashboard Generator"
description: "Programmatically generates Grafana dashboards from service definitions using the Grafana HTTP API /api/dashboards/db endpoint. Creates panels for RED metrics, SLO tracking, and infrastructure views."
slug: "grafana-dashboard-generator-3"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/grafana-dashboard-generator-3/"
---

# Grafana Dashboard Generator

Programmatically generates Grafana dashboards from service definitions using the Grafana HTTP API /api/dashboards/db endpoint. Creates panels for RED metrics, SLO tracking, and infrastructure views.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install grafana-dashboard-generator-3
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Grafana Dashboard Generator creates standardized monitoring dashboards by querying service registries and generating Grafana dashboard JSON models. It uses the Grafana HTTP API with token-based authentication to push dashboards via the /api/dashboards/db endpoint.
For each service definition, the skill generates RED metrics panels (Rate, Errors, Duration) using PromQL query templates, SLO tracking panels with error budget burn rate calculations, and infrastructure overview panels pulling from node_exporter and kube-state-metrics. All panels use Grafana variable templating for environment and namespace selection.
The skill supports multiple data source types including Prometheus, InfluxDB, and Elasticsearch, automatically configuring panel queries for each backend. It manages dashboard versioning via the Grafana API, supports folder organization, and can generate alerting rules embedded in dashboard panels. Library panel support allows sharing common visualizations across dashboards, and the skill includes a CI integration mode that validates dashboard JSON against the Grafana schema before deployment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-generator-3/)

---
title: Grafana Dashboard Generator
description: The Grafana Dashboard Generator creates standardized monitoring dashboards
  by querying service registries and generating Grafana dashboard JSON models. It
  uses the Grafana HTTP API with token-based authentication to push dashboards via
  the /api/dashboards/db endpoint. For each service definition, the skill generates
  RED metrics panels (Rate, Errors, Duration) using PromQL query templates, SLO tracking
  panels with error budget burn rate calculations, and infrastructure overview panels
  pulling from node_exporter and kube-state-metrics. All panels use Grafana variable
  templating for environment and namespace selection. The skill supports multiple
  data source types including Prometheus, InfluxDB, and Elasticsearch, automatically
  configuring panel queries for each backend. It manages dashboard versioning via
  the Grafana API, supports folder organization, and can generate alerting rules embedded
  in dashboard panels. Library panel support allows sharing common visualizations
  across dashboards, and the skill includes a CI integration mode that validates dashboard
  JSON against the Grafana schema before deployment.
verification: security_reviewed
source: https://agentskillexchange.com/skills/grafana-dashboard-generator-3/
category:
- Monitoring &amp; Alerts
framework:
- Cursor
---

# Grafana Dashboard Generator

The Grafana Dashboard Generator creates standardized monitoring dashboards by querying service registries and generating Grafana dashboard JSON models. It uses the Grafana HTTP API with token-based authentication to push dashboards via the /api/dashboards/db endpoint. For each service definition, the skill generates RED metrics panels (Rate, Errors, Duration) using PromQL query templates, SLO tracking panels with error budget burn rate calculations, and infrastructure overview panels pulling from node_exporter and kube-state-metrics. All panels use Grafana variable templating for environment and namespace selection. The skill supports multiple data source types including Prometheus, InfluxDB, and Elasticsearch, automatically configuring panel queries for each backend. It manages dashboard versioning via the Grafana API, supports folder organization, and can generate alerting rules embedded in dashboard panels. Library panel support allows sharing common visualizations across dashboards, and the skill includes a CI integration mode that validates dashboard JSON against the Grafana schema before deployment.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-generator-3/)

---
title: "Grafana Dashboard Template Generator"
description: "Programmatically creates Grafana dashboard JSON models using the Grafana HTTP API and grafonnet-lib. Supports templated variables, panel linking, and multi-datasource layouts for Prometheus, Loki, and Tempo."
verification: "security_reviewed"
source: "https://github.com/grafana/grafana"
category:
  - "Monitoring & Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
  license: "AGPL-3.0"
---

# Grafana Dashboard Template Generator

The Grafana Dashboard Template Generator automates dashboard creation by producing Grafana-compatible JSON models through the Grafana HTTP API (v9+). It leverages grafonnet-lib patterns to construct panels, rows, and templating variables programmatically, supporting Prometheus, Loki, Tempo, and Elasticsearch datasources in a single dashboard.


Given a service name and its metrics schema, the agent generates a comprehensive dashboard with: RED metrics panels (Rate, Errors, Duration) using PromQL, log volume histograms from Loki LogQL queries, trace duration distributions from Tempo TraceQL, and resource utilization gauges. All panels include proper unit formatting, threshold coloring, and drill-down links.


The generator supports Grafana folder organization, provisioning-compatible YAML output for gitops workflows, and annotation queries for deployment markers. It can also produce reusable library panels and dashboard variables with custom regex filters. Output dashboards are validated against Grafana’s JSON schema before deployment via the Dashboard API.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-template-generator/)

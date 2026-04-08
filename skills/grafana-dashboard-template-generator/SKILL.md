---
title: Grafana Dashboard Template Generator
description: 'The Grafana Dashboard Template Generator automates dashboard creation
  by producing Grafana-compatible JSON models through the Grafana HTTP API (v9+).
  It leverages grafonnet-lib patterns to construct panels, rows, and templating variables
  programmatically, supporting Prometheus, Loki, Tempo, and Elasticsearch datasources
  in a single dashboard. Given a service name and its metrics schema, the agent generates
  a comprehensive dashboard with: RED metrics panels (Rate, Errors, Duration) using
  PromQL, log volume histograms from Loki LogQL queries, trace duration distributions
  from Tempo TraceQL, and resource utilization gauges. All panels include proper unit
  formatting, threshold coloring, and drill-down links. The generator supports Grafana
  folder organization, provisioning-compatible YAML output for gitops workflows, and
  annotation queries for deployment markers. It can also produce reusable library
  panels and dashboard variables with custom regex filters. Output dashboards are
  validated against Grafana’s JSON schema before deployment via the Dashboard API.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/grafana-dashboard-template-generator/
category:
- Monitoring &amp; Alerts
framework:
- Cursor
---

# Grafana Dashboard Template Generator

The Grafana Dashboard Template Generator automates dashboard creation by producing Grafana-compatible JSON models through the Grafana HTTP API (v9+). It leverages grafonnet-lib patterns to construct panels, rows, and templating variables programmatically, supporting Prometheus, Loki, Tempo, and Elasticsearch datasources in a single dashboard. Given a service name and its metrics schema, the agent generates a comprehensive dashboard with: RED metrics panels (Rate, Errors, Duration) using PromQL, log volume histograms from Loki LogQL queries, trace duration distributions from Tempo TraceQL, and resource utilization gauges. All panels include proper unit formatting, threshold coloring, and drill-down links. The generator supports Grafana folder organization, provisioning-compatible YAML output for gitops workflows, and annotation queries for deployment markers. It can also produce reusable library panels and dashboard variables with custom regex filters. Output dashboards are validated against Grafana’s JSON schema before deployment via the Dashboard API.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-template-generator/)

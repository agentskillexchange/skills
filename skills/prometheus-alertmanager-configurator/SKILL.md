---
title: "Prometheus AlertManager Configurator"
description: "The Prometheus AlertManager Configurator skill automates the creation of AlertManager configuration files with sophisticated routing and notification setups. It generates routing trees with match and match_re label-based routing, group_by configurations for alert aggregation, and group_wait/group_interval/repeat_interval tuning for notification frequency control. The skill configures receiver integrations including PagerDuty via Events API v2 with severity mapping from alert labels, Slack webhook receivers with Block Kit message templates using tmpl function customization, and OpsGenie API integration with priority mapping and team routing. It generates inhibition rules for parent-child alert suppression based on label equality matching. Advanced features include amtool configuration generation for CLI-based alert management, silence creation templates with duration calculations, and alertmanager-webhook-receiver configurations for custom notification endpoints. The skill produces Prometheus recording rules for pre-computed metric aggregation, generates alert unit test files compatible with promtool test rules, and creates Grafana alert dashboard JSON models with panel-to-alertrule linkage via the Grafana Alerting API v1."
source: "https://github.com/prometheus/prometheus"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus AlertManager Configurator

The Prometheus AlertManager Configurator skill automates the creation of AlertManager configuration files with sophisticated routing and notification setups. It generates routing trees with match and match_re label-based routing, group_by configurations for alert aggregation, and group_wait/group_interval/repeat_interval tuning for notification frequency control. The skill configures receiver integrations including PagerDuty via Events API v2 with severity mapping from alert labels, Slack webhook receivers with Block Kit message templates using tmpl function customization, and OpsGenie API integration with priority mapping and team routing. It generates inhibition rules for parent-child alert suppression based on label equality matching. Advanced features include amtool configuration generation for CLI-based alert management, silence creation templates with duration calculations, and alertmanager-webhook-receiver configurations for custom notification endpoints. The skill produces Prometheus recording rules for pre-computed metric aggregation, generates alert unit test files compatible with promtool test rules, and creates Grafana alert dashboard JSON models with panel-to-alertrule linkage via the Grafana Alerting API v1.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-configurator/)

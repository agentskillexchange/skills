---
title: "Prometheus AlertManager Configurator"
description: "Generates Prometheus AlertManager configurations with routing trees, inhibition rules, and receiver integrations for PagerDuty, Slack, and OpsGenie APIs. Supports template-based notification customization."
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
  license: "Apache-2.0"
---

# Prometheus AlertManager Configurator

The Prometheus AlertManager Configurator skill automates the creation of AlertManager configuration files with sophisticated routing and notification setups. It generates routing trees with match and match_re label-based routing, group_by configurations for alert aggregation, and group_wait/group_interval/repeat_interval tuning for notification frequency control.

The skill configures receiver integrations including PagerDuty via Events API v2 with severity mapping from alert labels, Slack webhook receivers with Block Kit message templates using tmpl function customization, and OpsGenie API integration with priority mapping and team routing. It generates inhibition rules for parent-child alert suppression based on label equality matching.

Advanced features include amtool configuration generation for CLI-based alert management, silence creation templates with duration calculations, and alertmanager-webhook-receiver configurations for custom notification endpoints. The skill produces Prometheus recording rules for pre-computed metric aggregation, generates alert unit test files compatible with promtool test rules, and creates Grafana alert dashboard JSON models with panel-to-alertrule linkage via the Grafana Alerting API v1.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-configurator/)

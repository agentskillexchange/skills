---
title: Prometheus AlertManager Configurator
description: The Prometheus AlertManager Configurator skill automates the creation
  of AlertManager configuration files with sophisticated routing and notification
  setups. It generates routing trees with match and match_re label-based routing,
  group_by configurations for alert aggregation, and group_wait/group_interval/repeat_interval
  tuning for notification frequency control. The skill configures receiver integrations
  including PagerDuty via Events API v2 with severity mapping from alert labels, Slack
  webhook receivers with Block Kit message templates using tmpl function customization,
  and OpsGenie API integration with priority mapping and team routing. It generates
  inhibition rules for parent-child alert suppression based on label equality matching.
  Advanced features include amtool configuration generation for CLI-based alert management,
  silence creation templates with duration calculations, and alertmanager-webhook-receiver
  configurations for custom notification endpoints. The skill produces Prometheus
  recording rules for pre-computed metric aggregation, generates alert unit test files
  compatible with promtool test rules, and creates Grafana alert dashboard JSON models
  with panel-to-alertrule linkage via the Grafana Alerting API v1.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alertmanager-configurator/
category:
- Monitoring &amp; Alerts
framework:
- Custom Agents
---

# Prometheus AlertManager Configurator

The Prometheus AlertManager Configurator skill automates the creation of AlertManager configuration files with sophisticated routing and notification setups. It generates routing trees with match and match_re label-based routing, group_by configurations for alert aggregation, and group_wait/group_interval/repeat_interval tuning for notification frequency control. The skill configures receiver integrations including PagerDuty via Events API v2 with severity mapping from alert labels, Slack webhook receivers with Block Kit message templates using tmpl function customization, and OpsGenie API integration with priority mapping and team routing. It generates inhibition rules for parent-child alert suppression based on label equality matching. Advanced features include amtool configuration generation for CLI-based alert management, silence creation templates with duration calculations, and alertmanager-webhook-receiver configurations for custom notification endpoints. The skill produces Prometheus recording rules for pre-computed metric aggregation, generates alert unit test files compatible with promtool test rules, and creates Grafana alert dashboard JSON models with panel-to-alertrule linkage via the Grafana Alerting API v1.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-configurator/)

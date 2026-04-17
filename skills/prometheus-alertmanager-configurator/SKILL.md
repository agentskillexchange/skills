---
title: "Prometheus AlertManager Configurator"
description: "The Prometheus AlertManager Configurator skill automates the creation of AlertManager configuration files with sophisticated routing and notification setups. It generates routing trees with match and match_re label-based routing, group_by configurations for alert aggregation, and group_wait/group_interval/repeat_interval tuning for notification frequency control.\nThe skill configures receiver integrations including PagerDuty via Events API v2 with severity mapping from alert labels, Slack webhook receivers with Block Kit message templates using tmpl function customization, and OpsGenie API integration with priority mapping and team routing. It generates inhibition rules for parent-child alert suppression based on label equality matching.\nAdvanced features include amtool configuration generation for CLI-based alert management, silence creation templates with duration calculations, and alertmanager-webhook-receiver configurations for custom notification endpoints. The skill produces Prometheus recording rules for pre-computed metric aggregation, generates alert unit test files compatible with promtool test rules, and creates Grafana alert dashboard JSON models with panel-to-alertrule linkage via the Grafana Alerting API v1."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus AlertManager Configurator

The Prometheus AlertManager Configurator skill automates the creation of AlertManager configuration files with sophisticated routing and notification setups. It generates routing trees with match and match_re label-based routing, group_by configurations for alert aggregation, and group_wait/group_interval/repeat_interval tuning for notification frequency control.
The skill configures receiver integrations including PagerDuty via Events API v2 with severity mapping from alert labels, Slack webhook receivers with Block Kit message templates using tmpl function customization, and OpsGenie API integration with priority mapping and team routing. It generates inhibition rules for parent-child alert suppression based on label equality matching.
Advanced features include amtool configuration generation for CLI-based alert management, silence creation templates with duration calculations, and alertmanager-webhook-receiver configurations for custom notification endpoints. The skill produces Prometheus recording rules for pre-computed metric aggregation, generates alert unit test files compatible with promtool test rules, and creates Grafana alert dashboard JSON models with panel-to-alertrule linkage via the Grafana Alerting API v1.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alertmanager-configurator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alertmanager-configurator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-configurator/)

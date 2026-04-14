---
title: "Prometheus AlertManager Configurator"
description: "Generates Prometheus AlertManager configurations with routing trees, inhibition rules, and receiver integrations for PagerDuty, Slack, and OpsGenie APIs. Supports template-based notification customization."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring &amp; Alerts"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-configurator/)

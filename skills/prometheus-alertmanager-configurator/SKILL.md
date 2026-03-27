---
name: "Prometheus AlertManager Configurator"
description: "Generates Prometheus AlertManager configurations with routing trees, inhibition rules, and receiver integrations for PagerDuty, Slack, and OpsGenie APIs. Supports template-based notification customization."
category: "Monitoring & Alerts"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prometheus-alertmanager-configurator/"
tool_ecosystem:
  tool: prometheus
  github_stars: 63289
  npm_weekly_downloads: 5319832
  github_repo: prometheus/prometheus
  license: Apache-2.0
  maintained: true
---

# Prometheus AlertManager Configurator

Generates Prometheus AlertManager configurations with routing trees, inhibition rules, and receiver integrations for PagerDuty, Slack, and OpsGenie APIs. Supports template-based notification customization.

## Overview

The Prometheus AlertManager Configurator skill automates the creation of AlertManager configuration files with sophisticated routing and notification setups. It generates routing trees with match and match_re label-based routing, group_by configurations for alert aggregation, and group_wait/group_interval/repeat_interval tuning for notification frequency control.

The skill configures receiver integrations including PagerDuty via Events API v2 with severity mapping from alert labels, Slack webhook receivers with Block Kit message templates using tmpl function customization, and OpsGenie API integration with priority mapping and team routing. It generates inhibition rules for parent-child alert suppression based on label equality matching.

Advanced features include amtool configuration generation for CLI-based alert management, silence creation templates with duration calculations, and alertmanager-webhook-receiver configurations for custom notification endpoints. The skill produces Prometheus recording rules for pre-computed metric aggregation, generates alert unit test files compatible with promtool test rules, and creates Grafana alert dashboard JSON models with panel-to-alertrule linkage via the Grafana Alerting API v1.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-configurator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-configurator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-configurator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-configurator -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alertmanager-configurator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prometheus-alertmanager-configurator/

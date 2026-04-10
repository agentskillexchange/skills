---
title: "Prometheus AlertManager Rule Generator"
description: "Generates Prometheus alerting rules and AlertManager routing configs from natural language descriptions. Leverages PromQL query builder and the Alertmanager API v2 for live rule validation."
slug: "prometheus-alertmanager-rule-generator"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/prometheus-alertmanager-rule-generator/"
---

# Prometheus AlertManager Rule Generator

Generates Prometheus alerting rules and AlertManager routing configs from natural language descriptions. Leverages PromQL query builder and the Alertmanager API v2 for live rule validation.

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
clawhub install prometheus-alertmanager-rule-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Prometheus AlertManager Rule Generator converts natural language alert descriptions into production-ready PromQL alerting rules and AlertManager routing configurations. It uses the Prometheus HTTP API to validate queries against live metric endpoints, ensuring rules match actual metric names and label sets. The skill generates YAML rule groups compatible with Prometheus Operator PrometheusRule CRDs and standalone rule_files configurations. It supports complex PromQL functions including rate(), histogram_quantile(), predict_linear(), and absent(). AlertManager routing trees are generated with proper grouping, inhibition rules, and receiver configurations for Slack, PagerDuty, Opsgenie, and email. The skill includes a dry-run mode that evaluates rules against the last 24 hours of data to estimate alert frequency, preventing noisy alerting. It also handles recording rules for expensive queries that need pre-computation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-generator/)

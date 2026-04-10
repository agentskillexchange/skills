---
title: "Prometheus AlertManager Rule Builder"
description: "Generates Prometheus alerting rules and AlertManager routing configs using PromQL validation via the Prometheus HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configurations."
slug: "prometheus-alertmanager-rule-builder"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/prometheus-alertmanager-rule-builder/"
listed: true
---

# Prometheus AlertManager Rule Builder

Generates Prometheus alerting rules and AlertManager routing configs using PromQL validation via the Prometheus HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configurations.

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
clawhub install prometheus-alertmanager-rule-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Prometheus AlertManager Rule Builder creates and validates alerting rules by interfacing with the Prometheus HTTP API for PromQL expression validation and metric discovery. It generates recording rules for performance-critical queries and alerting rules with proper for-duration, severity labels, and runbook annotations following SRE best practices. The skill configures AlertManager routing trees with proper grouping, inhibition rules, and silence management via the AlertManager API. It supports receiver configurations for PagerDuty (using the Events API v2), OpsGenie (via the Alert API), Slack (using Block Kit message formatting), and custom webhook endpoints. The builder implements alert fatigue reduction strategies including proper group_wait, group_interval, and repeat_interval tuning based on alert severity. It validates rule configurations against promtool for syntax correctness and tests alert conditions using Prometheus’s unit testing framework with mock time series data.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-builder/)

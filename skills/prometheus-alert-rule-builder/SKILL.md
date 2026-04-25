---
title: "Prometheus Alert Rule Builder"
description: "Creates and validates Prometheus alerting rules using PromQL expressions and the Prometheus HTTP API. Configures Alertmanager routing trees with PagerDuty, Slack, and OpsGenie receiver integrations."
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring & Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Rule Builder

The Prometheus Alert Rule Builder skill automates the creation and management of Prometheus alerting rules and Alertmanager configurations. It generates valid PromQL expressions for common monitoring patterns and validates them against running Prometheus instances via the HTTP API. Alert rule generation covers standard SRE patterns including error rate thresholds (rate of 5xx responses), latency percentile breaches (histogram_quantile calculations), saturation alerts (CPU, memory, disk usage), and traffic anomaly detection using predict_linear functions. Each rule includes proper for duration clauses to prevent flapping, severity labels for routing, and runbook_url annotations linking to remediation documentation. The skill validates PromQL syntax using the /api/v1/query endpoint before committing rules. Alertmanager configuration management builds routing trees with proper match/match_re selectors, group_by labels, and timing parameters (group_wait, group_interval, repeat_interval). Receiver definitions support PagerDuty Events API v2 integration keys, Slack incoming webhooks with custom message templates using Go template syntax, OpsGenie API integration with priority mapping, and email SMTP configuration. The skill generates inhibition rules to suppress dependent alerts and manages silences programmatically via the Alertmanager API. Recording rules for expensive PromQL queries are auto-generated to improve dashboard performance.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prometheus-alert-rule-builder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-rule-builder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prometheus-alert-rule-builder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-builder/)

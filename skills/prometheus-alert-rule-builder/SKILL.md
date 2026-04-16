---
title: "Prometheus Alert Rule Builder"
description: "Creates and validates Prometheus alerting rules using PromQL expressions and the Prometheus HTTP API. Configures Alertmanager routing trees with PagerDuty, Slack, and OpsGenie receiver integrations."
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
  license: "Apache-2.0"
---

# Prometheus Alert Rule Builder

The Prometheus Alert Rule Builder skill automates the creation and management of Prometheus alerting rules and Alertmanager configurations. It generates valid PromQL expressions for common monitoring patterns and validates them against running Prometheus instances via the HTTP API.

Alert rule generation covers standard SRE patterns including error rate thresholds (rate of 5xx responses), latency percentile breaches (histogram_quantile calculations), saturation alerts (CPU, memory, disk usage), and traffic anomaly detection using predict_linear functions. Each rule includes proper for duration clauses to prevent flapping, severity labels for routing, and runbook_url annotations linking to remediation documentation. The skill validates PromQL syntax using the /api/v1/query endpoint before committing rules.

Alertmanager configuration management builds routing trees with proper match/match_re selectors, group_by labels, and timing parameters (group_wait, group_interval, repeat_interval). Receiver definitions support PagerDuty Events API v2 integration keys, Slack incoming webhooks with custom message templates using Go template syntax, OpsGenie API integration with priority mapping, and email SMTP configuration. The skill generates inhibition rules to suppress dependent alerts and manages silences programmatically via the Alertmanager API. Recording rules for expensive PromQL queries are auto-generated to improve dashboard performance.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-builder/)

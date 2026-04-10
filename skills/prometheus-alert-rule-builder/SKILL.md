---
name: "Prometheus Alert Rule Builder"
description: "Creates and validates Prometheus alerting rules using PromQL expressions and the Prometheus HTTP API. Configures Alertmanager routing trees with PagerDuty, Slack, and OpsGenie receiver integrations."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prometheus-alert-rule-builder/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
---

# Prometheus Alert Rule Builder

The Prometheus Alert Rule Builder skill automates the creation and management of Prometheus alerting rules and Alertmanager configurations. It generates valid PromQL expressions for common monitoring patterns and validates them against running Prometheus instances via the HTTP API.
Alert rule generation covers standard SRE patterns including error rate thresholds (rate of 5xx responses), latency percentile breaches (histogram_quantile calculations), saturation alerts (CPU, memory, disk usage), and traffic anomaly detection using predict_linear functions. Each rule includes proper for duration clauses to prevent flapping, severity labels for routing, and runbook_url annotations linking to remediation documentation. The skill validates PromQL syntax using the /api/v1/query endpoint before committing rules.
Alertmanager configuration management builds routing trees with proper match/match_re selectors, group_by labels, and timing parameters (group_wait, group_interval, repeat_interval). Receiver definitions support PagerDuty Events API v2 integration keys, Slack incoming webhooks with custom message templates using Go template syntax, OpsGenie API integration with priority mapping, and email SMTP configuration. The skill generates inhibition rules to suppress dependent alerts and manages silences programmatically via the Alertmanager API. Recording rules for expensive PromQL queries are auto-generated to improve dashboard performance.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-builder/)

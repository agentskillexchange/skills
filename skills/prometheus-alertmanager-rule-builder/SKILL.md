---
name: Prometheus AlertManager Rule Builder
description: Generates Prometheus alerting rules and AlertManager routing configs
  using PromQL validation via the Prometheus HTTP API. Supports PagerDuty, OpsGenie,
  and Slack receiver configurations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alertmanager-rule-builder/
category:
- Monitoring &amp; Alerts
framework:
- ChatGPT Agents
---
# Prometheus AlertManager Rule Builder

The Prometheus AlertManager Rule Builder creates and validates alerting rules by interfacing with the Prometheus HTTP API for PromQL expression validation and metric discovery. It generates recording rules for performance-critical queries and alerting rules with proper for-duration, severity labels, and runbook annotations following SRE best practices. The skill configures AlertManager routing trees with proper grouping, inhibition rules, and silence management via the AlertManager API. It supports receiver configurations for PagerDuty (using the Events API v2), OpsGenie (via the Alert API), Slack (using Block Kit message formatting), and custom webhook endpoints. The builder implements alert fatigue reduction strategies including proper group_wait, group_interval, and repeat_interval tuning based on alert severity. It validates rule configurations against promtool for syntax correctness and tests alert conditions using Prometheus's unit testing framework with mock time series data.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-builder/)

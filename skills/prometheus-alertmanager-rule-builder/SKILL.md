---
title: "Prometheus AlertManager Rule Builder"
description: "Generates Prometheus alerting rules and AlertManager routing configs using PromQL validation via the Prometheus HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configurations."
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring & Alerts"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
  license: "Apache-2.0"
---

# Prometheus AlertManager Rule Builder

The Prometheus AlertManager Rule Builder creates and validates alerting rules by interfacing with the Prometheus HTTP API for PromQL expression validation and metric discovery. It generates recording rules for performance-critical queries and alerting rules with proper for-duration, severity labels, and runbook annotations following SRE best practices. The skill configures AlertManager routing trees with proper grouping, inhibition rules, and silence management via the AlertManager API. It supports receiver configurations for PagerDuty (using the Events API v2), OpsGenie (via the Alert API), Slack (using Block Kit message formatting), and custom webhook endpoints. The builder implements alert fatigue reduction strategies including proper group_wait, group_interval, and repeat_interval tuning based on alert severity. It validates rule configurations against promtool for syntax correctness and tests alert conditions using Prometheus’s unit testing framework with mock time series data.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-builder/)

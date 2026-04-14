---
title: "Prometheus AlertManager Rule Builder"
description: "Generates Prometheus alerting rules and AlertManager routing configs using PromQL validation via the Prometheus HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configurations."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus AlertManager Rule Builder

The Prometheus AlertManager Rule Builder creates and validates alerting rules by interfacing with the Prometheus HTTP API for PromQL expression validation and metric discovery. It generates recording rules for performance-critical queries and alerting rules with proper for-duration, severity labels, and runbook annotations following SRE best practices. The skill configures AlertManager routing trees with proper grouping, inhibition rules, and silence management via the AlertManager API. It supports receiver configurations for PagerDuty (using the Events API v2), OpsGenie (via the Alert API), Slack (using Block Kit message formatting), and custom webhook endpoints. The builder implements alert fatigue reduction strategies including proper group_wait, group_interval, and repeat_interval tuning based on alert severity. It validates rule configurations against promtool for syntax correctness and tests alert conditions using Prometheus’s unit testing framework with mock time series data.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-builder/)

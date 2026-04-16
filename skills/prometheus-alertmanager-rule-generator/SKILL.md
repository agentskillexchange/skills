---
title: "Prometheus AlertManager Rule Generator"
description: "Generates Prometheus alerting rules and AlertManager routing configs from natural language descriptions. Leverages PromQL query builder and the Alertmanager API v2 for live rule validation."
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
  license: "Apache-2.0"
---

# Prometheus AlertManager Rule Generator

The Prometheus AlertManager Rule Generator converts natural language alert descriptions into production-ready PromQL alerting rules and AlertManager routing configurations. It uses the Prometheus HTTP API to validate queries against live metric endpoints, ensuring rules match actual metric names and label sets. The skill generates YAML rule groups compatible with Prometheus Operator PrometheusRule CRDs and standalone rule_files configurations. It supports complex PromQL functions including rate(), histogram_quantile(), predict_linear(), and absent(). AlertManager routing trees are generated with proper grouping, inhibition rules, and receiver configurations for Slack, PagerDuty, Opsgenie, and email. The skill includes a dry-run mode that evaluates rules against the last 24 hours of data to estimate alert frequency, preventing noisy alerting. It also handles recording rules for expensive queries that need pre-computation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-generator/)

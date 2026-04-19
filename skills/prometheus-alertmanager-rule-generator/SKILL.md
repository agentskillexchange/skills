---
title: "Prometheus AlertManager Rule Generator"
description: "The Prometheus AlertManager Rule Generator converts natural language alert descriptions into production-ready PromQL alerting rules and AlertManager routing configurations. It uses the Prometheus HTTP API to validate queries against live metric endpoints, ensuring rules match actual metric names and label sets. The skill generates YAML rule groups compatible with Prometheus Operator PrometheusRule CRDs and standalone rule_files configurations. It supports complex PromQL functions including rate(), histogram_quantile(), predict_linear(), and absent(). AlertManager routing trees are generated with proper grouping, inhibition rules, and receiver configurations for Slack, PagerDuty, Opsgenie, and email. The skill includes a dry-run mode that evaluates rules against the last 24 hours of data to estimate alert frequency, preventing noisy alerting. It also handles recording rules for expensive queries that need pre-computation."
source: "https://github.com/prometheus/prometheus"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus AlertManager Rule Generator

The Prometheus AlertManager Rule Generator converts natural language alert descriptions into production-ready PromQL alerting rules and AlertManager routing configurations. It uses the Prometheus HTTP API to validate queries against live metric endpoints, ensuring rules match actual metric names and label sets. The skill generates YAML rule groups compatible with Prometheus Operator PrometheusRule CRDs and standalone rule_files configurations. It supports complex PromQL functions including rate(), histogram_quantile(), predict_linear(), and absent(). AlertManager routing trees are generated with proper grouping, inhibition rules, and receiver configurations for Slack, PagerDuty, Opsgenie, and email. The skill includes a dry-run mode that evaluates rules against the last 24 hours of data to estimate alert frequency, preventing noisy alerting. It also handles recording rules for expensive queries that need pre-computation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-generator/)

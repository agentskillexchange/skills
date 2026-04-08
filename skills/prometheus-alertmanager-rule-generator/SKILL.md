---
title: Prometheus AlertManager Rule Generator
description: The Prometheus AlertManager Rule Generator converts natural language
  alert descriptions into production-ready PromQL alerting rules and AlertManager
  routing configurations. It uses the Prometheus HTTP API to validate queries against
  live metric endpoints, ensuring rules match actual metric names and label sets.
  The skill generates YAML rule groups compatible with Prometheus Operator PrometheusRule
  CRDs and standalone rule_files configurations. It supports complex PromQL functions
  including rate(), histogram_quantile(), predict_linear(), and absent(). AlertManager
  routing trees are generated with proper grouping, inhibition rules, and receiver
  configurations for Slack, PagerDuty, Opsgenie, and email. The skill includes a dry-run
  mode that evaluates rules against the last 24 hours of data to estimate alert frequency,
  preventing noisy alerting. It also handles recording rules for expensive queries
  that need pre-computation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alertmanager-rule-generator/
category:
- Monitoring &amp; Alerts
framework:
- Claude Code
---

# Prometheus AlertManager Rule Generator

The Prometheus AlertManager Rule Generator converts natural language alert descriptions into production-ready PromQL alerting rules and AlertManager routing configurations. It uses the Prometheus HTTP API to validate queries against live metric endpoints, ensuring rules match actual metric names and label sets. The skill generates YAML rule groups compatible with Prometheus Operator PrometheusRule CRDs and standalone rule_files configurations. It supports complex PromQL functions including rate(), histogram_quantile(), predict_linear(), and absent(). AlertManager routing trees are generated with proper grouping, inhibition rules, and receiver configurations for Slack, PagerDuty, Opsgenie, and email. The skill includes a dry-run mode that evaluates rules against the last 24 hours of data to estimate alert frequency, preventing noisy alerting. It also handles recording rules for expensive queries that need pre-computation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-generator/)

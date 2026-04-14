---
title: "Prometheus AlertManager Rule Generator"
description: "Generates Prometheus alerting rules and AlertManager routing configs from natural language descriptions. Leverages PromQL query builder and the Alertmanager API v2 for live rule validation."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-generator/)

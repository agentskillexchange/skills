---
name: Prometheus Alertmanager Rule Auditor
description: Validates Prometheus recording and alerting rules using promtool check
  rules, analyzes Alertmanager routing trees for notification gaps, and tests alert
  expressions against live TSDB data via the Prometheus HTTP API.
verification: security_reviewed
source: https://github.com/prometheus/alertmanager
category:
- Monitoring &amp; Alerts
framework:
- Gemini
tool_ecosystem:
  github_repo: prometheus/alertmanager
  github_stars: 8403
---
# Prometheus Alertmanager Rule Auditor

The Prometheus Alertmanager Rule Auditor performs comprehensive validation and testing of Prometheus monitoring configurations. Using promtool check rules, it validates YAML syntax, PromQL expression correctness, and label consistency across all recording and alerting rules before they reach production. The auditor analyzes Alertmanager routing trees to identify notification blind spots where alerts could be silently dropped due to missing route matches or inhibition rule conflicts. Alert expressions are tested against live TSDB data through the Prometheus HTTP API, executing range queries to verify that rules would have fired during known incident windows. The skill detects common anti-patterns including alerts without runbook annotations, recording rules with excessive cardinality, and alerting rules with inadequate for durations that could cause alert fatigue. Silence and inhibition rule analysis identifies overly broad configurations that might suppress legitimate alerts. The auditor generates coverage reports showing which services and SLOs have monitoring coverage and where gaps exist. Integration with version control enables rule change review workflows where proposed modifications are tested against historical data before merging.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-auditor/)

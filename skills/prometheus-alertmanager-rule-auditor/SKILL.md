---
title: "Prometheus Alertmanager Rule Auditor"
description: "The Prometheus Alertmanager Rule Auditor performs comprehensive validation and testing of Prometheus monitoring configurations. Using promtool check rules, it validates YAML syntax, PromQL expression correctness, and label consistency across all recording and alerting rules before they reach production. The auditor analyzes Alertmanager routing trees to identify notification blind spots where alerts could be silently dropped due to missing route matches or inhibition rule conflicts. Alert expressions are tested against live TSDB data through the Prometheus HTTP API, executing range queries to verify that rules would have fired during known incident windows. The skill detects common anti-patterns including alerts without runbook annotations, recording rules with excessive cardinality, and alerting rules with inadequate for durations that could cause alert fatigue. Silence and inhibition rule analysis identifies overly broad configurations that might suppress legitimate alerts. The auditor generates coverage reports showing which services and SLOs have monitoring coverage and where gaps exist. Integration with version control enables rule change review workflows where proposed modifications are tested against historical data before merging."
verification: security_reviewed
source: "https://github.com/prometheus/alertmanager"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "prometheus/alertmanager"
  github_stars: 8403
---

# Prometheus Alertmanager Rule Auditor

The Prometheus Alertmanager Rule Auditor performs comprehensive validation and testing of Prometheus monitoring configurations. Using promtool check rules, it validates YAML syntax, PromQL expression correctness, and label consistency across all recording and alerting rules before they reach production. The auditor analyzes Alertmanager routing trees to identify notification blind spots where alerts could be silently dropped due to missing route matches or inhibition rule conflicts. Alert expressions are tested against live TSDB data through the Prometheus HTTP API, executing range queries to verify that rules would have fired during known incident windows. The skill detects common anti-patterns including alerts without runbook annotations, recording rules with excessive cardinality, and alerting rules with inadequate for durations that could cause alert fatigue. Silence and inhibition rule analysis identifies overly broad configurations that might suppress legitimate alerts. The auditor generates coverage reports showing which services and SLOs have monitoring coverage and where gaps exist. Integration with version control enables rule change review workflows where proposed modifications are tested against historical data before merging.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alertmanager-rule-auditor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alertmanager-rule-auditor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-auditor/)

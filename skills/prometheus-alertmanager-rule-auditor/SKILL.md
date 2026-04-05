---
name: "Prometheus Alertmanager Rule Auditor"
description: "Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API."
category: "Monitoring & Alerts"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/prometheus/alertmanager"
tool_ecosystem:
  github_repo: "prometheus/alertmanager"
  github_stars: 8405
---
# Prometheus Alertmanager Rule Auditor

Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API.

The Prometheus Alertmanager Rule Auditor performs comprehensive validation and testing of Prometheus monitoring configurations. Using promtool check rules, it validates YAML syntax, PromQL expression correctness, and label consistency across all recording and alerting rules before they reach production. The auditor analyzes Alertmanager routing trees to identify notification blind spots where alerts could be silently dropped due to missing route matches or inhibition rule conflicts. Alert expressions are tested against live TSDB data through the Prometheus HTTP API, executing range queries to verify that rules would have fired during known incident windows. The skill detects common anti-patterns including alerts without runbook annotations, recording rules with excessive cardinality, and alerting rules with inadequate for durations that could cause alert fatigue. Silence and inhibition rule analysis identifies overly broad configurations that might suppress legitimate alerts. The auditor generates coverage reports showing which services and SLOs have monitoring coverage and where gaps exist. Integration with version control enables rule change review workflows where proposed modifications are tested against historical data before merging.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-auditor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-auditor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-auditor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-auditor -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alertmanager-rule-auditor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-auditor/)

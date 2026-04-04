---
name: "Prometheus Alertmanager Rule Auditor"
category: "Monitoring & Alerts"
verification: "security_reviewed"
source: "https://github.com/prometheus/alertmanager"
tool_ecosystem:
  github_repo: "prometheus/alertmanager"
  github_stars: 8405
---

# Prometheus Alertmanager Rule Auditor

Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API.

## Installation

Install this skill using one of the following methods:

```bash
# ClawHub CLI
clawhub install prometheus-alertmanager-rule-auditor

# OpenClaw CLI
openclaw skills install prometheus-alertmanager-rule-auditor

# Chat command
/skill install prometheus-alertmanager-rule-auditor

# Direct download
curl -L https://agentskillexchange.com/skills/prometheus-alertmanager-rule-auditor/download -o prometheus-alertmanager-rule-auditor.zip

# Git clone this repo and copy the skill folder
cp -r skills/prometheus-alertmanager-rule-auditor ~/.openclaw/workspace/skills/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-auditor/)

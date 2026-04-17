---
name: Prometheus Alertmanager Rule Auditor
description: Validates Prometheus recording and alerting rules using promtool check
  rules, analyzes Alertmanager routing trees for notification gaps, and tests alert
  expressions against live TSDB data via the Prometheus HTTP API.
category: Monitoring & Alerts
framework: Gemini
verification: security_reviewed
source: https://github.com/prometheus/alertmanager
tool_ecosystem:
  github_repo: prometheus/alertmanager
  github_stars: 8403
  tool: alertmanager
---
# Prometheus Alertmanager Rule Auditor
Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API.

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

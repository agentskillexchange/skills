---
title: "Prometheus Alertmanager Rule Auditor"
description: "Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API."
verification: security_reviewed
source: "https://github.com/prometheus/alertmanager"
category:
  - "Monitoring & Alerts"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "prometheus/alertmanager"
  github_stars: 8403
---

# Prometheus Alertmanager Rule Auditor

Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prometheus-alertmanager-rule-auditor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alertmanager-rule-auditor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prometheus-alertmanager-rule-auditor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-auditor/)

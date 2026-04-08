---
title: "Prometheus Alertmanager Rule Auditor"
slug: "prometheus-alertmanager-rule-auditor"
description: "Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API."
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://github.com/prometheus/alertmanager"
tool_ecosystem:
  github_repo: "prometheus/alertmanager"
  github_stars: 8405
---

# Prometheus Alertmanager Rule Auditor

Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-auditor/)

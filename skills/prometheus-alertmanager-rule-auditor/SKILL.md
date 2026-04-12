---
title: "Prometheus Alertmanager Rule Auditor"
description: "Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API."
verification: security_reviewed
source: "https://github.com/prometheus/alertmanager"
tool_ecosystem:
  github_repo: "prometheus/alertmanager"
  github_stars: 8403
---

# Prometheus Alertmanager Rule Auditor

Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-auditor/)

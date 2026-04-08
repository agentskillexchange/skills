---
title: "Prometheus Alertmanager Rule Auditor"
slug: "prometheus-alertmanager-rule-auditor"
verification: "security_reviewed"
description: "Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API."
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
source: "https://github.com/prometheus/alertmanager"
tool_ecosystem:
  github_repo: "prometheus/alertmanager"
  github_stars: 8405
---

# Prometheus Alertmanager Rule Auditor

Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your local skills workspace.
2. Install it with ClawHub if it is available there.
3. Copy the folder into your OpenClaw or AgentSkills directory manually.
4. Add it as a git submodule if you manage skills as pinned dependencies.
5. Vendor it directly into a project repo when you need a fixed internal copy.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-auditor/)

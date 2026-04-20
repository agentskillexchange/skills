---
title: "Prometheus Alert Rule Synthesizer"
description: "Uses the Prometheus HTTP API v1 and PromQL to auto-generate alerting rules from metric baselines. Integrates with Alertmanager API for routing configuration and PagerDuty Events API v2 for escalation."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring & Alerts"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Rule Synthesizer

Uses the Prometheus HTTP API v1 and PromQL to auto-generate alerting rules from metric baselines. Integrates with Alertmanager API for routing configuration and PagerDuty Events API v2 for escalation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prometheus-alert-rule-synthesizer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-rule-synthesizer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prometheus-alert-rule-synthesizer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-synthesizer/)

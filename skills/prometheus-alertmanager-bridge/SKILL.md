---
title: "Prometheus AlertManager Bridge"
description: "Connects to Prometheus AlertManager API to query active alerts, silences, and alert groups. Parses PromQL alert rules and suggests runbook actions. Integrates with PagerDuty escalation policies."
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

# Prometheus AlertManager Bridge

Connects to Prometheus AlertManager API to query active alerts, silences, and alert groups. Parses PromQL alert rules and suggests runbook actions. Integrates with PagerDuty escalation policies.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prometheus-alertmanager-bridge/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alertmanager-bridge
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prometheus-alertmanager-bridge`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-bridge/)

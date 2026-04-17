---
name: Prometheus AlertManager Router
description: Configures and manages Prometheus AlertManager routing trees and silences
  via the AlertManager HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver
  configuration with inhibition rules.
category: Monitoring & Alerts
framework: Cursor
verification: security_reviewed
source: https://github.com/prometheus/prometheus
tool_ecosystem:
  github_repo: prometheus/prometheus
  github_stars: 63584
  tool: prometheus
  license: Apache-2.0
  maintained: true
---
# Prometheus AlertManager Router
Configures and manages Prometheus AlertManager routing trees and silences via the AlertManager HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configuration with inhibition rules.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alertmanager-router
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alertmanager-router` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-router/)

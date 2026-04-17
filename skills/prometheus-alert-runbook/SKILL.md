---
name: Prometheus Alert Runbook
description: Execute structured runbook procedures triggered by Prometheus AlertManager
  webhooks. Queries PromQL metrics via the Prometheus HTTP API for automated incident
  diagnosis and escalation.
category: Runbooks & Diagnostics
framework: MCP
verification: security_reviewed
source: https://github.com/prometheus/prometheus
tool_ecosystem:
  github_repo: prometheus/prometheus
  github_stars: 63584
  tool: prometheus
  license: Apache-2.0
  maintained: true
---
# Prometheus Alert Runbook
Execute structured runbook procedures triggered by Prometheus AlertManager webhooks. Queries PromQL metrics via the Prometheus HTTP API for automated incident diagnosis and escalation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-runbook
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alert-runbook` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook/)

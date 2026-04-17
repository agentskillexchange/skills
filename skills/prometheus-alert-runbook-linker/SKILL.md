---
name: Prometheus Alert Runbook Linker
description: Links Prometheus alerting rules to operational runbooks by parsing AlertManager
  configurations and PrometheusRule CRDs. Validates runbook_url annotations exist
  and are reachable, and generates stub runbooks for undocumented alerts.
category: Runbooks & Diagnostics
framework: Gemini
verification: security_reviewed
source: https://github.com/prometheus/prometheus
tool_ecosystem:
  github_repo: prometheus/prometheus
  github_stars: 63584
  tool: prometheus
  license: Apache-2.0
  maintained: true
---
# Prometheus Alert Runbook Linker
Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-runbook-linker
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alert-runbook-linker` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook-linker/)

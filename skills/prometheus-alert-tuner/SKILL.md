---
name: Prometheus Alert Tuner
description: Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL
  query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds
  via histogram_quantile, and configuring inhibition rules.
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
# Prometheus Alert Tuner
Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds via histogram_quantile, and configuring inhibition rules.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-tuner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alert-tuner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-tuner/)

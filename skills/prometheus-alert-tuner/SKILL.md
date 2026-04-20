---
title: "Prometheus Alert Tuner"
description: "Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds via histogram_quantile, and configuring inhibition rules."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Tuner

Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds via histogram_quantile, and configuring inhibition rules.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prometheus-alert-tuner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-tuner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prometheus-alert-tuner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-tuner/)

---
title: Prometheus Alert Resolver
description: Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range
  endpoints for metric time series analysis. Executes playbook steps for common alerts
  like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences
  alerts via Alertmanager /api/v2/silences.
verification: security_reviewed
source: https://github.com/prometheus/prometheus
category:
- Runbooks & Diagnostics
framework:
- Gemini
tool_ecosystem:
  github_repo: prometheus/prometheus
  github_stars: 63584
---

# Prometheus Alert Resolver

Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-resolver-skill
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prometheus-alert-resolver-skill`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/)

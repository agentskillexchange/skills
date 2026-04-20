---
title: "Prometheus Alert Rule Tester"
description: "Tests Prometheus alerting rules against historical metrics using promtool and the Prometheus HTTP API query_range endpoint. Validates PromQL expressions, simulates alert firing, and checks routing configurations."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Rule Tester

Tests Prometheus alerting rules against historical metrics using promtool and the Prometheus HTTP API query_range endpoint. Validates PromQL expressions, simulates alert firing, and checks routing configurations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prometheus-alert-rule-tester/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-rule-tester
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prometheus-alert-rule-tester`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-tester/)

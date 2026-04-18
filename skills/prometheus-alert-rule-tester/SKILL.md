---
title: "Prometheus Alert Rule Tester"
description: "Tests Prometheus alerting rules against historical metrics using promtool and the Prometheus HTTP API query_range endpoint. Validates PromQL expressions, simulates alert firing, and checks routing configurations."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
  license: "Apache-2.0"
---

# Prometheus Alert Rule Tester

Tests Prometheus alerting rules against historical metrics using promtool and the Prometheus HTTP API query_range endpoint. Validates PromQL expressions, simulates alert firing, and checks routing configurations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-rule-tester
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alert-rule-tester` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-tester/)

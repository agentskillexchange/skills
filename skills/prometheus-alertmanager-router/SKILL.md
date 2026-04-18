---
title: "Prometheus AlertManager Router"
description: "Configures and manages Prometheus AlertManager routing trees and silences via the AlertManager HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configuration with inhibition rules."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring & Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus AlertManager Router

The Prometheus AlertManager Router skill provides intelligent alert routing and management through the AlertManager HTTP API. It enables agents to programmatically create, modify, and debug complex routing trees that determine how alerts flow from Prometheus to notification receivers like PagerDuty, OpsGenie, Slack, and email.

Key features include routing tree visualization and validation before applying changes, automatic silence creation during maintenance windows with scheduled expiry, and inhibition rule management to suppress dependent alerts when root-cause alerts are already firing. The skill can analyze alert group patterns to suggest routing optimizations.

It supports match and match_re label-based routing, continue flags for multi-receiver fan-out, group_by/group_wait/group_interval tuning for alert batching, and receiver template customization using Go template syntax. Integration with Prometheus’s /api/v1/rules endpoint enables correlation between recording rules, alerting rules, and their AlertManager routing destinations for end-to-end observability pipeline verification.

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

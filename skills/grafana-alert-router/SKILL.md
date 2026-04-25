---
title: "Grafana Alert Router"
description: "Routes Grafana alerting webhook payloads to Slack, PagerDuty, and OpsGenie channels based on label matching rules. Supports alert grouping and silence management via the Grafana Alerting API."
verification: "security_reviewed"
source: "https://github.com/grafana/grafana"
category:
  - "Monitoring & Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Alert Router

The Grafana Alert Router skill processes incoming webhook payloads from Grafana Unified Alerting and routes them to the appropriate notification channels based on configurable label matchers. It integrates with Slack (via Block Kit API), PagerDuty (Events API v2), and OpsGenie (Alert API). The skill manages alert lifecycle states including firing, resolved, and silenced. It supports alert grouping by configurable labels to reduce notification noise, and can auto-create silences via the Grafana Silences API for scheduled maintenance windows. Advanced routing rules use CEL (Common Expression Language) expressions for complex matching logic. The skill maintains a local SQLite database of alert history for trend analysis and includes a dashboard template that visualizes alert frequency, MTTR, and channel distribution using Grafana’s own visualization capabilities.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/grafana-alert-router/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grafana-alert-router
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/grafana-alert-router`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-alert-router/)

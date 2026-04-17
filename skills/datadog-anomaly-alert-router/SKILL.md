---
title: "Datadog Anomaly Alert Router"
description: "The Datadog Anomaly Alert Router processes anomaly detection alerts from Datadog monitors and routes them to the appropriate incident response channels. It listens to Datadog webhook payloads containing monitor state transitions (OK → Alert → Warn → No Data) and applies configurable routing rules based on monitor tags, alert severity, and affected service. The skill queries the Datadog Monitors API v1 /api/v1/monitor/{monitor_id} endpoint to fetch full monitor configuration including thresholds, evaluation windows, and tagged scopes. Severity classification uses a three-tier model: P1 alerts trigger PagerDuty incidents via the PagerDuty Events API v2 /enqueue endpoint, P2 alerts post to team-specific Slack channels via incoming webhooks, and P3 alerts are logged to a Datadog Event stream via POST /api/v1/events. The router maintains an alert correlation engine that groups related anomalies by service tag and time window, preventing alert storms from generating duplicate pages. Includes automatic escalation: if a P2 alert remains unacknowledged for a configurable timeout (checked via Datadog /api/v1/monitor/{id}?group_states=alert), it escalates to P1. Dashboard integration exposes routing statistics through Datadog custom metrics via the /api/v2/series endpoint."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  ase_npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Anomaly Alert Router

The Datadog Anomaly Alert Router processes anomaly detection alerts from Datadog monitors and routes them to the appropriate incident response channels. It listens to Datadog webhook payloads containing monitor state transitions (OK → Alert → Warn → No Data) and applies configurable routing rules based on monitor tags, alert severity, and affected service. The skill queries the Datadog Monitors API v1 /api/v1/monitor/{monitor_id} endpoint to fetch full monitor configuration including thresholds, evaluation windows, and tagged scopes. Severity classification uses a three-tier model: P1 alerts trigger PagerDuty incidents via the PagerDuty Events API v2 /enqueue endpoint, P2 alerts post to team-specific Slack channels via incoming webhooks, and P3 alerts are logged to a Datadog Event stream via POST /api/v1/events. The router maintains an alert correlation engine that groups related anomalies by service tag and time window, preventing alert storms from generating duplicate pages. Includes automatic escalation: if a P2 alert remains unacknowledged for a configurable timeout (checked via Datadog /api/v1/monitor/{id}?group_states=alert), it escalates to P1. Dashboard integration exposes routing statistics through Datadog custom metrics via the /api/v2/series endpoint.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-anomaly-alert-router
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/datadog-anomaly-alert-router` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-anomaly-alert-router/)

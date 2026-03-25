---
name: "Datadog Anomaly Alert Router"
description: "Routes Datadog anomaly detection alerts to appropriate response channels using the Datadog Events API v2 and Monitors API. Applies severity-based escalation rules with PagerDuty and Slack webhook integration."
category: "Monitoring & Alerts"
framework: "MCP-compatible"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/datadog-anomaly-alert-router/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "datadog"  # from ase_tool_match
  github_stars: 787  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 6043057  # from ase_npm_downloads
  github_repo: "DataDog/dd-trace-js"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Datadog Anomaly Alert Router

Routes Datadog anomaly detection alerts to appropriate response channels using the Datadog Events API v2 and Monitors API. Applies severity-based escalation rules with PagerDuty and Slack webhook integration.

## Overview

The Datadog Anomaly Alert Router processes anomaly detection alerts from Datadog monitors and routes them to the appropriate incident response channels. It listens to Datadog webhook payloads containing monitor state transitions (OK → Alert → Warn → No Data) and applies configurable routing rules based on monitor tags, alert severity, and affected service. The skill queries the Datadog Monitors API v1 /api/v1/monitor/{monitor_id} endpoint to fetch full monitor configuration including thresholds, evaluation windows, and tagged scopes. Severity classification uses a three-tier model: P1 alerts trigger PagerDuty incidents via the PagerDuty Events API v2 /enqueue endpoint, P2 alerts post to team-specific Slack channels via incoming webhooks, and P3 alerts are logged to a Datadog Event stream via POST /api/v1/events. The router maintains an alert correlation engine that groups related anomalies by service tag and time window, preventing alert storms from generating duplicate pages. Includes automatic escalation: if a P2 alert remains unacknowledged for a configurable timeout (checked via Datadog /api/v1/monitor/{id}?group_states=alert), it escalates to P1. Dashboard integration exposes routing statistics through Datadog custom metrics via the /api/v2/series endpoint.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-anomaly-alert-router
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-anomaly-alert-router -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-anomaly-alert-router -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-anomaly-alert-router -a codex
```

### OpenClaw

```bash
clawhub install datadog-anomaly-alert-router
```

## Source

- Marketplace: https://agentskillexchange.com/skills/datadog-anomaly-alert-router/

---
name: "Uptime Robot Status Page Webhook Alerter"
description: "Integrates with the Uptime Robot API to monitor status page changes and push webhook alerts to Slack or PagerDuty. Uses the UptimeRobot getMonitors endpoint to detect downtime transitions."
category: "40"
framework: "22"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/uptime-robot-status-page-webhook-alerter/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pagerduty"  # from ase_tool_match
  github_stars: 69  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 210829  # from ase_npm_downloads
  github_repo: "PagerDuty/pdjs"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Uptime Robot Status Page Webhook Alerter

Integrates with the Uptime Robot API to monitor status page changes and push webhook alerts to Slack or PagerDuty. Uses the UptimeRobot getMonitors endpoint to detect downtime transitions.

## Overview

The Uptime Robot Status Page Webhook Alerter monitors your Uptime Robot status pages and pushes real-time alerts when monitors transition between up, down, and paused states. It polls the UptimeRobot v2 API getMonitors endpoint at configurable intervals and compares current status against cached state. When a transition is detected, the skill formats a structured webhook payload including monitor friendly name, URL, response time, and downtime duration, then dispatches it to configured endpoints such as Slack incoming webhooks or PagerDuty Events API v2. The skill supports custom alert templates, threshold-based filtering to suppress flapping monitors, and maintenance window awareness via the getMaintenanceWindows API. It handles API rate limiting with exponential backoff and stores state in a local SQLite database for persistence across restarts.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill uptime-robot-status-page-webhook-alerter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill uptime-robot-status-page-webhook-alerter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill uptime-robot-status-page-webhook-alerter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill uptime-robot-status-page-webhook-alerter -a codex
```

### OpenClaw

```bash
clawhub install uptime-robot-status-page-webhook-alerter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/uptime-robot-status-page-webhook-alerter/

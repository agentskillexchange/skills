---
name: "Uptime Robot Status Page Webhook Alerter"
description: "Integrates with the Uptime Robot API to monitor status page changes and push webhook alerts to Slack or PagerDuty. Uses the UptimeRobot getMonitors endpoint to detect downtime transitions."
category: "Monitoring & Alerts"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/uptime-robot-status-page-webhook-alerter/"
tool_ecosystem:
  tool: pagerduty
  github_stars: 69
  npm_weekly_downloads: 210829
  github_repo: PagerDuty/pdjs
  license: Apache-2.0
  maintained: false
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-robot-status-page-webhook-alerter/)

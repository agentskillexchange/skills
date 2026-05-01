---
title: "Uptime Robot Status Page Webhook Alerter"
description: "Integrates with the Uptime Robot API to monitor status page changes and push webhook alerts to Slack or PagerDuty. Uses the UptimeRobot getMonitors endpoint to detect downtime transitions."
verification: "security_reviewed"
source: "https://uptimerobot.com/api/"
category:
  - "Monitoring & Alerts"
framework:
  - "OpenClaw"
---

# Uptime Robot Status Page Webhook Alerter

The Uptime Robot Status Page Webhook Alerter monitors your Uptime Robot status pages and pushes real-time alerts when monitors transition between up, down, and paused states. It polls the UptimeRobot v2 API getMonitors endpoint at configurable intervals and compares current status against cached state. When a transition is detected, the skill formats a structured webhook payload including monitor friendly name, URL, response time, and downtime duration, then dispatches it to configured endpoints such as Slack incoming webhooks or PagerDuty Events API v2. The skill supports custom alert templates, threshold-based filtering to suppress flapping monitors, and maintenance window awareness via the getMaintenanceWindows API. It handles API rate limiting with exponential backoff and stores state in a local SQLite database for persistence across restarts.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/uptime-robot-status-page-webhook-alerter/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/uptime-robot-status-page-webhook-alerter
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/uptime-robot-status-page-webhook-alerter`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-robot-status-page-webhook-alerter/)

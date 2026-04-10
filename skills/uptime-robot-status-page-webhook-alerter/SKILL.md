---
title: "Uptime Robot Status Page Webhook Alerter"
description: "Integrates with the Uptime Robot API to monitor status page changes and push webhook alerts to Slack or PagerDuty. Uses the UptimeRobot getMonitors endpoint to detect downtime transitions."
slug: "uptime-robot-status-page-webhook-alerter"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://uptimerobot.com/api/"
---

# Uptime Robot Status Page Webhook Alerter

Integrates with the Uptime Robot API to monitor status page changes and push webhook alerts to Slack or PagerDuty. Uses the UptimeRobot getMonitors endpoint to detect downtime transitions.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install uptime-robot-status-page-webhook-alerter
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Uptime Robot Status Page Webhook Alerter monitors your Uptime Robot status pages and pushes real-time alerts when monitors transition between up, down, and paused states. It polls the UptimeRobot v2 API getMonitors endpoint at configurable intervals and compares current status against cached state. When a transition is detected, the skill formats a structured webhook payload including monitor friendly name, URL, response time, and downtime duration, then dispatches it to configured endpoints such as Slack incoming webhooks or PagerDuty Events API v2. The skill supports custom alert templates, threshold-based filtering to suppress flapping monitors, and maintenance window awareness via the getMaintenanceWindows API. It handles API rate limiting with exponential backoff and stores state in a local SQLite database for persistence across restarts.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-robot-status-page-webhook-alerter/)

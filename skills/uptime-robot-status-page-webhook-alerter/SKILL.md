---
title: "Uptime Robot Status Page Webhook Alerter"
description: "The Uptime Robot Status Page Webhook Alerter monitors your Uptime Robot status pages and pushes real-time alerts when monitors transition between up, down, and paused states. It polls the UptimeRobot v2 API getMonitors endpoint at configurable intervals and compares current status against cached state. When a transition is detected, the skill formats a structured webhook payload including monitor friendly name, URL, response time, and downtime duration, then dispatches it to configured endpoints such as Slack incoming webhooks or PagerDuty Events API v2. The skill supports custom alert templates, threshold-based filtering to suppress flapping monitors, and maintenance window awareness via the getMaintenanceWindows API. It handles API rate limiting with exponential backoff and stores state in a local SQLite database for persistence across restarts."
verification: security_reviewed
source: "https://uptimerobot.com/api/"
framework:
  - "OpenClaw"
---

# Uptime Robot Status Page Webhook Alerter

The Uptime Robot Status Page Webhook Alerter monitors your Uptime Robot status pages and pushes real-time alerts when monitors transition between up, down, and paused states. It polls the UptimeRobot v2 API getMonitors endpoint at configurable intervals and compares current status against cached state. When a transition is detected, the skill formats a structured webhook payload including monitor friendly name, URL, response time, and downtime duration, then dispatches it to configured endpoints such as Slack incoming webhooks or PagerDuty Events API v2. The skill supports custom alert templates, threshold-based filtering to suppress flapping monitors, and maintenance window awareness via the getMaintenanceWindows API. It handles API rate limiting with exponential backoff and stores state in a local SQLite database for persistence across restarts.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/uptime-robot-status-page-webhook-alerter
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/uptime-robot-status-page-webhook-alerter` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-robot-status-page-webhook-alerter/)

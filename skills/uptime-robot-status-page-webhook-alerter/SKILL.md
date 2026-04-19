---
title: "Uptime Robot Status Page Webhook Alerter"
description: "The Uptime Robot Status Page Webhook Alerter monitors your Uptime Robot status pages and pushes real-time alerts when monitors transition between up, down, and paused states. It polls the UptimeRobot v2 API getMonitors endpoint at configurable intervals and compares current status against cached state. When a transition is detected, the skill formats a structured webhook payload including monitor friendly name, URL, response time, and downtime duration, then dispatches it to configured endpoints such as Slack incoming webhooks or PagerDuty Events API v2. The skill supports custom alert templates, threshold-based filtering to suppress flapping monitors, and maintenance window awareness via the getMaintenanceWindows API. It handles API rate limiting with exponential backoff and stores state in a local SQLite database for persistence across restarts."
source: "https://uptimerobot.com/api/"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
---

# Uptime Robot Status Page Webhook Alerter

The Uptime Robot Status Page Webhook Alerter monitors your Uptime Robot status pages and pushes real-time alerts when monitors transition between up, down, and paused states. It polls the UptimeRobot v2 API getMonitors endpoint at configurable intervals and compares current status against cached state. When a transition is detected, the skill formats a structured webhook payload including monitor friendly name, URL, response time, and downtime duration, then dispatches it to configured endpoints such as Slack incoming webhooks or PagerDuty Events API v2. The skill supports custom alert templates, threshold-based filtering to suppress flapping monitors, and maintenance window awareness via the getMaintenanceWindows API. It handles API rate limiting with exponential backoff and stores state in a local SQLite database for persistence across restarts.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-robot-status-page-webhook-alerter/)

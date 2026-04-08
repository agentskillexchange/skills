---
title: Uptime Robot Status Page Webhook Alerter
description: The Uptime Robot Status Page Webhook Alerter monitors your Uptime Robot
  status pages and pushes real-time alerts when monitors transition between up, down,
  and paused states. It polls the UptimeRobot v2 API getMonitors endpoint at configurable
  intervals and compares current status against cached state. When a transition is
  detected, the skill formats a structured webhook payload including monitor friendly
  name, URL, response time, and downtime duration, then dispatches it to configured
  endpoints such as Slack incoming webhooks or PagerDuty Events API v2. The skill
  supports custom alert templates, threshold-based filtering to suppress flapping
  monitors, and maintenance window awareness via the getMaintenanceWindows API. It
  handles API rate limiting with exponential backoff and stores state in a local SQLite
  database for persistence across restarts.
verification: security_reviewed
source: https://uptimerobot.com/api/
category:
- Monitoring &amp; Alerts
framework:
- OpenClaw
---

# Uptime Robot Status Page Webhook Alerter

The Uptime Robot Status Page Webhook Alerter monitors your Uptime Robot status pages and pushes real-time alerts when monitors transition between up, down, and paused states. It polls the UptimeRobot v2 API getMonitors endpoint at configurable intervals and compares current status against cached state. When a transition is detected, the skill formats a structured webhook payload including monitor friendly name, URL, response time, and downtime duration, then dispatches it to configured endpoints such as Slack incoming webhooks or PagerDuty Events API v2. The skill supports custom alert templates, threshold-based filtering to suppress flapping monitors, and maintenance window awareness via the getMaintenanceWindows API. It handles API rate limiting with exponential backoff and stores state in a local SQLite database for persistence across restarts.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-robot-status-page-webhook-alerter/)

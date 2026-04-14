---
title: "Uptime Robot Status Page Webhook Alerter"
description: "Integrates with the Uptime Robot API to monitor status page changes and push webhook alerts to Slack or PagerDuty. Uses the UptimeRobot getMonitors endpoint to detect downtime transitions."
verification: security_reviewed
source: "https://uptimerobot.com/api/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
---

# Uptime Robot Status Page Webhook Alerter

The Uptime Robot Status Page Webhook Alerter monitors your Uptime Robot status pages and pushes real-time alerts when monitors transition between up, down, and paused states. It polls the UptimeRobot v2 API getMonitors endpoint at configurable intervals and compares current status against cached state. When a transition is detected, the skill formats a structured webhook payload including monitor friendly name, URL, response time, and downtime duration, then dispatches it to configured endpoints such as Slack incoming webhooks or PagerDuty Events API v2. The skill supports custom alert templates, threshold-based filtering to suppress flapping monitors, and maintenance window awareness via the getMaintenanceWindows API. It handles API rate limiting with exponential backoff and stores state in a local SQLite database for persistence across restarts.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-robot-status-page-webhook-alerter/)

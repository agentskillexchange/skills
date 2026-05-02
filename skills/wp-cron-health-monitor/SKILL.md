---
title: "WP Cron Health Monitor"
description: "Monitors WordPress wp-cron scheduled events using the WP_Cron API and Action Scheduler library. Detects stuck, overdue, or orphaned cron jobs and reports via WP REST API webhooks with configurable alert thresholds."
verification: "security_reviewed"
source: "https://developer.wordpress.org/plugins/cron/"
category:
  - "WordPress & CMS"
framework:
  - "OpenClaw"
---

# WP Cron Health Monitor

WP Cron Health Monitor provides comprehensive monitoring of WordPress scheduled task infrastructure. It hooks into the wp-cron system using wp_get_scheduled_event() and _get_cron_array() to enumerate all registered cron hooks, their schedules, and last execution timestamps.

The skill integrates with Action Scheduler (used by WooCommerce and other major plugins) to monitor async action queues, detecting actions stuck in pending or failed states. It exposes a custom REST endpoint at /wp-json/cron-health/v1/status returning structured JSON with overdue counts, average execution times, and failure rates.

Alert thresholds are configurable per-hook: set maximum allowed delay before a cron event is flagged as stuck. Supports email notifications via wp_mail(), Slack webhooks, and PagerDuty integration. Includes a WP-CLI command wp cron-health report for server-side diagnostics and a dashboard widget showing cron health at a glance.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/wp-cron-health-monitor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wp-cron-health-monitor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/wp-cron-health-monitor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cron-health-monitor/)

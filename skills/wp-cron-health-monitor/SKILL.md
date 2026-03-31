---
name: "WP Cron Health Monitor"
description: "Monitors WordPress wp-cron scheduled events using the WP_Cron API and Action Scheduler library. Detects stuck, overdue, or orphaned cron jobs and reports via WP REST API webhooks with configurable alert thresholds."
category: "WordPress &amp; CMS"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/wp-cron-health-monitor/"
---
# WP Cron Health Monitor

Monitors WordPress wp-cron scheduled events using the WP_Cron API and Action Scheduler library. Detects stuck, overdue, or orphaned cron jobs and reports via WP REST API webhooks with configurable alert thresholds.

## Overview

WP Cron Health Monitor provides comprehensive monitoring of WordPress scheduled task infrastructure. It hooks into the wp-cron system using wp_get_scheduled_event() and _get_cron_array() to enumerate all registered cron hooks, their schedules, and last execution timestamps.

The skill integrates with Action Scheduler (used by WooCommerce and other major plugins) to monitor async action queues, detecting actions stuck in pending or failed states. It exposes a custom REST endpoint at /wp-json/cron-health/v1/status returning structured JSON with overdue counts, average execution times, and failure rates.

Alert thresholds are configurable per-hook: set maximum allowed delay before a cron event is flagged as stuck. Supports email notifications via wp_mail(), Slack webhooks, and PagerDuty integration. Includes a WP-CLI command wp cron-health report for server-side diagnostics and a dashboard widget showing cron health at a glance.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wp-cron-health-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wp-cron-health-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wp-cron-health-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wp-cron-health-monitor -a codex
```

### OpenClaw

```bash
clawhub install wp-cron-health-monitor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cron-health-monitor/)

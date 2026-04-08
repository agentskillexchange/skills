---
title: WP Cron Health Monitor
description: 'WP Cron Health Monitor provides comprehensive monitoring of WordPress
  scheduled task infrastructure. It hooks into the wp-cron system using wp_get_scheduled_event()
  and _get_cron_array() to enumerate all registered cron hooks, their schedules, and
  last execution timestamps. The skill integrates with Action Scheduler (used by WooCommerce
  and other major plugins) to monitor async action queues, detecting actions stuck
  in pending or failed states. It exposes a custom REST endpoint at /wp-json/cron-health/v1/status
  returning structured JSON with overdue counts, average execution times, and failure
  rates. Alert thresholds are configurable per-hook: set maximum allowed delay before
  a cron event is flagged as stuck. Supports email notifications via wp_mail() , Slack
  webhooks, and PagerDuty integration. Includes a WP-CLI command wp cron-health report
  for server-side diagnostics and a dashboard widget showing cron health at a glance.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/wp-cron-health-monitor/
category:
- WordPress &amp; CMS
framework:
- OpenClaw
---

# WP Cron Health Monitor

WP Cron Health Monitor provides comprehensive monitoring of WordPress scheduled task infrastructure. It hooks into the wp-cron system using wp_get_scheduled_event() and _get_cron_array() to enumerate all registered cron hooks, their schedules, and last execution timestamps. The skill integrates with Action Scheduler (used by WooCommerce and other major plugins) to monitor async action queues, detecting actions stuck in pending or failed states. It exposes a custom REST endpoint at /wp-json/cron-health/v1/status returning structured JSON with overdue counts, average execution times, and failure rates. Alert thresholds are configurable per-hook: set maximum allowed delay before a cron event is flagged as stuck. Supports email notifications via wp_mail() , Slack webhooks, and PagerDuty integration. Includes a WP-CLI command wp cron-health report for server-side diagnostics and a dashboard widget showing cron health at a glance.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cron-health-monitor/)

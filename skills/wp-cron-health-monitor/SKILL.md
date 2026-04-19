---
title: "WP Cron Health Monitor"
description: "WP Cron Health Monitor provides comprehensive monitoring of WordPress scheduled task infrastructure. It hooks into the wp-cron system using wp_get_scheduled_event() and _get_cron_array() to enumerate all registered cron hooks, their schedules, and last execution timestamps. The skill integrates with Action Scheduler (used by WooCommerce and other major plugins) to monitor async action queues, detecting actions stuck in pending or failed states. It exposes a custom REST endpoint at /wp-json/cron-health/v1/status returning structured JSON with overdue counts, average execution times, and failure rates. Alert thresholds are configurable per-hook: set maximum allowed delay before a cron event is flagged as stuck. Supports email notifications via wp_mail() , Slack webhooks, and PagerDuty integration. Includes a WP-CLI command wp cron-health report for server-side diagnostics and a dashboard widget showing cron health at a glance."
source: "https://agentskillexchange.com/skills/wp-cron-health-monitor/"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "OpenClaw"
---

# WP Cron Health Monitor

WP Cron Health Monitor provides comprehensive monitoring of WordPress scheduled task infrastructure. It hooks into the wp-cron system using wp_get_scheduled_event() and _get_cron_array() to enumerate all registered cron hooks, their schedules, and last execution timestamps. The skill integrates with Action Scheduler (used by WooCommerce and other major plugins) to monitor async action queues, detecting actions stuck in pending or failed states. It exposes a custom REST endpoint at /wp-json/cron-health/v1/status returning structured JSON with overdue counts, average execution times, and failure rates. Alert thresholds are configurable per-hook: set maximum allowed delay before a cron event is flagged as stuck. Supports email notifications via wp_mail() , Slack webhooks, and PagerDuty integration. Includes a WP-CLI command wp cron-health report for server-side diagnostics and a dashboard widget showing cron health at a glance.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cron-health-monitor/)

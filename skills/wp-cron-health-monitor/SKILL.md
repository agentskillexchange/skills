---
name: "WP Cron Health Monitor"
slug: "wp-cron-health-monitor"
description: "Monitors WordPress wp-cron scheduled events using the WP_Cron API and Action Scheduler library. Detects stuck, overdue, or orphaned cron jobs and reports via WP REST API webhooks with configurable alert thresholds."
verification: "listed"
source: "https://developer.wordpress.org/plugins/cron/"
author: "WordPress"
category: "WordPress & CMS"
framework: "OpenClaw"
---

# WP Cron Health Monitor

Monitors WordPress wp-cron scheduled events using the WP_Cron API and Action Scheduler library. Detects stuck, overdue, or orphaned cron jobs and reports via WP REST API webhooks with configurable alert thresholds.

## Installation

Use the upstream install or setup path that matches your environment:
- Make WordPress

Basic usage or getting-started notes:
- WP-Cron works by checking, on every page load, a list of scheduled tasks to see what needs to be run. Any tasks due to run will be called during that page load.
- WP-Cron does not run constantly as the system cron does; it is only triggered on page load.
- With the system scheduler, if the time passes and the task did not run, it will not be re-attempted. With WP-Cron, all scheduled tasks are put into a queue and will run at the next opportunity (meaning the next page l...

- Source: https://developer.wordpress.org/plugins/cron/

## Documentation

- https://developer.wordpress.org/plugins/cron/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cron-health-monitor/)

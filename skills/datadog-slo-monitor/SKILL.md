---
title: Datadog SLO Monitor
description: The Datadog SLO Monitor skill continuously tracks Service Level Objectives
  defined in Datadog using the SLO API v2 endpoints. It calculates real-time burn
  rates across 5-minute, 1-hour, and 30-day windows to detect fast-burn and slow-burn
  scenarios. When error budgets approach exhaustion thresholds, the skill triggers
  configurable remediation workflows including automated rollbacks via deployment
  APIs, traffic shifting through load balancer configurations, and team notifications
  via Datadog Events. Features include SLO history export to CSV for compliance reporting,
  multi-SLO dashboard generation using Datadog Dashboards API, and integration with
  Datadog Monitors API for creating composite alert conditions. Supports custom burn
  rate alerting rules and weekly SLO digest summaries sent via email or Slack.
verification: security_reviewed
source: https://agentskillexchange.com/skills/datadog-slo-monitor/
category:
- Monitoring &amp; Alerts
framework:
- Claude Code
---

# Datadog SLO Monitor

The Datadog SLO Monitor skill continuously tracks Service Level Objectives defined in Datadog using the SLO API v2 endpoints. It calculates real-time burn rates across 5-minute, 1-hour, and 30-day windows to detect fast-burn and slow-burn scenarios. When error budgets approach exhaustion thresholds, the skill triggers configurable remediation workflows including automated rollbacks via deployment APIs, traffic shifting through load balancer configurations, and team notifications via Datadog Events. Features include SLO history export to CSV for compliance reporting, multi-SLO dashboard generation using Datadog Dashboards API, and integration with Datadog Monitors API for creating composite alert conditions. Supports custom burn rate alerting rules and weekly SLO digest summaries sent via email or Slack.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-slo-monitor/)

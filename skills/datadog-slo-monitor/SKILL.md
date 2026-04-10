---
name: Datadog SLO Monitor
description: Monitors Datadog Service Level Objectives and burn rate alerts via the
  Datadog API v2. Generates SLO compliance reports and triggers remediation workflows
  when error budgets are exhausted.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-slo-monitor/)

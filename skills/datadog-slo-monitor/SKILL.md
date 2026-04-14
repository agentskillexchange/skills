---
title: "Datadog SLO Monitor"
description: "Monitors Datadog Service Level Objectives and burn rate alerts via the Datadog API v2. Generates SLO compliance reports and triggers remediation workflows when error budgets are exhausted."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog SLO Monitor

The Datadog SLO Monitor skill continuously tracks Service Level Objectives defined in Datadog using the SLO API v2 endpoints. It calculates real-time burn rates across 5-minute, 1-hour, and 30-day windows to detect fast-burn and slow-burn scenarios. When error budgets approach exhaustion thresholds, the skill triggers configurable remediation workflows including automated rollbacks via deployment APIs, traffic shifting through load balancer configurations, and team notifications via Datadog Events. Features include SLO history export to CSV for compliance reporting, multi-SLO dashboard generation using Datadog Dashboards API, and integration with Datadog Monitors API for creating composite alert conditions. Supports custom burn rate alerting rules and weekly SLO digest summaries sent via email or Slack.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-slo-monitor/)

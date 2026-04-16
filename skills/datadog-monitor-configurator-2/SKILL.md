---
title: "Datadog Monitor Configurator"
description: "Manages Datadog monitors and dashboards via the Datadog REST API v2. Creates metric, log, and APM monitors with composite conditions and configures notification routing through @-mention integrations."
verification: "security_reviewed"
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
---

# Datadog Monitor Configurator

The Datadog Monitor Configurator skill provides programmatic management of Datadog monitoring infrastructure through the Datadog REST API v1 and v2. It creates, updates, and organizes monitors, dashboards, and SLOs without requiring manual configuration through the Datadog UI.

Monitor creation supports all Datadog monitor types: metric monitors with query aggregation (avg, sum, min, max over rolling windows), log monitors using Datadog log query syntax with facet filters, APM monitors tracking service latency and error rates from trace data, and composite monitors combining multiple conditions with boolean logic. Each monitor includes proper thresholds (warning, critical, critical_recovery), evaluation windows, and no-data handling configuration.

Notification routing uses Datadog @-mention syntax to direct alerts to the appropriate channels: @slack-channel for Slack integration, @pagerduty-service for PagerDuty escalation, @webhook-name for custom webhook endpoints, and @team-handle for team-based routing. The skill generates dashboard JSON definitions using the Datadog Dashboard API with timeseries widgets, query value widgets, SLO widgets, and log stream panels. Monitor downtime scheduling uses the Downtime API for maintenance windows. Terraform-compatible HCL output is available for infrastructure-as-code workflows using the datadog Terraform provider, ensuring monitor configurations are version-controlled and reproducible.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-configurator-2/)

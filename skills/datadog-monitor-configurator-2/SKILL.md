---
title: "Datadog Monitor Configurator"
description: "Manages Datadog monitors and dashboards via the Datadog REST API v2. Creates metric, log, and APM monitors with composite conditions and configures notification routing through @-mention integrations."
verification: "security_reviewed"
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring & Alerts"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Monitor Configurator

The Datadog Monitor Configurator skill provides programmatic management of Datadog monitoring infrastructure through the Datadog REST API v1 and v2. It creates, updates, and organizes monitors, dashboards, and SLOs without requiring manual configuration through the Datadog UI.

Monitor creation supports all Datadog monitor types: metric monitors with query aggregation (avg, sum, min, max over rolling windows), log monitors using Datadog log query syntax with facet filters, APM monitors tracking service latency and error rates from trace data, and composite monitors combining multiple conditions with boolean logic. Each monitor includes proper thresholds (warning, critical, critical_recovery), evaluation windows, and no-data handling configuration.

Notification routing uses Datadog @-mention syntax to direct alerts to the appropriate channels: @slack-channel for Slack integration, @pagerduty-service for PagerDuty escalation, @webhook-name for custom webhook endpoints, and @team-handle for team-based routing. The skill generates dashboard JSON definitions using the Datadog Dashboard API with timeseries widgets, query value widgets, SLO widgets, and log stream panels. Monitor downtime scheduling uses the Downtime API for maintenance windows. Terraform-compatible HCL output is available for infrastructure-as-code workflows using the datadog Terraform provider, ensuring monitor configurations are version-controlled and reproducible.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/datadog-monitor-configurator-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-monitor-configurator-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/datadog-monitor-configurator-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-configurator-2/)

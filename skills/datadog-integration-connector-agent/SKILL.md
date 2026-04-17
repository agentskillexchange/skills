---
title: "Datadog Integration Connector"
description: "The Datadog Integration Connector establishes comprehensive application monitoring through the Datadog API v2. It submits custom metrics using the v2/series endpoint with proper metric types (count, rate, gauge), configures log forwarding through the v2/logs endpoint with proper attribute mapping and log pipelines, and manages APM trace data via the Trace API for distributed tracing visualization. The skill creates and manages dashboards using the Dashboards API, generating JSON templates for common monitoring patterns including service health overviews, deployment tracking, and error rate correlation. It configures monitors through the Monitors API with composite conditions, multi-alert grouping, and escalation policies. The connector manages service level objectives (SLOs) via the SLO API, implements Real User Monitoring (RUM) application setup, and configures Synthetic Tests for API and browser-based uptime monitoring. It handles tag management across infrastructure using the Tags API, sets up metric metadata and units via the Metrics API, and manages downtime schedules for maintenance windows. Advanced features include Notebook API integration for incident analysis, Log-to-Metric generation rules, and custom facet management for log exploration."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  ase_npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Integration Connector

The Datadog Integration Connector establishes comprehensive application monitoring through the Datadog API v2. It submits custom metrics using the v2/series endpoint with proper metric types (count, rate, gauge), configures log forwarding through the v2/logs endpoint with proper attribute mapping and log pipelines, and manages APM trace data via the Trace API for distributed tracing visualization. The skill creates and manages dashboards using the Dashboards API, generating JSON templates for common monitoring patterns including service health overviews, deployment tracking, and error rate correlation. It configures monitors through the Monitors API with composite conditions, multi-alert grouping, and escalation policies. The connector manages service level objectives (SLOs) via the SLO API, implements Real User Monitoring (RUM) application setup, and configures Synthetic Tests for API and browser-based uptime monitoring. It handles tag management across infrastructure using the Tags API, sets up metric metadata and units via the Metrics API, and manages downtime schedules for maintenance windows. Advanced features include Notebook API integration for incident analysis, Log-to-Metric generation rules, and custom facet management for log exploration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-integration-connector-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/datadog-integration-connector-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-integration-connector-agent/)

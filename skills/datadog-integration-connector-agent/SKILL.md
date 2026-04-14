---
title: "Datadog Integration Connector"
description: "Connects applications to Datadog monitoring using the Datadog API v2 for metrics submission, log forwarding, APM trace ingestion, and dashboard JSON template management."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Integration Connector

The Datadog Integration Connector establishes comprehensive application monitoring through the Datadog API v2. It submits custom metrics using the v2/series endpoint with proper metric types (count, rate, gauge), configures log forwarding through the v2/logs endpoint with proper attribute mapping and log pipelines, and manages APM trace data via the Trace API for distributed tracing visualization. The skill creates and manages dashboards using the Dashboards API, generating JSON templates for common monitoring patterns including service health overviews, deployment tracking, and error rate correlation. It configures monitors through the Monitors API with composite conditions, multi-alert grouping, and escalation policies. The connector manages service level objectives (SLOs) via the SLO API, implements Real User Monitoring (RUM) application setup, and configures Synthetic Tests for API and browser-based uptime monitoring. It handles tag management across infrastructure using the Tags API, sets up metric metadata and units via the Metrics API, and manages downtime schedules for maintenance windows. Advanced features include Notebook API integration for incident analysis, Log-to-Metric generation rules, and custom facet management for log exploration.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-integration-connector-agent/)

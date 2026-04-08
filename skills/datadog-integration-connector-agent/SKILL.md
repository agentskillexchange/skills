---
title: Datadog Integration Connector
description: The Datadog Integration Connector establishes comprehensive application
  monitoring through the Datadog API v2. It submits custom metrics using the v2/series
  endpoint with proper metric types (count, rate, gauge), configures log forwarding
  through the v2/logs endpoint with proper attribute mapping and log pipelines, and
  manages APM trace data via the Trace API for distributed tracing visualization.
  The skill creates and manages dashboards using the Dashboards API, generating JSON
  templates for common monitoring patterns including service health overviews, deployment
  tracking, and error rate correlation. It configures monitors through the Monitors
  API with composite conditions, multi-alert grouping, and escalation policies. The
  connector manages service level objectives (SLOs) via the SLO API, implements Real
  User Monitoring (RUM) application setup, and configures Synthetic Tests for API
  and browser-based uptime monitoring. It handles tag management across infrastructure
  using the Tags API, sets up metric metadata and units via the Metrics API, and manages
  downtime schedules for maintenance windows. Advanced features include Notebook API
  integration for incident analysis, Log-to-Metric generation rules, and custom facet
  management for log exploration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/datadog-integration-connector-agent/
category:
- Integrations &amp; Connectors
framework:
- Gemini
---

# Datadog Integration Connector

The Datadog Integration Connector establishes comprehensive application monitoring through the Datadog API v2. It submits custom metrics using the v2/series endpoint with proper metric types (count, rate, gauge), configures log forwarding through the v2/logs endpoint with proper attribute mapping and log pipelines, and manages APM trace data via the Trace API for distributed tracing visualization. The skill creates and manages dashboards using the Dashboards API, generating JSON templates for common monitoring patterns including service health overviews, deployment tracking, and error rate correlation. It configures monitors through the Monitors API with composite conditions, multi-alert grouping, and escalation policies. The connector manages service level objectives (SLOs) via the SLO API, implements Real User Monitoring (RUM) application setup, and configures Synthetic Tests for API and browser-based uptime monitoring. It handles tag management across infrastructure using the Tags API, sets up metric metadata and units via the Metrics API, and manages downtime schedules for maintenance windows. Advanced features include Notebook API integration for incident analysis, Log-to-Metric generation rules, and custom facet management for log exploration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-integration-connector-agent/)

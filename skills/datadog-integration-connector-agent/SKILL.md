---
title: "Datadog Integration Connector"
description: "Connects applications to Datadog monitoring using the Datadog API v2 for metrics submission, log forwarding, APM trace ingestion, and dashboard JSON template management."
slug: "datadog-integration-connector-agent"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/datadog-integration-connector-agent/"
listed: true
---

# Datadog Integration Connector

Connects applications to Datadog monitoring using the Datadog API v2 for metrics submission, log forwarding, APM trace ingestion, and dashboard JSON template management.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install datadog-integration-connector-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Datadog Integration Connector establishes comprehensive application monitoring through the Datadog API v2. It submits custom metrics using the v2/series endpoint with proper metric types (count, rate, gauge), configures log forwarding through the v2/logs endpoint with proper attribute mapping and log pipelines, and manages APM trace data via the Trace API for distributed tracing visualization. The skill creates and manages dashboards using the Dashboards API, generating JSON templates for common monitoring patterns including service health overviews, deployment tracking, and error rate correlation. It configures monitors through the Monitors API with composite conditions, multi-alert grouping, and escalation policies. The connector manages service level objectives (SLOs) via the SLO API, implements Real User Monitoring (RUM) application setup, and configures Synthetic Tests for API and browser-based uptime monitoring. It handles tag management across infrastructure using the Tags API, sets up metric metadata and units via the Metrics API, and manages downtime schedules for maintenance windows. Advanced features include Notebook API integration for incident analysis, Log-to-Metric generation rules, and custom facet management for log exploration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-integration-connector-agent/)

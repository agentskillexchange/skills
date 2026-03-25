---
name: "Datadog Integration Connector"
description: "Connects applications to Datadog monitoring using the Datadog API v2 for metrics submission, log forwarding, APM trace ingestion, and dashboard JSON template management."
category: "Integrations & Connectors"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/datadog-integration-connector-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "datadog"  # from ase_tool_match
  github_stars: 789  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 6043057  # from ase_npm_downloads
  github_repo: "DataDog/dd-trace-js"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Datadog Integration Connector

Connects applications to Datadog monitoring using the Datadog API v2 for metrics submission, log forwarding, APM trace ingestion, and dashboard JSON template management.

## Overview

The Datadog Integration Connector establishes comprehensive application monitoring through the Datadog API v2. It submits custom metrics using the v2/series endpoint with proper metric types (count, rate, gauge), configures log forwarding through the v2/logs endpoint with proper attribute mapping and log pipelines, and manages APM trace data via the Trace API for distributed tracing visualization. The skill creates and manages dashboards using the Dashboards API, generating JSON templates for common monitoring patterns including service health overviews, deployment tracking, and error rate correlation. It configures monitors through the Monitors API with composite conditions, multi-alert grouping, and escalation policies. The connector manages service level objectives (SLOs) via the SLO API, implements Real User Monitoring (RUM) application setup, and configures Synthetic Tests for API and browser-based uptime monitoring. It handles tag management across infrastructure using the Tags API, sets up metric metadata and units via the Metrics API, and manages downtime schedules for maintenance windows. Advanced features include Notebook API integration for incident analysis, Log-to-Metric generation rules, and custom facet management for log exploration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-integration-connector-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-integration-connector-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-integration-connector-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-integration-connector-agent -a codex
```

### OpenClaw

```bash
clawhub install datadog-integration-connector-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/datadog-integration-connector-agent/

---
title: "Datadog Metric Exporter"
description: "Exports custom metrics and traces to Datadog using the DogStatsD protocol and Datadog API v2. Supports histogram aggregation, tag-based filtering, and SLO tracking."
verification: "security_reviewed"
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring & Alerts"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Metric Exporter

The Datadog Metric Exporter skill sends custom application metrics to Datadog through both the DogStatsD UDP protocol for high-frequency data and the Datadog API v2 REST endpoints for batch submissions. It supports all metric types: count, rate, gauge, histogram, and distribution. The skill handles tag management following Datadog’s best practices with automatic tag normalization, reserved tag detection, and cardinality warnings. It can create and update monitors programmatically using the Monitors API, including composite monitors with boolean logic. SLO tracking is built in with support for monitor-based and metric-based SLOs. The skill calculates error budgets, generates burn rate alerts, and can export SLO reports as PDF via the Datadog SLO API. Integration with OpenTelemetry allows trace context propagation through the OTLP exporter configured for Datadog’s intake endpoint.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/datadog-metric-exporter/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-metric-exporter
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/datadog-metric-exporter`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-metric-exporter/)

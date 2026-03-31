---
name: "Datadog Metric Exporter"
description: "Exports custom metrics and traces to Datadog using the DogStatsD protocol and Datadog API v2. Supports histogram aggregation, tag-based filtering, and SLO tracking."
category: "Monitoring &amp; Alerts"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/datadog-metric-exporter/"
---
# Datadog Metric Exporter

Exports custom metrics and traces to Datadog using the DogStatsD protocol and Datadog API v2. Supports histogram aggregation, tag-based filtering, and SLO tracking.

## Overview

The Datadog Metric Exporter skill sends custom application metrics to Datadog through both the DogStatsD UDP protocol for high-frequency data and the Datadog API v2 REST endpoints for batch submissions. It supports all metric types: count, rate, gauge, histogram, and distribution.

The skill handles tag management following Datadog's best practices with automatic tag normalization, reserved tag detection, and cardinality warnings. It can create and update monitors programmatically using the Monitors API, including composite monitors with boolean logic.

SLO tracking is built in with support for monitor-based and metric-based SLOs. The skill calculates error budgets, generates burn rate alerts, and can export SLO reports as PDF via the Datadog SLO API. Integration with OpenTelemetry allows trace context propagation through the OTLP exporter configured for Datadog's intake endpoint.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-metric-exporter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-metric-exporter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-metric-exporter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-metric-exporter -a codex
```

### OpenClaw

```bash
clawhub install datadog-metric-exporter
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-metric-exporter/)

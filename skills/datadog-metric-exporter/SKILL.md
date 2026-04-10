---
name: "Datadog Metric Exporter"
description: "Exports custom metrics and traces to Datadog using the DogStatsD protocol and Datadog API v2. Supports histogram aggregation, tag-based filtering, and SLO tracking."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/datadog-metric-exporter/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
---

# Datadog Metric Exporter

The Datadog Metric Exporter skill sends custom application metrics to Datadog through both the DogStatsD UDP protocol for high-frequency data and the Datadog API v2 REST endpoints for batch submissions. It supports all metric types: count, rate, gauge, histogram, and distribution.
The skill handles tag management following Datadog's best practices with automatic tag normalization, reserved tag detection, and cardinality warnings. It can create and update monitors programmatically using the Monitors API, including composite monitors with boolean logic.
SLO tracking is built in with support for monitor-based and metric-based SLOs. The skill calculates error budgets, generates burn rate alerts, and can export SLO reports as PDF via the Datadog SLO API. Integration with OpenTelemetry allows trace context propagation through the OTLP exporter configured for Datadog's intake endpoint.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-metric-exporter/)

---
title: Datadog Metric Exporter
description: 'The Datadog Metric Exporter skill sends custom application metrics to
  Datadog through both the DogStatsD UDP protocol for high-frequency data and the
  Datadog API v2 REST endpoints for batch submissions. It supports all metric types:
  count, rate, gauge, histogram, and distribution. The skill handles tag management
  following Datadog’s best practices with automatic tag normalization, reserved tag
  detection, and cardinality warnings. It can create and update monitors programmatically
  using the Monitors API, including composite monitors with boolean logic. SLO tracking
  is built in with support for monitor-based and metric-based SLOs. The skill calculates
  error budgets, generates burn rate alerts, and can export SLO reports as PDF via
  the Datadog SLO API. Integration with OpenTelemetry allows trace context propagation
  through the OTLP exporter configured for Datadog’s intake endpoint.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/datadog-metric-exporter/
category:
- Monitoring &amp; Alerts
framework:
- Gemini
---

# Datadog Metric Exporter

The Datadog Metric Exporter skill sends custom application metrics to Datadog through both the DogStatsD UDP protocol for high-frequency data and the Datadog API v2 REST endpoints for batch submissions. It supports all metric types: count, rate, gauge, histogram, and distribution. The skill handles tag management following Datadog’s best practices with automatic tag normalization, reserved tag detection, and cardinality warnings. It can create and update monitors programmatically using the Monitors API, including composite monitors with boolean logic. SLO tracking is built in with support for monitor-based and metric-based SLOs. The skill calculates error budgets, generates burn rate alerts, and can export SLO reports as PDF via the Datadog SLO API. Integration with OpenTelemetry allows trace context propagation through the OTLP exporter configured for Datadog’s intake endpoint.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-metric-exporter/)

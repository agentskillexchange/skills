---
title: "Datadog Metric Exporter"
description: "Exports custom metrics and traces to Datadog using the DogStatsD protocol and Datadog API v2. Supports histogram aggregation, tag-based filtering, and SLO tracking."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Metric Exporter

The Datadog Metric Exporter skill sends custom application metrics to Datadog through both the DogStatsD UDP protocol for high-frequency data and the Datadog API v2 REST endpoints for batch submissions. It supports all metric types: count, rate, gauge, histogram, and distribution.

The skill handles tag management following Datadog’s best practices with automatic tag normalization, reserved tag detection, and cardinality warnings. It can create and update monitors programmatically using the Monitors API, including composite monitors with boolean logic.

SLO tracking is built in with support for monitor-based and metric-based SLOs. The skill calculates error budgets, generates burn rate alerts, and can export SLO reports as PDF via the Datadog SLO API. Integration with OpenTelemetry allows trace context propagation through the OTLP exporter configured for Datadog’s intake endpoint.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-metric-exporter/)

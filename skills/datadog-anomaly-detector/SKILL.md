---
title: "Datadog Anomaly Detector"
description: "Leverages the Datadog API v2 metrics and events endpoints to detect anomalous patterns. Uses the Datadog Monitors API to create dynamic thresholds and sends escalations via OpsGenie REST API."
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

# Datadog Anomaly Detector

The Datadog Anomaly Detector skill enables AI agents to perform proactive infrastructure monitoring by interfacing with the Datadog API v2. It queries the /api/v2/query/timeseries endpoint to pull metric data across configurable time windows, supporting all Datadog metric types including count, rate, gauge, and distribution.

Anomaly detection uses a combination of Datadog built-in anomaly functions (anomalies() with basic, agile, and robust algorithms) and custom statistical analysis. The skill creates and manages monitors via the /api/v1/monitor endpoint, implementing dynamic thresholds that adapt to seasonal patterns detected through Fourier decomposition of historical data.

When anomalies trigger, the skill creates OpsGenie alerts via the REST API v2 (/v2/alerts), attaching metric visualizations generated from the Datadog Embeddable Graphs API. Incident timelines are automatically populated with correlated events from the Datadog Events API, including recent deployments, configuration changes, and related monitor state transitions. The skill maintains an anomaly knowledge base in PostgreSQL for pattern recognition across incidents.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-anomaly-detector/)

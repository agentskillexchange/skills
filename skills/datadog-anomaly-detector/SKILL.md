---
title: "Datadog Anomaly Detector"
description: "Leverages the Datadog API v2 metrics and events endpoints to detect anomalous patterns. Uses the Datadog Monitors API to create dynamic thresholds and sends escalations via OpsGenie REST API."
verification: "security_reviewed"
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring & Alerts"
framework:
  - "Gemini"
---

# Datadog Anomaly Detector

The Datadog Anomaly Detector skill enables AI agents to perform proactive infrastructure monitoring by interfacing with the Datadog API v2. It queries the /api/v2/query/timeseries endpoint to pull metric data across configurable time windows, supporting all Datadog metric types including count, rate, gauge, and distribution.


Anomaly detection uses a combination of Datadog built-in anomaly functions (anomalies() with basic, agile, and robust algorithms) and custom statistical analysis. The skill creates and manages monitors via the /api/v1/monitor endpoint, implementing dynamic thresholds that adapt to seasonal patterns detected through Fourier decomposition of historical data.


When anomalies trigger, the skill creates OpsGenie alerts via the REST API v2 (/v2/alerts), attaching metric visualizations generated from the Datadog Embeddable Graphs API. Incident timelines are automatically populated with correlated events from the Datadog Events API, including recent deployments, configuration changes, and related monitor state transitions. The skill maintains an anomaly knowledge base in PostgreSQL for pattern recognition across incidents.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-anomaly-detector/)

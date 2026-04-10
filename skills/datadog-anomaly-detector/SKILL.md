---
title: "Datadog Anomaly Detector"
description: "Leverages the Datadog API v2 metrics and events endpoints to detect anomalous patterns. Uses the Datadog Monitors API to create dynamic thresholds and sends escalations via OpsGenie REST API."
slug: "datadog-anomaly-detector"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/datadog-anomaly-detector/"
---

# Datadog Anomaly Detector

Leverages the Datadog API v2 metrics and events endpoints to detect anomalous patterns. Uses the Datadog Monitors API to create dynamic thresholds and sends escalations via OpsGenie REST API.

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
clawhub install datadog-anomaly-detector
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Datadog Anomaly Detector skill enables AI agents to perform proactive infrastructure monitoring by interfacing with the Datadog API v2. It queries the /api/v2/query/timeseries endpoint to pull metric data across configurable time windows, supporting all Datadog metric types including count, rate, gauge, and distribution.
Anomaly detection uses a combination of Datadog built-in anomaly functions (anomalies() with basic, agile, and robust algorithms) and custom statistical analysis. The skill creates and manages monitors via the /api/v1/monitor endpoint, implementing dynamic thresholds that adapt to seasonal patterns detected through Fourier decomposition of historical data.
When anomalies trigger, the skill creates OpsGenie alerts via the REST API v2 (/v2/alerts), attaching metric visualizations generated from the Datadog Embeddable Graphs API. Incident timelines are automatically populated with correlated events from the Datadog Events API, including recent deployments, configuration changes, and related monitor state transitions. The skill maintains an anomaly knowledge base in PostgreSQL for pattern recognition across incidents.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-anomaly-detector/)

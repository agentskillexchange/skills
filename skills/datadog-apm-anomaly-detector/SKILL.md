---
title: "Datadog APM Anomaly Detector"
description: "Detects performance anomalies in Datadog APM traces using the Datadog API v2 metrics endpoint. Applies DBSCAN clustering on latency distributions to identify outlier service behaviors."
slug: "datadog-apm-anomaly-detector"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/datadog-apm-anomaly-detector/"
---

# Datadog APM Anomaly Detector

Detects performance anomalies in Datadog APM traces using the Datadog API v2 metrics endpoint. Applies DBSCAN clustering on latency distributions to identify outlier service behaviors.

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
clawhub install datadog-apm-anomaly-detector
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Datadog APM Anomaly Detector integrates with the Datadog API v2 to pull APM trace metrics and identify performance anomalies across your service fleet. It queries the /api/v2/query/timeseries endpoint for trace duration, error rate, and throughput metrics per service-resource-operation combination. Using DBSCAN clustering on latency distributions, it identifies outlier patterns that simple threshold alerts miss: gradual degradation, bimodal latency splits, and cascading timeout chains. The skill correlates APM anomalies with infrastructure metrics (CPU, memory, network) from the same time window to suggest root causes. It supports custom faceted queries using Datadog trace search syntax and generates Notebook-compatible JSON cells for sharing investigations. Alert recommendations include suggested Datadog monitor configurations with appropriate evaluation windows, recovery thresholds, and composite conditions for reducing false positives.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-anomaly-detector/)

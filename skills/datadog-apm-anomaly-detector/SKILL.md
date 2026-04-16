---
title: "Datadog APM Anomaly Detector"
description: "Detects performance anomalies in Datadog APM traces using the Datadog API v2 metrics endpoint. Applies DBSCAN clustering on latency distributions to identify outlier service behaviors."
verification: "security_reviewed"
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
---

# Datadog APM Anomaly Detector

The Datadog APM Anomaly Detector integrates with the Datadog API v2 to pull APM trace metrics and identify performance anomalies across your service fleet. It queries the /api/v2/query/timeseries endpoint for trace duration, error rate, and throughput metrics per service-resource-operation combination. Using DBSCAN clustering on latency distributions, it identifies outlier patterns that simple threshold alerts miss: gradual degradation, bimodal latency splits, and cascading timeout chains. The skill correlates APM anomalies with infrastructure metrics (CPU, memory, network) from the same time window to suggest root causes. It supports custom faceted queries using Datadog trace search syntax and generates Notebook-compatible JSON cells for sharing investigations. Alert recommendations include suggested Datadog monitor configurations with appropriate evaluation windows, recovery thresholds, and composite conditions for reducing false positives.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-anomaly-detector/)

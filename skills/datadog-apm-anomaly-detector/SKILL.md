---
title: Datadog APM Anomaly Detector
description: 'The Datadog APM Anomaly Detector integrates with the Datadog API v2
  to pull APM trace metrics and identify performance anomalies across your service
  fleet. It queries the /api/v2/query/timeseries endpoint for trace duration, error
  rate, and throughput metrics per service-resource-operation combination. Using DBSCAN
  clustering on latency distributions, it identifies outlier patterns that simple
  threshold alerts miss: gradual degradation, bimodal latency splits, and cascading
  timeout chains. The skill correlates APM anomalies with infrastructure metrics (CPU,
  memory, network) from the same time window to suggest root causes. It supports custom
  faceted queries using Datadog trace search syntax and generates Notebook-compatible
  JSON cells for sharing investigations. Alert recommendations include suggested Datadog
  monitor configurations with appropriate evaluation windows, recovery thresholds,
  and composite conditions for reducing false positives.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/datadog-apm-anomaly-detector/
category:
- Monitoring &amp; Alerts
framework:
- ChatGPT Agents
---

# Datadog APM Anomaly Detector

The Datadog APM Anomaly Detector integrates with the Datadog API v2 to pull APM trace metrics and identify performance anomalies across your service fleet. It queries the /api/v2/query/timeseries endpoint for trace duration, error rate, and throughput metrics per service-resource-operation combination. Using DBSCAN clustering on latency distributions, it identifies outlier patterns that simple threshold alerts miss: gradual degradation, bimodal latency splits, and cascading timeout chains. The skill correlates APM anomalies with infrastructure metrics (CPU, memory, network) from the same time window to suggest root causes. It supports custom faceted queries using Datadog trace search syntax and generates Notebook-compatible JSON cells for sharing investigations. Alert recommendations include suggested Datadog monitor configurations with appropriate evaluation windows, recovery thresholds, and composite conditions for reducing false positives.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-anomaly-detector/)

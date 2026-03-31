---
name: "Datadog APM Anomaly Detector"
description: "Detects performance anomalies in Datadog APM traces using the Datadog API v2 metrics endpoint. Applies DBSCAN clustering on latency distributions to identify outlier service behaviors."
category: "Monitoring & Alerts"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/datadog-apm-anomaly-detector/"
---
# Datadog APM Anomaly Detector

Detects performance anomalies in Datadog APM traces using the Datadog API v2 metrics endpoint. Applies DBSCAN clustering on latency distributions to identify outlier service behaviors.

## Overview

The Datadog APM Anomaly Detector integrates with the Datadog API v2 to pull APM trace metrics and identify performance anomalies across your service fleet. It queries the /api/v2/query/timeseries endpoint for trace duration, error rate, and throughput metrics per service-resource-operation combination. Using DBSCAN clustering on latency distributions, it identifies outlier patterns that simple threshold alerts miss: gradual degradation, bimodal latency splits, and cascading timeout chains. The skill correlates APM anomalies with infrastructure metrics (CPU, memory, network) from the same time window to suggest root causes. It supports custom faceted queries using Datadog trace search syntax and generates Notebook-compatible JSON cells for sharing investigations. Alert recommendations include suggested Datadog monitor configurations with appropriate evaluation windows, recovery thresholds, and composite conditions for reducing false positives.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-apm-anomaly-detector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-apm-anomaly-detector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-apm-anomaly-detector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-apm-anomaly-detector -a codex
```

### OpenClaw

```bash
clawhub install datadog-apm-anomaly-detector
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-anomaly-detector/)

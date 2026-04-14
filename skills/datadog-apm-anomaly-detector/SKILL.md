---
title: "Datadog APM Anomaly Detector"
description: "Detects performance anomalies in Datadog APM traces using the Datadog API v2 metrics endpoint. Applies DBSCAN clustering on latency distributions to identify outlier service behaviors."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog APM Anomaly Detector

The Datadog APM Anomaly Detector integrates with the Datadog API v2 to pull APM trace metrics and identify performance anomalies across your service fleet. It queries the /api/v2/query/timeseries endpoint for trace duration, error rate, and throughput metrics per service-resource-operation combination. Using DBSCAN clustering on latency distributions, it identifies outlier patterns that simple threshold alerts miss: gradual degradation, bimodal latency splits, and cascading timeout chains. The skill correlates APM anomalies with infrastructure metrics (CPU, memory, network) from the same time window to suggest root causes. It supports custom faceted queries using Datadog trace search syntax and generates Notebook-compatible JSON cells for sharing investigations. Alert recommendations include suggested Datadog monitor configurations with appropriate evaluation windows, recovery thresholds, and composite conditions for reducing false positives.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-anomaly-detector/)

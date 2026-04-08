---
title: Datadog Anomaly Detection Agent
description: The Datadog Anomaly Detection Agent provides intelligent monitoring by
  connecting directly to the Datadog Metrics API v2. It continuously evaluates time-series
  data for CPU, memory, disk I/O, and custom metrics, applying statistical models
  (DBSCAN, Z-score, seasonal decomposition) to identify anomalous patterns before
  they escalate into incidents. Key capabilities include automatic threshold calibration
  based on historical baselines, multi-metric correlation to reduce false positives,
  and configurable severity levels. When anomalies are detected, the agent routes
  alerts through PagerDuty Events API v2 for on-call escalation and Slack Block Kit
  messages for team visibility. The agent supports tag-based filtering to scope monitoring
  to specific services, environments, or teams. It can also generate Datadog dashboard
  JSON definitions for visualizing detected anomalies alongside normal operating ranges.
  Configuration is YAML-driven with support for per-service override profiles.
verification: security_reviewed
source: https://agentskillexchange.com/skills/datadog-anomaly-detection-agent-2/
category:
- Monitoring &amp; Alerts
framework:
- OpenClaw
---

# Datadog Anomaly Detection Agent

The Datadog Anomaly Detection Agent provides intelligent monitoring by connecting directly to the Datadog Metrics API v2. It continuously evaluates time-series data for CPU, memory, disk I/O, and custom metrics, applying statistical models (DBSCAN, Z-score, seasonal decomposition) to identify anomalous patterns before they escalate into incidents. Key capabilities include automatic threshold calibration based on historical baselines, multi-metric correlation to reduce false positives, and configurable severity levels. When anomalies are detected, the agent routes alerts through PagerDuty Events API v2 for on-call escalation and Slack Block Kit messages for team visibility. The agent supports tag-based filtering to scope monitoring to specific services, environments, or teams. It can also generate Datadog dashboard JSON definitions for visualizing detected anomalies alongside normal operating ranges. Configuration is YAML-driven with support for per-service override profiles.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-anomaly-detection-agent-2/)

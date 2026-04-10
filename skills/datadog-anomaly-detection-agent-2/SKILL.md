---
title: "Datadog Anomaly Detection Agent"
description: "Monitors Datadog metric streams using the Datadog API v2 and applies ML-based anomaly detection to alert on infrastructure drift. Integrates with PagerDuty and Slack webhooks for multi-channel incident routing."
slug: "datadog-anomaly-detection-agent-2"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/datadog-anomaly-detection-agent-2/"
listed: true
---

# Datadog Anomaly Detection Agent

Monitors Datadog metric streams using the Datadog API v2 and applies ML-based anomaly detection to alert on infrastructure drift. Integrates with PagerDuty and Slack webhooks for multi-channel incident routing.

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
clawhub install datadog-anomaly-detection-agent-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Datadog Anomaly Detection Agent provides intelligent monitoring by connecting directly to the Datadog Metrics API v2. It continuously evaluates time-series data for CPU, memory, disk I/O, and custom metrics, applying statistical models (DBSCAN, Z-score, seasonal decomposition) to identify anomalous patterns before they escalate into incidents.
Key capabilities include automatic threshold calibration based on historical baselines, multi-metric correlation to reduce false positives, and configurable severity levels. When anomalies are detected, the agent routes alerts through PagerDuty Events API v2 for on-call escalation and Slack Block Kit messages for team visibility.
The agent supports tag-based filtering to scope monitoring to specific services, environments, or teams. It can also generate Datadog dashboard JSON definitions for visualizing detected anomalies alongside normal operating ranges. Configuration is YAML-driven with support for per-service override profiles.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-anomaly-detection-agent-2/)

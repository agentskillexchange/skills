---
title: "Datadog Anomaly Detection Agent"
description: "Monitors Datadog metric streams using the Datadog API v2 and applies ML-based anomaly detection to alert on infrastructure drift. Integrates with PagerDuty and Slack webhooks for multi-channel incident routing."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring & Alerts"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Anomaly Detection Agent

The Datadog Anomaly Detection Agent provides intelligent monitoring by connecting directly to the Datadog Metrics API v2. It continuously evaluates time-series data for CPU, memory, disk I/O, and custom metrics, applying statistical models (DBSCAN, Z-score, seasonal decomposition) to identify anomalous patterns before they escalate into incidents.

Key capabilities include automatic threshold calibration based on historical baselines, multi-metric correlation to reduce false positives, and configurable severity levels. When anomalies are detected, the agent routes alerts through PagerDuty Events API v2 for on-call escalation and Slack Block Kit messages for team visibility.

The agent supports tag-based filtering to scope monitoring to specific services, environments, or teams. It can also generate Datadog dashboard JSON definitions for visualizing detected anomalies alongside normal operating ranges. Configuration is YAML-driven with support for per-service override profiles.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-anomaly-detection-agent-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/datadog-anomaly-detection-agent-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-anomaly-detection-agent-2/)

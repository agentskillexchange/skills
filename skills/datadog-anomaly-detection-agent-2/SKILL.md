---
title: "Datadog Anomaly Detection Agent"
description: "Monitors Datadog metric streams using the Datadog API v2 and applies ML-based anomaly detection to alert on infrastructure drift. Integrates with PagerDuty and Slack webhooks for multi-channel incident routing."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring &amp; Alerts"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-anomaly-detection-agent-2/)

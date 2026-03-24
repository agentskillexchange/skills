---
name: "Datadog Anomaly Detection Agent"
description: "Monitors Datadog metric streams using the Datadog API v2 and applies ML-based anomaly detection to alert on infrastructure drift. Integrates with PagerDuty and Slack webhooks for multi-channel incident routing."
category: "Monitoring & Alerts"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/datadog-anomaly-detection-agent-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "datadog"  # from ase_tool_match
  github_stars: 787  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 6043057  # from ase_npm_downloads
  github_repo: "DataDog/dd-trace-js"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Datadog Anomaly Detection Agent

Monitors Datadog metric streams using the Datadog API v2 and applies ML-based anomaly detection to alert on infrastructure drift. Integrates with PagerDuty and Slack webhooks for multi-channel incident routing.

## Overview

The Datadog Anomaly Detection Agent provides intelligent monitoring by connecting directly to the Datadog Metrics API v2. It continuously evaluates time-series data for CPU, memory, disk I/O, and custom metrics, applying statistical models (DBSCAN, Z-score, seasonal decomposition) to identify anomalous patterns before they escalate into incidents.

Key capabilities include automatic threshold calibration based on historical baselines, multi-metric correlation to reduce false positives, and configurable severity levels. When anomalies are detected, the agent routes alerts through PagerDuty Events API v2 for on-call escalation and Slack Block Kit messages for team visibility.

The agent supports tag-based filtering to scope monitoring to specific services, environments, or teams. It can also generate Datadog dashboard JSON definitions for visualizing detected anomalies alongside normal operating ranges. Configuration is YAML-driven with support for per-service override profiles.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-anomaly-detection-agent-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-anomaly-detection-agent-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-anomaly-detection-agent-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-anomaly-detection-agent-2 -a codex
```

### OpenClaw

```bash
clawhub install datadog-anomaly-detection-agent-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/datadog-anomaly-detection-agent-2/

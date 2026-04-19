---
title: "Datadog APM Anomaly Detector"
description: "Detects performance anomalies in Datadog APM traces using the Datadog API v2 metrics endpoint. Applies DBSCAN clustering on latency distributions to identify outlier service behaviors."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring & Alerts"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog APM Anomaly Detector

Detects performance anomalies in Datadog APM traces using the Datadog API v2 metrics endpoint. Applies DBSCAN clustering on latency distributions to identify outlier service behaviors.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-apm-anomaly-detector
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/datadog-apm-anomaly-detector` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-anomaly-detector/)

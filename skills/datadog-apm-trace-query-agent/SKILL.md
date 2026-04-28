---
title: Datadog APM Trace Query Agent
description: Queries distributed traces from Datadog APM using the Trace Search API
  with faceted filtering. Analyzes p99 latency breakdowns across service spans and
  identifies slow database queries via db.statement tags.
verification: security_reviewed
source: https://github.com/DataDog/dd-trace-js
category:
- Monitoring & Alerts
framework:
- MCP
tool_ecosystem:
  github_repo: datadog/dd-trace-js
  github_stars: 791
  npm_package: dd-trace
  npm_weekly_downloads: 6596660
---

# Datadog APM Trace Query Agent

Queries distributed traces from Datadog APM using the Trace Search API with faceted filtering. Analyzes p99 latency breakdowns across service spans and identifies slow database queries via db.statement tags.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/datadog-apm-trace-query-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-apm-trace-query-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/datadog-apm-trace-query-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-trace-query-agent/)

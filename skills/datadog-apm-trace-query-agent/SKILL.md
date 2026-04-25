---
title: "Datadog APM Trace Query Agent"
description: "Queries distributed traces from Datadog APM using the Trace Search API with faceted filtering. Analyzes p99 latency breakdowns across service spans and identifies slow database queries via db.statement tags."
verification: "security_reviewed"
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring & Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog APM Trace Query Agent

The Datadog APM Trace Query Agent skill enables intelligent analysis of distributed traces collected by Datadog’s APM platform. Using the Trace Search API, it performs faceted queries across trace data filtered by service name, operation, resource, duration percentiles, and custom span tags to identify performance bottlenecks. The skill specializes in latency analysis, decomposing p99 response times across service-to-service spans in distributed architectures. It identifies slow database queries by analyzing db.statement span tags, detects N+1 query patterns through span count analysis, and correlates high-latency traces with infrastructure metrics like CPU utilization and garbage collection pauses. Advanced capabilities include trace comparison between deployment versions using the deployment.environment tag, error rate analysis with stack trace grouping, service dependency map generation from trace topology data, and retention filter optimization recommendations based on trace volume and query patterns. The skill outputs structured reports with flame graph data compatible with Datadog’s trace visualization, and supports alerting threshold recommendations based on historical latency distributions.

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

---
name: "Datadog APM Trace Query Agent"
description: "Queries distributed traces from Datadog APM using the Trace Search API with faceted filtering. Analyzes p99 latency breakdowns across service spans and identifies slow database queries via db.statement tags."
category: "Monitoring & Alerts"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
tool_ecosystem:
  tool: datadog
  github_stars: 789
  npm_weekly_downloads: 6043057
  github_repo: DataDog/dd-trace-js
  maintained: true
---
# Datadog APM Trace Query Agent

Queries distributed traces from Datadog APM using the Trace Search API with faceted filtering. Analyzes p99 latency breakdowns across service spans and identifies slow database queries via db.statement tags.

## Overview

The Datadog APM Trace Query Agent skill enables intelligent analysis of distributed traces collected by Datadog’s APM platform. Using the Trace Search API, it performs faceted queries across trace data filtered by service name, operation, resource, duration percentiles, and custom span tags to identify performance bottlenecks.

The skill specializes in latency analysis, decomposing p99 response times across service-to-service spans in distributed architectures. It identifies slow database queries by analyzing db.statement span tags, detects N+1 query patterns through span count analysis, and correlates high-latency traces with infrastructure metrics like CPU utilization and garbage collection pauses.

Advanced capabilities include trace comparison between deployment versions using the deployment.environment tag, error rate analysis with stack trace grouping, service dependency map generation from trace topology data, and retention filter optimization recommendations based on trace volume and query patterns. The skill outputs structured reports with flame graph data compatible with Datadog’s trace visualization, and supports alerting threshold recommendations based on historical latency distributions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-apm-trace-query-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-apm-trace-query-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-apm-trace-query-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-apm-trace-query-agent -a codex
```

### OpenClaw

```bash
clawhub install datadog-apm-trace-query-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-trace-query-agent/)

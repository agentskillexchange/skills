---
title: "Datadog APM Trace Query Agent"
description: "Queries distributed traces from Datadog APM using the Trace Search API with faceted filtering. Analyzes p99 latency breakdowns across service spans and identifies slow database queries via db.statement tags."
slug: "datadog-apm-trace-query-agent"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/datadog-apm-trace-query-agent/"
listed: true
---

# Datadog APM Trace Query Agent

Queries distributed traces from Datadog APM using the Trace Search API with faceted filtering. Analyzes p99 latency breakdowns across service spans and identifies slow database queries via db.statement tags.

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
clawhub install datadog-apm-trace-query-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Datadog APM Trace Query Agent skill enables intelligent analysis of distributed traces collected by Datadog’s APM platform. Using the Trace Search API, it performs faceted queries across trace data filtered by service name, operation, resource, duration percentiles, and custom span tags to identify performance bottlenecks.
The skill specializes in latency analysis, decomposing p99 response times across service-to-service spans in distributed architectures. It identifies slow database queries by analyzing db.statement span tags, detects N+1 query patterns through span count analysis, and correlates high-latency traces with infrastructure metrics like CPU utilization and garbage collection pauses.
Advanced capabilities include trace comparison between deployment versions using the deployment.environment tag, error rate analysis with stack trace grouping, service dependency map generation from trace topology data, and retention filter optimization recommendations based on trace volume and query patterns. The skill outputs structured reports with flame graph data compatible with Datadog’s trace visualization, and supports alerting threshold recommendations based on historical latency distributions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-trace-query-agent/)

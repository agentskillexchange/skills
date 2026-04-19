---
title: "Datadog APM Trace Query Agent"
description: "The Datadog APM Trace Query Agent skill enables intelligent analysis of distributed traces collected by Datadog&#8217;s APM platform. Using the Trace Search API, it performs faceted queries across trace data filtered by service name, operation, resource, duration percentiles, and custom span tags to identify performance bottlenecks. The skill specializes in latency analysis, decomposing p99 response times across service-to-service spans in distributed architectures. It identifies slow database queries by analyzing db.statement span tags, detects N+1 query patterns through span count analysis, and correlates high-latency traces with infrastructure metrics like CPU utilization and garbage collection pauses. Advanced capabilities include trace comparison between deployment versions using the deployment.environment tag, error rate analysis with stack trace grouping, service dependency map generation from trace topology data, and retention filter optimization recommendations based on trace volume and query patterns. The skill outputs structured reports with flame graph data compatible with Datadog&#8217;s trace visualization, and supports alerting threshold recommendations based on historical latency distributions."
source: "https://github.com/DataDog/dd-trace-js"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog APM Trace Query Agent

The Datadog APM Trace Query Agent skill enables intelligent analysis of distributed traces collected by Datadog&#8217;s APM platform. Using the Trace Search API, it performs faceted queries across trace data filtered by service name, operation, resource, duration percentiles, and custom span tags to identify performance bottlenecks. The skill specializes in latency analysis, decomposing p99 response times across service-to-service spans in distributed architectures. It identifies slow database queries by analyzing db.statement span tags, detects N+1 query patterns through span count analysis, and correlates high-latency traces with infrastructure metrics like CPU utilization and garbage collection pauses. Advanced capabilities include trace comparison between deployment versions using the deployment.environment tag, error rate analysis with stack trace grouping, service dependency map generation from trace topology data, and retention filter optimization recommendations based on trace volume and query patterns. The skill outputs structured reports with flame graph data compatible with Datadog&#8217;s trace visualization, and supports alerting threshold recommendations based on historical latency distributions.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-trace-query-agent/)

---
title: "Datadog APM Trace Analyzer"
description: "The Datadog APM Trace Analyzer skill connects to the Datadog Tracing API v2 to retrieve and analyze distributed trace data across microservice architectures. It queries trace search endpoints with faceted filters for service name, resource, duration percentiles, and error status to identify latency bottlenecks and high-error-rate endpoints. The skill generates flame graph summaries that highlight the slowest spans in each trace, calculates service-level p50/p95/p99 latency metrics, and maps upstream and downstream dependency impacts using the Datadog Service Map API. It configures custom trace metrics using the Datadog Metrics API for ongoing monitoring, sets up anomaly detection monitors for sudden latency spikes, and produces root cause analysis reports correlating trace degradation with recent deployments via the Datadog Events API. Output includes actionable recommendations with specific span-level optimization targets."
source: "https://github.com/DataDog/dd-trace-js"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog APM Trace Analyzer

The Datadog APM Trace Analyzer skill connects to the Datadog Tracing API v2 to retrieve and analyze distributed trace data across microservice architectures. It queries trace search endpoints with faceted filters for service name, resource, duration percentiles, and error status to identify latency bottlenecks and high-error-rate endpoints. The skill generates flame graph summaries that highlight the slowest spans in each trace, calculates service-level p50/p95/p99 latency metrics, and maps upstream and downstream dependency impacts using the Datadog Service Map API. It configures custom trace metrics using the Datadog Metrics API for ongoing monitoring, sets up anomaly detection monitors for sudden latency spikes, and produces root cause analysis reports correlating trace degradation with recent deployments via the Datadog Events API. Output includes actionable recommendations with specific span-level optimization targets.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-trace-analyzer-2/)

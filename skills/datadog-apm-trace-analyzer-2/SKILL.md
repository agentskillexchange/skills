---
title: Datadog APM Trace Analyzer
description: The Datadog APM Trace Analyzer skill connects to the Datadog Tracing
  API v2 to retrieve and analyze distributed trace data across microservice architectures.
  It queries trace search endpoints with faceted filters for service name, resource,
  duration percentiles, and error status to identify latency bottlenecks and high-error-rate
  endpoints. The skill generates flame graph summaries that highlight the slowest
  spans in each trace, calculates service-level p50/p95/p99 latency metrics, and maps
  upstream and downstream dependency impacts using the Datadog Service Map API. It
  configures custom trace metrics using the Datadog Metrics API for ongoing monitoring,
  sets up anomaly detection monitors for sudden latency spikes, and produces root
  cause analysis reports correlating trace degradation with recent deployments via
  the Datadog Events API. Output includes actionable recommendations with specific
  span-level optimization targets.
verification: security_reviewed
source: https://agentskillexchange.com/skills/datadog-apm-trace-analyzer-2/
category:
- Monitoring &amp; Alerts
framework:
- Claude Agents
---

# Datadog APM Trace Analyzer

The Datadog APM Trace Analyzer skill connects to the Datadog Tracing API v2 to retrieve and analyze distributed trace data across microservice architectures. It queries trace search endpoints with faceted filters for service name, resource, duration percentiles, and error status to identify latency bottlenecks and high-error-rate endpoints. The skill generates flame graph summaries that highlight the slowest spans in each trace, calculates service-level p50/p95/p99 latency metrics, and maps upstream and downstream dependency impacts using the Datadog Service Map API. It configures custom trace metrics using the Datadog Metrics API for ongoing monitoring, sets up anomaly detection monitors for sudden latency spikes, and produces root cause analysis reports correlating trace degradation with recent deployments via the Datadog Events API. Output includes actionable recommendations with specific span-level optimization targets.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-trace-analyzer-2/)

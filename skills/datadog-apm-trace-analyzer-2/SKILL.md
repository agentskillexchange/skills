---
title: "Datadog APM Trace Analyzer"
description: "Queries Datadog APM trace data via the Datadog Tracing API v2 to identify latency bottlenecks and error hotspots. Generates flame graph summaries and service dependency impact reports."
verification: "security_reviewed"
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Agents"
---

# Datadog APM Trace Analyzer

The Datadog APM Trace Analyzer skill connects to the Datadog Tracing API v2 to retrieve and analyze distributed trace data across microservice architectures. It queries trace search endpoints with faceted filters for service name, resource, duration percentiles, and error status to identify latency bottlenecks and high-error-rate endpoints. The skill generates flame graph summaries that highlight the slowest spans in each trace, calculates service-level p50/p95/p99 latency metrics, and maps upstream and downstream dependency impacts using the Datadog Service Map API. It configures custom trace metrics using the Datadog Metrics API for ongoing monitoring, sets up anomaly detection monitors for sudden latency spikes, and produces root cause analysis reports correlating trace degradation with recent deployments via the Datadog Events API. Output includes actionable recommendations with specific span-level optimization targets.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-trace-analyzer-2/)

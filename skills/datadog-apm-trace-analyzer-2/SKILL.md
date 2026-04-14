---
title: "Datadog APM Trace Analyzer"
description: "Queries Datadog APM trace data via the Datadog Tracing API v2 to identify latency bottlenecks and error hotspots. Generates flame graph summaries and service dependency impact reports."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-apm-trace-analyzer-2/)

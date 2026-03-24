---
name: "Datadog APM Trace Analyzer"
description: "Queries Datadog APM trace data via the Datadog Tracing API v2 to identify latency bottlenecks and error hotspots. Generates flame graph summaries and service dependency impact reports."
category: "Monitoring & Alerts"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/datadog-apm-trace-analyzer-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "datadog"  # from ase_tool_match
  github_stars: 787  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 6043057  # from ase_npm_downloads
  github_repo: "DataDog/dd-trace-js"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Datadog APM Trace Analyzer

Queries Datadog APM trace data via the Datadog Tracing API v2 to identify latency bottlenecks and error hotspots. Generates flame graph summaries and service dependency impact reports.

## Overview

The Datadog APM Trace Analyzer skill connects to the Datadog Tracing API v2 to retrieve and analyze distributed trace data across microservice architectures. It queries trace search endpoints with faceted filters for service name, resource, duration percentiles, and error status to identify latency bottlenecks and high-error-rate endpoints. The skill generates flame graph summaries that highlight the slowest spans in each trace, calculates service-level p50/p95/p99 latency metrics, and maps upstream and downstream dependency impacts using the Datadog Service Map API. It configures custom trace metrics using the Datadog Metrics API for ongoing monitoring, sets up anomaly detection monitors for sudden latency spikes, and produces root cause analysis reports correlating trace degradation with recent deployments via the Datadog Events API. Output includes actionable recommendations with specific span-level optimization targets.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-apm-trace-analyzer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-apm-trace-analyzer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-apm-trace-analyzer-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-apm-trace-analyzer-2 -a codex
```

### OpenClaw

```bash
clawhub install datadog-apm-trace-analyzer-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/datadog-apm-trace-analyzer-2/

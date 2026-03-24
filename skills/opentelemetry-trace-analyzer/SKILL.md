---
name: "OpenTelemetry Trace Analyzer"
description: "Queries distributed traces from Jaeger and Tempo via their gRPC and HTTP APIs. Identifies latency bottlenecks using OpenTelemetry Collector processors and correlates with Loki log streams."
category: "Library & API Reference"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/opentelemetry-trace-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "grafana"  # from ase_tool_match
  github_stars: 72784  # from ase_github_stars (integer, not string)
  github_repo: "grafana/grafana"  # from ase_github_repo
  license: "AGPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OpenTelemetry Trace Analyzer

Queries distributed traces from Jaeger and Tempo via their gRPC and HTTP APIs. Identifies latency bottlenecks using OpenTelemetry Collector processors and correlates with Loki log streams.

## Overview

The OpenTelemetry Trace Analyzer skill provides deep observability insights by querying distributed tracing backends. It supports Jaeger Query API (/api/traces/{traceID}) and Grafana Tempo HTTP API (/api/traces/{traceID}) for trace retrieval, with automatic backend detection based on configured endpoints.

Trace analysis identifies latency bottlenecks by computing critical path analysis across span trees, highlighting services contributing the most to end-to-end request duration. The skill processes span attributes and events following OpenTelemetry Semantic Conventions, extracting HTTP status codes, database query durations, and messaging queue wait times for structured analysis.

Log correlation connects trace context (trace_id, span_id) to Grafana Loki log streams via the LogQL API (/loki/api/v1/query_range), displaying relevant log lines alongside trace spans for root cause analysis. The skill configures OpenTelemetry Collector pipeline processors including tail-based sampling (probabilistic and rate-limiting) and span metrics generation via the spanmetrics connector. Results are visualized through Grafana dashboard JSON models pushed via the Grafana HTTP API (/api/dashboards/db), creating service dependency graphs and latency heatmaps from TraceQL query results.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill opentelemetry-trace-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill opentelemetry-trace-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill opentelemetry-trace-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill opentelemetry-trace-analyzer -a codex
```

### OpenClaw

```bash
clawhub install opentelemetry-trace-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/opentelemetry-trace-analyzer/

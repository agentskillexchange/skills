---
title: "OpenTelemetry Trace Analyzer"
description: "Queries distributed traces from Jaeger and Tempo via their gRPC and HTTP APIs. Identifies latency bottlenecks using OpenTelemetry Collector processors and correlates with Loki log streams."
verification: "security_reviewed"
source: "https://opentelemetry.io/"
category:
  - "Library & API Reference"
framework:
  - "Codex"
---

# OpenTelemetry Trace Analyzer

The OpenTelemetry Trace Analyzer skill provides deep observability insights by querying distributed tracing backends. It supports Jaeger Query API (/api/traces/{traceID}) and Grafana Tempo HTTP API (/api/traces/{traceID}) for trace retrieval, with automatic backend detection based on configured endpoints. Trace analysis identifies latency bottlenecks by computing critical path analysis across span trees, highlighting services contributing the most to end-to-end request duration. The skill processes span attributes and events following OpenTelemetry Semantic Conventions, extracting HTTP status codes, database query durations, and messaging queue wait times for structured analysis. Log correlation connects trace context (trace_id, span_id) to Grafana Loki log streams via the LogQL API (/loki/api/v1/query_range), displaying relevant log lines alongside trace spans for root cause analysis. The skill configures OpenTelemetry Collector pipeline processors including tail-based sampling (probabilistic and rate-limiting) and span metrics generation via the spanmetrics connector. Results are visualized through Grafana dashboard JSON models pushed via the Grafana HTTP API (/api/dashboards/db), creating service dependency graphs and latency heatmaps from TraceQL query results.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/opentelemetry-trace-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/opentelemetry-trace-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/opentelemetry-trace-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-analyzer/)

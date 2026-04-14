---
title: "OpenTelemetry Trace Analyzer"
description: "Queries distributed traces from Jaeger and Tempo via their gRPC and HTTP APIs. Identifies latency bottlenecks using OpenTelemetry Collector processors and correlates with Loki log streams."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/opentelemetry-trace-analyzer/"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
---

# OpenTelemetry Trace Analyzer

The OpenTelemetry Trace Analyzer skill provides deep observability insights by querying distributed tracing backends. It supports Jaeger Query API (/api/traces/{traceID}) and Grafana Tempo HTTP API (/api/traces/{traceID}) for trace retrieval, with automatic backend detection based on configured endpoints.

Trace analysis identifies latency bottlenecks by computing critical path analysis across span trees, highlighting services contributing the most to end-to-end request duration. The skill processes span attributes and events following OpenTelemetry Semantic Conventions, extracting HTTP status codes, database query durations, and messaging queue wait times for structured analysis.

Log correlation connects trace context (trace_id, span_id) to Grafana Loki log streams via the LogQL API (/loki/api/v1/query_range), displaying relevant log lines alongside trace spans for root cause analysis. The skill configures OpenTelemetry Collector pipeline processors including tail-based sampling (probabilistic and rate-limiting) and span metrics generation via the spanmetrics connector. Results are visualized through Grafana dashboard JSON models pushed via the Grafana HTTP API (/api/dashboards/db), creating service dependency graphs and latency heatmaps from TraceQL query results.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-analyzer/)

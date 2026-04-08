---
title: OpenTelemetry Trace Analyzer
description: The OpenTelemetry Trace Analyzer skill provides deep observability insights
  by querying distributed tracing backends. It supports Jaeger Query API (/api/traces/{traceID})
  and Grafana Tempo HTTP API (/api/traces/{traceID}) for trace retrieval, with automatic
  backend detection based on configured endpoints. Trace analysis identifies latency
  bottlenecks by computing critical path analysis across span trees, highlighting
  services contributing the most to end-to-end request duration. The skill processes
  span attributes and events following OpenTelemetry Semantic Conventions, extracting
  HTTP status codes, database query durations, and messaging queue wait times for
  structured analysis. Log correlation connects trace context (trace_id, span_id)
  to Grafana Loki log streams via the LogQL API (/loki/api/v1/query_range), displaying
  relevant log lines alongside trace spans for root cause analysis. The skill configures
  OpenTelemetry Collector pipeline processors including tail-based sampling (probabilistic
  and rate-limiting) and span metrics generation via the spanmetrics connector. Results
  are visualized through Grafana dashboard JSON models pushed via the Grafana HTTP
  API (/api/dashboards/db), creating service dependency graphs and latency heatmaps
  from TraceQL query results.
verification: security_reviewed
source: https://agentskillexchange.com/skills/opentelemetry-trace-analyzer/
category:
- Library &amp; API Reference
framework:
- Codex
---

# OpenTelemetry Trace Analyzer

The OpenTelemetry Trace Analyzer skill provides deep observability insights by querying distributed tracing backends. It supports Jaeger Query API (/api/traces/{traceID}) and Grafana Tempo HTTP API (/api/traces/{traceID}) for trace retrieval, with automatic backend detection based on configured endpoints. Trace analysis identifies latency bottlenecks by computing critical path analysis across span trees, highlighting services contributing the most to end-to-end request duration. The skill processes span attributes and events following OpenTelemetry Semantic Conventions, extracting HTTP status codes, database query durations, and messaging queue wait times for structured analysis. Log correlation connects trace context (trace_id, span_id) to Grafana Loki log streams via the LogQL API (/loki/api/v1/query_range), displaying relevant log lines alongside trace spans for root cause analysis. The skill configures OpenTelemetry Collector pipeline processors including tail-based sampling (probabilistic and rate-limiting) and span metrics generation via the spanmetrics connector. Results are visualized through Grafana dashboard JSON models pushed via the Grafana HTTP API (/api/dashboards/db), creating service dependency graphs and latency heatmaps from TraceQL query results.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-analyzer/)

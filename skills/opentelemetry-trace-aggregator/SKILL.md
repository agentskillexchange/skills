---
name: "OpenTelemetry Trace Aggregator"
description: "Aggregates OpenTelemetry trace spans from Jaeger and Zipkin backends into unified flame graphs. Uses the OTLP gRPC exporter SDK to correlate distributed service calls across microservice boundaries."
category: "Monitoring & Alerts"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/opentelemetry-trace-aggregator/"
tool_ecosystem:
  tool: kubernetes
  github_stars: 121334
  github_repo: kubernetes/kubernetes
  license: Apache-2.0
  maintained: true
---

# OpenTelemetry Trace Aggregator

Aggregates OpenTelemetry trace spans from Jaeger and Zipkin backends into unified flame graphs. Uses the OTLP gRPC exporter SDK to correlate distributed service calls across microservice boundaries.

## Overview

The OpenTelemetry Trace Aggregator skill provides deep integration with the OpenTelemetry Collector and its OTLP gRPC/HTTP exporters. It connects to Jaeger, Zipkin, and Tempo backends to pull trace data, then reconstructs distributed call graphs across microservice boundaries. The skill uses the opentelemetry-sdk Python package to parse SpanContext propagation headers (W3C TraceContext and B3) and build unified flame graphs. It supports tail-based sampling configuration, trace ID lookup, and latency percentile analysis (p50, p95, p99). Engineers can query traces by service name, operation, duration threshold, or error status. The output includes Mermaid sequence diagrams showing inter-service communication patterns, making it invaluable for debugging latency spikes in distributed systems. Compatible with Kubernetes service meshes running Istio or Linkerd sidecars.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill opentelemetry-trace-aggregator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill opentelemetry-trace-aggregator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill opentelemetry-trace-aggregator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill opentelemetry-trace-aggregator -a codex
```

### OpenClaw

```bash
clawhub install opentelemetry-trace-aggregator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/opentelemetry-trace-aggregator/

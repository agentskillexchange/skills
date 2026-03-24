---
name: "OpenTelemetry Trace Aggregator"
description: "Aggregates OpenTelemetry trace spans from Jaeger and Zipkin backends into unified flame graphs. Uses the OTLP gRPC exporter SDK to correlate distributed service calls across microservice boundaries."
category: "Monitoring & Alerts"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/opentelemetry-trace-aggregator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

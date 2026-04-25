---
title: "OpenTelemetry Trace Aggregator"
description: "Aggregates OpenTelemetry trace spans from Jaeger and Zipkin backends into unified flame graphs. Uses the OTLP gRPC exporter SDK to correlate distributed service calls across microservice boundaries."
verification: "security_reviewed"
source: "https://opentelemetry.io/"
category:
  - "Monitoring & Alerts"
framework:
  - "OpenClaw"
---

# OpenTelemetry Trace Aggregator

The OpenTelemetry Trace Aggregator skill provides deep integration with the OpenTelemetry Collector and its OTLP gRPC/HTTP exporters. It connects to Jaeger, Zipkin, and Tempo backends to pull trace data, then reconstructs distributed call graphs across microservice boundaries. The skill uses the opentelemetry-sdk Python package to parse SpanContext propagation headers (W3C TraceContext and B3) and build unified flame graphs. It supports tail-based sampling configuration, trace ID lookup, and latency percentile analysis (p50, p95, p99). Engineers can query traces by service name, operation, duration threshold, or error status. The output includes Mermaid sequence diagrams showing inter-service communication patterns, making it invaluable for debugging latency spikes in distributed systems. Compatible with Kubernetes service meshes running Istio or Linkerd sidecars.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/opentelemetry-trace-aggregator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/opentelemetry-trace-aggregator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/opentelemetry-trace-aggregator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-aggregator/)

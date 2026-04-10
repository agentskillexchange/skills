---
title: "OpenTelemetry Trace Aggregator"
description: "Aggregates OpenTelemetry trace spans from Jaeger and Zipkin backends into unified flame graphs. Uses the OTLP gRPC exporter SDK to correlate distributed service calls across microservice boundaries."
slug: "opentelemetry-trace-aggregator"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/opentelemetry-trace-aggregator/"
listed: true
---

# OpenTelemetry Trace Aggregator

Aggregates OpenTelemetry trace spans from Jaeger and Zipkin backends into unified flame graphs. Uses the OTLP gRPC exporter SDK to correlate distributed service calls across microservice boundaries.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install opentelemetry-trace-aggregator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The OpenTelemetry Trace Aggregator skill provides deep integration with the OpenTelemetry Collector and its OTLP gRPC/HTTP exporters. It connects to Jaeger, Zipkin, and Tempo backends to pull trace data, then reconstructs distributed call graphs across microservice boundaries. The skill uses the opentelemetry-sdk Python package to parse SpanContext propagation headers (W3C TraceContext and B3) and build unified flame graphs. It supports tail-based sampling configuration, trace ID lookup, and latency percentile analysis (p50, p95, p99). Engineers can query traces by service name, operation, duration threshold, or error status. The output includes Mermaid sequence diagrams showing inter-service communication patterns, making it invaluable for debugging latency spikes in distributed systems. Compatible with Kubernetes service meshes running Istio or Linkerd sidecars.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-aggregator/)

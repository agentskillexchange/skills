---
name: OpenTelemetry Trace Aggregator
description: Aggregates OpenTelemetry trace spans from Jaeger and Zipkin backends
  into unified flame graphs. Uses the OTLP gRPC exporter SDK to correlate distributed
  service calls across microservice boundaries.
verification: security_reviewed
source: https://agentskillexchange.com/skills/opentelemetry-trace-aggregator/
category:
- Monitoring &amp; Alerts
framework:
- OpenClaw
---
# OpenTelemetry Trace Aggregator

The OpenTelemetry Trace Aggregator skill provides deep integration with the OpenTelemetry Collector and its OTLP gRPC/HTTP exporters. It connects to Jaeger, Zipkin, and Tempo backends to pull trace data, then reconstructs distributed call graphs across microservice boundaries. The skill uses the opentelemetry-sdk Python package to parse SpanContext propagation headers (W3C TraceContext and B3) and build unified flame graphs. It supports tail-based sampling configuration, trace ID lookup, and latency percentile analysis (p50, p95, p99). Engineers can query traces by service name, operation, duration threshold, or error status. The output includes Mermaid sequence diagrams showing inter-service communication patterns, making it invaluable for debugging latency spikes in distributed systems. Compatible with Kubernetes service meshes running Istio or Linkerd sidecars.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-aggregator/)

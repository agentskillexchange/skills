---
title: OpenTelemetry Trace Aggregator
description: The OpenTelemetry Trace Aggregator skill provides deep integration with
  the OpenTelemetry Collector and its OTLP gRPC/HTTP exporters. It connects to Jaeger,
  Zipkin, and Tempo backends to pull trace data, then reconstructs distributed call
  graphs across microservice boundaries. The skill uses the opentelemetry-sdk Python
  package to parse SpanContext propagation headers (W3C TraceContext and B3) and build
  unified flame graphs. It supports tail-based sampling configuration, trace ID lookup,
  and latency percentile analysis (p50, p95, p99). Engineers can query traces by service
  name, operation, duration threshold, or error status. The output includes Mermaid
  sequence diagrams showing inter-service communication patterns, making it invaluable
  for debugging latency spikes in distributed systems. Compatible with Kubernetes
  service meshes running Istio or Linkerd sidecars.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-aggregator/)

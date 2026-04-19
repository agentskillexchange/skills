---
title: "OpenTelemetry Trace Aggregator"
description: "The OpenTelemetry Trace Aggregator skill provides deep integration with the OpenTelemetry Collector and its OTLP gRPC/HTTP exporters. It connects to Jaeger, Zipkin, and Tempo backends to pull trace data, then reconstructs distributed call graphs across microservice boundaries. The skill uses the opentelemetry-sdk Python package to parse SpanContext propagation headers (W3C TraceContext and B3) and build unified flame graphs. It supports tail-based sampling configuration, trace ID lookup, and latency percentile analysis (p50, p95, p99). Engineers can query traces by service name, operation, duration threshold, or error status. The output includes Mermaid sequence diagrams showing inter-service communication patterns, making it invaluable for debugging latency spikes in distributed systems. Compatible with Kubernetes service meshes running Istio or Linkerd sidecars."
source: "https://agentskillexchange.com/skills/opentelemetry-trace-aggregator/"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
---

# OpenTelemetry Trace Aggregator

The OpenTelemetry Trace Aggregator skill provides deep integration with the OpenTelemetry Collector and its OTLP gRPC/HTTP exporters. It connects to Jaeger, Zipkin, and Tempo backends to pull trace data, then reconstructs distributed call graphs across microservice boundaries. The skill uses the opentelemetry-sdk Python package to parse SpanContext propagation headers (W3C TraceContext and B3) and build unified flame graphs. It supports tail-based sampling configuration, trace ID lookup, and latency percentile analysis (p50, p95, p99). Engineers can query traces by service name, operation, duration threshold, or error status. The output includes Mermaid sequence diagrams showing inter-service communication patterns, making it invaluable for debugging latency spikes in distributed systems. Compatible with Kubernetes service meshes running Istio or Linkerd sidecars.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-aggregator/)

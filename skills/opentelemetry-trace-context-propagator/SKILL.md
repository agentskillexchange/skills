---
title: "OpenTelemetry Trace Context Propagator"
description: "Implements W3C TraceContext and Baggage propagation using the OpenTelemetry JS SDK and @opentelemetry/api. Injects and extracts trace context headers (traceparent, tracestate) across HTTP, gRPC, and message queue boundaries. Integrates with Jaeger, Zipkin, and OTLP exporters for distributed trace correlation."
verification: "security_reviewed"
source: "https://opentelemetry.io/docs/languages/js/propagation/"
category:
  - "Library & API Reference"
framework:
  - "Claude Code"
---

# OpenTelemetry Trace Context Propagator

This skill provides a complete OpenTelemetry trace context propagation implementation using the @opentelemetry/api and @opentelemetry/sdk-trace-node packages. It configures the W3CTraceContextPropagator and W3CBaggagePropagator for injecting and extracting traceparent, tracestate, and baggage headers across HTTP requests via the @opentelemetry/instrumentation-http module. For gRPC services it uses the @opentelemetry/instrumentation-grpc interceptor. Message queue propagation covers AWS SQS message attributes and Kafka headers using the @opentelemetry/instrumentation-aws-sdk and kafkajs context injection. The skill configures OTLP exporters for Jaeger and Zipkin, with sampling strategies including parent-based and trace-id ratio samplers. Resource detectors for AWS ECS and GCP Cloud Run automatically populate service metadata. Includes setup for the OpenTelemetry Collector as an aggregation layer.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/opentelemetry-trace-context-propagator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/opentelemetry-trace-context-propagator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/opentelemetry-trace-context-propagator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-context-propagator/)

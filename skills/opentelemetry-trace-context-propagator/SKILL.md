---
title: "OpenTelemetry Trace Context Propagator"
description: "Implements W3C TraceContext and Baggage propagation using the OpenTelemetry JS SDK and @opentelemetry/api. Injects and extracts trace context headers (traceparent, tracestate) across HTTP, gRPC, and message queue boundaries. Integrates with Jaeger, Zipkin, and OTLP exporters for distributed trace correlation."
slug: "opentelemetry-trace-context-propagator"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/opentelemetry-trace-context-propagator/"
listed: true
---

# OpenTelemetry Trace Context Propagator

Implements W3C TraceContext and Baggage propagation using the OpenTelemetry JS SDK and @opentelemetry/api. Injects and extracts trace context headers (traceparent, tracestate) across HTTP, gRPC, and message queue boundaries. Integrates with Jaeger, Zipkin, and OTLP exporters for distributed trace correlation.

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
clawhub install opentelemetry-trace-context-propagator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill provides a complete OpenTelemetry trace context propagation implementation using the @opentelemetry/api and @opentelemetry/sdk-trace-node packages. It configures the W3CTraceContextPropagator and W3CBaggagePropagator for injecting and extracting traceparent, tracestate, and baggage headers across HTTP requests via the @opentelemetry/instrumentation-http module. For gRPC services it uses the @opentelemetry/instrumentation-grpc interceptor. Message queue propagation covers AWS SQS message attributes and Kafka headers using the @opentelemetry/instrumentation-aws-sdk and kafkajs context injection. The skill configures OTLP exporters for Jaeger and Zipkin, with sampling strategies including parent-based and trace-id ratio samplers. Resource detectors for AWS ECS and GCP Cloud Run automatically populate service metadata. Includes setup for the OpenTelemetry Collector as an aggregation layer.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-context-propagator/)

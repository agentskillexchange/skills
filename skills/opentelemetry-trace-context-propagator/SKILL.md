---
name: "OpenTelemetry Trace Context Propagator"
description: "Implements W3C TraceContext and Baggage propagation using the OpenTelemetry JS SDK and @opentelemetry/api. Injects and extracts trace context headers (traceparent, tracestate) across HTTP, gRPC, and message queue boundaries. Integrates with Jaeger, Zipkin, and OTLP exporters for distributed trace correlation."
category: "Library & API Reference"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/opentelemetry-trace-context-propagator/"
---
# OpenTelemetry Trace Context Propagator

Implements W3C TraceContext and Baggage propagation using the OpenTelemetry JS SDK and @opentelemetry/api. Injects and extracts trace context headers (traceparent, tracestate) across HTTP, gRPC, and message queue boundaries. Integrates with Jaeger, Zipkin, and OTLP exporters for distributed trace correlation.

## Overview

This skill provides a complete OpenTelemetry trace context propagation implementation using the @opentelemetry/api and @opentelemetry/sdk-trace-node packages. It configures the W3CTraceContextPropagator and W3CBaggagePropagator for injecting and extracting traceparent, tracestate, and baggage headers across HTTP requests via the @opentelemetry/instrumentation-http module. For gRPC services it uses the @opentelemetry/instrumentation-grpc interceptor. Message queue propagation covers AWS SQS message attributes and Kafka headers using the @opentelemetry/instrumentation-aws-sdk and kafkajs context injection. The skill configures OTLP exporters for Jaeger and Zipkin, with sampling strategies including parent-based and trace-id ratio samplers. Resource detectors for AWS ECS and GCP Cloud Run automatically populate service metadata. Includes setup for the OpenTelemetry Collector as an aggregation layer.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill opentelemetry-trace-context-propagator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill opentelemetry-trace-context-propagator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill opentelemetry-trace-context-propagator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill opentelemetry-trace-context-propagator -a codex
```

### OpenClaw

```bash
clawhub install opentelemetry-trace-context-propagator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-context-propagator/)

---
title: "OpenTelemetry Trace Context Propagator"
description: "This skill provides a complete OpenTelemetry trace context propagation implementation using the @opentelemetry/api and @opentelemetry/sdk-trace-node packages. It configures the W3CTraceContextPropagator and W3CBaggagePropagator for injecting and extracting traceparent, tracestate, and baggage headers across HTTP requests via the @opentelemetry/instrumentation-http module. For gRPC services it uses the @opentelemetry/instrumentation-grpc interceptor. Message queue propagation covers AWS SQS message attributes and Kafka headers using the @opentelemetry/instrumentation-aws-sdk and kafkajs context injection. The skill configures OTLP exporters for Jaeger and Zipkin, with sampling strategies including parent-based and trace-id ratio samplers. Resource detectors for AWS ECS and GCP Cloud Run automatically populate service metadata. Includes setup for the OpenTelemetry Collector as an aggregation layer."
source: "https://agentskillexchange.com/skills/opentelemetry-trace-context-propagator/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
---

# OpenTelemetry Trace Context Propagator

This skill provides a complete OpenTelemetry trace context propagation implementation using the @opentelemetry/api and @opentelemetry/sdk-trace-node packages. It configures the W3CTraceContextPropagator and W3CBaggagePropagator for injecting and extracting traceparent, tracestate, and baggage headers across HTTP requests via the @opentelemetry/instrumentation-http module. For gRPC services it uses the @opentelemetry/instrumentation-grpc interceptor. Message queue propagation covers AWS SQS message attributes and Kafka headers using the @opentelemetry/instrumentation-aws-sdk and kafkajs context injection. The skill configures OTLP exporters for Jaeger and Zipkin, with sampling strategies including parent-based and trace-id ratio samplers. Resource detectors for AWS ECS and GCP Cloud Run automatically populate service metadata. Includes setup for the OpenTelemetry Collector as an aggregation layer.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-context-propagator/)

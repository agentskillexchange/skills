---
title: OpenTelemetry Trace Context Propagator
description: This skill provides a complete OpenTelemetry trace context propagation
  implementation using the @opentelemetry/api and @opentelemetry/sdk-trace-node packages.
  It configures the W3CTraceContextPropagator and W3CBaggagePropagator for injecting
  and extracting traceparent, tracestate, and baggage headers across HTTP requests
  via the @opentelemetry/instrumentation-http module. For gRPC services it uses the
  @opentelemetry/instrumentation-grpc interceptor. Message queue propagation covers
  AWS SQS message attributes and Kafka headers using the @opentelemetry/instrumentation-aws-sdk
  and kafkajs context injection. The skill configures OTLP exporters for Jaeger and
  Zipkin, with sampling strategies including parent-based and trace-id ratio samplers.
  Resource detectors for AWS ECS and GCP Cloud Run automatically populate service
  metadata. Includes setup for the OpenTelemetry Collector as an aggregation layer.
verification: security_reviewed
source: https://agentskillexchange.com/skills/opentelemetry-trace-context-propagator/
category:
- Library &amp; API Reference
framework:
- Claude Code
---

# OpenTelemetry Trace Context Propagator

This skill provides a complete OpenTelemetry trace context propagation implementation using the @opentelemetry/api and @opentelemetry/sdk-trace-node packages. It configures the W3CTraceContextPropagator and W3CBaggagePropagator for injecting and extracting traceparent, tracestate, and baggage headers across HTTP requests via the @opentelemetry/instrumentation-http module. For gRPC services it uses the @opentelemetry/instrumentation-grpc interceptor. Message queue propagation covers AWS SQS message attributes and Kafka headers using the @opentelemetry/instrumentation-aws-sdk and kafkajs context injection. The skill configures OTLP exporters for Jaeger and Zipkin, with sampling strategies including parent-based and trace-id ratio samplers. Resource detectors for AWS ECS and GCP Cloud Run automatically populate service metadata. Includes setup for the OpenTelemetry Collector as an aggregation layer.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-context-propagator/)

---
title: "OpenTelemetry Trace Context Propagator"
description: "Implements W3C TraceContext and Baggage propagation using the OpenTelemetry JS SDK and @opentelemetry/api. Injects and extracts trace context headers (traceparent, tracestate) across HTTP, gRPC, and message queue boundaries. Integrates with Jaeger, Zipkin, and OTLP exporters for distributed trace correlation."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/opentelemetry-trace-context-propagator/"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
---

# OpenTelemetry Trace Context Propagator

This skill provides a complete OpenTelemetry trace context propagation implementation using the @opentelemetry/api and @opentelemetry/sdk-trace-node packages. It configures the W3CTraceContextPropagator and W3CBaggagePropagator for injecting and extracting traceparent, tracestate, and baggage headers across HTTP requests via the @opentelemetry/instrumentation-http module. For gRPC services it uses the @opentelemetry/instrumentation-grpc interceptor. Message queue propagation covers AWS SQS message attributes and Kafka headers using the @opentelemetry/instrumentation-aws-sdk and kafkajs context injection. The skill configures OTLP exporters for Jaeger and Zipkin, with sampling strategies including parent-based and trace-id ratio samplers. Resource detectors for AWS ECS and GCP Cloud Run automatically populate service metadata. Includes setup for the OpenTelemetry Collector as an aggregation layer.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentelemetry-trace-context-propagator/)

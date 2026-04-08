---
title: OpenTelemetry Collector Pipeline Designer
description: The OpenTelemetry Collector Pipeline Designer skill generates comprehensive
  otel-collector configuration files for telemetry data routing and transformation.
  It configures receivers including otlp (gRPC/HTTP), prometheus for metric scraping
  with scrape_configs, filelog for structured log ingestion with multiline parsing,
  and hostmetrics for system-level CPU/memory/disk collection. The skill designs processor
  chains with batch processor for throughput optimization with send_batch_size and
  timeout tuning, attributes processor for span/metric attribute manipulation (insert,
  update, delete, hash operations), memory_limiter for backpressure management, and
  tail_sampling for intelligent trace sampling based on latency, error status, and
  string attribute policies. Advanced pipeline configurations include multi-pipeline
  fanout for sending traces to both jaeger and otlphttp exporters simultaneously,
  connector usage for traces-to-metrics (spanmetrics connector) and logs-to-metrics
  (count connector) derivation, and extension configurations for health_check, pprof,
  and zpages debugging endpoints. The skill generates Kubernetes-native configurations
  using the OpenTelemetry Operator CRDs (OpenTelemetryCollector kind) with DaemonSet
  and Deployment mode selection, and produces Helm values.yaml for the opentelemetry-collector
  chart deployment.
verification: security_reviewed
source: https://agentskillexchange.com/skills/otel-collector-pipeline-designer/
category:
- Monitoring &amp; Alerts
framework:
- OpenClaw
---

# OpenTelemetry Collector Pipeline Designer

The OpenTelemetry Collector Pipeline Designer skill generates comprehensive otel-collector configuration files for telemetry data routing and transformation. It configures receivers including otlp (gRPC/HTTP), prometheus for metric scraping with scrape_configs, filelog for structured log ingestion with multiline parsing, and hostmetrics for system-level CPU/memory/disk collection. The skill designs processor chains with batch processor for throughput optimization with send_batch_size and timeout tuning, attributes processor for span/metric attribute manipulation (insert, update, delete, hash operations), memory_limiter for backpressure management, and tail_sampling for intelligent trace sampling based on latency, error status, and string attribute policies. Advanced pipeline configurations include multi-pipeline fanout for sending traces to both jaeger and otlphttp exporters simultaneously, connector usage for traces-to-metrics (spanmetrics connector) and logs-to-metrics (count connector) derivation, and extension configurations for health_check, pprof, and zpages debugging endpoints. The skill generates Kubernetes-native configurations using the OpenTelemetry Operator CRDs (OpenTelemetryCollector kind) with DaemonSet and Deployment mode selection, and produces Helm values.yaml for the opentelemetry-collector chart deployment.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/otel-collector-pipeline-designer/)

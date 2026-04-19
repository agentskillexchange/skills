---
title: "OpenTelemetry Collector Pipeline Designer"
description: "The OpenTelemetry Collector Pipeline Designer skill generates comprehensive otel-collector configuration files for telemetry data routing and transformation. It configures receivers including otlp (gRPC/HTTP), prometheus for metric scraping with scrape_configs, filelog for structured log ingestion with multiline parsing, and hostmetrics for system-level CPU/memory/disk collection. The skill designs processor chains with batch processor for throughput optimization with send_batch_size and timeout tuning, attributes processor for span/metric attribute manipulation (insert, update, delete, hash operations), memory_limiter for backpressure management, and tail_sampling for intelligent trace sampling based on latency, error status, and string attribute policies. Advanced pipeline configurations include multi-pipeline fanout for sending traces to both jaeger and otlphttp exporters simultaneously, connector usage for traces-to-metrics (spanmetrics connector) and logs-to-metrics (count connector) derivation, and extension configurations for health_check, pprof, and zpages debugging endpoints. The skill generates Kubernetes-native configurations using the OpenTelemetry Operator CRDs (OpenTelemetryCollector kind) with DaemonSet and Deployment mode selection, and produces Helm values.yaml for the opentelemetry-collector chart deployment."
source: "https://agentskillexchange.com/skills/otel-collector-pipeline-designer/"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
---

# OpenTelemetry Collector Pipeline Designer

The OpenTelemetry Collector Pipeline Designer skill generates comprehensive otel-collector configuration files for telemetry data routing and transformation. It configures receivers including otlp (gRPC/HTTP), prometheus for metric scraping with scrape_configs, filelog for structured log ingestion with multiline parsing, and hostmetrics for system-level CPU/memory/disk collection. The skill designs processor chains with batch processor for throughput optimization with send_batch_size and timeout tuning, attributes processor for span/metric attribute manipulation (insert, update, delete, hash operations), memory_limiter for backpressure management, and tail_sampling for intelligent trace sampling based on latency, error status, and string attribute policies. Advanced pipeline configurations include multi-pipeline fanout for sending traces to both jaeger and otlphttp exporters simultaneously, connector usage for traces-to-metrics (spanmetrics connector) and logs-to-metrics (count connector) derivation, and extension configurations for health_check, pprof, and zpages debugging endpoints. The skill generates Kubernetes-native configurations using the OpenTelemetry Operator CRDs (OpenTelemetryCollector kind) with DaemonSet and Deployment mode selection, and produces Helm values.yaml for the opentelemetry-collector chart deployment.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/otel-collector-pipeline-designer/)

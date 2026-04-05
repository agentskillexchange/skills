---
name: "OpenTelemetry Collector Pipeline Designer"
description: "Designs OpenTelemetry Collector pipeline configurations with receivers (otlp, prometheus, filelog), processors (batch, attributes, tail_sampling), and exporters (otlphttp, jaeger, elasticsearch)."
category: "Monitoring &amp; Alerts"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/otel-collector-pipeline-designer/"
---
# OpenTelemetry Collector Pipeline Designer

Designs OpenTelemetry Collector pipeline configurations with receivers (otlp, prometheus, filelog), processors (batch, attributes, tail_sampling), and exporters (otlphttp, jaeger, elasticsearch).

The OpenTelemetry Collector Pipeline Designer skill generates comprehensive otel-collector configuration files for telemetry data routing and transformation. It configures receivers including otlp (gRPC/HTTP), prometheus for metric scraping with scrape_configs, filelog for structured log ingestion with multiline parsing, and hostmetrics for system-level CPU/memory/disk collection.

The skill designs processor chains with batch processor for throughput optimization with send_batch_size and timeout tuning, attributes processor for span/metric attribute manipulation (insert, update, delete, hash operations), memory_limiter for backpressure management, and tail_sampling for intelligent trace sampling based on latency, error status, and string attribute policies.

Advanced pipeline configurations include multi-pipeline fanout for sending traces to both jaeger and otlphttp exporters simultaneously, connector usage for traces-to-metrics (spanmetrics connector) and logs-to-metrics (count connector) derivation, and extension configurations for health_check, pprof, and zpages debugging endpoints. The skill generates Kubernetes-native configurations using the OpenTelemetry Operator CRDs (OpenTelemetryCollector kind) with DaemonSet and Deployment mode selection, and produces Helm values.yaml for the opentelemetry-collector chart deployment.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill otel-collector-pipeline-designer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill otel-collector-pipeline-designer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill otel-collector-pipeline-designer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill otel-collector-pipeline-designer -a codex
```

### OpenClaw

```bash
clawhub install otel-collector-pipeline-designer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/otel-collector-pipeline-designer/)

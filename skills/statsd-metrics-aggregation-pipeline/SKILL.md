---
name: "StatsD Metrics Aggregation Pipeline"
description: "Configures StatsD metric collection with custom aggregation rules and flush intervals. Routes metrics to Graphite Carbon, InfluxDB Line Protocol, or Datadog DogStatsD endpoints with tag-based dimensional routing."
category: "Monitoring & Alerts"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/statsd-metrics-aggregation-pipeline/"
tool_ecosystem:
  tool: "datadog"
  github_stars: 789
  npm_weekly_downloads: 6043057
  github_repo: "DataDog/dd-trace-js"
  maintained: true
---

# StatsD Metrics Aggregation Pipeline

Configures StatsD metric collection with custom aggregation rules and flush intervals. Routes metrics to Graphite Carbon, InfluxDB Line Protocol, or Datadog DogStatsD endpoints with tag-based dimensional routing.

## Overview

The StatsD Metrics Aggregation Pipeline skill manages application metrics collection and routing through StatsD-compatible metric pipelines. It configures metric type handling for counters, gauges, timers, histograms, and sets with customizable aggregation rules including percentile calculations, moving averages, and rate conversions.

The skill supports multi-backend routing where aggregated metrics are simultaneously flushed to Graphite’s Carbon protocol (plaintext and pickle), InfluxDB Line Protocol with tag preservation, and Datadog’s DogStatsD extension format. Tag-based routing rules enable sending different metric namespaces to different backends based on dimensional metadata.

Configuration capabilities include flush interval tuning with per-metric-type overrides, sampling rate adjustment to manage high-cardinality metric volume, prefix/suffix namespacing for multi-service environments, and metric filtering with allowlist/blocklist patterns. The skill also manages health monitoring of the metrics pipeline itself, tracking flush latency, packet loss rates, and backend write failures. It supports hot-reload of routing configuration without metric loss and provides metric throughput dashboards showing ingestion rates, aggregation overhead, and backend delivery confirmation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill statsd-metrics-aggregation-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill statsd-metrics-aggregation-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill statsd-metrics-aggregation-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill statsd-metrics-aggregation-pipeline -a codex
```

### OpenClaw

```bash
clawhub install statsd-metrics-aggregation-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/statsd-metrics-aggregation-pipeline/

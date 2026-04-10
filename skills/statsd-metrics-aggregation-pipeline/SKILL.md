---
name: "StatsD Metrics Aggregation Pipeline"
description: "Configures StatsD metric collection with custom aggregation rules and flush intervals. Routes metrics to Graphite Carbon, InfluxDB Line Protocol, or Datadog DogStatsD endpoints with tag-based dimensional routing."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/statsd-metrics-aggregation-pipeline/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Custom Agents"
---

# StatsD Metrics Aggregation Pipeline

The StatsD Metrics Aggregation Pipeline skill manages application metrics collection and routing through StatsD-compatible metric pipelines. It configures metric type handling for counters, gauges, timers, histograms, and sets with customizable aggregation rules including percentile calculations, moving averages, and rate conversions.
The skill supports multi-backend routing where aggregated metrics are simultaneously flushed to Graphite's Carbon protocol (plaintext and pickle), InfluxDB Line Protocol with tag preservation, and Datadog's DogStatsD extension format. Tag-based routing rules enable sending different metric namespaces to different backends based on dimensional metadata.
Configuration capabilities include flush interval tuning with per-metric-type overrides, sampling rate adjustment to manage high-cardinality metric volume, prefix/suffix namespacing for multi-service environments, and metric filtering with allowlist/blocklist patterns. The skill also manages health monitoring of the metrics pipeline itself, tracking flush latency, packet loss rates, and backend write failures. It supports hot-reload of routing configuration without metric loss and provides metric throughput dashboards showing ingestion rates, aggregation overhead, and backend delivery confirmation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/statsd-metrics-aggregation-pipeline/)

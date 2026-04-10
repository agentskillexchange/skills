---
title: "Quickwit Cloud-Native Search Engine for Observability Logs and Traces"
description: "Quickwit is a cloud-native search engine built in Rust for log management and distributed tracing. It offers sub-second search on cloud storage (S3, Azure Blob, GCS), an Elasticsearch-compatible API, native OpenTelemetry and Jaeger integration, and decoupled compute and storage architecture."
slug: "quickwit-cloud-native-search-engine-observability"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/quickwit-oss/quickwit"
---

# Quickwit Cloud-Native Search Engine for Observability Logs and Traces

Quickwit is a cloud-native search engine built in Rust for log management and distributed tracing. It offers sub-second search on cloud storage (S3, Azure Blob, GCS), an Elasticsearch-compatible API, native OpenTelemetry and Jaeger integration, and decoupled compute and storage architecture.

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
clawhub install quickwit-cloud-native-search-engine-observability
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Quickwit is an open-source cloud-native search engine purpose-built for observability data including logs and distributed traces. Written in Rust and licensed under Apache 2.0, it provides an alternative to Datadog, Elasticsearch, Loki, and Tempo with significantly lower infrastructure costs by leveraging object storage as its primary data store.
Core Capabilities
Quickwit delivers full-text search and aggregation queries with sub-second latency directly on cloud storage services including Amazon S3, Azure Blob Storage, and Google Cloud Storage. It supports both schemaless and strict schema indexing, enabling flexible data ingestion from multiple sources. The engine provides schemaless analytics, multi-tenancy with many indexes and partitioning, retention policies, and delete tasks for GDPR compliance use cases.
Observability Integration
The platform is OTEL-native for both logs and traces, with built-in support for OpenTelemetry collectors. It integrates natively with Jaeger for distributed tracing visualization and provides a Grafana data source plugin for dashboard creation. Data can be ingested from Kafka, Kinesis, and Pulsar natively, plus any system that supports the Elasticsearch ingest API (Vector, Fluent Bit, Syslog).
Elasticsearch Compatibility
Quickwit supports a large subset of the Elasticsearch and OpenSearch API, including the ingest API for easy migration of log shippers, popular search endpoints, query DSL, and aggregations. This makes it a drop-in replacement for many Elasticsearch-based observability stacks with minimal configuration changes.
Architecture and Deployment
The architecture decouples compute and storage with stateless indexers and searchers, making horizontal scaling straightforward. Quickwit is Kubernetes-ready with official Helm charts for deployment. High availability is supported for search operations, with HA indexing available when using a Kafka source. The system builds on Tantivy, a full-text search engine library also maintained by the Quickwit team.
Agent Integration
AI agents can use Quickwit’s REST API to ingest log data, run search queries, perform aggregations, and analyze distributed traces programmatically. Agents monitoring infrastructure can query Quickwit for log anomalies, trace latency spikes, or error patterns across microservices. The Elasticsearch-compatible API means existing agent skills built for Elasticsearch can often work with Quickwit with minimal modification.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/quickwit-cloud-native-search-engine-observability/)

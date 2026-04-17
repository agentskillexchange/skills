---
title: "Redpanda Connect Declarative Stream Processor"
description: "Redpanda Connect, formerly known as Benthos, is an open-source stream processor written in Go. It connects input sources to output sinks through declarative YAML configuration files, with a pipeline stage for transformations, enrichments, and filtering. The tool handles at-least-once delivery guarantees without requiring disk-persisted state, making deployment and scaling straightforward.\nA typical pipeline configuration specifies an input (such as Kafka, AWS SQS, GCP Pub/Sub, or HTTP), a list of processors that transform messages, and an output (such as Redis Streams, Elasticsearch, PostgreSQL, or S3). The built-in mapping language, Bloblang, provides a concise syntax for restructuring payloads, extracting fields, performing arithmetic, and handling errors. Pipelines can be as simple as three lines or as complex as multi-stage enrichment workflows with conditional branching.\nRedpanda Connect supports a wide range of connectors: AWS services (DynamoDB, Kinesis, S3, SQS, SNS), Azure storage, GCP Pub/Sub and Cloud Storage, Kafka, NATS, MQTT, AMQP, Redis, Cassandra, MongoDB, SQL databases (MySQL, PostgreSQL, ClickHouse, MSSQL), HTTP clients and servers including WebSockets, and many more. This breadth makes it a versatile glue layer for data infrastructure.\nThe tool ships as a static binary and Docker image. It exposes HTTP health-check endpoints (/ping for liveness, /ready for readiness) and exports metrics for monitoring. Configuration can be provided via files, environment variable interpolation, or CLI flags. Redpanda Connect also supports running as an embedded library in Go applications for custom deployments.\nWith over 8,000 GitHub stars across its Benthos lineage and active development by Redpanda Data, the project is widely used in production for ETL pipelines, event-driven architectures, and real-time data integration. It is available via Homebrew, Docker, and standalone binaries."
verification: security_reviewed
source: "https://github.com/redpanda-data/connect"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "redpanda-data/connect"
  github_stars: 8618
---

# Redpanda Connect Declarative Stream Processor

Redpanda Connect, formerly known as Benthos, is an open-source stream processor written in Go. It connects input sources to output sinks through declarative YAML configuration files, with a pipeline stage for transformations, enrichments, and filtering. The tool handles at-least-once delivery guarantees without requiring disk-persisted state, making deployment and scaling straightforward.
A typical pipeline configuration specifies an input (such as Kafka, AWS SQS, GCP Pub/Sub, or HTTP), a list of processors that transform messages, and an output (such as Redis Streams, Elasticsearch, PostgreSQL, or S3). The built-in mapping language, Bloblang, provides a concise syntax for restructuring payloads, extracting fields, performing arithmetic, and handling errors. Pipelines can be as simple as three lines or as complex as multi-stage enrichment workflows with conditional branching.
Redpanda Connect supports a wide range of connectors: AWS services (DynamoDB, Kinesis, S3, SQS, SNS), Azure storage, GCP Pub/Sub and Cloud Storage, Kafka, NATS, MQTT, AMQP, Redis, Cassandra, MongoDB, SQL databases (MySQL, PostgreSQL, ClickHouse, MSSQL), HTTP clients and servers including WebSockets, and many more. This breadth makes it a versatile glue layer for data infrastructure.
The tool ships as a static binary and Docker image. It exposes HTTP health-check endpoints (/ping for liveness, /ready for readiness) and exports metrics for monitoring. Configuration can be provided via files, environment variable interpolation, or CLI flags. Redpanda Connect also supports running as an embedded library in Go applications for custom deployments.
With over 8,000 GitHub stars across its Benthos lineage and active development by Redpanda Data, the project is widely used in production for ETL pipelines, event-driven architectures, and real-time data integration. It is available via Homebrew, Docker, and standalone binaries.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/redpanda-connect-declarative-stream-processor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/redpanda-connect-declarative-stream-processor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/redpanda-connect-declarative-stream-processor/)

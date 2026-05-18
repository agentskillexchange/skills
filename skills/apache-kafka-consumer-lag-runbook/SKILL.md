---
name: "Apache Kafka Consumer Lag Runbook"
slug: "apache-kafka-consumer-lag-runbook"
description: "Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count."
github_stars: 32388
verification: "listed"
source: "https://github.com/apache/kafka"
author: "Apache"
category: "Runbooks & Diagnostics"
framework: "Cursor"
tool_ecosystem:
  github_repo: "apache/kafka"
  github_stars: 32388
---

# Apache Kafka Consumer Lag Runbook

Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count.

## Prerequisites

Java

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -p 9092:9092 apache/kafka:latest

Requirements and caveats from upstream:
- Using docker image:
- See [docker/README.md](docker/README.md) for detailed information.

Basic usage or getting-started notes:
- ### Build a JAR and run it
- ### Run unit/integration tests
- ./gradlew test -Pkafka.test.run.flaky=true # runs tests that are marked as flaky

- Source: https://github.com/apache/kafka
- Extracted from upstream docs: https://raw.githubusercontent.com/apache/kafka/HEAD/README.md

## Documentation

- https://kafka.apache.org/documentation/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/)

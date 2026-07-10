---
name: "Apache Kafka Stream Processor"
slug: "apache-kafka-stream-processor"
description: ""
github_stars: 32373
verification: "security_reviewed"
source: "https://github.com/apache/kafka"
author: "apache"
category: "Data Extraction & Transformation"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "apache/kafka"
  github_stars: 32373
---

# Apache Kafka Stream Processor



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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-stream-processor/)

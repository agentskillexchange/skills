---
title: "Apache Kafka Consumer Lag Runbook"
slug: "apache-kafka-consumer-lag-runbook"
description: "Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count."
category: "Runbooks &amp; Diagnostics"
framework: "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/"
---

# Apache Kafka Consumer Lag Runbook

Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your skills directory.
2. Install it through your agent platform's skill manager if supported.
3. Add it as a Git submodule or vendored folder in your repo.
4. Copy the files into a local custom skills/workspace directory.
5. Pull it from the Agent Skill Exchange catalog or this GitHub repo.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/)

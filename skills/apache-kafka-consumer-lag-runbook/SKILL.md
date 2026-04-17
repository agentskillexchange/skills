---
name: Apache Kafka Consumer Lag Runbook
description: Diagnoses Kafka consumer group lag using the Kafka AdminClient API and
  JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic
  partition hotspots, and broker rebalance storms that contribute to lag growth. Provides
  a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition
  count.
category: Runbooks & Diagnostics
framework: Cursor
verification: security_reviewed
source: https://github.com/apache/kafka
tool_ecosystem:
  github_repo: apache/kafka
  github_stars: 32388
  tool: kafka
---
# Apache Kafka Consumer Lag Runbook
Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apache-kafka-consumer-lag-runbook
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/apache-kafka-consumer-lag-runbook` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/)

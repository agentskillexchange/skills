---
name: Apache Kafka Consumer Lag Runbook
description: Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.3
reviews: 86
source: https://agentskillexchange.com/skill/apache-kafka-consumer-lag-runbook/
---

# Apache Kafka Consumer Lag Runbook

Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count.

## Overview

Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-consumer-lag-runbook
```

### OpenClaw

```bash
clawhub install apache-kafka-consumer-lag-runbook
```

### Claude Code

```bash
claude mcp add apache-kafka-consumer-lag-runbook
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/apache-kafka-consumer-lag-runbook/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.3/5 (86 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/apache-kafka-consumer-lag-runbook/)

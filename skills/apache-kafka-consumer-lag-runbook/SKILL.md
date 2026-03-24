---
name: "Apache Kafka Consumer Lag Runbook"
description: "Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed
rating: 4.3
reviews: 86
creator: "Isabella Rossi"
creator_handle: "@irossi"
creator_verified: false
source: "https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/"
---
# Apache Kafka Consumer Lag Runbook

Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-consumer-lag-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-consumer-lag-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-consumer-lag-runbook -a cursor
```

### OpenClaw

```bash
clawhub install apache-kafka-consumer-lag-runbook
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-consumer-lag-runbook -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Cursor |
| Verification | Security Reviewed |
| Rating | 4.3/5 (86 reviews) |

## Creator

**Isabella Rossi**
- Profile: [@irossi](https://agentskillexchange.com/browse-skills/?creator=irossi)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/apache-kafka-consumer-lag-runbook/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)

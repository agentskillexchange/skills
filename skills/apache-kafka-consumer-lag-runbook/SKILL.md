---
name: "Apache Kafka Consumer Lag Runbook"
description: "Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/"
tool_ecosystem:
  tool: "kafka"
  github_stars: 3987
  npm_weekly_downloads: 2396148
  github_repo: "tulios/kafkajs"
  license: "MIT"
  maintained: false
---

# Apache Kafka Consumer Lag Runbook

Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Cursor |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [kafka](https://github.com/tulios/kafkajs) — ⭐ 4.0k · MIT |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*

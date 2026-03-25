---
name: "Queue Backup Runbook"
description: "Runbook for resolving message queue backup incidents. Covers consumer lag diagnosis, poison pill message handling, dead letter queue analysis, and throughput restoration for SQS, Kafka, RabbitMQ, and similar systems."
category: "Runbooks & Diagnostics"
framework: "Custom Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/queue-backup-runbook/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kafka"  # from ase_tool_match
  github_stars: 3987  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2396148  # from ase_npm_downloads
  github_repo: "tulios/kafkajs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Queue Backup Runbook

Runbook for resolving message queue backup incidents. Covers consumer lag diagnosis, poison pill message handling, dead letter queue analysis, and throughput restoration for SQS, Kafka, RabbitMQ, and similar systems.

## Overview

Runbook for resolving message queue backup incidents. Covers consumer lag diagnosis, poison pill message handling, dead letter queue analysis, and throughput restoration for SQS, Kafka, RabbitMQ, and similar systems.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill queue-backup-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill queue-backup-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill queue-backup-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill queue-backup-runbook -a codex
```

### OpenClaw

```bash
clawhub install queue-backup-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/queue-backup-runbook/

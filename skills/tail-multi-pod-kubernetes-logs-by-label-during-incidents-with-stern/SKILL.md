---
title: "Tail multi-pod Kubernetes logs by label during incidents with Stern"
description: "Use Stern when an agent needs to follow logs across many Kubernetes pods at once during an outage, rollout, or noisy incident. The agent can select pods by label or pattern, stream their logs together, and highlight which workload is failing or flapping. Invoke this instead of using the product normally when the task is multi-pod incident log triage, not general log platform setup or cluster administration. The boundary is targeted live log aggregation from Kubernetes workloads during diagnosis, not a generic logging product listing."
verification: listed
source: "https://github.com/stern/stern"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "stern/stern"
  github_stars: 4636
---

# Tail multi-pod Kubernetes logs by label during incidents with Stern

Use Stern when an agent needs to follow logs across many Kubernetes pods at once during an outage, rollout, or noisy incident. The agent can select pods by label or pattern, stream their logs together, and highlight which workload is failing or flapping. Invoke this instead of using the product normally when the task is multi-pod incident log triage, not general log platform setup or cluster administration. The boundary is targeted live log aggregation from Kubernetes workloads during diagnosis, not a generic logging product listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern/)

---
title: "Tail multi-pod Kubernetes logs by label during incidents with Stern"
description: "Aggregate and follow logs from matching Kubernetes pods during incident triage without hopping pod by pod."
verification: "listed"
source: "https://github.com/stern/stern"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "stern/stern"
  github_stars: 4636
---

# Tail multi-pod Kubernetes logs by label during incidents with Stern

Use Stern when an agent needs to follow logs across many Kubernetes pods at once during an outage, rollout, or noisy incident. The agent can select pods by label or pattern, stream their logs together, and highlight which workload is failing or flapping. Invoke this instead of using the product normally when the task is multi-pod incident log triage, not general log platform setup or cluster administration. The boundary is targeted live log aggregation from Kubernetes workloads during diagnosis, not a generic logging product listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern/)

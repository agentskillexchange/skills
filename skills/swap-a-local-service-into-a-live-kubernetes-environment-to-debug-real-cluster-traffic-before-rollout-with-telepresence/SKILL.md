---
title: "Swap a local service into a live Kubernetes environment to debug real cluster traffic before rollout with Telepresence"
description: "Intercept a Kubernetes service and route live cluster traffic into a local process so debugging happens against real dependencies before release."
verification: "listed"
source: "https://github.com/telepresenceio/telepresence"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "telepresenceio/telepresence"
  github_stars: 7183
---

# Swap a local service into a live Kubernetes environment to debug real cluster traffic before rollout with Telepresence

Use Telepresence when an agent needs to replace or intercept one service inside a running Kubernetes environment so local code can handle real in-cluster requests. A user should invoke this instead of using Kubernetes normally when the task is live dependency-aware debugging or pre-rollout verification, not ordinary deployment or cluster administration. The scope boundary is tight and skill-shaped: intercepting a workload and bridging local execution into cluster traffic, not listing a general Kubernetes platform or networking product.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/swap-a-local-service-into-a-live-kubernetes-environment-to-debug-real-cluster-traffic-before-rollout-with-telepresence/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/swap-a-local-service-into-a-live-kubernetes-environment-to-debug-real-cluster-traffic-before-rollout-with-telepresence
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/swap-a-local-service-into-a-live-kubernetes-environment-to-debug-real-cluster-traffic-before-rollout-with-telepresence`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swap-a-local-service-into-a-live-kubernetes-environment-to-debug-real-cluster-traffic-before-rollout-with-telepresence/)

---
title: "Watch Kubernetes resources explain rollout stalls and surface live status transitions with kubespy"
description: "Follow a Kubernetes workload live so an agent can explain why it is pending, failing, or not becoming ready."
verification: "listed"
source: "https://github.com/pulumi/kubespy"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pulumi/kubespy"
  github_stars: 3056
---

# Watch Kubernetes resources explain rollout stalls and surface live status transitions with kubespy

Use kubespy when an agent needs to observe a rollout or workload live instead of guessing from static kubectl output. The agent can watch resource transitions, surface readiness blockers, and explain why a deployment is stalling while the event stream is still unfolding. Invoke this instead of using the product normally when the task is rollout diagnosis and live status interpretation, not general Kubernetes administration. The boundary is time-bound observation of resource state changes during deploy or incident response, not a generic cluster toolkit listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy/)

---
title: "Watch Kubernetes resources explain rollout stalls and surface live status transitions with kubespy"
description: "Use kubespy when an agent needs to observe a rollout or workload live instead of guessing from static kubectl output. The agent can watch resource transitions, surface readiness blockers, and explain why a deployment is stalling while the event stream is still unfolding. Invoke this instead of using the product normally when the task is rollout diagnosis and live status interpretation, not general Kubernetes administration. The boundary is time-bound observation of resource state changes during deploy or incident response, not a generic cluster toolkit listing."
verification: listed
source: "https://github.com/pulumi/kubespy"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pulumi/kubespy"
  github_stars: 3056
---

# Watch Kubernetes resources explain rollout stalls and surface live status transitions with kubespy

Use kubespy when an agent needs to observe a rollout or workload live instead of guessing from static kubectl output. The agent can watch resource transitions, surface readiness blockers, and explain why a deployment is stalling while the event stream is still unfolding. Invoke this instead of using the product normally when the task is rollout diagnosis and live status interpretation, not general Kubernetes administration. The boundary is time-bound observation of resource state changes during deploy or incident response, not a generic cluster toolkit listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy/)

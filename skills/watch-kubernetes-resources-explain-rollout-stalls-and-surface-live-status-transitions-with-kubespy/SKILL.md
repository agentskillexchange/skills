---
title: "Watch Kubernetes resources explain rollout stalls and surface live status transitions with kubespy"
description: "Use kubespy when an agent needs to observe a rollout or workload live instead of guessing from static kubectl output. The agent can watch resource transitions, surface readiness blockers, and explain why a deployment is stalling while the event stream is still unfolding. Invoke this instead of using the product normally when the task is rollout diagnosis and live status interpretation, not general Kubernetes administration. The boundary is time-bound observation of resource state changes during deploy or incident response, not a generic cluster toolkit listing."
source: "https://github.com/pulumi/kubespy"
verification: "listed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pulumi/kubespy"
  github_stars: 3056
---

# Watch Kubernetes resources explain rollout stalls and surface live status transitions with kubespy

Use kubespy when an agent needs to observe a rollout or workload live instead of guessing from static kubectl output. The agent can watch resource transitions, surface readiness blockers, and explain why a deployment is stalling while the event stream is still unfolding. Invoke this instead of using the product normally when the task is rollout diagnosis and live status interpretation, not general Kubernetes administration. The boundary is time-bound observation of resource state changes during deploy or incident response, not a generic cluster toolkit listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy/)

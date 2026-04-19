---
title: "Swap a local service into a live Kubernetes environment to debug real cluster traffic before rollout with Telepresence"
description: "Use Telepresence when an agent needs to replace or intercept one service inside a running Kubernetes environment so local code can handle real in-cluster requests. A user should invoke this instead of using Kubernetes normally when the task is live dependency-aware debugging or pre-rollout verification, not ordinary deployment or cluster administration. The scope boundary is tight and skill-shaped: intercepting a workload and bridging local execution into cluster traffic, not listing a general Kubernetes platform or networking product."
source: "https://github.com/telepresenceio/telepresence"
verification: "listed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "telepresenceio/telepresence"
  github_stars: 7183
---

# Swap a local service into a live Kubernetes environment to debug real cluster traffic before rollout with Telepresence

Use Telepresence when an agent needs to replace or intercept one service inside a running Kubernetes environment so local code can handle real in-cluster requests. A user should invoke this instead of using Kubernetes normally when the task is live dependency-aware debugging or pre-rollout verification, not ordinary deployment or cluster administration. The scope boundary is tight and skill-shaped: intercepting a workload and bridging local execution into cluster traffic, not listing a general Kubernetes platform or networking product.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swap-a-local-service-into-a-live-kubernetes-environment-to-debug-real-cluster-traffic-before-rollout-with-telepresence/)

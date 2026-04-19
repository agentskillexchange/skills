---
title: "Tail multi-pod Kubernetes logs by label during incidents with Stern"
description: "Use Stern when an agent needs to follow logs across many Kubernetes pods at once during an outage, rollout, or noisy incident. The agent can select pods by label or pattern, stream their logs together, and highlight which workload is failing or flapping. Invoke this instead of using the product normally when the task is multi-pod incident log triage, not general log platform setup or cluster administration. The boundary is targeted live log aggregation from Kubernetes workloads during diagnosis, not a generic logging product listing."
source: "https://github.com/stern/stern"
verification: "listed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "stern/stern"
  github_stars: 4636
---

# Tail multi-pod Kubernetes logs by label during incidents with Stern

Use Stern when an agent needs to follow logs across many Kubernetes pods at once during an outage, rollout, or noisy incident. The agent can select pods by label or pattern, stream their logs together, and highlight which workload is failing or flapping. Invoke this instead of using the product normally when the task is multi-pod incident log triage, not general log platform setup or cluster administration. The boundary is targeted live log aggregation from Kubernetes workloads during diagnosis, not a generic logging product listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern/)

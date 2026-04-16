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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern/)

---
title: "Watch Kubernetes resources explain rollout stalls and surface live status transitions with kubespy"
description: "Follow a Kubernetes workload live so an agent can explain why it is pending, failing, or not becoming ready."
verification: "listed"
source: "https://github.com/pulumi/kubespy"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy/)

---
name: "Watch Kubernetes resources explain rollout stalls and surface live status transitions with kubespy"
slug: "watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy"
description: "Follow a Kubernetes workload live so an agent can explain why it is pending, failing, or not becoming ready."
github_stars: 3056
verification: "security_reviewed"
source: "https://github.com/pulumi/kubespy"
author: "Pulumi"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "pulumi/kubespy"
  github_stars: 3056
---

# Watch Kubernetes resources explain rollout stalls and surface live status transitions with kubespy

Follow a Kubernetes workload live so an agent can explain why it is pending, failing, or not becoming ready.

## Prerequisites

kubespy CLI, Kubernetes cluster access

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install kubespy from the project repository, connect it to the target cluster context, and watch the resource type and name involved in the rollout or incident.
```

## Documentation

- https://github.com/pulumi/kubespy

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy/)

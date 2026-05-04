---
title: "Lint live Kubernetes clusters for misconfigurations and operational hygiene with Popeye"
description: "Inspect a live Kubernetes cluster for unhealthy resource settings, missing probes, and other operational smells."
verification: "listed"
source: "https://github.com/derailed/popeye"
author: "derailed"
publisher_type: "organization"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "derailed/popeye"
  github_stars: 6262
---

# Lint live Kubernetes clusters for misconfigurations and operational hygiene with Popeye

Inspect a live Kubernetes cluster for unhealthy resource settings, missing probes, and other operational smells.

## Prerequisites

Kubernetes cluster access, Popeye binary

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Popeye from a release or package manager, configure kubeconfig access, then run `popeye` or `popeye -A` to scan the target cluster.
```

## Documentation

- https://github.com/derailed/popeye

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-live-kubernetes-clusters-for-misconfigurations-and-operational-hygiene-with-popeye/)

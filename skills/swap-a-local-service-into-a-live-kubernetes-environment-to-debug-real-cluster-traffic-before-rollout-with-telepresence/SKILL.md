---
title: "Swap a local service into a live Kubernetes environment to debug real cluster traffic before rollout with Telepresence"
slug: "swap-a-local-service-into-a-live-kubernetes-environment-to-debug-real-cluster-traffic-before-rollout-with-telepresence"
description: "Intercept a Kubernetes service and route live cluster traffic into a local process so debugging happens against real dependencies before release."
github_stars: 7183
verification: "security_reviewed"
source: "https://github.com/telepresenceio/telepresence"
author: "telepresenceio"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "telepresenceio/telepresence"
  github_stars: 7183
---

# Swap a local service into a live Kubernetes environment to debug real cluster traffic before rollout with Telepresence

Intercept a Kubernetes service and route live cluster traffic into a local process so debugging happens against real dependencies before release.

## Prerequisites

Telepresence CLI, kubectl access, kubeconfig for the target cluster, a locally runnable service, and permission to create intercepts in the namespace

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the Telepresence CLI from the upstream packages or release binaries, connect it to the target Kubernetes cluster with working kubectl credentials, then run the documented intercept workflow against the service you want to replace locally.
```

## Documentation

- https://github.com/telepresenceio/telepresence

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swap-a-local-service-into-a-live-kubernetes-environment-to-debug-real-cluster-traffic-before-rollout-with-telepresence/)

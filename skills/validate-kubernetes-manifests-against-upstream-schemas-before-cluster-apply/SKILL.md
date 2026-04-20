---
title: Validate Kubernetes manifests against upstream schemas before cluster apply
description: Uses kubeconform to validate Kubernetes manifests against versioned schemas
  before anything touches a cluster. The agent can review rendered Helm output, raw
  manifests, or PR diffs and return invalid resources, missing schemas, and strict-mode
  failures without requiring live cluster credentials.
verification: security_reviewed
source: https://github.com/yannh/kubeconform
category:
- CI/CD Integrations
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: yannh/kubeconform
  github_stars: 2986
---

# Validate Kubernetes manifests against upstream schemas before cluster apply

Uses kubeconform to validate Kubernetes manifests against versioned schemas before anything touches a cluster. The agent can review rendered Helm output, raw manifests, or PR diffs and return invalid resources, missing schemas, and strict-mode failures without requiring live cluster credentials.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply/)

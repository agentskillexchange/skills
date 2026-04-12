---
title: "Validate Kubernetes manifests against upstream schemas before cluster apply"
slug: "validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply"
description: "Uses kubeconform to validate Kubernetes manifests against versioned schemas before anything touches a cluster. The agent can review rendered Helm output, raw manifests, or PR diffs and return invalid resources, missing schemas, and strict-mode failures without requiring live cluster credentials."
verification: listed
source: "https://github.com/yannh/kubeconform"
category:
  - "CI/CD Integrations"
tool_ecosystem:
  github_repo: "https://github.com/yannh/kubeconform"
  github_stars: 2986
---

# Validate Kubernetes manifests against upstream schemas before cluster apply

Uses kubeconform to validate Kubernetes manifests against versioned schemas before anything touches a cluster. The agent can review rendered Helm output, raw manifests, or PR diffs and return invalid resources, missing schemas, and strict-mode failures without requiring live cluster credentials.

## Installation

Choose the setup path that fits your environment:

1. Install from the Agent Skill Exchange UI
2. Clone or download this skill into your skills directory
3. Install with your agent platform's skill manager, if supported
4. Vendor the skill into your workspace or repo
5. Copy the skill files manually for local customization

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply/)

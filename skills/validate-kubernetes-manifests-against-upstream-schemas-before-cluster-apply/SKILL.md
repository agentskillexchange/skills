---
title: "Validate Kubernetes manifests against upstream schemas before cluster apply"
slug: "validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply"
verification: security_reviewed
source: "https://github.com/yannh/kubeconform"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "yannh/kubeconform"
  github_stars: 2986
---
# Validate Kubernetes manifests against upstream schemas before cluster apply

Uses kubeconform to validate Kubernetes manifests against versioned schemas before anything touches a cluster. The agent can review rendered Helm output, raw manifests, or PR diffs and return invalid resources, missing schemas, and strict-mode failures without requiring live cluster credentials.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply/)

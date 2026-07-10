---
name: "Validate Kubernetes manifests against upstream schemas before cluster apply"
slug: "validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply"
description: "Uses kubeconform to validate Kubernetes manifests against versioned schemas before anything touches a cluster. The agent can review rendered Helm output, raw manifests, or PR diffs and return invalid resources, missing schemas, and strict-mode failures without requiring live cluster credentials."
github_stars: 2986
verification: "listed"
source: "https://github.com/yannh/kubeconform"
author: "yannh"
publisher_type: "Open Source Project"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "yannh/kubeconform"
  github_stars: 2986
---

# Validate Kubernetes manifests against upstream schemas before cluster apply

Uses kubeconform to validate Kubernetes manifests against versioned schemas before anything touches a cluster. The agent can review rendered Helm output, raw manifests, or PR diffs and return invalid resources, missing schemas, and strict-mode failures without requiring live cluster credentials.

## Prerequisites

Kubernetes manifests plus the kubeconform binary

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/yannh/kubeconform

## Documentation

- https://github.com/yannh/kubeconform

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply/)

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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply/)

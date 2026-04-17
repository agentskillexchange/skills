---
name: Validate Kubernetes manifests against upstream schemas before cluster apply
description: Uses kubeconform to validate Kubernetes manifests against versioned schemas
  before anything touches a cluster. The agent can review rendered Helm output, raw
  manifests, or PR diffs and return invalid resources, missing schemas, and strict-mode
  failures without requiring live cluster credentials.
category: CI/CD Integrations
framework: Multi-Framework
verification: security_reviewed
source: https://github.com/yannh/kubeconform
tool_ecosystem:
  github_repo: yannh/kubeconform
  github_stars: 2986
  tool: kubeconform
---
# Validate Kubernetes manifests against upstream schemas before cluster apply
Uses kubeconform to validate Kubernetes manifests against versioned schemas before anything touches a cluster. The agent can review rendered Helm output, raw manifests, or PR diffs and return invalid resources, missing schemas, and strict-mode failures without requiring live cluster credentials.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply/)

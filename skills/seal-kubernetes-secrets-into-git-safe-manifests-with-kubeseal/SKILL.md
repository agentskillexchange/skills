---
title: "Seal Kubernetes Secrets into Git-safe manifests with kubeseal"
description: "Encrypt Kubernetes Secret manifests against a Sealed Secrets controller so agents can commit cluster-targeted secrets to Git without exposing plaintext."
verification: "listed"
source: "https://github.com/bitnami-labs/sealed-secrets"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bitnami-labs/sealed-secrets"
  github_stars: 9045
---

# Seal Kubernetes Secrets into Git-safe manifests with kubeseal

Use kubeseal when an agent needs to turn a plaintext Kubernetes Secret manifest into an encrypted SealedSecret that is safe to store in Git and later decrypt only inside the target cluster. A user should invoke this instead of handling Secrets normally when the job is certificate-aware secret sealing for GitOps, rekeying, or controller-bound secret delivery, not day to day secret viewing or generic secret management. The scope boundary is narrow and skill-shaped: encrypting Kubernetes Secret manifests for the Sealed Secrets controller, not listing a Kubernetes platform or generic security product.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/seal-kubernetes-secrets-into-git-safe-manifests-with-kubeseal/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/seal-kubernetes-secrets-into-git-safe-manifests-with-kubeseal
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/seal-kubernetes-secrets-into-git-safe-manifests-with-kubeseal`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/seal-kubernetes-secrets-into-git-safe-manifests-with-kubeseal/)

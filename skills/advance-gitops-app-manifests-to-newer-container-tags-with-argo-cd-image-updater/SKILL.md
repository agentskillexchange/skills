---
title: "Advance GitOps app manifests to newer container tags with Argo CD Image Updater"
description: "Track approved container images and write back the matching GitOps manifest changes instead of hand-editing tags across Argo CD applications."
verification: "security_reviewed"
source: "https://github.com/argoproj-labs/argocd-image-updater"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "argoproj-labs/argocd-image-updater"
  github_stars: 1661
---

# Advance GitOps app manifests to newer container tags with Argo CD Image Updater

Use Argo CD Image Updater when an agent needs to watch approved image registries, choose newer tags under explicit update rules, and write the resulting tag changes back to the GitOps source of truth for Argo CD-managed workloads. Invoke this instead of using Argo CD normally when the job is specifically image selection plus manifest or parameter write-back, not general deployment sync, application health review, or cluster operations. The scope boundary is concrete: detect eligible image updates and advance Argo CD application manifests for supported Helm or Kustomize workloads, which makes this a bounded operator workflow rather than a plain platform listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/advance-gitops-app-manifests-to-newer-container-tags-with-argo-cd-image-updater/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/advance-gitops-app-manifests-to-newer-container-tags-with-argo-cd-image-updater
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/advance-gitops-app-manifests-to-newer-container-tags-with-argo-cd-image-updater`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/advance-gitops-app-manifests-to-newer-container-tags-with-argo-cd-image-updater/)

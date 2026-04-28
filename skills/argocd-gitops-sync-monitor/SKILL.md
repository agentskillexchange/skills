---
title: "ArgoCD GitOps Sync Monitor"
description: "Monitors ArgoCD application sync status using the ArgoCD REST API /api/v1/applications endpoint. Detects drift between Git manifests and live Kubernetes cluster state via the Kubernetes API."
verification: security_reviewed
source: "https://github.com/argoproj/argo-cd"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
  license: "Apache-2.0"
---

# ArgoCD GitOps Sync Monitor

Monitors ArgoCD application sync status using the ArgoCD REST API /api/v1/applications endpoint. Detects drift between Git manifests and live Kubernetes cluster state via the Kubernetes API.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/argocd-gitops-sync-monitor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argocd-gitops-sync-monitor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/argocd-gitops-sync-monitor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-gitops-sync-monitor/)

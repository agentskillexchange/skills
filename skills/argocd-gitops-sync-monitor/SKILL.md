---
name: ArgoCD GitOps Sync Monitor
description: Monitors ArgoCD application sync status using the ArgoCD REST API /api/v1/applications
  endpoint. Detects drift between Git manifests and live Kubernetes cluster state
  via the Kubernetes API.
category: CI/CD Integrations
framework: Gemini
verification: security_reviewed
source: https://github.com/argoproj/argo-cd
tool_ecosystem:
  github_repo: argoproj/argo-cd
  github_stars: 22593
  tool: argo-cd
  license: Apache-2.0
  maintained: true
---
# ArgoCD GitOps Sync Monitor
Monitors ArgoCD application sync status using the ArgoCD REST API /api/v1/applications endpoint. Detects drift between Git manifests and live Kubernetes cluster state via the Kubernetes API.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argocd-gitops-sync-monitor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/argocd-gitops-sync-monitor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-gitops-sync-monitor/)

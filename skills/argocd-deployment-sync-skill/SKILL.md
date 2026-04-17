---
name: ArgoCD Deployment Sync Skill
description: Manages GitOps deployments via the ArgoCD REST API and argocd CLI. Triggers
  application syncs through /api/v1/applications/{name}/sync, monitors health status
  via /api/v1/applications/{name}, and manages rollbacks using /api/v1/applications/{name}/rollback
  for Kubernetes workloads.
category: CI/CD Integrations
framework: Claude Agents
verification: security_reviewed
source: https://github.com/argoproj/argo-cd
tool_ecosystem:
  github_repo: argoproj/argo-cd
  github_stars: 22593
  tool: argo-cd
  license: Apache-2.0
  maintained: true
---
# ArgoCD Deployment Sync Skill
Manages GitOps deployments via the ArgoCD REST API and argocd CLI. Triggers application syncs through /api/v1/applications/{name}/sync, monitors health status via /api/v1/applications/{name}, and manages rollbacks using /api/v1/applications/{name}/rollback for Kubernetes workloads.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argocd-deployment-sync-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/argocd-deployment-sync-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-deployment-sync-skill/)

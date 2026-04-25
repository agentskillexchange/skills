---
title: "ArgoCD GitOps Sync Controller"
description: "Manages ArgoCD Application and ApplicationSet resources for Kubernetes GitOps deployments. Uses the ArgoCD REST API and argocd CLI to automate sync waves, health checks, and progressive rollout configurations."
verification: "security_reviewed"
source: "https://github.com/argoproj/argo-cd"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD GitOps Sync Controller

The ArgoCD GitOps Sync Controller provides comprehensive management of Kubernetes deployments through ArgoCD Application resources. It generates Application and ApplicationSet manifests with sync policies, automated pruning, and self-healing configurations.

The skill interfaces with the ArgoCD REST API for application state monitoring, sync status checking, and rollback operations. It configures sync waves and hooks using argocd.argoproj.io/sync-wave annotations for ordered deployment of dependent resources like ConfigMaps, Secrets, Deployments, and Services.

Advanced capabilities include ApplicationSet generation with Git directory and Pull Request generators for automatic environment provisioning, progressive delivery integration with Argo Rollouts for canary and blue-green deployments, and health check customization using Lua scripts. The controller also manages ArgoCD project configurations with RBAC policies, source repository restrictions, and destination namespace allowlists. Notification templates for Slack, email, and webhook integrations are generated using the argocd-notifications ConfigMap patterns.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/argocd-gitops-sync-controller/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argocd-gitops-sync-controller
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/argocd-gitops-sync-controller`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-gitops-sync-controller/)

---
title: "ArgoCD GitOps Sync Controller"
description: "Manages ArgoCD Application and ApplicationSet resources for Kubernetes GitOps deployments. Uses the ArgoCD REST API and argocd CLI to automate sync waves, health checks, and progressive rollout configurations."
slug: "argocd-gitops-sync-controller"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/argocd-gitops-sync-controller/"
---

# ArgoCD GitOps Sync Controller

Manages ArgoCD Application and ApplicationSet resources for Kubernetes GitOps deployments. Uses the ArgoCD REST API and argocd CLI to automate sync waves, health checks, and progressive rollout configurations.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install argocd-gitops-sync-controller
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ArgoCD GitOps Sync Controller provides comprehensive management of Kubernetes deployments through ArgoCD Application resources. It generates Application and ApplicationSet manifests with sync policies, automated pruning, and self-healing configurations.
The skill interfaces with the ArgoCD REST API for application state monitoring, sync status checking, and rollback operations. It configures sync waves and hooks using argocd.argoproj.io/sync-wave annotations for ordered deployment of dependent resources like ConfigMaps, Secrets, Deployments, and Services.
Advanced capabilities include ApplicationSet generation with Git directory and Pull Request generators for automatic environment provisioning, progressive delivery integration with Argo Rollouts for canary and blue-green deployments, and health check customization using Lua scripts. The controller also manages ArgoCD project configurations with RBAC policies, source repository restrictions, and destination namespace allowlists. Notification templates for Slack, email, and webhook integrations are generated using the argocd-notifications ConfigMap patterns.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-gitops-sync-controller/)

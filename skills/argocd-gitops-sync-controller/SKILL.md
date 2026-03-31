---
name: "ArgoCD GitOps Sync Controller"
description: "Manages ArgoCD Application and ApplicationSet resources for Kubernetes GitOps deployments. Uses the ArgoCD REST API and argocd CLI to automate sync waves, health checks, and progressive rollout configurations."
category: "CI/CD Integrations"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argocd-gitops-sync-controller/"
---
# ArgoCD GitOps Sync Controller

Manages ArgoCD Application and ApplicationSet resources for Kubernetes GitOps deployments. Uses the ArgoCD REST API and argocd CLI to automate sync waves, health checks, and progressive rollout configurations.

## Overview

The ArgoCD GitOps Sync Controller provides comprehensive management of Kubernetes deployments through ArgoCD Application resources. It generates Application and ApplicationSet manifests with sync policies, automated pruning, and self-healing configurations.

The skill interfaces with the ArgoCD REST API for application state monitoring, sync status checking, and rollback operations. It configures sync waves and hooks using argocd.argoproj.io/sync-wave annotations for ordered deployment of dependent resources like ConfigMaps, Secrets, Deployments, and Services.

Advanced capabilities include ApplicationSet generation with Git directory and Pull Request generators for automatic environment provisioning, progressive delivery integration with Argo Rollouts for canary and blue-green deployments, and health check customization using Lua scripts. The controller also manages ArgoCD project configurations with RBAC policies, source repository restrictions, and destination namespace allowlists. Notification templates for Slack, email, and webhook integrations are generated using the argocd-notifications ConfigMap patterns.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-gitops-sync-controller
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-gitops-sync-controller -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-gitops-sync-controller -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-gitops-sync-controller -a codex
```

### OpenClaw

```bash
clawhub install argocd-gitops-sync-controller
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-gitops-sync-controller/)

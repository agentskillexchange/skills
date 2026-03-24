---
name: "ArgoCD GitOps Sync Controller"
description: "Manages ArgoCD Application and ApplicationSet resources for Kubernetes GitOps deployments. Uses the ArgoCD REST API and argocd CLI to automate sync waves, health checks, and progressive rollout configurations."
category: "CI/CD Integrations"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/argocd-gitops-sync-controller/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "argocd"  # from ase_tool_match
  github_stars: 22391  # from ase_github_stars (integer, not string)
  github_repo: "argoproj/argo-cd"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/argocd-gitops-sync-controller/

---
name: "ArgoCD Deployment Sync Skill"
description: "Manages GitOps deployments via the ArgoCD REST API and argocd CLI. Triggers application syncs through /api/v1/applications/{name}/sync, monitors health status via /api/v1/applications/{name}, and manages rollbacks using /api/v1/applications/{name}/rollback for Kubernetes workloads."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/argocd-deployment-sync-skill/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "argocd"  # from ase_tool_match
  github_stars: 22391  # from ase_github_stars (integer, not string)
  github_repo: "argoproj/argo-cd"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ArgoCD Deployment Sync Skill

Manages GitOps deployments via the ArgoCD REST API and argocd CLI. Triggers application syncs through /api/v1/applications/{name}/sync, monitors health status via /api/v1/applications/{name}, and manages rollbacks using /api/v1/applications/{name}/rollback for Kubernetes workloads.

## Overview

The ArgoCD Deployment Sync Skill provides GitOps-based continuous deployment management for Kubernetes clusters through the ArgoCD REST API. It handles application lifecycle management from creation through sync, health monitoring, and rollback.

Application management uses the /api/v1/applications endpoint for CRUD operations. The agent creates Application resources with configurable source repositories, target clusters, sync policies, and Helm/Kustomize parameter overrides. It supports ApplicationSets for multi-cluster and multi-tenant deployments using generators (list, cluster, git, matrix).

Sync operations are triggered via /api/v1/applications/{name}/sync with options for selective resource syncing, dry-run preview, prune control, and sync strategy (apply vs hook). The skill monitors sync progress through server-sent events at /api/v1/stream/applications, tracking resource-level sync and health status in real time.

Health monitoring queries /api/v1/applications/{name} for aggregate and per-resource health status (Healthy, Progressing, Degraded, Missing). The agent implements automated remediation workflows including sync retries, resource deletion for stuck resources, and automated rollback via /api/v1/applications/{name}/rollback when health checks fail.

Additional features include diff preview between desired and live state, RBAC project management through /api/v1/projects, repository credential management, and notification integration via ArgoCD Notifications for Slack/webhook alerts on sync events.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-sync-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-sync-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-sync-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-sync-skill -a codex
```

### OpenClaw

```bash
clawhub install argocd-deployment-sync-skill
```

## Source

- Marketplace: https://agentskillexchange.com/skills/argocd-deployment-sync-skill/

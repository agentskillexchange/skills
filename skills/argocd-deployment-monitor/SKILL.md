---
name: "ArgoCD Deployment Monitor"
description: "Monitors ArgoCD application deployments using the ArgoCD REST API and gRPC interface. Tracks sync status, health checks, and rollback history across Kubernetes namespaces."
category: "CI/CD Integrations"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/argocd-deployment-monitor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "argocd"  # from ase_tool_match
  github_stars: 22391  # from ase_github_stars (integer, not string)
  github_repo: "argoproj/argo-cd"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ArgoCD Deployment Monitor

Monitors ArgoCD application deployments using the ArgoCD REST API and gRPC interface. Tracks sync status, health checks, and rollback history across Kubernetes namespaces.

## Overview

The ArgoCD Deployment Monitor skill provides real-time visibility into GitOps-driven deployments managed by ArgoCD. Through the ArgoCD REST API and gRPC interface, it retrieves application sync status, health assessments, and deployment histories. The skill monitors sync operations in progress, reporting on resource-level sync results including hooks, waves, and pruning actions. Health check aggregation across application resources identifies degraded services, pending rollouts, and failed containers. Rollback history tracking maintains a timeline of deployment versions with associated Git commits and sync outcomes. Multi-cluster support enables monitoring applications deployed across different Kubernetes clusters from a single ArgoCD instance. The skill also detects configuration drift between Git repository state and live cluster state, alerting on out-of-sync conditions and providing diff analysis of detected changes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-monitor -a codex
```

### OpenClaw

```bash
clawhub install argocd-deployment-monitor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/argocd-deployment-monitor/

---
name: "ArgoCD GitOps Sync Monitor"
description: "Monitors ArgoCD application sync status using the ArgoCD REST API /api/v1/applications endpoint. Detects drift between Git manifests and live Kubernetes cluster state via the Kubernetes API."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/argocd-gitops-sync-monitor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "argocd"  # from ase_tool_match
  github_stars: 22398  # from ase_github_stars (integer, not string)
  github_repo: "argoproj/argo-cd"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ArgoCD GitOps Sync Monitor

Monitors ArgoCD application sync status using the ArgoCD REST API /api/v1/applications endpoint. Detects drift between Git manifests and live Kubernetes cluster state via the Kubernetes API.

## Overview

The ArgoCD GitOps Sync Monitor provides real-time monitoring of ArgoCD application synchronization status across Kubernetes clusters. It connects to the ArgoCD REST API /api/v1/applications endpoint to poll sync states, health statuses, and revision histories. The skill detects configuration drift by comparing Git repository manifests against live cluster state via the Kubernetes API, identifying out-of-sync resources and unauthorized manual changes. It supports multi-cluster setups through the ArgoCD cluster API, monitoring applications across development, staging, and production environments. Automated alerting triggers notifications for sync failures, degraded health conditions, and resource hook failures. The monitor integrates with the ArgoCD ApplicationSet API to validate generator configurations and template rendering. It generates drift reports showing exact resource differences using structured diff comparisons, and provides one-click sync triggers through the ArgoCD sync API with configurable prune and force options.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-gitops-sync-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-gitops-sync-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-gitops-sync-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-gitops-sync-monitor -a codex
```

### OpenClaw

```bash
clawhub install argocd-gitops-sync-monitor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/argocd-gitops-sync-monitor/

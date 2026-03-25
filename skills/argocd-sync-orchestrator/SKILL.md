---
name: "ArgoCD Sync Orchestrator"
description: "Manages ArgoCD application syncs using the argocd CLI and the Argo CD REST API (v1alpha1). Supports progressive delivery with Argo Rollouts integration and automated health checks via Kubernetes readiness probes."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/argocd-sync-orchestrator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "argocd"  # from ase_tool_match
  github_stars: 22398  # from ase_github_stars (integer, not string)
  github_repo: "argoproj/argo-cd"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ArgoCD Sync Orchestrator

Manages ArgoCD application syncs using the argocd CLI and the Argo CD REST API (v1alpha1). Supports progressive delivery with Argo Rollouts integration and automated health checks via Kubernetes readiness probes.

## Overview

The ArgoCD Sync Orchestrator skill automates GitOps deployment workflows through the Argo CD platform. It uses the argocd CLI and REST API (v1alpha1) to manage application synchronization, health monitoring, and rollback operations.

The skill implements progressive delivery patterns by integrating with Argo Rollouts for canary and blue-green deployment strategies. It monitors Kubernetes readiness and liveness probes to verify deployment health before promoting new versions.

Key capabilities include multi-cluster sync coordination, automatic drift detection and remediation, and integration with notification services like Slack and PagerDuty for deployment status updates. The skill supports Kustomize and Helm chart rendering, manages application sets for multi-tenant environments, and handles sync waves and hooks for complex deployment ordering.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install argocd-sync-orchestrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/argocd-sync-orchestrator/

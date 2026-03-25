---
name: "ArgoCD Sync Wave Orchestrator"
description: "Manages ArgoCD application sync waves and hooks using the ArgoCD API and argocd CLI. Coordinates multi-application deployment ordering with sync-wave annotations, health checks, and progressive rollout gates."
category: "CI/CD Integrations"
framework: "MCP-compatible"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/argocd-sync-wave-orchestrator-wave48/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "argocd"  # from ase_tool_match
  github_stars: 22391  # from ase_github_stars (integer, not string)
  github_repo: "argoproj/argo-cd"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ArgoCD Sync Wave Orchestrator

Manages ArgoCD application sync waves and hooks using the ArgoCD API and argocd CLI. Coordinates multi-application deployment ordering with sync-wave annotations, health checks, and progressive rollout gates.

## Overview

The ArgoCD Sync Wave Orchestrator skill manages complex multi-application deployment sequences in ArgoCD-managed Kubernetes environments. It uses the ArgoCD REST API and argocd CLI to configure sync waves, define resource hooks, and coordinate deployment ordering across dependent applications.

This skill generates proper sync-wave annotations (argocd.argoproj.io/sync-wave) for Kubernetes manifests to ensure resources are created in the correct order: namespaces and CRDs first, then configmaps and secrets, followed by deployments and services, and finally ingress resources and monitoring configurations.

Key capabilities include ApplicationSet template generation for managing multiple environments, sync policy configuration with automated self-healing and pruning, and hook definition for PreSync database migrations, Sync deployment steps, and PostSync verification tests. The skill understands ArgoCD health assessment for custom resources via lua health checks.

Advanced features include progressive delivery integration with Argo Rollouts for canary and blue-green deployment strategies, notification configuration via argocd-notifications for Slack and webhook alerts on sync failures, and multi-cluster application distribution using placement policies and cluster generators.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-wave-orchestrator-wave48
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-wave-orchestrator-wave48 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-wave-orchestrator-wave48 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-wave-orchestrator-wave48 -a codex
```

### OpenClaw

```bash
clawhub install argocd-sync-wave-orchestrator-wave48
```

## Source

- Marketplace: https://agentskillexchange.com/skills/argocd-sync-wave-orchestrator-wave48/

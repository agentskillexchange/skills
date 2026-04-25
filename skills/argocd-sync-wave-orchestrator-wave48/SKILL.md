---
title: "ArgoCD Sync Wave Orchestrator"
description: "Manages ArgoCD application sync waves and hooks using the ArgoCD API and argocd CLI. Coordinates multi-application deployment ordering with sync-wave annotations, health checks, and progressive rollout gates."
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

# ArgoCD Sync Wave Orchestrator

The ArgoCD Sync Wave Orchestrator skill manages complex multi-application deployment sequences in ArgoCD-managed Kubernetes environments. It uses the ArgoCD REST API and argocd CLI to configure sync waves, define resource hooks, and coordinate deployment ordering across dependent applications. This skill generates proper sync-wave annotations (argocd.argoproj.io/sync-wave) for Kubernetes manifests to ensure resources are created in the correct order: namespaces and CRDs first, then configmaps and secrets, followed by deployments and services, and finally ingress resources and monitoring configurations. Key capabilities include ApplicationSet template generation for managing multiple environments, sync policy configuration with automated self-healing and pruning, and hook definition for PreSync database migrations, Sync deployment steps, and PostSync verification tests. The skill understands ArgoCD health assessment for custom resources via lua health checks. Advanced features include progressive delivery integration with Argo Rollouts for canary and blue-green deployment strategies, notification configuration via argocd-notifications for Slack and webhook alerts on sync failures, and multi-cluster application distribution using placement policies and cluster generators.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/argocd-sync-wave-orchestrator-wave48/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argocd-sync-wave-orchestrator-wave48
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/argocd-sync-wave-orchestrator-wave48`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-wave-orchestrator-wave48/)

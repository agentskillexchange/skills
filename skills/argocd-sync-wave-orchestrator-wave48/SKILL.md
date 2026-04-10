---
title: "ArgoCD Sync Wave Orchestrator"
description: "Manages ArgoCD application sync waves and hooks using the ArgoCD API and argocd CLI. Coordinates multi-application deployment ordering with sync-wave annotations, health checks, and progressive rollout gates."
slug: "argocd-sync-wave-orchestrator-wave48"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/argocd-sync-wave-orchestrator-wave48/"
listed: true
---

# ArgoCD Sync Wave Orchestrator

Manages ArgoCD application sync waves and hooks using the ArgoCD API and argocd CLI. Coordinates multi-application deployment ordering with sync-wave annotations, health checks, and progressive rollout gates.

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
clawhub install argocd-sync-wave-orchestrator-wave48
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ArgoCD Sync Wave Orchestrator skill manages complex multi-application deployment sequences in ArgoCD-managed Kubernetes environments. It uses the ArgoCD REST API and argocd CLI to configure sync waves, define resource hooks, and coordinate deployment ordering across dependent applications.
This skill generates proper sync-wave annotations (argocd.argoproj.io/sync-wave) for Kubernetes manifests to ensure resources are created in the correct order: namespaces and CRDs first, then configmaps and secrets, followed by deployments and services, and finally ingress resources and monitoring configurations.
Key capabilities include ApplicationSet template generation for managing multiple environments, sync policy configuration with automated self-healing and pruning, and hook definition for PreSync database migrations, Sync deployment steps, and PostSync verification tests. The skill understands ArgoCD health assessment for custom resources via lua health checks.
Advanced features include progressive delivery integration with Argo Rollouts for canary and blue-green deployment strategies, notification configuration via argocd-notifications for Slack and webhook alerts on sync failures, and multi-cluster application distribution using placement policies and cluster generators.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-wave-orchestrator-wave48/)

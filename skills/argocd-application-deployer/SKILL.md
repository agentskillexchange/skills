---
title: "ArgoCD Application Deployer"
description: "Manages ArgoCD application deployments via the ArgoCD REST API and argocd CLI. Configures GitOps sync policies, automated rollbacks, and multi-cluster application sets with generator templates."
slug: "argocd-application-deployer"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/argocd-application-deployer/"
listed: true
---

# ArgoCD Application Deployer

Manages ArgoCD application deployments via the ArgoCD REST API and argocd CLI. Configures GitOps sync policies, automated rollbacks, and multi-cluster application sets with generator templates.

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
clawhub install argocd-application-deployer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ArgoCD Application Deployer skill automates Kubernetes GitOps deployments through the ArgoCD REST API and argocd CLI tooling. It manages Application and ApplicationSet custom resources for declarative, Git-driven continuous deployment across single and multi-cluster environments.
Application management creates ArgoCD Application manifests with proper source repository configuration, target cluster/namespace settings, and sync policy definitions. Automated sync policies include self-heal for drift correction, auto-prune for resource cleanup, and configurable sync windows that restrict deployments to approved maintenance periods. The skill configures health checks using custom Lua scripts for CRDs and manages resource hooks (PreSync, Sync, PostSync) for database migrations and smoke tests.
ApplicationSet support enables multi-cluster and multi-tenant deployment patterns using generators: Git directory generators for monorepo structures, cluster generators for fleet-wide rollouts, matrix generators for combinatorial deployments, and pull request generators for preview environments. The skill interfaces with the ArgoCD API to monitor sync status, retrieve application health, trigger manual syncs, and initiate rollbacks to previous Git revisions. Notification configuration integrates ArgoCD Notifications with Slack, Teams, and webhook triggers for deployment status updates. It generates Kustomize overlays and Helm value files organized by environment (dev/staging/production) with proper ArgoCD source directory or Helm chart references.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-deployer/)

---
title: "ArgoCD Application Sync Manager"
description: "Manages ArgoCD application synchronization using the ArgoCD REST API and argocd CLI. Handles sync waves, hooks, and health assessments for GitOps-driven Kubernetes deployments."
slug: "argocd-application-sync-manager-2"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/argocd-application-sync-manager-2/"
listed: true
---

# ArgoCD Application Sync Manager

Manages ArgoCD application synchronization using the ArgoCD REST API and argocd CLI. Handles sync waves, hooks, and health assessments for GitOps-driven Kubernetes deployments.

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
clawhub install argocd-application-sync-manager-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ArgoCD Application Sync Manager skill automates GitOps deployment workflows through the ArgoCD REST API (v1/applications) and the argocd CLI. It manages application sync operations with full control over sync waves, resource hooks (PreSync, Sync, PostSync, SyncFail), and health assessment checks.
The skill creates and manages ArgoCD Application resources with proper source tracking, including Helm chart references with value overrides, Kustomize overlays, and plain YAML directory structures. It supports multi-cluster deployments by managing destination configurations across different Kubernetes contexts.
For progressive delivery, the skill integrates with ArgoCD sync windows to enforce deployment schedules, configures auto-sync policies with self-heal and prune options, and monitors sync status through the Application Controller API. It handles ApplicationSets for generating applications from Git directory structures, cluster lists, or pull request generators, enabling scalable GitOps patterns across hundreds of microservices.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-sync-manager-2/)

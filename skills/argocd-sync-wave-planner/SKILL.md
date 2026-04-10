---
title: "ArgoCD Sync Wave Planner"
description: "Manages ArgoCD Application sync waves and hooks through the ArgoCD REST API and Kubernetes custom resources. Uses kubectl diff and Helm template rendering to validate manifests before triggering progressive rollouts via Argo Rollouts."
slug: "argocd-sync-wave-planner"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/argocd-sync-wave-planner/"
---

# ArgoCD Sync Wave Planner

Manages ArgoCD Application sync waves and hooks through the ArgoCD REST API and Kubernetes custom resources. Uses kubectl diff and Helm template rendering to validate manifests before triggering progressive rollouts via Argo Rollouts.

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
clawhub install argocd-sync-wave-planner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
The ArgoCD Sync Wave Planner manages complex Kubernetes deployment ordering through ArgoCD’s sync wave and hook mechanism. It ensures infrastructure components deploy before application workloads by analyzing resource dependencies and configuring appropriate argocd.argoproj.io/sync-wave annotations.
Key Capabilities
This skill uses the ArgoCD REST API to inspect Application sync status, health checks, and resource tree structures. It runs kubectl diff against live cluster state and renders Helm templates to validate manifests before triggering sync operations. Integration with Argo Rollouts enables progressive delivery strategies including canary deployments and blue-green cutover with automated analysis.
Deployment Workflow
Manages PreSync hooks for database migrations, Sync hooks for deployment coordination, and PostSync hooks for smoke tests and notification dispatch. Supports ApplicationSet generators for multi-cluster fleet management and integrates with Argo Notifications for Slack and webhook-based deployment tracking across environments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-wave-planner/)

---
title: "ArgoCD Deployment Runbook Agent"
description: "Manages GitOps deployments using ArgoCD API, argocd CLI, and Kustomize overlays. Automates sync operations, rollback procedures, and application health monitoring."
slug: "argocd-deployment-runbook-agent"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/argocd-deployment-runbook-agent/"
---

# ArgoCD Deployment Runbook Agent

Manages GitOps deployments using ArgoCD API, argocd CLI, and Kustomize overlays. Automates sync operations, rollback procedures, and application health monitoring.

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
clawhub install argocd-deployment-runbook-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ArgoCD Deployment Runbook Agent manages GitOps-based deployments through the ArgoCD REST API (/api/v1/applications, /api/v1/session) and argocd CLI. It automates sync operations, monitors application health, and executes rollback procedures when deployments fail.
The agent creates and manages ArgoCD Application resources with Kustomize overlays for environment-specific configuration (dev, staging, production). It handles sync waves and hooks for ordered deployment of dependent resources, including pre-sync database migrations and post-sync smoke tests.
Health monitoring covers application sync status, resource health (Healthy, Progressing, Degraded, Missing), and diff detection between desired and live state. The agent responds to sync failures by analyzing resource events, checking pod logs for crash reasons, and executing automated rollbacks (argocd app rollback) to the last healthy revision.
Advanced features include multi-cluster deployment coordination, ApplicationSet generation for dynamic environment provisioning, and Progressive Delivery integration with Argo Rollouts for canary and blue-green deployment strategies. The agent generates deployment audit logs and tracks mean time to recovery across application revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-deployment-runbook-agent/)

---
title: "ArgoCD Deployment Runbook Agent"
description: "The ArgoCD Deployment Runbook Agent manages GitOps-based deployments through the ArgoCD REST API (/api/v1/applications, /api/v1/session) and argocd CLI. It automates sync operations, monitors application health, and executes rollback procedures when deployments fail.\nThe agent creates and manages ArgoCD Application resources with Kustomize overlays for environment-specific configuration (dev, staging, production). It handles sync waves and hooks for ordered deployment of dependent resources, including pre-sync database migrations and post-sync smoke tests.\nHealth monitoring covers application sync status, resource health (Healthy, Progressing, Degraded, Missing), and diff detection between desired and live state. The agent responds to sync failures by analyzing resource events, checking pod logs for crash reasons, and executing automated rollbacks (argocd app rollback) to the last healthy revision.\nAdvanced features include multi-cluster deployment coordination, ApplicationSet generation for dynamic environment provisioning, and Progressive Delivery integration with Argo Rollouts for canary and blue-green deployment strategies. The agent generates deployment audit logs and tracks mean time to recovery across application revisions."
verification: security_reviewed
source: "https://github.com/argoproj/argo-cd"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD Deployment Runbook Agent

The ArgoCD Deployment Runbook Agent manages GitOps-based deployments through the ArgoCD REST API (/api/v1/applications, /api/v1/session) and argocd CLI. It automates sync operations, monitors application health, and executes rollback procedures when deployments fail.
The agent creates and manages ArgoCD Application resources with Kustomize overlays for environment-specific configuration (dev, staging, production). It handles sync waves and hooks for ordered deployment of dependent resources, including pre-sync database migrations and post-sync smoke tests.
Health monitoring covers application sync status, resource health (Healthy, Progressing, Degraded, Missing), and diff detection between desired and live state. The agent responds to sync failures by analyzing resource events, checking pod logs for crash reasons, and executing automated rollbacks (argocd app rollback) to the last healthy revision.
Advanced features include multi-cluster deployment coordination, ApplicationSet generation for dynamic environment provisioning, and Progressive Delivery integration with Argo Rollouts for canary and blue-green deployment strategies. The agent generates deployment audit logs and tracks mean time to recovery across application revisions.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argocd-deployment-runbook-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/argocd-deployment-runbook-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-deployment-runbook-agent/)

---
name: "ArgoCD Deployment Runbook Agent"
description: "Manages GitOps deployments using ArgoCD API, argocd CLI, and Kustomize overlays. Automates sync operations, rollback procedures, and application health monitoring."
category: "Runbooks &amp; Diagnostics"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argocd-deployment-runbook-agent/"
---
# ArgoCD Deployment Runbook Agent

Manages GitOps deployments using ArgoCD API, argocd CLI, and Kustomize overlays. Automates sync operations, rollback procedures, and application health monitoring.

The ArgoCD Deployment Runbook Agent manages GitOps-based deployments through the ArgoCD REST API (/api/v1/applications, /api/v1/session) and argocd CLI. It automates sync operations, monitors application health, and executes rollback procedures when deployments fail.

The agent creates and manages ArgoCD Application resources with Kustomize overlays for environment-specific configuration (dev, staging, production). It handles sync waves and hooks for ordered deployment of dependent resources, including pre-sync database migrations and post-sync smoke tests.

Health monitoring covers application sync status, resource health (Healthy, Progressing, Degraded, Missing), and diff detection between desired and live state. The agent responds to sync failures by analyzing resource events, checking pod logs for crash reasons, and executing automated rollbacks (argocd app rollback) to the last healthy revision.

Advanced features include multi-cluster deployment coordination, ApplicationSet generation for dynamic environment provisioning, and Progressive Delivery integration with Argo Rollouts for canary and blue-green deployment strategies. The agent generates deployment audit logs and tracks mean time to recovery across application revisions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-runbook-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-runbook-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-runbook-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-runbook-agent -a codex
```

### OpenClaw

```bash
clawhub install argocd-deployment-runbook-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-deployment-runbook-agent/)

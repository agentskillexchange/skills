---
name: "ArgoCD Deployment Sync Skill"
description: "Manages GitOps deployments via the ArgoCD REST API and argocd CLI. Triggers application syncs through /api/v1/applications/{name}/sync, monitors health status via /api/v1/applications/{name}, and manages rollbacks using /api/v1/applications/{name}/rollback for Kubernetes workloads."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argocd-deployment-sync-skill/"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
---

# ArgoCD Deployment Sync Skill

The ArgoCD Deployment Sync Skill provides GitOps-based continuous deployment management for Kubernetes clusters through the ArgoCD REST API. It handles application lifecycle management from creation through sync, health monitoring, and rollback.
Application management uses the /api/v1/applications endpoint for CRUD operations. The agent creates Application resources with configurable source repositories, target clusters, sync policies, and Helm/Kustomize parameter overrides. It supports ApplicationSets for multi-cluster and multi-tenant deployments using generators (list, cluster, git, matrix).
Sync operations are triggered via /api/v1/applications/{name}/sync with options for selective resource syncing, dry-run preview, prune control, and sync strategy (apply vs hook). The skill monitors sync progress through server-sent events at /api/v1/stream/applications, tracking resource-level sync and health status in real time.
Health monitoring queries /api/v1/applications/{name} for aggregate and per-resource health status (Healthy, Progressing, Degraded, Missing). The agent implements automated remediation workflows including sync retries, resource deletion for stuck resources, and automated rollback via /api/v1/applications/{name}/rollback when health checks fail.
Additional features include diff preview between desired and live state, RBAC project management through /api/v1/projects, repository credential management, and notification integration via ArgoCD Notifications for Slack/webhook alerts on sync events.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-deployment-sync-skill/)

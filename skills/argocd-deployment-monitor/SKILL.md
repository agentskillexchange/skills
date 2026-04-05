---
name: "ArgoCD Deployment Monitor"
description: "Monitors ArgoCD application deployments using the ArgoCD REST API and gRPC interface. Tracks sync status, health checks, and rollback history across Kubernetes namespaces."
category: "CI/CD Integrations"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argocd-deployment-monitor/"
---
# ArgoCD Deployment Monitor

Monitors ArgoCD application deployments using the ArgoCD REST API and gRPC interface. Tracks sync status, health checks, and rollback history across Kubernetes namespaces.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-deployment-monitor -a codex
```

### OpenClaw

```bash
clawhub install argocd-deployment-monitor
```

## Details

The ArgoCD Deployment Monitor skill provides real-time visibility into GitOps-driven deployments managed by ArgoCD. Through the ArgoCD REST API and gRPC interface, it retrieves application sync status, health assessments, and deployment histories. The skill monitors sync operations in progress, reporting on resource-level sync results including hooks, waves, and pruning actions. Health check aggregation across application resources identifies degraded services, pending rollouts, and failed containers. Rollback history tracking maintains a timeline of deployment versions with associated Git commits and sync outcomes. Multi-cluster support enables monitoring applications deployed across different Kubernetes clusters from a single ArgoCD instance. The skill also detects configuration drift between Git repository state and live cluster state, alerting on out-of-sync conditions and providing diff analysis of detected changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-deployment-monitor/)

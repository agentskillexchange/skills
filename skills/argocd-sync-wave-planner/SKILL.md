---
name: "ArgoCD Sync Wave Planner"
description: "Manages ArgoCD Application sync waves and hooks through the ArgoCD REST API and Kubernetes custom resources. Uses kubectl diff and Helm template rendering to validate manifests before triggering progressive rollouts via Argo Rollouts."
category: "CI/CD Integrations"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argocd-sync-wave-planner/"
tool_ecosystem:
  tool: "argocd"
  github_stars: 22398
  github_repo: "argoproj/argo-cd"
  license: "Apache-2.0"
  maintained: true
---

# ArgoCD Sync Wave Planner

Manages ArgoCD Application sync waves and hooks through the ArgoCD REST API and Kubernetes custom resources. Uses kubectl diff and Helm template rendering to validate manifests before triggering progressive rollouts via Argo Rollouts.

## Overview

Overview

The ArgoCD Sync Wave Planner manages complex Kubernetes deployment ordering through ArgoCD’s sync wave and hook mechanism. It ensures infrastructure components deploy before application workloads by analyzing resource dependencies and configuring appropriate `argocd.argoproj.io/sync-wave` annotations.

Key Capabilities

This skill uses the ArgoCD REST API to inspect Application sync status, health checks, and resource tree structures. It runs `kubectl diff` against live cluster state and renders Helm templates to validate manifests before triggering sync operations. Integration with Argo Rollouts enables progressive delivery strategies including canary deployments and blue-green cutover with automated analysis.

Deployment Workflow

Manages PreSync hooks for database migrations, Sync hooks for deployment coordination, and PostSync hooks for smoke tests and notification dispatch. Supports ApplicationSet generators for multi-cluster fleet management and integrates with Argo Notifications for Slack and webhook-based deployment tracking across environments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-wave-planner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-wave-planner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-wave-planner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-wave-planner -a codex
```

### OpenClaw

```bash
clawhub install argocd-sync-wave-planner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/argocd-sync-wave-planner/

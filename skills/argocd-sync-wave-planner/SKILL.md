---
title: "ArgoCD Sync Wave Planner"
description: "Manages ArgoCD Application sync waves and hooks through the ArgoCD REST API and Kubernetes custom resources. Uses kubectl diff and Helm template rendering to validate manifests before triggering progressive rollouts via Argo Rollouts."
verification: security_reviewed
source: "https://github.com/argoproj/argo-cd"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD Sync Wave Planner

Overview
The ArgoCD Sync Wave Planner manages complex Kubernetes deployment ordering through ArgoCD’s sync wave and hook mechanism. It ensures infrastructure components deploy before application workloads by analyzing resource dependencies and configuring appropriate argocd.argoproj.io/sync-wave annotations.

Key Capabilities
This skill uses the ArgoCD REST API to inspect Application sync status, health checks, and resource tree structures. It runs kubectl diff against live cluster state and renders Helm templates to validate manifests before triggering sync operations. Integration with Argo Rollouts enables progressive delivery strategies including canary deployments and blue-green cutover with automated analysis.

Deployment Workflow
Manages PreSync hooks for database migrations, Sync hooks for deployment coordination, and PostSync hooks for smoke tests and notification dispatch. Supports ApplicationSet generators for multi-cluster fleet management and integrates with Argo Notifications for Slack and webhook-based deployment tracking across environments.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argocd-sync-wave-planner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/argocd-sync-wave-planner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-wave-planner/)

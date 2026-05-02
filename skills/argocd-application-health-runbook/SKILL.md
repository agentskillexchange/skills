---
title: "ArgoCD Application Health Runbook"
description: "Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions."
verification: "security_reviewed"
source: "https://github.com/argoproj/argo-cd"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD Application Health Runbook

This runbook skill connects to an ArgoCD instance via its REST API and argocd CLI to diagnose application health issues. It queries the /api/v1/applications/{name} endpoint for detailed sync status, resource health trees, and operation state. The skill interprets OutOfSync, Degraded, Unknown, and Missing conditions and provides step-by-step remediation guidance. For common failure modes like ImagePullBackOff, CrashLoopBackOff, and failed Helm hooks, it suggests specific kubectl and argocd commands. It also checks the ArgoCD application controller logs via the Kubernetes API for deeper diagnostics. Integration with PagerDuty incident notes and Slack runbook channels allows operators to share remediation context during on-call incidents. The skill supports multi-cluster ArgoCD setups and respects RBAC policies.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/argocd-application-health-runbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argocd-application-health-runbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/argocd-application-health-runbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-health-runbook/)

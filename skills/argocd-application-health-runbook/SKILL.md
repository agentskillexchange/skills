---
name: "ArgoCD Application Health Runbook"
description: "Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argocd-application-health-runbook/"
tool_ecosystem:
  tool: "argocd"
  github_stars: 22398
  github_repo: "argoproj/argo-cd"
  license: "Apache-2.0"
  maintained: true
---

# ArgoCD Application Health Runbook

Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions.

## Overview

This runbook skill connects to an ArgoCD instance via its REST API and argocd CLI to diagnose application health issues. It queries the /api/v1/applications/{name} endpoint for detailed sync status, resource health trees, and operation state. The skill interprets OutOfSync, Degraded, Unknown, and Missing conditions and provides step-by-step remediation guidance. For common failure modes like ImagePullBackOff, CrashLoopBackOff, and failed Helm hooks, it suggests specific kubectl and argocd commands. It also checks the ArgoCD application controller logs via the Kubernetes API for deeper diagnostics. Integration with PagerDuty incident notes and Slack runbook channels allows operators to share remediation context during on-call incidents. The skill supports multi-cluster ArgoCD setups and respects RBAC policies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook -a codex
```

### OpenClaw

```bash
clawhub install argocd-application-health-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/argocd-application-health-runbook/

---
title: "ArgoCD Application Health Runbook"
description: "This runbook skill connects to an ArgoCD instance via its REST API and argocd CLI to diagnose application health issues. It queries the /api/v1/applications/{name} endpoint for detailed sync status, resource health trees, and operation state. The skill interprets OutOfSync, Degraded, Unknown, and Missing conditions and provides step-by-step remediation guidance. For common failure modes like ImagePullBackOff, CrashLoopBackOff, and failed Helm hooks, it suggests specific kubectl and argocd commands. It also checks the ArgoCD application controller logs via the Kubernetes API for deeper diagnostics. Integration with PagerDuty incident notes and Slack runbook channels allows operators to share remediation context during on-call incidents. The skill supports multi-cluster ArgoCD setups and respects RBAC policies."
source: "https://github.com/argoproj/argo-cd"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD Application Health Runbook

This runbook skill connects to an ArgoCD instance via its REST API and argocd CLI to diagnose application health issues. It queries the /api/v1/applications/{name} endpoint for detailed sync status, resource health trees, and operation state. The skill interprets OutOfSync, Degraded, Unknown, and Missing conditions and provides step-by-step remediation guidance. For common failure modes like ImagePullBackOff, CrashLoopBackOff, and failed Helm hooks, it suggests specific kubectl and argocd commands. It also checks the ArgoCD application controller logs via the Kubernetes API for deeper diagnostics. Integration with PagerDuty incident notes and Slack runbook channels allows operators to share remediation context during on-call incidents. The skill supports multi-cluster ArgoCD setups and respects RBAC policies.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-health-runbook/)

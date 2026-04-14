---
title: "ArgoCD Application Health Runbook"
description: "Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions."
verification: security_reviewed
source: "https://github.com/argoproj/argo-cd"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-health-runbook/)

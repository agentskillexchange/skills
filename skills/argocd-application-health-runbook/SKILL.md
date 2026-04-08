---
title: ArgoCD Application Health Runbook
description: This runbook skill connects to an ArgoCD instance via its REST API and
  argocd CLI to diagnose application health issues. It queries the /api/v1/applications/{name}
  endpoint for detailed sync status, resource health trees, and operation state. The
  skill interprets OutOfSync, Degraded, Unknown, and Missing conditions and provides
  step-by-step remediation guidance. For common failure modes like ImagePullBackOff,
  CrashLoopBackOff, and failed Helm hooks, it suggests specific kubectl and argocd
  commands. It also checks the ArgoCD application controller logs via the Kubernetes
  API for deeper diagnostics. Integration with PagerDuty incident notes and Slack
  runbook channels allows operators to share remediation context during on-call incidents.
  The skill supports multi-cluster ArgoCD setups and respects RBAC policies.
verification: security_reviewed
source: https://agentskillexchange.com/skills/argocd-application-health-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---

# ArgoCD Application Health Runbook

This runbook skill connects to an ArgoCD instance via its REST API and argocd CLI to diagnose application health issues. It queries the /api/v1/applications/{name} endpoint for detailed sync status, resource health trees, and operation state. The skill interprets OutOfSync, Degraded, Unknown, and Missing conditions and provides step-by-step remediation guidance. For common failure modes like ImagePullBackOff, CrashLoopBackOff, and failed Helm hooks, it suggests specific kubectl and argocd commands. It also checks the ArgoCD application controller logs via the Kubernetes API for deeper diagnostics. Integration with PagerDuty incident notes and Slack runbook channels allows operators to share remediation context during on-call incidents. The skill supports multi-cluster ArgoCD setups and respects RBAC policies.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-health-runbook/)

---
title: ArgoCD Application Health Runbook
description: Diagnoses ArgoCD application sync failures and degraded states using
  the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync
  status, resource health, and operation state. Provides automated remediation steps
  for OutOfSync, Degraded, and Missing resource conditions.
verification: security_reviewed
source: https://agentskillexchange.com/skills/argocd-application-health-runbook/
category:
- Runbooks & Diagnostics
framework:
- OpenClaw
---


# ArgoCD Application Health Runbook

Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-health-runbook/)

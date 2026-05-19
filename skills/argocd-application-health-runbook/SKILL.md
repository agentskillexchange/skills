---
name: "ArgoCD Application Health Runbook"
slug: "argocd-application-health-runbook"
description: "Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions."
github_stars: 22593
verification: "security_reviewed"
source: "https://github.com/argoproj/argo-cd"
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD Application Health Runbook

Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions.

## Installation

Basic usage or getting-started notes:
- [Couchbase - How To Run a Database Cluster in Kubernetes Using Argo CD](https://youtu.be/nkPoPaVzExY)
- [Getting Started with ArgoCD for GitOps Deployments](https://youtu.be/AvLuplh1skA)

- Source: https://github.com/argoproj/argo-cd
- Extracted from upstream docs: https://raw.githubusercontent.com/argoproj/argo-cd/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-health-runbook/)

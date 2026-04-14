---
title: "ArgoCD Deployment Runbook Agent"
description: "Manages GitOps deployments using ArgoCD API, argocd CLI, and Kustomize overlays. Automates sync operations, rollback procedures, and application health monitoring."
verification: security_reviewed
source: "https://github.com/argoproj/argo-cd"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD Deployment Runbook Agent

The ArgoCD Deployment Runbook Agent manages GitOps-based deployments through the ArgoCD REST API (/api/v1/applications, /api/v1/session) and argocd CLI. It automates sync operations, monitors application health, and executes rollback procedures when deployments fail.

The agent creates and manages ArgoCD Application resources with Kustomize overlays for environment-specific configuration (dev, staging, production). It handles sync waves and hooks for ordered deployment of dependent resources, including pre-sync database migrations and post-sync smoke tests.

Health monitoring covers application sync status, resource health (Healthy, Progressing, Degraded, Missing), and diff detection between desired and live state. The agent responds to sync failures by analyzing resource events, checking pod logs for crash reasons, and executing automated rollbacks (argocd app rollback) to the last healthy revision.

Advanced features include multi-cluster deployment coordination, ApplicationSet generation for dynamic environment provisioning, and Progressive Delivery integration with Argo Rollouts for canary and blue-green deployment strategies. The agent generates deployment audit logs and tracks mean time to recovery across application revisions.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-deployment-runbook-agent/)

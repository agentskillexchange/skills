---
title: ArgoCD GitOps Sync Controller
description: The ArgoCD GitOps Sync Controller provides comprehensive management of
  Kubernetes deployments through ArgoCD Application resources. It generates Application
  and ApplicationSet manifests with sync policies, automated pruning, and self-healing
  configurations. The skill interfaces with the ArgoCD REST API for application state
  monitoring, sync status checking, and rollback operations. It configures sync waves
  and hooks using argocd.argoproj.io/sync-wave annotations for ordered deployment
  of dependent resources like ConfigMaps, Secrets, Deployments, and Services. Advanced
  capabilities include ApplicationSet generation with Git directory and Pull Request
  generators for automatic environment provisioning, progressive delivery integration
  with Argo Rollouts for canary and blue-green deployments, and health check customization
  using Lua scripts. The controller also manages ArgoCD project configurations with
  RBAC policies, source repository restrictions, and destination namespace allowlists.
  Notification templates for Slack, email, and webhook integrations are generated
  using the argocd-notifications ConfigMap patterns.
verification: security_reviewed
source: https://agentskillexchange.com/skills/argocd-gitops-sync-controller/
category:
- CI/CD Integrations
framework:
- MCP
---

# ArgoCD GitOps Sync Controller

The ArgoCD GitOps Sync Controller provides comprehensive management of Kubernetes deployments through ArgoCD Application resources. It generates Application and ApplicationSet manifests with sync policies, automated pruning, and self-healing configurations. The skill interfaces with the ArgoCD REST API for application state monitoring, sync status checking, and rollback operations. It configures sync waves and hooks using argocd.argoproj.io/sync-wave annotations for ordered deployment of dependent resources like ConfigMaps, Secrets, Deployments, and Services. Advanced capabilities include ApplicationSet generation with Git directory and Pull Request generators for automatic environment provisioning, progressive delivery integration with Argo Rollouts for canary and blue-green deployments, and health check customization using Lua scripts. The controller also manages ArgoCD project configurations with RBAC policies, source repository restrictions, and destination namespace allowlists. Notification templates for Slack, email, and webhook integrations are generated using the argocd-notifications ConfigMap patterns.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-gitops-sync-controller/)

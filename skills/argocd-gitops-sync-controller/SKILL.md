---
title: "ArgoCD GitOps Sync Controller"
description: "Manages ArgoCD Application and ApplicationSet resources for Kubernetes GitOps deployments. Uses the ArgoCD REST API and argocd CLI to automate sync waves, health checks, and progressive rollout configurations."
verification: security_reviewed
source: "https://github.com/argoproj/argo-cd"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD GitOps Sync Controller

The ArgoCD GitOps Sync Controller provides comprehensive management of Kubernetes deployments through ArgoCD Application resources. It generates Application and ApplicationSet manifests with sync policies, automated pruning, and self-healing configurations.

The skill interfaces with the ArgoCD REST API for application state monitoring, sync status checking, and rollback operations. It configures sync waves and hooks using argocd.argoproj.io/sync-wave annotations for ordered deployment of dependent resources like ConfigMaps, Secrets, Deployments, and Services.

Advanced capabilities include ApplicationSet generation with Git directory and Pull Request generators for automatic environment provisioning, progressive delivery integration with Argo Rollouts for canary and blue-green deployments, and health check customization using Lua scripts. The controller also manages ArgoCD project configurations with RBAC policies, source repository restrictions, and destination namespace allowlists. Notification templates for Slack, email, and webhook integrations are generated using the argocd-notifications ConfigMap patterns.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-gitops-sync-controller/)

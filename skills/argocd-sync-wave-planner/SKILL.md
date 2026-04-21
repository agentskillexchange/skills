---
title: "ArgoCD Sync Wave Planner"
slug: "argocd-sync-wave-planner"
description: "Manages ArgoCD Application sync waves and hooks through the ArgoCD REST API and Kubernetes custom resources. Uses kubectl diff and Helm template rendering to validate manifests before triggering progressive rollouts via Argo Rollouts."
verification: security_reviewed
source: "https://github.com/argoproj/argo-cd"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD Sync Wave Planner

Manages ArgoCD Application sync waves and hooks through the ArgoCD REST API and Kubernetes custom resources. Uses kubectl diff and Helm template rendering to validate manifests before triggering progressive rollouts via Argo Rollouts.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-wave-planner/)

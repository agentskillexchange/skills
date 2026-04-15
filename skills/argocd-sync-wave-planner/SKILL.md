---
title: "ArgoCD Sync Wave Planner"
description: "Manages ArgoCD Application sync waves and hooks through the ArgoCD REST API and Kubernetes custom resources. Uses kubectl diff and Helm template rendering to validate manifests before triggering progressive rollouts via Argo Rollouts."
verification: listed
source: "https://agentskillexchange.com/skills/argocd-sync-wave-planner/"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
---

# ArgoCD Sync Wave Planner

Manages ArgoCD Application sync waves and hooks through the ArgoCD REST API and Kubernetes custom resources. Uses kubectl diff and Helm template rendering to validate manifests before triggering progressive rollouts via Argo Rollouts.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-wave-planner/)

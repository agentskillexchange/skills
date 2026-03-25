---
name: "ArgoCD Application Sync Manager"
description: "Manages ArgoCD application synchronization using the ArgoCD REST API and argocd CLI. Handles sync waves, hooks, and health assessments for GitOps-driven Kubernetes deployments."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/argocd-application-sync-manager-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "argocd"  # from ase_tool_match
  github_stars: 22398  # from ase_github_stars (integer, not string)
  github_repo: "argoproj/argo-cd"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ArgoCD Application Sync Manager

Manages ArgoCD application synchronization using the ArgoCD REST API and argocd CLI. Handles sync waves, hooks, and health assessments for GitOps-driven Kubernetes deployments.

## Overview

The ArgoCD Application Sync Manager skill automates GitOps deployment workflows through the ArgoCD REST API (v1/applications) and the argocd CLI. It manages application sync operations with full control over sync waves, resource hooks (PreSync, Sync, PostSync, SyncFail), and health assessment checks.

The skill creates and manages ArgoCD Application resources with proper source tracking, including Helm chart references with value overrides, Kustomize overlays, and plain YAML directory structures. It supports multi-cluster deployments by managing destination configurations across different Kubernetes contexts.

For progressive delivery, the skill integrates with ArgoCD sync windows to enforce deployment schedules, configures auto-sync policies with self-heal and prune options, and monitors sync status through the Application Controller API. It handles ApplicationSets for generating applications from Git directory structures, cluster lists, or pull request generators, enabling scalable GitOps patterns across hundreds of microservices.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-application-sync-manager-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-application-sync-manager-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-application-sync-manager-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-application-sync-manager-2 -a codex
```

### OpenClaw

```bash
clawhub install argocd-application-sync-manager-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/argocd-application-sync-manager-2/

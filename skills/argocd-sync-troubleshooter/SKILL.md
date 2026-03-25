---
name: "ArgoCD Sync Troubleshooter"
description: "Diagnoses ArgoCD application sync failures using the ArgoCD REST API and Kubernetes resource diff analysis. Identifies Helm value conflicts, Kustomize overlay errors, and resource health check failures."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/argocd-sync-troubleshooter/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "argocd"  # from ase_tool_match
  github_stars: 22398  # from ase_github_stars (integer, not string)
  github_repo: "argoproj/argo-cd"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ArgoCD Sync Troubleshooter

Diagnoses ArgoCD application sync failures using the ArgoCD REST API and Kubernetes resource diff analysis. Identifies Helm value conflicts, Kustomize overlay errors, and resource health check failures.

## Overview

The ArgoCD Sync Troubleshooter skill automates the diagnosis of GitOps synchronization failures in ArgoCD-managed Kubernetes deployments. It connects via the ArgoCD REST API to retrieve application sync status, resource tree structures, and detailed diff information between desired and live states.

For Helm-based applications, the troubleshooter analyzes rendered manifests against value file hierarchies to identify template rendering failures, missing values, and type mismatches. Kustomize application diagnostics cover overlay application order, strategic merge patch conflicts, and JSON patch validation errors.

The skill performs deep Kubernetes resource health analysis using ArgoCD’s health assessment framework, checking custom health checks defined in argocd-cm ConfigMap, Lua-based health scripts, and standard resource health indicators (Deployment rollout status, StatefulSet ready replicas, Job completion).

Sync failure diagnosis includes permission analysis (RBAC errors for the ArgoCD application controller service account), namespace validation, CRD dependency checking, and resource quota evaluation. The troubleshooter generates step-by-step remediation runbooks tailored to each specific failure type with kubectl commands ready for execution.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-troubleshooter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-troubleshooter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-troubleshooter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-troubleshooter -a codex
```

### OpenClaw

```bash
clawhub install argocd-sync-troubleshooter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/argocd-sync-troubleshooter/

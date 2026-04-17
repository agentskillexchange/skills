---
title: "ArgoCD Sync Drift Detector"
description: "The ArgoCD Sync Drift Detector skill continuously monitors your GitOps deployments for configuration drift between the desired state in Git and the live state in your Kubernetes clusters. It connects to the ArgoCD server via the ArgoCD REST API (backed by grpc-gateway) to enumerate applications and their sync statuses.\nWhen drift is detected, the skill uses kubectl diff against the target cluster to produce a human-readable comparison of the divergent resources. It categorizes drift into severity levels: critical (security-related changes like RBAC modifications or secret mutations), warning (resource limit changes, replica count modifications), and informational (annotation or label changes).\nThe skill integrates with the Kubernetes client-go library patterns to authenticate against multiple clusters using kubeconfig contexts or ArgoCD-managed cluster secrets. It can parse Helm values overrides, Kustomize patches, and plain YAML manifests to identify the root cause of drift.\nRemediation playbooks are generated automatically, offering options to either force-sync from Git, update Git to match the live state, or create a targeted argocd app sync command with the –prune flag for specific resources."
verification: security_reviewed
source: "https://github.com/argoproj/argo-cd"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD Sync Drift Detector

The ArgoCD Sync Drift Detector skill continuously monitors your GitOps deployments for configuration drift between the desired state in Git and the live state in your Kubernetes clusters. It connects to the ArgoCD server via the ArgoCD REST API (backed by grpc-gateway) to enumerate applications and their sync statuses.
When drift is detected, the skill uses kubectl diff against the target cluster to produce a human-readable comparison of the divergent resources. It categorizes drift into severity levels: critical (security-related changes like RBAC modifications or secret mutations), warning (resource limit changes, replica count modifications), and informational (annotation or label changes).
The skill integrates with the Kubernetes client-go library patterns to authenticate against multiple clusters using kubeconfig contexts or ArgoCD-managed cluster secrets. It can parse Helm values overrides, Kustomize patches, and plain YAML manifests to identify the root cause of drift.
Remediation playbooks are generated automatically, offering options to either force-sync from Git, update Git to match the live state, or create a targeted argocd app sync command with the –prune flag for specific resources.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argocd-sync-drift-detector
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/argocd-sync-drift-detector` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-drift-detector/)

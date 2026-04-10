---
title: "ArgoCD Sync Drift Detector"
description: "Monitors ArgoCD applications for configuration drift using the ArgoCD REST API and grpc-gateway. Compares live Kubernetes manifests against Git-declared state and generates remediation playbooks via kubectl diff."
slug: "argocd-sync-drift-detector"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/argocd-sync-drift-detector/"
listed: true
---

# ArgoCD Sync Drift Detector

Monitors ArgoCD applications for configuration drift using the ArgoCD REST API and grpc-gateway. Compares live Kubernetes manifests against Git-declared state and generates remediation playbooks via kubectl diff.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install argocd-sync-drift-detector
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ArgoCD Sync Drift Detector skill continuously monitors your GitOps deployments for configuration drift between the desired state in Git and the live state in your Kubernetes clusters. It connects to the ArgoCD server via the ArgoCD REST API (backed by grpc-gateway) to enumerate applications and their sync statuses.
When drift is detected, the skill uses kubectl diff against the target cluster to produce a human-readable comparison of the divergent resources. It categorizes drift into severity levels: critical (security-related changes like RBAC modifications or secret mutations), warning (resource limit changes, replica count modifications), and informational (annotation or label changes).
The skill integrates with the Kubernetes client-go library patterns to authenticate against multiple clusters using kubeconfig contexts or ArgoCD-managed cluster secrets. It can parse Helm values overrides, Kustomize patches, and plain YAML manifests to identify the root cause of drift.
Remediation playbooks are generated automatically, offering options to either force-sync from Git, update Git to match the live state, or create a targeted argocd app sync command with the –prune flag for specific resources.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-drift-detector/)

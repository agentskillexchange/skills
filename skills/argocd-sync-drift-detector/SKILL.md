---
name: "ArgoCD Sync Drift Detector"
description: "Monitors ArgoCD applications for configuration drift using the ArgoCD REST API and grpc-gateway. Compares live Kubernetes manifests against Git-declared state and generates remediation playbooks via kubectl diff."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argocd-sync-drift-detector/"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
---

# ArgoCD Sync Drift Detector

The ArgoCD Sync Drift Detector skill continuously monitors your GitOps deployments for configuration drift between the desired state in Git and the live state in your Kubernetes clusters. It connects to the ArgoCD server via the ArgoCD REST API (backed by grpc-gateway) to enumerate applications and their sync statuses.
When drift is detected, the skill uses kubectl diff against the target cluster to produce a human-readable comparison of the divergent resources. It categorizes drift into severity levels: critical (security-related changes like RBAC modifications or secret mutations), warning (resource limit changes, replica count modifications), and informational (annotation or label changes).
The skill integrates with the Kubernetes client-go library patterns to authenticate against multiple clusters using kubeconfig contexts or ArgoCD-managed cluster secrets. It can parse Helm values overrides, Kustomize patches, and plain YAML manifests to identify the root cause of drift.
Remediation playbooks are generated automatically, offering options to either force-sync from Git, update Git to match the live state, or create a targeted argocd app sync command with the -prune flag for specific resources.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-drift-detector/)

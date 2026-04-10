---
name: ArgoCD Sync Troubleshooter
description: Diagnoses ArgoCD application sync failures using the ArgoCD REST API
  and Kubernetes resource diff analysis. Identifies Helm value conflicts, Kustomize
  overlay errors, and resource health check failures.
verification: security_reviewed
source: https://agentskillexchange.com/skills/argocd-sync-troubleshooter/
category:
- CI/CD Integrations
framework:
- Claude Agents
---
# ArgoCD Sync Troubleshooter

The ArgoCD Sync Troubleshooter skill automates the diagnosis of GitOps synchronization failures in ArgoCD-managed Kubernetes deployments. It connects via the ArgoCD REST API to retrieve application sync status, resource tree structures, and detailed diff information between desired and live states.
For Helm-based applications, the troubleshooter analyzes rendered manifests against value file hierarchies to identify template rendering failures, missing values, and type mismatches. Kustomize application diagnostics cover overlay application order, strategic merge patch conflicts, and JSON patch validation errors.
The skill performs deep Kubernetes resource health analysis using ArgoCD's health assessment framework, checking custom health checks defined in argocd-cm ConfigMap, Lua-based health scripts, and standard resource health indicators (Deployment rollout status, StatefulSet ready replicas, Job completion).
Sync failure diagnosis includes permission analysis (RBAC errors for the ArgoCD application controller service account), namespace validation, CRD dependency checking, and resource quota evaluation. The troubleshooter generates step-by-step remediation runbooks tailored to each specific failure type with kubectl commands ready for execution.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-troubleshooter/)

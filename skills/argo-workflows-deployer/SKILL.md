---
name: "Argo Workflows Deployer"
description: "Orchestrates deployment pipelines using the Argo Workflows Engine API and Argo CD ApplicationSet controller. Implements progressive delivery with Argo Rollouts canary and blue-green strategies."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argo-workflows-deployer/"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
---

# Argo Workflows Deployer

The Argo Workflows Deployer skill creates sophisticated deployment pipelines using the Argo ecosystem on Kubernetes. It leverages the Argo Workflows Engine API to define DAG-based and step-based workflow templates with conditional execution, retry policies, and resource-aware scheduling. The skill integrates with Argo CD ApplicationSet controller to generate Application resources dynamically from Git repositories, pull request generators, and cluster generators for multi-cluster deployments. Progressive delivery is implemented through Argo Rollouts, configuring canary deployments with automated analysis using Prometheus metrics, blue-green strategies with traffic shifting via Istio or AWS ALB, and experiment-based validation. The skill manages Argo Events sensors and event sources for GitOps-driven automation, connecting repository changes to deployment workflows. It supports artifact repositories backed by S3, GCS, or MinIO, workflow-level memoization for expensive steps, and integration with Vault for secrets management during deployments.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-deployer/)

---
title: "Argo Workflows Deployer"
description: "Orchestrates deployment pipelines using the Argo Workflows Engine API and Argo CD ApplicationSet controller. Implements progressive delivery with Argo Rollouts canary and blue-green strategies."
verification: "security_reviewed"
source: "https://github.com/argoproj/argo-workflows"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "argoproj/argo-workflows"
  github_stars: 16616
---

# Argo Workflows Deployer

The Argo Workflows Deployer skill creates sophisticated deployment pipelines using the Argo ecosystem on Kubernetes. It leverages the Argo Workflows Engine API to define DAG-based and step-based workflow templates with conditional execution, retry policies, and resource-aware scheduling. The skill integrates with Argo CD ApplicationSet controller to generate Application resources dynamically from Git repositories, pull request generators, and cluster generators for multi-cluster deployments. Progressive delivery is implemented through Argo Rollouts, configuring canary deployments with automated analysis using Prometheus metrics, blue-green strategies with traffic shifting via Istio or AWS ALB, and experiment-based validation. The skill manages Argo Events sensors and event sources for GitOps-driven automation, connecting repository changes to deployment workflows. It supports artifact repositories backed by S3, GCS, or MinIO, workflow-level memoization for expensive steps, and integration with Vault for secrets management during deployments.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/argo-workflows-deployer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argo-workflows-deployer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/argo-workflows-deployer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-deployer/)

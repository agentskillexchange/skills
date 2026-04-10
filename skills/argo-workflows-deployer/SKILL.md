---
title: "Argo Workflows Deployer"
description: "Orchestrates deployment pipelines using the Argo Workflows Engine API and Argo CD ApplicationSet controller. Implements progressive delivery with Argo Rollouts canary and blue-green strategies."
slug: "argo-workflows-deployer"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/argo-workflows-deployer/"
listed: true
---

# Argo Workflows Deployer

Orchestrates deployment pipelines using the Argo Workflows Engine API and Argo CD ApplicationSet controller. Implements progressive delivery with Argo Rollouts canary and blue-green strategies.

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
clawhub install argo-workflows-deployer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Argo Workflows Deployer skill creates sophisticated deployment pipelines using the Argo ecosystem on Kubernetes. It leverages the Argo Workflows Engine API to define DAG-based and step-based workflow templates with conditional execution, retry policies, and resource-aware scheduling. The skill integrates with Argo CD ApplicationSet controller to generate Application resources dynamically from Git repositories, pull request generators, and cluster generators for multi-cluster deployments. Progressive delivery is implemented through Argo Rollouts, configuring canary deployments with automated analysis using Prometheus metrics, blue-green strategies with traffic shifting via Istio or AWS ALB, and experiment-based validation. The skill manages Argo Events sensors and event sources for GitOps-driven automation, connecting repository changes to deployment workflows. It supports artifact repositories backed by S3, GCS, or MinIO, workflow-level memoization for expensive steps, and integration with Vault for secrets management during deployments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-deployer/)

---
name: "Argo Workflows Deployer"
description: "Orchestrates deployment pipelines using the Argo Workflows Engine API and Argo CD ApplicationSet controller. Implements progressive delivery with Argo Rollouts canary and blue-green strategies."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argo-workflows-deployer/"
tool_ecosystem:
  tool: kubernetes
  github_stars: 121334
  github_repo: kubernetes/kubernetes
  license: Apache-2.0
  maintained: true
---
# Argo Workflows Deployer

Orchestrates deployment pipelines using the Argo Workflows Engine API and Argo CD ApplicationSet controller. Implements progressive delivery with Argo Rollouts canary and blue-green strategies.

## Overview

The Argo Workflows Deployer skill creates sophisticated deployment pipelines using the Argo ecosystem on Kubernetes. It leverages the Argo Workflows Engine API to define DAG-based and step-based workflow templates with conditional execution, retry policies, and resource-aware scheduling. The skill integrates with Argo CD ApplicationSet controller to generate Application resources dynamically from Git repositories, pull request generators, and cluster generators for multi-cluster deployments. Progressive delivery is implemented through Argo Rollouts, configuring canary deployments with automated analysis using Prometheus metrics, blue-green strategies with traffic shifting via Istio or AWS ALB, and experiment-based validation. The skill manages Argo Events sensors and event sources for GitOps-driven automation, connecting repository changes to deployment workflows. It supports artifact repositories backed by S3, GCS, or MinIO, workflow-level memoization for expensive steps, and integration with Vault for secrets management during deployments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argo-workflows-deployer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argo-workflows-deployer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argo-workflows-deployer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argo-workflows-deployer -a codex
```

### OpenClaw

```bash
clawhub install argo-workflows-deployer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-deployer/)

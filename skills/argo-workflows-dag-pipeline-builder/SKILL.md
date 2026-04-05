---
name: "Argo Workflows DAG Pipeline Builder"
description: "Constructs Kubernetes-native workflow DAGs using Argo Workflows CRDs with configurable retry strategies, artifact passing via S3/MinIO, and template composition through WorkflowTemplates and ClusterWorkflowTemplates."
category: "Templates & Workflows"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/argoproj/argo-workflows"
tool_ecosystem:
  tool: kubernetes
  github_repo: argoproj/argo-workflows
  github_stars: 16596
---
# Argo Workflows DAG Pipeline Builder

Constructs Kubernetes-native workflow DAGs using Argo Workflows CRDs with configurable retry strategies, artifact passing via S3/MinIO, and template composition through WorkflowTemplates and ClusterWorkflowTemplates.

## Overview

The Argo Workflows DAG Pipeline Builder creates sophisticated Kubernetes-native CI/CD and data processing pipelines using Argo Workflows custom resource definitions. It constructs directed acyclic graph workflows where each step runs as a Kubernetes pod with precisely defined resource requests, node affinity rules, and tolerations. Artifact passing between workflow steps is configured through S3-compatible storage including AWS S3, MinIO, and Google Cloud Storage, with automatic compression and lifecycle management policies. The builder leverages WorkflowTemplates and ClusterWorkflowTemplates for reusable step definitions that can be shared across teams and namespaces. Retry strategies are configurable per step with exponential backoff, maximum duration limits, and conditional retry expressions based on exit codes or output parameters. The skill handles workflow-of-workflows patterns for complex orchestration scenarios, parameter passing between parent and child workflows, and event-driven triggers via Argo Events sensors. Resource cleanup policies ensure completed workflow pods are garbage collected according to configurable TTL strategies, preventing cluster resource exhaustion in high-throughput environments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argo-workflows-dag-pipeline-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argo-workflows-dag-pipeline-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argo-workflows-dag-pipeline-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argo-workflows-dag-pipeline-builder -a codex
```

### OpenClaw

```bash
clawhub install argo-workflows-dag-pipeline-builder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-dag-pipeline-builder/)

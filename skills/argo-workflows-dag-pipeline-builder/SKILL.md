---
name: "Argo Workflows DAG Pipeline Builder"
slug: "argo-workflows-dag-pipeline-builder"
description: "Constructs Kubernetes-native workflow DAGs using Argo Workflows CRDs with configurable retry strategies, artifact passing via S3/MinIO, and template composition through WorkflowTemplates and ClusterWorkflowTemplates."
github_stars: 16600
verification: "security_reviewed"
source: "https://github.com/argoproj/argo-workflows"
author: "argoproj"
category: "Templates & Workflows"
framework: "MCP"
tool_ecosystem:
  github_repo: "argoproj/argo-workflows"
  github_stars: 16600
---

# Argo Workflows DAG Pipeline Builder

Constructs Kubernetes-native workflow DAGs using Argo Workflows CRDs with configurable retry strategies, artifact passing via S3/MinIO, and template composition through WorkflowTemplates and ClusterWorkflowTemplates.

## Installation

Requirements and caveats from upstream:
- Including for Python users through [the Hera Python SDK for Argo Workflows](https://hera.readthedocs.io/en/stable/).
- Check out our [Java, Golang, Python (Hera), and Typescript (Juno) clients](docs/client-libraries.md).
- Scheduling (affinity/tolerations/node selectors)

Basic usage or getting-started notes:
- Easily run compute intensive jobs for machine learning or data processing in a fraction of the time using Argo Workflows on Kubernetes.
- Cloud agnostic and can run on any Kubernetes cluster.
- [Get started here](https://argo-workflows.readthedocs.io/en/latest/quick-start/)

- Source: https://github.com/argoproj/argo-workflows
- Extracted from upstream docs: https://raw.githubusercontent.com/argoproj/argo-workflows/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-dag-pipeline-builder/)

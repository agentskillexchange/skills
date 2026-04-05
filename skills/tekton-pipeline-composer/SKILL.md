---
name: "Tekton Pipeline Composer"
description: "Builds Tekton CI/CD pipelines on Kubernetes using the Tekton Pipelines API and tkn CLI. Composes Tasks, PipelineRuns, and TriggerBindings with proper workspace and result propagation between steps."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/tekton-pipeline-composer/"
---
# Tekton Pipeline Composer

Builds Tekton CI/CD pipelines on Kubernetes using the Tekton Pipelines API and tkn CLI. Composes Tasks, PipelineRuns, and TriggerBindings with proper workspace and result propagation between steps.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-composer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-composer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-composer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-composer -a codex
```

### OpenClaw

```bash
clawhub install tekton-pipeline-composer
```

## Details

The Tekton Pipeline Composer skill creates and manages cloud-native CI/CD pipelines using the Tekton Pipelines framework on Kubernetes. It generates Task, Pipeline, PipelineRun, and TriggerTemplate custom resource definitions that follow Tekton best practices for workspace sharing and result propagation.

This skill uses the tkn CLI and Kubernetes API to inspect cluster state, list available ClusterTasks, and validate resource definitions before applying them. It understands Tekton workspace types (emptyDir, PVC, ConfigMap, Secret) and ensures proper volume binding across pipeline tasks.

Key features include automatic generation of TriggerBindings and TriggerTemplates for webhook-driven pipelines, EventListener configuration with CEL interceptors for branch filtering, and proper parameterization of pipeline definitions for reuse across environments.

The skill handles complex scenarios like fan-out/fan-in patterns using Tekton’s when expressions, matrix parameters for parallel test execution, and custom task result propagation using $(tasks.taskname.results.resultname) syntax. It also integrates with Tekton Chains for supply chain security attestation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-composer/)

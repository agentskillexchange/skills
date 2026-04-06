---
name: "Tekton Pipeline Task Generator"
description: "Generates Tekton CI/CD pipeline tasks and PipelineRun manifests using the Tekton Pipelines API. Integrates with Tekton Hub for reusable task catalog lookups and automated resource binding."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/tekton-pipeline-task-generator/"
---
# Tekton Pipeline Task Generator

Generates Tekton CI/CD pipeline tasks and PipelineRun manifests using the Tekton Pipelines API. Integrates with Tekton Hub for reusable task catalog lookups and automated resource binding.

The Tekton Pipeline Task Generator skill creates Kubernetes-native CI/CD pipeline definitions using the Tekton Pipelines CRD API. It generates Task, Pipeline, and PipelineRun manifests with proper workspace bindings, parameter passing, and result propagation between steps. The skill queries the Tekton Hub API to discover and incorporate community tasks like git-clone, buildah, and kaniko for container builds. It configures PersistentVolumeClaim workspaces for artifact sharing, sets up Tekton Triggers with EventListener and TriggerTemplate resources for webhook-driven execution, and implements finally tasks for cleanup and notification. The generator handles step ordering with runAfter dependencies, configures resource requests and limits per step container, and validates pipeline DAG structure to prevent circular dependencies. Output includes complete YAML manifests ready for kubectl apply with proper RBAC ServiceAccount bindings.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-task-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-task-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-task-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-task-generator -a codex
```

### OpenClaw

```bash
clawhub install tekton-pipeline-task-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-task-generator/)

---
name: "Tekton Pipeline Scaffolder"
description: "Scaffolds Kubernetes-native CI/CD pipelines using Tekton Pipelines CRDs (Tasks, Pipelines, PipelineRuns) and the Tekton Hub API. Generates YAML manifests with proper workspace bindings, result passing, and when expressions."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/tekton-pipeline-scaffolder/"
---
# Tekton Pipeline Scaffolder

Scaffolds Kubernetes-native CI/CD pipelines using Tekton Pipelines CRDs (Tasks, Pipelines, PipelineRuns) and the Tekton Hub API. Generates YAML manifests with proper workspace bindings, result passing, and when expressions.

The Tekton Pipeline Scaffolder skill generates Kubernetes-native CI/CD pipeline definitions using the Tekton Pipelines API (tekton.dev/v1). It creates properly structured Task, Pipeline, PipelineRun, and TriggerTemplate custom resources.

The skill queries the Tekton Hub API (hub.tekton.dev/v1/resource) to find and incorporate community tasks like git-clone, buildah, kubernetes-actions, and kaniko. It generates custom Tasks with proper step containers, workspace declarations, param definitions, and result outputs.

Pipeline definitions include proper task ordering via runAfter, when expressions for conditional execution, workspace bindings with PersistentVolumeClaim or emptyDir backing, and result references between tasks using $(tasks.taskname.results.resultname) syntax.

The skill also generates EventListener and TriggerBinding resources for GitHub/GitLab webhook integration, proper RBAC ServiceAccount configurations, and Tekton Dashboard annotations for visualization. It supports both v1 and v1beta1 API versions and generates resource limit specifications appropriate for the workload type.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-scaffolder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-scaffolder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-scaffolder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-scaffolder -a codex
```

### OpenClaw

```bash
clawhub install tekton-pipeline-scaffolder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-scaffolder/)

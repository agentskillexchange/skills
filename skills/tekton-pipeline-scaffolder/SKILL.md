---
title: "Tekton Pipeline Scaffolder"
description: "Scaffolds Kubernetes-native CI/CD pipelines using Tekton Pipelines CRDs (Tasks, Pipelines, PipelineRuns) and the Tekton Hub API. Generates YAML manifests with proper workspace bindings, result passing, and when expressions."
verification: security_reviewed
source: "https://github.com/tektoncd/pipeline"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "tektoncd/pipeline"
  github_stars: 8936
---

# Tekton Pipeline Scaffolder

The Tekton Pipeline Scaffolder skill generates Kubernetes-native CI/CD pipeline definitions using the Tekton Pipelines API (tekton.dev/v1). It creates properly structured Task, Pipeline, PipelineRun, and TriggerTemplate custom resources.

The skill queries the Tekton Hub API (hub.tekton.dev/v1/resource) to find and incorporate community tasks like git-clone, buildah, kubernetes-actions, and kaniko. It generates custom Tasks with proper step containers, workspace declarations, param definitions, and result outputs.

Pipeline definitions include proper task ordering via runAfter, when expressions for conditional execution, workspace bindings with PersistentVolumeClaim or emptyDir backing, and result references between tasks using $(tasks.taskname.results.resultname) syntax.

The skill also generates EventListener and TriggerBinding resources for GitHub/GitLab webhook integration, proper RBAC ServiceAccount configurations, and Tekton Dashboard annotations for visualization. It supports both v1 and v1beta1 API versions and generates resource limit specifications appropriate for the workload type.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/tekton-pipeline-scaffolder
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/tekton-pipeline-scaffolder` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-scaffolder/)

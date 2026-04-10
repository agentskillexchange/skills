---
title: "Tekton Pipeline Scaffolder"
description: "Scaffolds Kubernetes-native CI/CD pipelines using Tekton Pipelines CRDs (Tasks, Pipelines, PipelineRuns) and the Tekton Hub API. Generates YAML manifests with proper workspace bindings, result passing, and when expressions."
slug: "tekton-pipeline-scaffolder"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/tekton-pipeline-scaffolder/"
listed: true
---

# Tekton Pipeline Scaffolder

Scaffolds Kubernetes-native CI/CD pipelines using Tekton Pipelines CRDs (Tasks, Pipelines, PipelineRuns) and the Tekton Hub API. Generates YAML manifests with proper workspace bindings, result passing, and when expressions.

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
clawhub install tekton-pipeline-scaffolder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Tekton Pipeline Scaffolder skill generates Kubernetes-native CI/CD pipeline definitions using the Tekton Pipelines API (tekton.dev/v1). It creates properly structured Task, Pipeline, PipelineRun, and TriggerTemplate custom resources.
The skill queries the Tekton Hub API (hub.tekton.dev/v1/resource) to find and incorporate community tasks like git-clone, buildah, kubernetes-actions, and kaniko. It generates custom Tasks with proper step containers, workspace declarations, param definitions, and result outputs.
Pipeline definitions include proper task ordering via runAfter, when expressions for conditional execution, workspace bindings with PersistentVolumeClaim or emptyDir backing, and result references between tasks using $(tasks.taskname.results.resultname) syntax.
The skill also generates EventListener and TriggerBinding resources for GitHub/GitLab webhook integration, proper RBAC ServiceAccount configurations, and Tekton Dashboard annotations for visualization. It supports both v1 and v1beta1 API versions and generates resource limit specifications appropriate for the workload type.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-scaffolder/)

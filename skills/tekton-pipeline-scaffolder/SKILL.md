---
title: Tekton Pipeline Scaffolder
description: The Tekton Pipeline Scaffolder skill generates Kubernetes-native CI/CD
  pipeline definitions using the Tekton Pipelines API (tekton.dev/v1). It creates
  properly structured Task, Pipeline, PipelineRun, and TriggerTemplate custom resources.
  The skill queries the Tekton Hub API (hub.tekton.dev/v1/resource) to find and incorporate
  community tasks like git-clone, buildah, kubernetes-actions, and kaniko. It generates
  custom Tasks with proper step containers, workspace declarations, param definitions,
  and result outputs. Pipeline definitions include proper task ordering via runAfter,
  when expressions for conditional execution, workspace bindings with PersistentVolumeClaim
  or emptyDir backing, and result references between tasks using $(tasks.taskname.results.resultname)
  syntax. The skill also generates EventListener and TriggerBinding resources for
  GitHub/GitLab webhook integration, proper RBAC ServiceAccount configurations, and
  Tekton Dashboard annotations for visualization. It supports both v1 and v1beta1
  API versions and generates resource limit specifications appropriate for the workload
  type.
verification: security_reviewed
source: https://agentskillexchange.com/skills/tekton-pipeline-scaffolder/
category:
- CI/CD Integrations
framework:
- Gemini
---

# Tekton Pipeline Scaffolder

The Tekton Pipeline Scaffolder skill generates Kubernetes-native CI/CD pipeline definitions using the Tekton Pipelines API (tekton.dev/v1). It creates properly structured Task, Pipeline, PipelineRun, and TriggerTemplate custom resources. The skill queries the Tekton Hub API (hub.tekton.dev/v1/resource) to find and incorporate community tasks like git-clone, buildah, kubernetes-actions, and kaniko. It generates custom Tasks with proper step containers, workspace declarations, param definitions, and result outputs. Pipeline definitions include proper task ordering via runAfter, when expressions for conditional execution, workspace bindings with PersistentVolumeClaim or emptyDir backing, and result references between tasks using $(tasks.taskname.results.resultname) syntax. The skill also generates EventListener and TriggerBinding resources for GitHub/GitLab webhook integration, proper RBAC ServiceAccount configurations, and Tekton Dashboard annotations for visualization. It supports both v1 and v1beta1 API versions and generates resource limit specifications appropriate for the workload type.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-scaffolder/)

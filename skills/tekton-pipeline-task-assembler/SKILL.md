---
name: "Tekton Pipeline Task Assembler"
description: "Assembles Tekton CI/CD pipelines from reusable Task and ClusterTask definitions using tkn CLI and Tekton Hub catalog. Manages PipelineRun parameters, workspace bindings, and result propagation across task steps."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/tektoncd/pipeline"
tool_ecosystem:
  tool: tekton
  github_repo: tektoncd/pipeline
  github_stars: 8924
  license: Apache-2.0
  maintained: true
---
# Tekton Pipeline Task Assembler

Assembles Tekton CI/CD pipelines from reusable Task and ClusterTask definitions using tkn CLI and Tekton Hub catalog. Manages PipelineRun parameters, workspace bindings, and result propagation across task steps.

## Overview

The Tekton Pipeline Task Assembler builds cloud-native CI/CD pipelines using Tekton on Kubernetes. It assembles Pipeline resources from reusable Task and ClusterTask definitions, sourcing community tasks from Tekton Hub catalog and combining them with custom tasks for organization-specific workflows. The tkn CLI integration provides pipeline execution, log streaming, and resource management capabilities. The assembler handles PipelineRun parameter propagation, mapping pipeline-level parameters to individual task parameters with type checking and default value resolution. Workspace bindings connect PersistentVolumeClaims, ConfigMaps, and Secrets to task steps, enabling data sharing across pipeline stages. Result propagation chains task outputs to downstream task inputs using the $(tasks.taskname.results.resultname) syntax with validation of result availability. The tool generates TriggerTemplate and TriggerBinding resources for event-driven pipeline execution from GitHub webhooks, GitLab push events, and container registry notifications. Pipeline-as-code with Tekton Chains provides supply chain security through automated artifact signing and attestation generation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-task-assembler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-task-assembler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-task-assembler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-task-assembler -a codex
```

### OpenClaw

```bash
clawhub install tekton-pipeline-task-assembler
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-task-assembler/)

---
name: "Tekton Pipeline Task Assembler"
description: "Assembles Tekton CI/CD pipelines from reusable Task and ClusterTask definitions using tkn CLI and Tekton Hub catalog. Manages PipelineRun parameters, workspace bindings, and result propagation across task steps."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/tekton-pipeline-task-assembler/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "tekton"  # from ase_tool_match
  github_stars: 8920  # from ase_github_stars (integer, not string)
  github_repo: "tektoncd/pipeline"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/tekton-pipeline-task-assembler/

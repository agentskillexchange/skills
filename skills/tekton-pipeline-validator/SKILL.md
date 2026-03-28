---
name: "Tekton Pipeline Validator"
description: "Validates Tekton Pipeline YAML manifests against the Tekton Pipelines API schema. Uses tkn CLI and Kubernetes admission webhooks to catch misconfigurations before deployment. Supports PipelineRun, TaskRun, and Trigger resource types."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/tektoncd/pipeline"
tool_ecosystem:
  tool: tekton
  github_stars: 8923
  github_repo: tektoncd/pipeline
  license: Apache-2.0
  maintained: true
---

# Tekton Pipeline Validator

Validates Tekton Pipeline YAML manifests against the Tekton Pipelines API schema. Uses tkn CLI and Kubernetes admission webhooks to catch misconfigurations before deployment. Supports PipelineRun, TaskRun, and Trigger resource types.

## Overview

The Tekton Pipeline Validator skill provides comprehensive validation for Tekton CI/CD pipeline definitions before they reach your Kubernetes cluster. It leverages the tkn CLI tool and the Tekton Pipelines admission webhook API to perform deep structural validation on PipelineRun, TaskRun, TriggerTemplate, and TriggerBinding resources.

The skill parses YAML manifests and checks them against the Tekton Pipelines v1 API schema, catching common errors like missing workspace bindings, invalid parameter references, and incompatible step image specifications. It integrates with the Kubernetes ValidatingAdmissionWebhook to simulate real cluster admission checks.

Key features include recursive directory scanning for multi-file pipelines, cross-resource reference validation (ensuring Tasks referenced by Pipelines actually exist), and detailed error reporting with line numbers. The validator supports both Tekton Pipelines v1beta1 and v1 API versions, automatically detecting the schema version from resource apiVersion fields.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-validator -a codex
```

### OpenClaw

```bash
clawhub install tekton-pipeline-validator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/tekton-pipeline-validator/

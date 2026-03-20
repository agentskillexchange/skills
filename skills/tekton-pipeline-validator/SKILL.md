---
name: Tekton Pipeline Validator
description: Validates Tekton Pipeline YAML manifests against the Tekton Pipelines API schema. Uses tkn CLI and Kubernetes admission webhooks to catch misconfigurations before deployment. Supports PipelineRun, Tas
category: CI/CD Integrations
framework: OpenClaw
verification: security_reviewed
rating: 4.9
reviews: 34
source: https://agentskillexchange.com/skill/tekton-pipeline-validator/
---

# Tekton Pipeline Validator

Validates Tekton Pipeline YAML manifests against the Tekton Pipelines API schema. Uses tkn CLI and Kubernetes admission webhooks to catch misconfigurations before deployment. Supports PipelineRun, TaskRun, and Trigger resource types.

## Overview

The Tekton Pipeline Validator skill provides comprehensive validation for Tekton CI/CD pipeline definitions before they reach your Kubernetes cluster. It leverages the tkn CLI tool and the Tekton Pipelines admission webhook API to perform deep structural validation on PipelineRun, TaskRun, TriggerTemplate, and TriggerBinding resources.
The skill parses YAML manifests and checks them against the Tekton Pipelines v1 API schema, catching common errors like missing workspace bindings, invalid parameter references, and incompatible step image specifications. It integrates with the Kubernetes ValidatingAdmissionWebhook to simulate real cluster admission checks.
Key features include recursive directory scanning for multi-file pipelines, cross-resource reference validation (ensuring Tasks referenced by Pipelines actually exist), and detailed error reporting with line numbers. The validator supports both Tekton Pipelines v1beta1 and v1 API versions, automatically detecting the schema version from resource apiVersion fields.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-validator
```

### OpenClaw

```bash
openclaw install tekton-pipeline-validator
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (34 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/tekton-pipeline-validator/)*

---
name: SageMaker Pipeline Orchestrator
description: Builds and triggers Amazon SageMaker Pipelines using boto3 sagemaker.workflow. Registers model artifacts to SageMaker Model Registry and invokes approval workflows via UpdateModelPackage API. Pulls tr
category: Integrations & Connectors
framework: MCP
verification: verified_metadata
rating: 4.9
reviews: 44
source: https://agentskillexchange.com/skill/sagemaker-pipeline-orchestrator/
---

# SageMaker Pipeline Orchestrator

Builds and triggers Amazon SageMaker Pipelines using boto3 sagemaker.workflow. Registers model artifacts to SageMaker Model Registry and invokes approval workflows via UpdateModelPackage API. Pulls training job metrics from CloudWatch Logs Insights for post-run analysis.

## Overview

Builds and triggers Amazon SageMaker Pipelines using boto3 sagemaker.workflow. Registers model artifacts to SageMaker Model Registry and invokes approval workflows via UpdateModelPackage API. Pulls training job metrics from CloudWatch Logs Insights for post-run analysis.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill sagemaker-pipeline-orchestrator
```

### OpenClaw

```bash
openclaw install sagemaker-pipeline-orchestrator
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Integrations & Connectors |
| Framework | MCP |
| Verification | Verified Metadata |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (44 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/sagemaker-pipeline-orchestrator/)*

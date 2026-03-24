---
name: "SageMaker Pipeline Orchestrator"
description: "Builds and triggers Amazon SageMaker Pipelines using boto3 sagemaker.workflow. Registers model artifacts to SageMaker Model Registry and invokes approval workflows via UpdateModelPackage API. Pulls training job metrics from CloudWatch Logs Insights for post-run analysis."
category: "Integrations & Connectors"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sagemaker-pipeline-orchestrator/"
---

# SageMaker Pipeline Orchestrator

Builds and triggers Amazon SageMaker Pipelines using boto3 sagemaker.workflow. Registers model artifacts to SageMaker Model Registry and invokes approval workflows via UpdateModelPackage API. Pulls training job metrics from CloudWatch Logs Insights for post-run analysis.

## Overview

Builds and triggers Amazon SageMaker Pipelines using boto3 sagemaker.workflow. Registers model artifacts to SageMaker Model Registry and invokes approval workflows via UpdateModelPackage API. Pulls training job metrics from CloudWatch Logs Insights for post-run analysis.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sagemaker-pipeline-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sagemaker-pipeline-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sagemaker-pipeline-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sagemaker-pipeline-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install sagemaker-pipeline-orchestrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sagemaker-pipeline-orchestrator/

---
name: MLflow to W&B Migration Assistant
description: Reads existing MLflow experiment runs via mlflow.search_runs() and bulk-imports them into Weights & Biases using wandb.init(). Maps MLflow artifact URIs to W&B Artifact objects, preserving metadata and lineage with original timestamps.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: verified_metadata
rating: 4.3
reviews: 35
source: https://agentskillexchange.com/skill/mlflow-to-wandb-migration/
---

# MLflow to W&B Migration Assistant

Reads existing MLflow experiment runs via mlflow.search_runs() and bulk-imports them into Weights & Biases using wandb.init(). Maps MLflow artifact URIs to W&B Artifact objects, preserving metadata and lineage with original timestamps.

## Overview

Reads existing MLflow experiment runs via mlflow.search_runs() and bulk-imports them into Weights & Biases using wandb.init(). Maps MLflow artifact URIs to W&B Artifact objects, preserving metadata and lineage with original timestamps.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill mlflow-to-wandb-migration
```

### OpenClaw

```bash
clawhub install mlflow-to-wandb-migration
```

### Claude Code

```bash
claude mcp add mlflow-to-wandb-migration
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/mlflow-to-wandb-migration/) for detailed installation instructions.

## Verification

- **Status**: verified_metadata
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.3/5 (35 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/mlflow-to-wandb-migration/)

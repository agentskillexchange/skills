---
name: "MLflow to W&B Migration Assistant"
description: "Reads existing MLflow experiment runs via mlflow.search_runs() and bulk-imports them into Weights & Biases using wandb.init(). Maps MLflow artifact URIs to W&B Artifact objects, preserving metadata and lineage with original timestamps."
category: "Runbooks & Diagnostics"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/mlflow-to-wandb-migration/"
---

# MLflow to W&B Migration Assistant

Reads existing MLflow experiment runs via mlflow.search_runs() and bulk-imports them into Weights & Biases using wandb.init(). Maps MLflow artifact URIs to W&B Artifact objects, preserving metadata and lineage with original timestamps.

## Overview

Reads existing MLflow experiment runs via mlflow.search_runs() and bulk-imports them into Weights & Biases using wandb.init(). Maps MLflow artifact URIs to W&B Artifact objects, preserving metadata and lineage with original timestamps.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mlflow-to-wandb-migration
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mlflow-to-wandb-migration -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mlflow-to-wandb-migration -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mlflow-to-wandb-migration -a codex
```

### OpenClaw

```bash
clawhub install mlflow-to-wandb-migration
```

## Source

- Marketplace: https://agentskillexchange.com/skills/mlflow-to-wandb-migration/

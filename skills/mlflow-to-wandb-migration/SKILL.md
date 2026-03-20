---
name: "MLflow to W&B Migration Assistant"
description: "Reads existing MLflow experiment runs via mlflow.search_runs() and bulk-imports them into Weights & Biases using wandb.init(). Maps MLflow artifact URIs to W&B Artifact objects, preserving metadata and lineage with original timestamps."
category: "Runbooks & Diagnostics"
framework: "Custom Agents"
verification: verified_metadata
rating: 4.3
reviews: 35
creator: Zara Ahmed
creator_handle: zaraahmed
creator_verified: true
source: https://agentskillexchange.com/skill/mlflow-to-wandb-migration/
---

# MLflow to W&B Migration Assistant

Reads existing MLflow experiment runs via mlflow.search_runs() and bulk-imports them into Weights & Biases using wandb.init(). Maps MLflow artifact URIs to W&B Artifact objects, preserving metadata and lineage with original timestamps.

## Installation

### Any agent (npx skills)

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

### OpenClaw

```bash
clawhub install mlflow-to-wandb-migration
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mlflow-to-wandb-migration -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Custom Agents |
| Verification | Verified Metadata |
| Rating | 4.3/5 (35 reviews) |

## Creator

**Zara Ahmed** (Verified Creator ✓)
- Profile: [@zaraahmed](https://agentskillexchange.com/browse-skills/?creator=zaraahmed)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/mlflow-to-wandb-migration/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)

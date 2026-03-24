---
name: "MLflow to W&B Migration Assistant"
description: "Reads existing MLflow experiment runs via mlflow.search_runs() and bulk-imports them into Weights & Biases using wandb.init(). Maps MLflow artifact URIs to W&B Artifact objects, preserving metadata and lineage with original timestamps."
category: "Runbooks & Diagnostics"
framework: "Custom Agents"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/mlflow-to-wandb-migration/"
---

# MLflow to W&B Migration Assistant

Reads existing MLflow experiment runs via mlflow.search_runs() and bulk-imports them into Weights & Biases using wandb.init(). Maps MLflow artifact URIs to W&B Artifact objects, preserving metadata and lineage with original timestamps.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Custom Agents |
| **Verification** | 📋 Listed |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/mlflow-to-wandb-migration/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*

---
name: "Weights & Biases Run Monitor"
description: "Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wandb-run-monitor/"
tool_ecosystem:
  tool: "slack"
  github_stars: 2900
  npm_weekly_downloads: 2433529
  github_repo: "slackapi/bolt-js"
  license: "MIT"
  maintained: true
---

# Weights & Biases Run Monitor

Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill wandb-run-monitor
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill wandb-run-monitor -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill wandb-run-monitor -a cursor
```

### OpenClaw
```bash
clawhub install wandb-run-monitor
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill wandb-run-monitor -a codex
```

## Details

| | |
|---|---|
| **Category** | Data Extraction & Transformation |
| **Framework** | Claude Code |
| **Verification** | 📋 Listed |
| **Tool** | [slack](https://github.com/slackapi/bolt-js) — ⭐ 2.9k · MIT |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/wandb-run-monitor/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*

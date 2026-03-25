---
name: "Weights & Biases Run Monitor"
description: "Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wandb-run-monitor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "slack"  # from ase_tool_match
  github_stars: 2900  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2433529  # from ase_npm_downloads
  github_repo: "slackapi/bolt-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Weights & Biases Run Monitor

Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking.

## Overview

Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking.

## Installation

### Any Agent

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

### Codex

```bash
npx skills add agentskillexchange/skills --skill wandb-run-monitor -a codex
```

### OpenClaw

```bash
clawhub install wandb-run-monitor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wandb-run-monitor/

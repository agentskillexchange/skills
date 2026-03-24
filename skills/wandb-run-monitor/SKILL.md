---
name: "Weights & Biases Run Monitor"
description: "Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: security_reviewed
rating: 4.5
reviews: 33
creator: "Priya Sharma"
creator_handle: "@priyasharma"
creator_verified: true
source: "https://agentskillexchange.com/skills/wandb-run-monitor/"
---
# Weights & Biases Run Monitor

Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | Data Extraction & Transformation |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | 4.5/5 (33 reviews) |

## Creator

**Priya Sharma** (Verified Creator ✓)
- Profile: [@priyasharma](https://agentskillexchange.com/browse-skills/?creator=priyasharma)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/wandb-run-monitor/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)

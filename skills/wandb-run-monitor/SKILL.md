---
name: Weights & Biases Run Monitor
description: Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking.
category: Data Extraction &amp; Transformation
framework: Any Agent
verification: security_reviewed
rating: 4.5
reviews: 33
source: https://agentskillexchange.com/skill/wandb-run-monitor/
---

# Weights & Biases Run Monitor

Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking.

## Overview

Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill wandb-run-monitor
```

### OpenClaw

```bash
clawhub install wandb-run-monitor
```

### Claude Code

```bash
claude mcp add wandb-run-monitor
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/wandb-run-monitor/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Data Extraction &amp; Transformation
- **Framework**: Any Agent
- **Rating**: 4.5/5 (33 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/wandb-run-monitor/)

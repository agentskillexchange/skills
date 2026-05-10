---
title: "Weights & Biases Run Monitor"
slug: "wandb-run-monitor"
description: "Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking."
verification: "security_reviewed"
source: "https://docs.wandb.ai/"
author: "Weights & Biases"
category: "Data Extraction & Transformation"
framework: "Claude Code"
---

# Weights & Biases Run Monitor

Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking.

## Prerequisites

Python, Weights & Biases SDK, Slack

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install wandb
```

## Documentation

- https://docs.wandb.ai/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wandb-run-monitor/)

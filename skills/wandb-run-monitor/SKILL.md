---
title: "Weights & Biases Run Monitor"
description: "Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/wandb-run-monitor/"
---

# Weights & Biases Run Monitor

Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wandb-run-monitor/)

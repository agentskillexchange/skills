---
title: "Weights & Biases Run Monitor"
slug: "wandb-run-monitor"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
source: "https://agentskillexchange.com/skills/wandb-run-monitor/"
---

# Weights & Biases Run Monitor

Uses the W&B Python SDK and Public API to stream live training metrics, system stats, and gradients from active runs. Alerts on metric regressions by querying run history via wandb.Api().runs() and posts summaries to Slack. Supports artifact versioning and lineage tracking.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wandb-run-monitor/)

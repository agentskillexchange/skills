---
name: "Run bounded metric-improvement experiments with MiMoCode"
slug: "run-bounded-metric-improvement-experiments-mimocode"
description: "Run MiMoCode’s opt-in experiment workflow against a fixed evaluation budget, then review kept changes, measured deltas and an independent audit."
github_stars: 13780
verification: "security_reviewed"
source: "https://github.com/XiaomiMiMo/MiMo-Code"
author: "XiaomiMiMo"
publisher_type: "organization"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "XiaomiMiMo/MiMo-Code"
  github_stars: 13780
---

# Run bounded metric-improvement experiments with MiMoCode

Run MiMoCode’s opt-in experiment workflow against a fixed evaluation budget, then review kept changes, measured deltas and an independent audit.

## Prerequisites

MiMoCode workflow runtime; configured provider; Git; disposable repository checkout; fixed-budget evaluator and explicit editable scope

## Installation

Install or set up from the source-backed instructions:

Use a reviewed build containing commit 676c654d7cd6fe83e064365b1461d567ab3c0102. For source setup inspect upstream requirements, check out that commit, use the repository-declared Bun 1.3.14 toolchain, install dependencies and launch the documented bun run dev entry with MIMOCODE_EXPERIMENTAL_WORKFLOW_TOOL=true. Configure an authorized provider and confirm workflow is offered. Supply the documented research-experiment args and use a disposable checkout. Installation and execution were not tested.

- Source: https://github.com/XiaomiMiMo/MiMo-Code

## Documentation

- https://github.com/XiaomiMiMo/MiMo-Code/blob/676c654d7cd6fe83e064365b1461d567ab3c0102/packages/cli/src/workflow/builtin/research-experiment.js

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-bounded-metric-improvement-experiments-mimocode/)

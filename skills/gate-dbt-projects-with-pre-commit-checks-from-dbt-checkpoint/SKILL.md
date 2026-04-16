---
title: "Gate dbt projects with pre-commit checks from dbt-checkpoint"
description: "Use dbt-checkpoint when an agent should catch dbt naming, dependency, metadata, and model-hygiene issues before review or merge."
verification: "listed"
source: "https://github.com/dbt-checkpoint/dbt-checkpoint"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dbt-checkpoint/dbt-checkpoint"
  github_stars: 738
---

# Gate dbt projects with pre-commit checks from dbt-checkpoint

dbt-checkpoint gives an agent a bounded repository guardrail workflow: run dbt-specific pre-commit checks, surface failures, and keep bad project hygiene from sliding into main. Invoke it when the real task is dbt project quality gating, not when you merely need the dbt runtime to execute models. The scope boundary is narrow and publishable: dbt-focused static and pre-commit checks, not a generic pre-commit framework card or a broad dbt product listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-dbt-projects-with-pre-commit-checks-from-dbt-checkpoint/)

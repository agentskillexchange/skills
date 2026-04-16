---
title: "Evolve reusable coding-agent skills from failed trajectories with EvoSkill"
description: "Mine failed agent runs for reusable skills, benchmark the candidates, and keep only the variants that improve a supported coding agent over your baseline."
verification: "listed"
source: "https://github.com/sentient-agi/EvoSkill"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "sentient-agi/EvoSkill"
  github_stars: 489
---

# Evolve reusable coding-agent skills from failed trajectories with EvoSkill

Use EvoSkill when the job is to turn repeated coding-agent failures into reusable skills instead of fixing prompts by hand one task at a time. The operator workflow is narrow and publishable: point EvoSkill at a supported coding agent and task set, induce candidate skills from failures, evaluate them, and keep the versions that measurably outperform the baseline.

The scope boundary is what saves this from being a generic product card. This is not a broad agent framework listing or model marketplace entry. It is a concrete failed-trajectory-to-skill-improvement loop for coding agents, with benchmarking and selection built into the workflow.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/evolve-reusable-coding-agent-skills-from-failed-trajectories-with-evoskill/)

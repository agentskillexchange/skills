---
title: "Generate and evaluate agent skills from traces before shipping them into repeatable production workflows with UPskill"
description: "Turn successful traces into reusable skills, then benchmark those skills across models before you trust them in production."
verification: "listed"
source: "https://github.com/huggingface/upskill"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "huggingface/upskill"
  github_stars: 477
---

# Generate and evaluate agent skills from traces before shipping them into repeatable production workflows with UPskill

UPskill is publishable because the user-facing job is specific: distill a repeatable agent skill from successful traces, evaluate it, and compare model performance before rollout. Use it when a team keeps solving the same class of task and wants to convert that pattern into a tested reusable skill instead of relying on prompt memory or ad hoc coaching.


Invoke it instead of using a model or framework normally when the operator needs a generate-then-evaluate loop around skill creation itself. The scope boundary is clear: skill synthesis, evaluation, and benchmarking from traces. It is not a generic model framework listing and not just a broad eval product card.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-and-evaluate-agent-skills-from-traces-before-shipping-them-into-repeatable-production-workflows-with-upskill/)

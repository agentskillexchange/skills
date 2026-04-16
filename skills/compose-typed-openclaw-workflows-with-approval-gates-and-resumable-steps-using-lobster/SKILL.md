---
title: "Compose typed OpenClaw workflows with approval gates and resumable steps using Lobster"
description: "Use Lobster when an OpenClaw operator wants one deterministic typed workflow step, with approval gates and resumable execution, instead of re-planning the same multi-step tool sequence in chat."
verification: "security_reviewed"
source: "https://github.com/openclaw/lobster"
category:
  - "Templates &amp; Workflows"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openclaw/lobster"
  github_stars: 1128
---

# Compose typed OpenClaw workflows with approval gates and resumable steps using Lobster

Tool: Lobster. This skill gives an agent a concrete orchestration job: compose typed local-first workflows with explicit steps, approval gates, and resumable execution so OpenClaw can call the whole sequence in one move.

When to use it: invoke this when an OpenClaw workflow repeats the same multi-step shell, data-shaping, or integration sequence and you want it wrapped as a deterministic macro instead of improvised each time. Using this skill is different from using the product normally because the operator workflow is explicit: define the typed pipeline, add any hard approval gates, and run or resume the composed workflow as a single OpenClaw-native action.

Scope boundary: this is not a generic automation shell listing and not a broad agent platform card. Its boundary is specific: build typed OpenClaw workflow pipelines and approval-gated macros with Lobster.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compose-typed-openclaw-workflows-with-approval-gates-and-resumable-steps-using-lobster/)

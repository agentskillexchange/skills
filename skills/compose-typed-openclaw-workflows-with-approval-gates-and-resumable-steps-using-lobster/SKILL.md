---
title: "Compose typed OpenClaw workflows with approval gates and resumable steps using Lobster"
description: "Tool: Lobster. This skill gives an agent a concrete orchestration job: compose typed local-first workflows with explicit steps, approval gates, and resumable execution so OpenClaw can call the whole sequence in one move.\nWhen to use it: invoke this when an OpenClaw workflow repeats the same multi-step shell, data-shaping, or integration sequence and you want it wrapped as a deterministic macro instead of improvised each time. Using this skill is different from using the product normally because the operator workflow is explicit: define the typed pipeline, add any hard approval gates, and run or resume the composed workflow as a single OpenClaw-native action.\nScope boundary: this is not a generic automation shell listing and not a broad agent platform card. Its boundary is specific: build typed OpenClaw workflow pipelines and approval-gated macros with Lobster."
verification: security_reviewed
source: "https://github.com/openclaw/lobster"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/compose-typed-openclaw-workflows-with-approval-gates-and-resumable-steps-using-lobster
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/compose-typed-openclaw-workflows-with-approval-gates-and-resumable-steps-using-lobster` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compose-typed-openclaw-workflows-with-approval-gates-and-resumable-steps-using-lobster/)

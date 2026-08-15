---
name: "Run long-horizon computer-use agent loops with LongHorizon-Harness"
slug: "run-long-horizon-computer-use-agent-loops-with-longhorizon-harness"
description: "Use LongHorizon-Harness to keep Claude Code, Codex, DeepSeek Harness, or custom agent backends working through long GUI and CLI tasks with verified state, role separation, checkpoints, and recovery loops."
github_stars: 714
verification: "security_reviewed"
source: "https://github.com/AMAP-ML/LongHorizon-Harness"
author: "AMAP-ML"
publisher_type: "organization"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "AMAP-ML/LongHorizon-Harness"
  github_stars: 714
---

# Run long-horizon computer-use agent loops with LongHorizon-Harness

Use LongHorizon-Harness to keep Claude Code, Codex, DeepSeek Harness, or custom agent backends working through long GUI and CLI tasks with verified state, role separation, checkpoints, and recovery loops.

## Prerequisites

Python >= 3.10; uv or pip; one agent runtime on PATH such as codex, claude, or dsh; Node.js 20+ for computer-use plugins when GUI tasks are needed

## Installation

Install or set up from the source-backed instructions:

uv tool install lh-harness # or: pip install lh-harness cd /path/to/your/project lh-harness init lh-harness web --workspace-root . # or: lh-harness run --task "Inspect the current directory and summarize its files." --agent codex

- Source: https://github.com/AMAP-ML/LongHorizon-Harness

## Documentation

- https://lh-harness.pages.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-long-horizon-computer-use-agent-loops-with-longhorizon-harness/)

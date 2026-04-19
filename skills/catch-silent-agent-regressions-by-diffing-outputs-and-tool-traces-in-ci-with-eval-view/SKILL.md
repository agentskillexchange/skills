---
title: "Catch silent agent regressions by diffing outputs and tool traces in CI with eval-view"
description: "Use eval-view when the job is regression-gating an existing agent workflow in CI, not when a user just wants a general observability product or benchmark library. The workflow is bounded: capture a baseline, rerun the same agent scenarios, diff outputs and tool traces, then classify whether the change is safe, flaky, or a release blocker. That scope boundary, behavior-regression review for multi-turn tool-calling agents, gives it a clear skill shape instead of leaving it as a generic eval toolkit listing."
source: "https://github.com/hidai25/eval-view"
verification: "listed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "hidai25/eval-view"
  github_stars: 84
---

# Catch silent agent regressions by diffing outputs and tool traces in CI with eval-view

Use eval-view when the job is regression-gating an existing agent workflow in CI, not when a user just wants a general observability product or benchmark library. The workflow is bounded: capture a baseline, rerun the same agent scenarios, diff outputs and tool traces, then classify whether the change is safe, flaky, or a release blocker. That scope boundary, behavior-regression review for multi-turn tool-calling agents, gives it a clear skill shape instead of leaving it as a generic eval toolkit listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/catch-silent-agent-regressions-by-diffing-outputs-and-tool-traces-in-ci-with-eval-view/)

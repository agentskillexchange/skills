---
title: "Catch silent agent regressions by diffing outputs and tool traces in CI with eval-view"
description: "Snapshot agent behavior, compare outputs and tool-call paths, and block releases when a model or prompt change quietly shifts behavior."
verification: "listed"
source: "https://github.com/hidai25/eval-view"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "hidai25/eval-view"
  github_stars: 84
---

# Catch silent agent regressions by diffing outputs and tool traces in CI with eval-view

Use eval-view when the job is regression-gating an existing agent workflow in CI, not when a user just wants a general observability product or benchmark library. The workflow is bounded: capture a baseline, rerun the same agent scenarios, diff outputs and tool traces, then classify whether the change is safe, flaky, or a release blocker. That scope boundary, behavior-regression review for multi-turn tool-calling agents, gives it a clear skill shape instead of leaving it as a generic eval toolkit listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/catch-silent-agent-regressions-by-diffing-outputs-and-tool-traces-in-ci-with-eval-view/)

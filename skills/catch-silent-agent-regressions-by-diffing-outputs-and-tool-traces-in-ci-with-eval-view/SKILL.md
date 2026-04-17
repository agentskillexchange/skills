---
title: "Catch silent agent regressions by diffing outputs and tool traces in CI with eval-view"
description: "Use eval-view when the job is regression-gating an existing agent workflow in CI, not when a user just wants a general observability product or benchmark library. The workflow is bounded: capture a baseline, rerun the same agent scenarios, diff outputs and tool traces, then classify whether the change is safe, flaky, or a release blocker. That scope boundary, behavior-regression review for multi-turn tool-calling agents, gives it a clear skill shape instead of leaving it as a generic eval toolkit listing."
verification: listed
source: "https://github.com/hidai25/eval-view"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "hidai25/eval-view"
  github_stars: 84
---

# Catch silent agent regressions by diffing outputs and tool traces in CI with eval-view

Use eval-view when the job is regression-gating an existing agent workflow in CI, not when a user just wants a general observability product or benchmark library. The workflow is bounded: capture a baseline, rerun the same agent scenarios, diff outputs and tool traces, then classify whether the change is safe, flaky, or a release blocker. That scope boundary, behavior-regression review for multi-turn tool-calling agents, gives it a clear skill shape instead of leaving it as a generic eval toolkit listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/catch-silent-agent-regressions-by-diffing-outputs-and-tool-traces-in-ci-with-eval-view
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/catch-silent-agent-regressions-by-diffing-outputs-and-tool-traces-in-ci-with-eval-view` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/catch-silent-agent-regressions-by-diffing-outputs-and-tool-traces-in-ci-with-eval-view/)

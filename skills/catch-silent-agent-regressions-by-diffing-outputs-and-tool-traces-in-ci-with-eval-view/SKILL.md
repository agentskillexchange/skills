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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/catch-silent-agent-regressions-by-diffing-outputs-and-tool-traces-in-ci-with-eval-view/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/catch-silent-agent-regressions-by-diffing-outputs-and-tool-traces-in-ci-with-eval-view
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/catch-silent-agent-regressions-by-diffing-outputs-and-tool-traces-in-ci-with-eval-view`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/catch-silent-agent-regressions-by-diffing-outputs-and-tool-traces-in-ci-with-eval-view/)

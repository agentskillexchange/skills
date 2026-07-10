---
title: "Catch silent agent regressions by diffing outputs and tool traces in CI with eval-view"
description: "Snapshot agent behavior, compare outputs and tool-call paths, and block releases when a model or prompt change quietly shifts behavior."
verification: "security_reviewed"
source: "https://github.com/hidai25/eval-view"
author: "hidai25"
publisher_type: "individual"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "hidai25/eval-view"
  github_stars: 84
---

# Catch silent agent regressions by diffing outputs and tool traces in CI with eval-view

Snapshot agent behavior, compare outputs and tool-call paths, and block releases when a model or prompt change quietly shifts behavior.

## Prerequisites

Python environment, eval-view installation, repeatable agent scenarios or tests, CI runner or local shell, supported agent stack under test

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install eval-view from the upstream Python package instructions, define baseline and comparison scenarios for the target agent flow, then run its documented check and replay commands locally or in CI.
```

## Documentation

- https://github.com/hidai25/eval-view

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/catch-silent-agent-regressions-by-diffing-outputs-and-tool-traces-in-ci-with-eval-view/)

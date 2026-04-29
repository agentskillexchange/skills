---
title: "Capture and replay Claude Code trajectories for multi-session debugging with Agent Lens"
description: "Record structured Claude Code trajectories, shadow git diffs, and replay branches when agent behavior needs forensic debugging instead of ad hoc transcript review."
verification: "security_reviewed"
source: "https://github.com/dreadnode/agent-lens"
author: "Dreadnode"
publisher_type: "organization"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "dreadnode/agent-lens"
  github_stars: 102
---

# Capture and replay Claude Code trajectories for multi-session debugging with Agent Lens

Record structured Claude Code trajectories, shadow git diffs, and replay branches when agent behavior needs forensic debugging instead of ad hoc transcript review.

## Prerequisites

Python 3.12+, uv, Agent Lens, and Claude Code access through a subscription or API key compatible with the Claude Agent SDK

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone the repository, run `uv sync`, then use `harness run <config.yaml>` to execute a trajectory and `harness inspect <run>` or the local UI to review and replay results.
```

## Documentation

- https://dreadnode.github.io/agent-lens/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-and-replay-claude-code-trajectories-for-multi-session-debugging-with-agent-lens/)

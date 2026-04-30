---
title: "Orchestrate parallel coding agents with autonomous CI and review handoff using Agent Orchestrator"
description: "Start one supervisor for a repository, fan work out across isolated worktrees, and route CI failures or review comments back to the right agent automatically."
verification: "listed"
source: "https://github.com/ComposioHQ/agent-orchestrator"
author: "Composio"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "ComposioHQ/agent-orchestrator"
  github_stars: 6270
---

# Orchestrate parallel coding agents with autonomous CI and review handoff using Agent Orchestrator

Start one supervisor for a repository, fan work out across isolated worktrees, and route CI failures or review comments back to the right agent automatically.

## Prerequisites

Node.js 20+, Git 2.25+, tmux, GitHub CLI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the CLI with `npm install -g @aoagents/ao`, then run `ao start <repo>` from a local repository or GitHub URL and adjust `agent-orchestrator.yaml` if you need custom runtimes, agents, or reaction rules.
```

## Documentation

- https://github.com/ComposioHQ/agent-orchestrator

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/orchestrate-parallel-coding-agents-with-autonomous-ci-and-review-handoff-using-agent-orchestrator/)

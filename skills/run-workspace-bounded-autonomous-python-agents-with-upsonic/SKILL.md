---
title: "Run workspace-bounded autonomous Python agents with Upsonic"
description: "Build and run Python agents that execute tasks against an explicit workspace, with tools, MCP connections, and prebuilt agent packages available when needed."
verification: "security_reviewed"
source: "https://github.com/Upsonic/Upsonic"
author: "Upsonic"
publisher_type: "organization"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "Upsonic/Upsonic"
  github_stars: 7880
---

# Run workspace-bounded autonomous Python agents with Upsonic

Build and run Python agents that execute tasks against an explicit workspace, with tools, MCP connections, and prebuilt agent packages available when needed.

## Prerequisites

Python, uv or pip, model provider credentials, optional MCP-compatible tools

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `uv pip install upsonic` or `pip install upsonic`, create an `AutonomousAgent` with a model and workspace path, then pass a `Task` to `agent.print_do()` for a bounded run.
```

## Documentation

- https://docs.upsonic.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-workspace-bounded-autonomous-python-agents-with-upsonic/)

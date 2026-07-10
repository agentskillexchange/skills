---
title: "Give coding agents sandboxed shell runtimes with SWE-ReX"
description: "Use SWE-ReX when a coding agent needs a consistent runtime interface for local, containerized, or remote shell sessions with command output, exit codes, interactive tools, and parallel execution."
verification: "security_reviewed"
source: "https://github.com/SWE-agent/SWE-ReX"
author: "SWE-agent"
publisher_type: "open_source"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "SWE-agent/SWE-ReX"
  github_stars: 543
---

# Give coding agents sandboxed shell runtimes with SWE-ReX

Use SWE-ReX when a coding agent needs a consistent runtime interface for local, containerized, or remote shell sessions with command output, exit codes, interactive tools, and parallel execution.

## Prerequisites

Python, swe-rex, optional Modal or Fargate backend, local or remote shell environment

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with pip install swe-rex. Add optional extras only when needed, such as pip install 'swe-rex[modal]', pip install 'swe-rex[fargate]', or pip install 'swe-rex[dev]' for development. Configure the selected runtime backend before giving agents access to shell sessions.
```

## Documentation

- https://swe-rex.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-coding-agents-sandboxed-shell-runtimes-with-swe-rex/)

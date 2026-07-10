---
title: "Run coding agents in a locked-down local sandbox with repo-only filesystem access and controlled egress using agent-sandbox"
description: "Put Claude Code, Codex, Gemini, or other supported agent CLIs inside a persistent local sandbox instead of letting them operate directly on the host."
verification: "security_reviewed"
source: "https://github.com/mattolson/agent-sandbox"
author: "mattolson"
publisher_type: "individual"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mattolson/agent-sandbox"
  github_stars: 163
---

# Run coding agents in a locked-down local sandbox with repo-only filesystem access and controlled egress using agent-sandbox

Put Claude Code, Codex, Gemini, or other supported agent CLIs inside a persistent local sandbox instead of letting them operate directly on the host.

## Prerequisites

Docker-compatible runtime, VM layer such as Colima, terminal or supported devcontainer IDE

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the `agentbox` binary from the project releases, run `agentbox init` to generate the sandbox config, then enter the environment with `agentbox exec` or attach through the generated devcontainer setup.
```

## Documentation

- https://github.com/mattolson/agent-sandbox#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-coding-agents-in-a-locked-down-local-sandbox-with-repo-only-filesystem-access-and-controlled-egress-using-agent-sandbox/)

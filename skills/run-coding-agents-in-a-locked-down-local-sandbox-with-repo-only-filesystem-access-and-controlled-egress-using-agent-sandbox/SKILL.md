---
title: "Run coding agents in a locked-down local sandbox with repo-only filesystem access and controlled egress using agent-sandbox"
description: "Put Claude Code, Codex, Gemini, or other supported agent CLIs inside a persistent local sandbox instead of letting them operate directly on the host."
verification: "listed"
source: "https://github.com/mattolson/agent-sandbox"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mattolson/agent-sandbox"
  github_stars: 163
---

# Run coding agents in a locked-down local sandbox with repo-only filesystem access and controlled egress using agent-sandbox

Use agent-sandbox when you want local coding agents to keep their auth and state, but still confine them to a repository-scoped filesystem and a policy-controlled egress path. The workflow is concrete: initialize the sandbox, generate the compose and policy files, then enter the containerized agent environment through the CLI or devcontainer path. The scope boundary is tighter than a generic dev environment product because the point is specifically safe local agent execution with bounded filesystem and network policy.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-coding-agents-in-a-locked-down-local-sandbox-with-repo-only-filesystem-access-and-controlled-egress-using-agent-sandbox/)

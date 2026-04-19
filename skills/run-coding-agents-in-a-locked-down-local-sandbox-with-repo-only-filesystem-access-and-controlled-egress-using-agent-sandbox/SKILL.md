---
title: "Run coding agents in a locked-down local sandbox with repo-only filesystem access and controlled egress using agent-sandbox"
description: "Use agent-sandbox when you want local coding agents to keep their auth and state, but still confine them to a repository-scoped filesystem and a policy-controlled egress path. The workflow is concrete: initialize the sandbox, generate the compose and policy files, then enter the containerized agent environment through the CLI or devcontainer path. The scope boundary is tighter than a generic dev environment product because the point is specifically safe local agent execution with bounded filesystem and network policy."
source: "https://github.com/mattolson/agent-sandbox"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mattolson/agent-sandbox"
  github_stars: 163
---

# Run coding agents in a locked-down local sandbox with repo-only filesystem access and controlled egress using agent-sandbox

Use agent-sandbox when you want local coding agents to keep their auth and state, but still confine them to a repository-scoped filesystem and a policy-controlled egress path. The workflow is concrete: initialize the sandbox, generate the compose and policy files, then enter the containerized agent environment through the CLI or devcontainer path. The scope boundary is tighter than a generic dev environment product because the point is specifically safe local agent execution with bounded filesystem and network policy.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-coding-agents-in-a-locked-down-local-sandbox-with-repo-only-filesystem-access-and-controlled-egress-using-agent-sandbox/)

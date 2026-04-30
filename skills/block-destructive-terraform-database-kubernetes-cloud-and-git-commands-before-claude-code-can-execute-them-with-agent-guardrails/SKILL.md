---
title: "Block destructive Terraform, database, Kubernetes, cloud, and Git commands before Claude Code can execute them with Agent Guardrails"
description: "Add hard pre-execution guardrails to Claude Code so destructive shell commands are blocked before an agent can run them."
verification: "listed"
source: "https://github.com/roboticforce/agent-guardrails"
author: "Robotic Force"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "roboticforce/agent-guardrails"
  github_stars: 2
---

# Block destructive Terraform, database, Kubernetes, cloud, and Git commands before Claude Code can execute them with Agent Guardrails

Add hard pre-execution guardrails to Claude Code so destructive shell commands are blocked before an agent can run them.

## Prerequisites

Claude Code, jq, shell access to project or user Claude config, repository clone of the guardrail scripts

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone the repository, copy the `claude-code` settings, hooks, and scripts into either your project `.claude/` directory or `~/.claude/`, make the shell scripts executable, then dry-run one of the guard scripts to verify blocking behavior.
```

## Documentation

- https://github.com/roboticforce/agent-guardrails

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-destructive-terraform-database-kubernetes-cloud-and-git-commands-before-claude-code-can-execute-them-with-agent-guardrails/)

---
name: "Block destructive Terraform, database, Kubernetes, cloud, and Git commands before Claude Code can execute them with Agent Guardrails"
slug: "block-destructive-terraform-database-kubernetes-cloud-and-git-commands-before-claude-code-can-execute-them-with-agent-guardrails"
description: "Add hard pre-execution guardrails to Claude Code so destructive shell commands are blocked before an agent can run them."
github_stars: 2
verification: "security_reviewed"
source: "https://github.com/roboticforce/agent-guardrails"
author: "Robotic Force"
publisher_type: "organization"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "roboticforce/agent-guardrails"
  github_stars: 2
---

# Block destructive Terraform, database, Kubernetes, cloud, and Git commands before Claude Code can execute them with Agent Guardrails

Add hard pre-execution guardrails to Claude Code so destructive shell commands are blocked before an agent can run them.

## Prerequisites

Claude Code, jq, shell access to project or user Claude config, repository clone of the guardrail scripts

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/roboticforce/agent-guardrails.git
- Make all .sh files executable.

Requirements and caveats from upstream:
- (if permissions require it)"}

Basic usage or getting-started notes:
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- [jq](https://jqlang.github.io/jq/download/) installed (used by guard scripts to parse tool input)
- Clone the repo:

- Source: https://github.com/roboticforce/agent-guardrails
- Extracted from upstream docs: https://raw.githubusercontent.com/roboticforce/agent-guardrails/HEAD/README.md

## Documentation

- https://github.com/roboticforce/agent-guardrails

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-destructive-terraform-database-kubernetes-cloud-and-git-commands-before-claude-code-can-execute-them-with-agent-guardrails/)

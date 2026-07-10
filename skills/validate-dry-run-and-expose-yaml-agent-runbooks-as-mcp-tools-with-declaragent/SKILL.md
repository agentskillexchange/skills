---
title: "Validate, dry-run, and expose YAML agent runbooks as MCP tools with DeclarAgent"
description: "Turn YAML runbooks into auditable agent actions with validation, dry-runs, destructive-step approval, and optional MCP exposure."
verification: "security_reviewed"
source: "https://github.com/shiehn/DeclarAgent"
author: "shiehn"
publisher_type: "individual"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "shiehn/DeclarAgent"
  github_stars: 11
---

# Validate, dry-run, and expose YAML agent runbooks as MCP tools with DeclarAgent

Turn YAML runbooks into auditable agent actions with validation, dry-runs, destructive-step approval, and optional MCP exposure.

## Prerequisites

Go, YAML runbooks, MCP-compatible client for MCP mode

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `go install github.com/shiehn/declaragent@latest`, validate plans with `declaragent validate plan.yaml`, and use `declaragent mcp --plans ./plans` when you want those runbooks exposed as MCP tools.
```

## Documentation

- https://github.com/shiehn/DeclarAgent

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-dry-run-and-expose-yaml-agent-runbooks-as-mcp-tools-with-declaragent/)

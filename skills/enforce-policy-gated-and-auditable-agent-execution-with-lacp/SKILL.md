---
title: "Enforce policy-gated and auditable agent execution with LACP"
description: "Run Claude, Codex, and related coding-agent tasks through policy gates, evidence loops, and auditable execution tiers before risky work proceeds."
verification: "listed"
source: "https://github.com/0xNyk/lacp"
author: "0xNyk"
publisher_type: "individual"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "0xNyk/lacp"
  github_stars: 211
---

# Enforce policy-gated and auditable agent execution with LACP

Run Claude, Codex, and related coding-agent tasks through policy gates, evidence loops, and auditable execution tiers before risky work proceeds.

## Prerequisites

Local development environment, supported agent runtime such as Claude or Codex, shell access, repository to govern, optional verification tooling

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install LACP from Homebrew or the upstream bootstrap path, run the documented bootstrap and doctor steps, configure the local policy profile, then route tasks through lacp run, posture, preflight, or worktree workflows as needed.
```

## Documentation

- https://github.com/0xNyk/lacp#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-policy-gated-and-auditable-agent-execution-with-lacp/)

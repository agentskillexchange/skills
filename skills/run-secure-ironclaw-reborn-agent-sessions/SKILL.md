---
title: "Run secure IronClaw Reborn agent sessions"
description: "Use IronClaw Reborn as a secure local agent runtime for model-routed CLI, REPL, and WebUI sessions with explicit state, policy, storage, and secret boundaries."
verification: "listed"
source: "https://github.com/nearai/ironclaw"
author: "NEAR AI / IronClaw contributors"
publisher_type: "open_source"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "nearai/ironclaw"
  github_stars: 12515
---

# Run secure IronClaw Reborn agent sessions

Use IronClaw Reborn as a secure local agent runtime for model-routed CLI, REPL, and WebUI sessions with explicit state, policy, storage, and secret boundaries.

## Prerequisites

Rust toolchain with Cargo, local checkout of nearai/ironclaw, configured LLM provider credentials, optional PostgreSQL storage and Node.js 22/pnpm for WebUI builds

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone https://github.com/nearai/ironclaw, build or run cargo run -q -p ironclaw_reborn_cli --bin ironclaw-reborn -- --help, set IRONCLAW_REBORN_HOME, configure a model with ironclaw-reborn models set-provider, then use ironclaw-reborn run, repl, doctor, or serve for agent sessions.
```

## Documentation

- https://www.ironclaw.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-secure-ironclaw-reborn-agent-sessions/)

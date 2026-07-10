---
title: "Give OpenCode project sessions persistent memory with opencode-mem"
description: "Add opencode-mem to OpenCode so coding sessions can store, search, and reuse project memories through a local SQLite and vector index."
verification: "security_reviewed"
source: "https://github.com/tickernelz/opencode-mem"
author: "tickernelz"
publisher_type: "individual"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "tickernelz/opencode-mem"
  github_stars: 1003
  npm_package: "opencode-mem"
  npm_weekly_downloads: 12093
---

# Give OpenCode project sessions persistent memory with opencode-mem

Add opencode-mem to OpenCode so coding sessions can store, search, and reuse project memories through a local SQLite and vector index.

## Prerequisites

OpenCode, opencode-mem plugin, Bun or standard OpenCode plugin runtime

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add opencode-mem to the plugin list in ~/.config/opencode/opencode.json, restart OpenCode so the plugin installs, then configure ~/.config/opencode/opencode-mem.jsonc for storage, embedding, and memory scope settings.
```

## Documentation

- https://github.com/tickernelz/opencode-mem

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-opencode-project-sessions-persistent-memory-with-opencode-mem/)

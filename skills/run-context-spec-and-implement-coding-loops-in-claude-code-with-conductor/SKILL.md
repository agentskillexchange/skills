---
title: "Run context → spec → implement coding loops in Claude Code with Conductor"
description: "Turn Claude Code into a structured project workflow that captures context, plans work, and executes implementation in reviewable tracks."
verification: "listed"
source: "https://github.com/wshobson/agents/tree/main/plugins/conductor"
author: "wshobson"
publisher_type: "individual"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
---

# Run context → spec → implement coding loops in Claude Code with Conductor

Turn Claude Code into a structured project workflow that captures context, plans work, and executes implementation in reviewable tracks.

## Prerequisites

Claude Code with plugin support, access to the wshobson/agents marketplace, a Git repository to manage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add the marketplace with /plugin marketplace add wshobson/agents if needed, then install the plugin with /plugin install conductor@claude-code-workflows and follow the documented /conductor:setup, /conductor:new-track, and /conductor:implement workflow.
```

## Documentation

- https://raw.githubusercontent.com/wshobson/agents/main/plugins/conductor/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-context-spec-and-implement-coding-loops-in-claude-code-with-conductor/)

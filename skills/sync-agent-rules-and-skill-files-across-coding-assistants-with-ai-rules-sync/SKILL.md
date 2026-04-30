---
title: "Sync agent rules and skill files across coding assistants with AI Rules Sync"
description: "Use AI Rules Sync when the same operating rules, commands, skills, or subagents need to stay aligned across Claude Code, Cursor, Codex, Copilot, and related tools instead of being copied and updated by hand."
verification: "security_reviewed"
source: "https://github.com/lbb00/ai-rules-sync"
author: "lbb00"
publisher_type: "individual"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "lbb00/ai-rules-sync"
  github_stars: 25
---

# Sync agent rules and skill files across coding assistants with AI Rules Sync

Use AI Rules Sync when the same operating rules, commands, skills, or subagents need to stay aligned across Claude Code, Cursor, Codex, Copilot, and related tools instead of being copied and updated by hand.

## Prerequisites

Git, AI Rules Sync, and at least two supported coding assistants or agent clients whose rule, command, skill, or agent directories need to stay synchronized.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install AI Rules Sync from the GitHub or npm distribution documented by the project, point it at the repositories or rule collections you want to use as sources, configure the supported assistants you want to target, then run the sync workflow so each tool receives the right files in its native layout.
```

## Documentation

- https://lbb00.github.io/ai-rules-sync/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sync-agent-rules-and-skill-files-across-coding-assistants-with-ai-rules-sync/)

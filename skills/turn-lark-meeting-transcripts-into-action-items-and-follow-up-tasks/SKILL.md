---
title: "Turn Lark meeting transcripts into action items and follow-up tasks"
description: "Read a Lark Minutes transcript, extract explicit and implied follow-ups, then let the agent execute selected tasks instead of leaving them as notes."
verification: "security_reviewed"
source: "https://github.com/zarazhangrui/lark-minutes-tasks"
author: "zarazhangrui"
publisher_type: "open_source_project"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "zarazhangrui/lark-minutes-tasks"
  github_stars: 40
---

# Turn Lark meeting transcripts into action items and follow-up tasks

Read a Lark Minutes transcript, extract explicit and implied follow-ups, then let the agent execute selected tasks instead of leaving them as notes.

## Prerequisites

Lark CLI, authenticated Lark account, Claude Code or another agent host that can load the command file

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Copy minutes.md into the agent command directory. For Claude Code: cp minutes.md ~/.claude/commands/minutes.md
```

## Documentation

- https://github.com/zarazhangrui/lark-minutes-tasks

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-lark-meeting-transcripts-into-action-items-and-follow-up-tasks/)

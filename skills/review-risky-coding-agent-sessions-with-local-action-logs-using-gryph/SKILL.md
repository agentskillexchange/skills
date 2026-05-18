---
name: "Review risky coding-agent sessions with local action logs using Gryph"
slug: "review-risky-coding-agent-sessions-with-local-action-logs-using-gryph"
description: "Capture and inspect file reads, writes, and shell activity from coding agents so developers can audit what actually happened after a session goes sideways."
github_stars: 105
verification: "security_reviewed"
source: "https://github.com/safedep/gryph"
author: "safedep"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "safedep/gryph"
  github_stars: 105
---

# Review risky coding-agent sessions with local action logs using Gryph

Capture and inspect file reads, writes, and shell activity from coding agents so developers can audit what actually happened after a session goes sideways.

## Prerequisites

Supported coding agent client, local SQLite storage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Gryph with the project install script, Homebrew, npm, or Go, then run `gryph install` to hook detected agents and use `gryph logs`, `gryph query`, or `gryph session <id>` to inspect captured activity.
```

## Documentation

- https://github.com/safedep/gryph

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-risky-coding-agent-sessions-with-local-action-logs-using-gryph/)

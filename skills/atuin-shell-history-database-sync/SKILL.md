---
title: "Atuin Shell History Database and Sync"
description: "Atuin replaces your existing shell history with a SQLite database that records additional context like exit codes, session IDs, working directories, and command durations. It provides encrypted cross-machine sync and a full-screen fuzzy search UI bound to Ctrl-R."
verification: "security_reviewed"
source: "https://github.com/atuinsh/atuin"
category: ["Developer Tools"]
framework: ["Claude Code"]
tool_ecosystem:
  github_repo: "atuinsh/atuin"
  github_stars: 28925
---

# Atuin Shell History Database and Sync

Atuin replaces your existing shell history with a SQLite database that records additional context like exit codes, session IDs, working directories, and command durations. It provides encrypted cross-machine sync and a full-screen fuzzy search UI bound to Ctrl-R.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/atuin-shell-history-database-sync/)

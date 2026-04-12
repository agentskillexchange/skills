---
title: "Atuin Shell History Database and Sync"
slug: "atuin-shell-history-database-sync"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
source: "https://github.com/atuinsh/atuin"
tool_ecosystem:
  github_repo: "atuinsh/atuin"
  github_stars: 28925
---

# Atuin Shell History Database and Sync

Atuin replaces your existing shell history with a SQLite database that records additional context like exit codes, session IDs, working directories, and command durations. It provides encrypted cross-machine sync and a full-screen fuzzy search UI bound to Ctrl-R.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/atuin-shell-history-database-sync/)

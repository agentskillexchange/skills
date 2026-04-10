---
title: "Atuin Shell History Database and Sync"
description: "Atuin replaces your existing shell history with a SQLite database that records additional context like exit codes, session IDs, working directories, and command durations. It provides encrypted cross-machine sync and a full-screen fuzzy search UI bound to Ctrl-R."
slug: "atuin-shell-history-database-sync"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/atuinsh/atuin"
tool_ecosystem:
  github_repo: "atuinsh/atuin"
  github_stars: 28925
---

# Atuin Shell History Database and Sync

Atuin replaces your existing shell history with a SQLite database that records additional context like exit codes, session IDs, working directories, and command durations. It provides encrypted cross-machine sync and a full-screen fuzzy search UI bound to Ctrl-R.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install atuin-shell-history-database-sync
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Atuin is a Rust-based shell history tool that stores every command you run in a local SQLite database along with metadata that standard shell history files discard. Each entry captures the command text, exit code, duration, working directory, hostname, and session identifier. This structured storage enables queries that traditional history files cannot support.
The primary interface is a full-screen TUI bound to Ctrl-R (configurable) that replaces the default reverse-search in bash, zsh, fish, nushell, and xonsh. The search supports fuzzy matching, prefix matching, and substring matching with filter modes that scope results to the current session, current directory, or the global history across all machines. Users press Alt plus a number key to quick-jump to recent items, and Tab to edit a command before executing it.
Atuin’s sync feature uses end-to-end encryption to replicate history across machines through an Atuin server. Users can run the hosted service or self-host using the open-source server component. The encryption ensures that the server operator — whether the Atuin team or the user themselves — cannot read command contents. The sync protocol merges histories from multiple machines into a unified timeline.
Advanced queries use the atuin search subcommand with flags for exit code filtering (–exit 0), time ranges (–after “yesterday 3pm”), and text patterns. The atuin stats command calculates usage statistics like most-run commands and total command counts. Import from existing history files is handled by atuin import auto, which detects and migrates from bash_history, zsh_history, fish_history, and other formats.
Atuin is distributed through its install script, Homebrew, cargo, pacman, and Nix. The project has an active community on Discord and a dedicated forum at forum.atuin.sh. It is licensed under MIT.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/atuin-shell-history-database-sync/)

---
title: "Atuin Shell History Database and Sync"
description: "Atuin is a Rust-based shell history tool that stores every command you run in a local SQLite database along with metadata that standard shell history files discard. Each entry captures the command text, exit code, duration, working directory, hostname, and session identifier. This structured storage enables queries that traditional history files cannot support. The primary interface is a full-screen TUI bound to Ctrl-R (configurable) that replaces the default reverse-search in bash, zsh, fish, nushell, and xonsh. The search supports fuzzy matching, prefix matching, and substring matching with filter modes that scope results to the current session, current directory, or the global history across all machines. Users press Alt plus a number key to quick-jump to recent items, and Tab to edit a command before executing it. Atuin&#8217;s sync feature uses end-to-end encryption to replicate history across machines through an Atuin server. Users can run the hosted service or self-host using the open-source server component. The encryption ensures that the server operator — whether the Atuin team or the user themselves — cannot read command contents. The sync protocol merges histories from multiple machines into a unified timeline. Advanced queries use the atuin search subcommand with flags for exit code filtering (&#8211;exit 0), time ranges (&#8211;after &#8220;yesterday 3pm&#8221;), and text patterns. The atuin stats command calculates usage statistics like most-run commands and total command counts. Import from existing history files is handled by atuin import auto, which detects and migrates from bash_history, zsh_history, fish_history, and other formats. Atuin is distributed through its install script, Homebrew, cargo, pacman, and Nix. The project has an active community on Discord and a dedicated forum at forum.atuin.sh. It is licensed under MIT."
source: "https://github.com/atuinsh/atuin"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "atuinsh/atuin"
  github_stars: 28925
---

# Atuin Shell History Database and Sync

Atuin is a Rust-based shell history tool that stores every command you run in a local SQLite database along with metadata that standard shell history files discard. Each entry captures the command text, exit code, duration, working directory, hostname, and session identifier. This structured storage enables queries that traditional history files cannot support. The primary interface is a full-screen TUI bound to Ctrl-R (configurable) that replaces the default reverse-search in bash, zsh, fish, nushell, and xonsh. The search supports fuzzy matching, prefix matching, and substring matching with filter modes that scope results to the current session, current directory, or the global history across all machines. Users press Alt plus a number key to quick-jump to recent items, and Tab to edit a command before executing it. Atuin&#8217;s sync feature uses end-to-end encryption to replicate history across machines through an Atuin server. Users can run the hosted service or self-host using the open-source server component. The encryption ensures that the server operator — whether the Atuin team or the user themselves — cannot read command contents. The sync protocol merges histories from multiple machines into a unified timeline. Advanced queries use the atuin search subcommand with flags for exit code filtering (&#8211;exit 0), time ranges (&#8211;after &#8220;yesterday 3pm&#8221;), and text patterns. The atuin stats command calculates usage statistics like most-run commands and total command counts. Import from existing history files is handled by atuin import auto, which detects and migrates from bash_history, zsh_history, fish_history, and other formats. Atuin is distributed through its install script, Homebrew, cargo, pacman, and Nix. The project has an active community on Discord and a dedicated forum at forum.atuin.sh. It is licensed under MIT.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/atuin-shell-history-database-sync/)

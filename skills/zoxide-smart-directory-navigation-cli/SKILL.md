---
name: "zoxide Smart Directory Navigation CLI"
description: "A smarter cd command written in Rust, inspired by z and autojump. zoxide learns your most-used directories and lets you jump to them with minimal keystrokes across all major shells."
category: "Developer Tools"
framework: "Claude Code"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/zoxide-smart-directory-navigation-cli/"
---
# zoxide Smart Directory Navigation CLI

A smarter cd command written in Rust, inspired by z and autojump. zoxide learns your most-used directories and lets you jump to them with minimal keystrokes across all major shells.

## Installation

### Claude Code
```bash
npx skills add https://agentskillexchange.com/skills/zoxide-smart-directory-navigation-cli/
```

### Cursor
```bash
npx skills add https://agentskillexchange.com/skills/zoxide-smart-directory-navigation-cli/ --cursor
```

### Codex
```bash
npx skills add https://agentskillexchange.com/skills/zoxide-smart-directory-navigation-cli/ --codex
```

### OpenClaw
```bash
clawhub install zoxide-smart-directory-navigation-cli
```

## Overview

zoxide is an intelligent directory navigation tool that replaces the standard cd command with a frecency-based ranking system. Written in Rust by Ajeet D’Souza, it has amassed over 34,000 GitHub stars and is packaged for virtually every major operating system and shell. The tool tracks which directories you visit most frequently and most recently, then uses that data to let you jump to any directory with just a partial name match.
For AI agents working across large codebases or multi-project environments, zoxide eliminates the friction of deep directory navigation. Instead of typing out full paths like cd ~/projects/company/backend/src/services, an agent can simply invoke z services and land in the right place. The tool supports interactive selection via fzf integration, tab completions in bash 4.4+, fish, and zsh, and works identically on Linux, macOS, Windows, and BSD systems.
The matching algorithm uses a combination of frequency and recency (frecency) to rank directories. Directories visited often rank higher, but recent visits are weighted more heavily so the tool adapts to changing workflows. The zi command provides interactive fuzzy selection when multiple matches exist, and z foo bar narrows results by matching multiple path components simultaneously.
Installation is straightforward across all platforms: a single curl install script for Linux, Homebrew on macOS, or cargo install from crates.io. zoxide integrates with bash, zsh, fish, PowerShell, Elvish, Nushell, and Xonsh. For agent-driven workflows that involve switching between project directories, navigating monorepo structures, or automating multi-step build processes across different locations, zoxide provides fast and predictable directory traversal without requiring absolute paths.

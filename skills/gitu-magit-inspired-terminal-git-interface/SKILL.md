---
title: "gitu Magit-Inspired Terminal Git Interface"
description: "gitu is a terminal user interface (TUI) for Git operations, built in Rust and directly inspired by Emacs Magit. It brings the powerful, keyboard-driven Git workflow that Magit users love to any terminal, without requiring Emacs. How It Works gitu presents your repository status in a clean terminal interface showing unstaged changes, staged changes, recent commits, and branch information. Users navigate and act using keyboard shortcuts that mirror Magit conventions. A which-key style help menu appears as you type, making commands discoverable without memorizing keybinds. The tool supports granular staging and unstaging at the file, hunk, or individual line level. You can commit, amend, and create fixup commits directly from the interface. Branch operations include checkout, creating new branches, and viewing logs for any branch. Rebasing supports interactive mode, autosquash, abort, and continue workflows. Key Features Staging and unstaging works at file, hunk, and line granularity. Commit operations include standard commit, amend, and fixup. Fetching, pulling, and pushing respect your configured upstream and pushDefault remotes. Interactive rebasing with autosquash support makes history cleanup straightforward. Stash operations cover save, pop, apply, and drop. Soft, mixed, and hard reset operations are available, along with commit reverting. Integration Points gitu respects the VISUAL, EDITOR, and GIT_EDITOR environment variables for opening files and commit messages in your preferred editor. Configuration lives in ~/.config/gitu/config.toml on Linux and macOS. The tool is available through most system package managers including Homebrew, pacman, apt, and cargo install. It works alongside any existing Git workflow and integrates with standard Git configuration. Output gitu renders an interactive terminal display showing repository status, diffs with syntax highlighting, commit logs, and operation results. All Git operations modify the actual repository just as command-line Git would."
source: "https://github.com/altsem/gitu"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "altsem/gitu"
  github_stars: 2664
---

# gitu Magit-Inspired Terminal Git Interface

gitu is a terminal user interface (TUI) for Git operations, built in Rust and directly inspired by Emacs Magit. It brings the powerful, keyboard-driven Git workflow that Magit users love to any terminal, without requiring Emacs. How It Works gitu presents your repository status in a clean terminal interface showing unstaged changes, staged changes, recent commits, and branch information. Users navigate and act using keyboard shortcuts that mirror Magit conventions. A which-key style help menu appears as you type, making commands discoverable without memorizing keybinds. The tool supports granular staging and unstaging at the file, hunk, or individual line level. You can commit, amend, and create fixup commits directly from the interface. Branch operations include checkout, creating new branches, and viewing logs for any branch. Rebasing supports interactive mode, autosquash, abort, and continue workflows. Key Features Staging and unstaging works at file, hunk, and line granularity. Commit operations include standard commit, amend, and fixup. Fetching, pulling, and pushing respect your configured upstream and pushDefault remotes. Interactive rebasing with autosquash support makes history cleanup straightforward. Stash operations cover save, pop, apply, and drop. Soft, mixed, and hard reset operations are available, along with commit reverting. Integration Points gitu respects the VISUAL, EDITOR, and GIT_EDITOR environment variables for opening files and commit messages in your preferred editor. Configuration lives in ~/.config/gitu/config.toml on Linux and macOS. The tool is available through most system package managers including Homebrew, pacman, apt, and cargo install. It works alongside any existing Git workflow and integrates with standard Git configuration. Output gitu renders an interactive terminal display showing repository status, diffs with syntax highlighting, commit logs, and operation results. All Git operations modify the actual repository just as command-line Git would.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitu-magit-inspired-terminal-git-interface/)

---
name: "gitu Magit-Inspired Terminal Git Interface"
description: "A fast terminal user interface for Git inspired by Emacs Magit, written in Rust. gitu provides keyboard-driven staging, committing, rebasing, stashing, and branch management with a discoverable which-key style help menu."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/altsem/gitu"
tool_ecosystem:
  github_repo: "altsem/gitu"
  github_stars: 2664
---
# gitu Magit-Inspired Terminal Git Interface

A fast terminal user interface for Git inspired by Emacs Magit, written in Rust. gitu provides keyboard-driven staging, committing, rebasing, stashing, and branch management with a discoverable which-key style help menu.

## Overview

gitu is a terminal user interface (TUI) for Git operations, built in Rust and directly inspired by Emacs Magit. It brings the powerful, keyboard-driven Git workflow that Magit users love to any terminal, without requiring Emacs.

How It Works

gitu presents your repository status in a clean terminal interface showing unstaged changes, staged changes, recent commits, and branch information. Users navigate and act using keyboard shortcuts that mirror Magit conventions. A which-key style help menu appears as you type, making commands discoverable without memorizing keybinds.

The tool supports granular staging and unstaging at the file, hunk, or individual line level. You can commit, amend, and create fixup commits directly from the interface. Branch operations include checkout, creating new branches, and viewing logs for any branch. Rebasing supports interactive mode, autosquash, abort, and continue workflows.

Key Features

Staging and unstaging works at file, hunk, and line granularity. Commit operations include standard commit, amend, and fixup. Fetching, pulling, and pushing respect your configured upstream and pushDefault remotes. Interactive rebasing with autosquash support makes history cleanup straightforward. Stash operations cover save, pop, apply, and drop. Soft, mixed, and hard reset operations are available, along with commit reverting.

Integration Points

gitu respects the VISUAL, EDITOR, and GIT_EDITOR environment variables for opening files and commit messages in your preferred editor. Configuration lives in ~/.config/gitu/config.toml on Linux and macOS. The tool is available through most system package managers including Homebrew, pacman, apt, and cargo install. It works alongside any existing Git workflow and integrates with standard Git configuration.

Output

gitu renders an interactive terminal display showing repository status, diffs with syntax highlighting, commit logs, and operation results. All Git operations modify the actual repository just as command-line Git would.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitu-magit-inspired-terminal-git-interface
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitu-magit-inspired-terminal-git-interface -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitu-magit-inspired-terminal-git-interface -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitu-magit-inspired-terminal-git-interface -a codex
```

### OpenClaw

```bash
clawhub install gitu-magit-inspired-terminal-git-interface
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitu-magit-inspired-terminal-git-interface/)

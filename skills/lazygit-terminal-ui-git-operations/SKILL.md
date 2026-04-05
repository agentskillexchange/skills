---
name: "lazygit Terminal UI for Git Operations"
description: "A simple terminal user interface for git commands built with Go. lazygit provides interactive staging, rebasing, conflict resolution, and branch management through an intuitive TUI that replaces arcane git command sequences with keyboard-driven workflows."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/jesseduffield/lazygit"
tool_ecosystem:
  tool: lazygit
  github_repo: jesseduffield/lazygit
  github_stars: 75400
---
# lazygit Terminal UI for Git Operations

A simple terminal user interface for git commands built with Go. lazygit provides interactive staging, rebasing, conflict resolution, and branch management through an intuitive TUI that replaces arcane git command sequences with keyboard-driven workflows.

## Overview

lazygit is a terminal-based user interface for git written in Go by Jesse Duffield. It wraps the full power of git behind a split-pane TUI that shows files, branches, commits, and stashes simultaneously, making complex git operations accessible without memorizing commands.

The skill leverages lazygit’s interactive staging panel where you can stage individual hunks or lines of code with a single keypress instead of editing patch files by hand. Interactive rebasing happens inside the UI — you reorder, squash, fixup, or drop commits by moving lines up and down, rather than editing a TODO file in a text editor. Merge conflicts display the conflicting sections side by side with one-key resolution choices.

Branch management covers creating, checking out, renaming, deleting, rebasing onto, and fast-forwarding branches. The commit panel supports conventional commit messages, amending, and signing. The stash panel lets you stash, pop, apply, and drop with visual feedback. Cherry-picking across branches is a matter of marking commits and applying them elsewhere.

lazygit integrates with custom commands and keybindings defined in a YAML configuration file, so agent workflows can extend its capabilities. It supports git worktrees, submodules, bisect operations, and reflog navigation. The tool outputs through a standard terminal, making it compatible with tmux, SSH sessions, and any environment that supports a terminal emulator.

Output includes real-time diff views, commit graphs, and status indicators. lazygit is distributed as a single binary with no dependencies beyond git itself. It is available via Homebrew, Scoop, pacman, apt, and direct GitHub releases for Linux, macOS, and Windows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill lazygit-terminal-ui-git-operations
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill lazygit-terminal-ui-git-operations -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill lazygit-terminal-ui-git-operations -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill lazygit-terminal-ui-git-operations -a codex
```

### OpenClaw

```bash
clawhub install lazygit-terminal-ui-git-operations
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lazygit-terminal-ui-git-operations/)

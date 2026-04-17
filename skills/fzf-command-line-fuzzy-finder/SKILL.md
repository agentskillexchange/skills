---
title: "fzf Command-Line Fuzzy Finder"
description: "fzf is an interactive Unix filter program created by Junegunn Choi and written in Go. Given any list piped to its stdin, fzf presents a full-screen or inline finder interface where the user types a query and sees matching results ranked by relevance in real time. The fuzzy matching algorithm handles character transpositions and omissions, making it fast to locate items without typing exact strings.\nShell integration is the primary use case. After running the install script, fzf binds Ctrl-R to fuzzy search through command history, Ctrl-T to find files and insert them at the cursor, and Alt-C to change directories. These bindings work in bash, zsh, and fish. The –preview flag displays file contents alongside the result list, commonly combined with bat for syntax-highlighted previews: fzf –preview “bat –color=always {}”.\nfzf supports several search syntaxes beyond simple fuzzy matching. Prefixing a term with a single quote (‘exact) requires an exact substring match. A caret (^prefix) anchors to the start, and a dollar sign (suffix$) anchors to the end. The exclamation mark (!term) inverts the match. Multiple terms are combined with spaces (AND) or pipes (OR). The –delimiter and –nth flags control which fields of each line participate in matching.\nThe –tmux flag (fzf 0.56+) renders the finder as a tmux popup instead of consuming the full terminal. The –height flag renders inline within the current terminal, preserving visible context. The –bind flag maps keys to actions like execute, reload, preview-scroll, and toggle-preview, enabling complex interactive workflows. Environment variables FZF_DEFAULT_COMMAND and FZF_DEFAULT_OPTS customize the default file source and options globally.\nfzf is distributed as a single static binary via Homebrew, apt, pacman, Chocolatey, and GitHub releases. It includes a Vim plugin (fzf.vim) and a Neovim integration (fzf-lua). The project is licensed under MIT and has extensive documentation in its README and wiki."
verification: security_reviewed
source: "https://github.com/junegunn/fzf"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "junegunn/fzf"
  github_stars: 79165
---

# fzf Command-Line Fuzzy Finder

fzf is an interactive Unix filter program created by Junegunn Choi and written in Go. Given any list piped to its stdin, fzf presents a full-screen or inline finder interface where the user types a query and sees matching results ranked by relevance in real time. The fuzzy matching algorithm handles character transpositions and omissions, making it fast to locate items without typing exact strings.
Shell integration is the primary use case. After running the install script, fzf binds Ctrl-R to fuzzy search through command history, Ctrl-T to find files and insert them at the cursor, and Alt-C to change directories. These bindings work in bash, zsh, and fish. The –preview flag displays file contents alongside the result list, commonly combined with bat for syntax-highlighted previews: fzf –preview “bat –color=always {}”.
fzf supports several search syntaxes beyond simple fuzzy matching. Prefixing a term with a single quote (‘exact) requires an exact substring match. A caret (^prefix) anchors to the start, and a dollar sign (suffix$) anchors to the end. The exclamation mark (!term) inverts the match. Multiple terms are combined with spaces (AND) or pipes (OR). The –delimiter and –nth flags control which fields of each line participate in matching.
The –tmux flag (fzf 0.56+) renders the finder as a tmux popup instead of consuming the full terminal. The –height flag renders inline within the current terminal, preserving visible context. The –bind flag maps keys to actions like execute, reload, preview-scroll, and toggle-preview, enabling complex interactive workflows. Environment variables FZF_DEFAULT_COMMAND and FZF_DEFAULT_OPTS customize the default file source and options globally.
fzf is distributed as a single static binary via Homebrew, apt, pacman, Chocolatey, and GitHub releases. It includes a Vim plugin (fzf.vim) and a Neovim integration (fzf-lua). The project is licensed under MIT and has extensive documentation in its README and wiki.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/fzf-command-line-fuzzy-finder
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/fzf-command-line-fuzzy-finder` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fzf-command-line-fuzzy-finder/)

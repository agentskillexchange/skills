---
name: "broot Interactive Tree-View File Navigator"
description: "broot is a Rust-based terminal tool that provides a new way to see and navigate directory trees. It offers fuzzy search, file preview, git status integration, and an interactive tree view that adapts to your terminal size."
category: "Uncategorized"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/Canop/broot"
---
# broot Interactive Tree-View File Navigator

broot is a Rust-based terminal tool that provides a new way to see and navigate directory trees. It offers fuzzy search, file preview, git status integration, and an interactive tree view that adapts to your terminal size.

## Overview

Overview
broot is an innovative terminal file manager and directory navigator written in Rust. Unlike traditional tools like tree or ls, broot provides an interactive, adaptive tree view that fits your terminal while letting you search, filter, and act on files without ever leaving the interface.

Key Features

Adaptive Tree View: broot intelligently adjusts how much of the directory tree it shows based on your terminal size, never overflowing the screen like tree does on large repos.
Fuzzy Search: Start typing to instantly filter and find files across the entire directory tree with fuzzy matching, similar to fzf but integrated into the tree context.
Git Integration: View git status for each file and directory directly in the tree view. Filter to see only modified, untracked, or staged files.
File Preview: Preview file contents with syntax highlighting directly inside broot, including images in supported terminals.
Custom Verbs: Define custom actions (verbs) in the configuration to run arbitrary commands on selected files or directories.
Panels: Open multiple panels side by side for copying, moving files, or comparing directories.

How It Works
An agent skill built around broot enables AI agents to navigate project structures efficiently. The agent can invoke broot's search capabilities to locate files by name or content pattern, inspect directory layouts, and perform bulk file operations. broot outputs structured data about matched files including paths, sizes, dates, and git status, making it ideal for programmatic directory exploration.

Technical Details
broot is distributed as a single Rust binary via cargo install broot, Homebrew (brew install broot), or system package managers. Configuration is stored in ~/.config/broot/ as HJSON or TOML files. The tool supports cross-platform operation on Linux, macOS, and Windows. It is released under the MIT license with over 12,000 GitHub stars and active development.

Integration Points

Shell function installation via br for directory-changing navigation
Configurable verbs for running editors, git commands, or custom scripts
JSON output mode for structured file listing data
Integration with other CLI tools through piping and command composition

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill broot-interactive-tree-view-file-navigator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill broot-interactive-tree-view-file-navigator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill broot-interactive-tree-view-file-navigator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill broot-interactive-tree-view-file-navigator -a codex
```

### OpenClaw

```bash
clawhub install broot-interactive-tree-view-file-navigator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/broot-interactive-tree-view-file-navigator/)

---
title: "broot Interactive Tree-View File Navigator"
description: "Overview\nbroot is an innovative terminal file manager and directory navigator written in Rust. Unlike traditional tools like tree or ls, broot provides an interactive, adaptive tree view that fits your terminal while letting you search, filter, and act on files without ever leaving the interface.\nKey Features\n\nAdaptive Tree View: broot intelligently adjusts how much of the directory tree it shows based on your terminal size, never overflowing the screen like tree does on large repos.\nFuzzy Search: Start typing to instantly filter and find files across the entire directory tree with fuzzy matching, similar to fzf but integrated into the tree context.\nGit Integration: View git status for each file and directory directly in the tree view. Filter to see only modified, untracked, or staged files.\nFile Preview: Preview file contents with syntax highlighting directly inside broot, including images in supported terminals.\nCustom Verbs: Define custom actions (verbs) in the configuration to run arbitrary commands on selected files or directories.\nPanels: Open multiple panels side by side for copying, moving files, or comparing directories.\n\nHow It Works\nAn agent skill built around broot enables AI agents to navigate project structures efficiently. The agent can invoke broot’s search capabilities to locate files by name or content pattern, inspect directory layouts, and perform bulk file operations. broot outputs structured data about matched files including paths, sizes, dates, and git status, making it ideal for programmatic directory exploration.\nTechnical Details\nbroot is distributed as a single Rust binary via cargo install broot, Homebrew (brew install broot), or system package managers. Configuration is stored in ~/.config/broot/ as HJSON or TOML files. The tool supports cross-platform operation on Linux, macOS, and Windows. It is released under the MIT license with over 12,000 GitHub stars and active development.\nIntegration Points\n\nShell function installation via br for directory-changing navigation\nConfigurable verbs for running editors, git commands, or custom scripts\nJSON output mode for structured file listing data\nIntegration with other CLI tools through piping and command composition"
verification: security_reviewed
source: "https://github.com/Canop/broot"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "Canop/broot"
  github_stars: 12549
---

# broot Interactive Tree-View File Navigator

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
An agent skill built around broot enables AI agents to navigate project structures efficiently. The agent can invoke broot’s search capabilities to locate files by name or content pattern, inspect directory layouts, and perform bulk file operations. broot outputs structured data about matched files including paths, sizes, dates, and git status, making it ideal for programmatic directory exploration.
Technical Details
broot is distributed as a single Rust binary via cargo install broot, Homebrew (brew install broot), or system package managers. Configuration is stored in ~/.config/broot/ as HJSON or TOML files. The tool supports cross-platform operation on Linux, macOS, and Windows. It is released under the MIT license with over 12,000 GitHub stars and active development.
Integration Points

Shell function installation via br for directory-changing navigation
Configurable verbs for running editors, git commands, or custom scripts
JSON output mode for structured file listing data
Integration with other CLI tools through piping and command composition

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/broot-interactive-tree-view-file-navigator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/broot-interactive-tree-view-file-navigator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/broot-interactive-tree-view-file-navigator/)

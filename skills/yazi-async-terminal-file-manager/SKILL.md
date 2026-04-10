---
title: "Yazi Async Terminal File Manager"
description: "Yazi is a blazing-fast terminal file manager written in Rust with async I/O, image previews, Vim keybindings, and a Lua plugin system. It integrates with ripgrep, fd, fzf, and zoxide for a seamless developer workflow in the terminal."
slug: "yazi-async-terminal-file-manager"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/sxyazi/yazi"
tool_ecosystem:
  github_repo: "sxyazi/yazi"
  github_stars: 35770
listed: true
---

# Yazi Async Terminal File Manager

Yazi is a blazing-fast terminal file manager written in Rust with async I/O, image previews, Vim keybindings, and a Lua plugin system. It integrates with ripgrep, fd, fzf, and zoxide for a seamless developer workflow in the terminal.

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
clawhub install yazi-async-terminal-file-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Yazi is a terminal file manager built in Rust that leverages non-blocking async I/O to deliver unmatched speed when browsing, previewing, and managing files. With over 35,000 GitHub stars, it has become one of the most popular terminal-based file management tools in the modern developer ecosystem.
The skill wraps Yazi’s extensive feature set into a workflow that agents can use for file system navigation, bulk operations, and workspace management. All I/O operations run asynchronously, and CPU-intensive tasks like syntax highlighting and image decoding are spread across multiple threads, making Yazi responsive even on large directory trees with thousands of files.
Yazi provides built-in support for multiple terminal image protocols including Kitty, iTerm2, and Sixel, allowing image previews directly in the terminal. It includes a concurrent plugin system powered by Lua, enabling custom previewers, preloaders, and fetchers. The built-in package manager lets users install themes and plugins with a single command.
Key integration points include ripgrep for fast search, fd for file finding, fzf for fuzzy selection, and zoxide for smart directory jumping. The tool supports multi-tab workflows, cross-directory selection, bulk renaming, archive extraction, visual mode, and Git integration. Agents can use Yazi to efficiently navigate codebases, organize project files, preview documents and images, and perform batch file operations from the terminal.
The output includes directory listings with metadata, file previews with syntax highlighting, and operation confirmations for moves, copies, and deletions. Yazi runs on Linux, macOS, Windows, and Android, making it a truly cross-platform file management solution.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yazi-async-terminal-file-manager/)

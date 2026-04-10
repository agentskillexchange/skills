---
name: Yazi Async Terminal File Manager
description: Yazi is a blazing-fast terminal file manager written in Rust with async
  I/O, image previews, Vim keybindings, and a Lua plugin system. It integrates with
  ripgrep, fd, fzf, and zoxide for a seamless developer workflow in the terminal.
verification: security_reviewed
source: https://github.com/sxyazi/yazi
category:
- Developer Tools
framework:
- Custom Agents
tool_ecosystem:
  github_repo: sxyazi/yazi
  github_stars: 35770
---
# Yazi Async Terminal File Manager

Yazi is a terminal file manager built in Rust that leverages non-blocking async I/O to deliver unmatched speed when browsing, previewing, and managing files. With over 35,000 GitHub stars, it has become one of the most popular terminal-based file management tools in the modern developer ecosystem.
The skill wraps Yazi's extensive feature set into a workflow that agents can use for file system navigation, bulk operations, and workspace management. All I/O operations run asynchronously, and CPU-intensive tasks like syntax highlighting and image decoding are spread across multiple threads, making Yazi responsive even on large directory trees with thousands of files.
Yazi provides built-in support for multiple terminal image protocols including Kitty, iTerm2, and Sixel, allowing image previews directly in the terminal. It includes a concurrent plugin system powered by Lua, enabling custom previewers, preloaders, and fetchers. The built-in package manager lets users install themes and plugins with a single command.
Key integration points include ripgrep for fast search, fd for file finding, fzf for fuzzy selection, and zoxide for smart directory jumping. The tool supports multi-tab workflows, cross-directory selection, bulk renaming, archive extraction, visual mode, and Git integration. Agents can use Yazi to efficiently navigate codebases, organize project files, preview documents and images, and perform batch file operations from the terminal.
The output includes directory listings with metadata, file previews with syntax highlighting, and operation confirmations for moves, copies, and deletions. Yazi runs on Linux, macOS, Windows, and Android, making it a truly cross-platform file management solution.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yazi-async-terminal-file-manager/)

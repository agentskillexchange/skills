---
title: "Yazi Async Terminal File Manager"
description: "Yazi is a blazing-fast terminal file manager written in Rust with async I/O, image previews, Vim keybindings, and a Lua plugin system. It integrates with ripgrep, fd, fzf, and zoxide for a seamless developer workflow in the terminal."
verification: security_reviewed
source: "https://github.com/sxyazi/yazi"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "sxyazi/yazi"
  github_stars: 35770
---

# Yazi Async Terminal File Manager

Yazi is a terminal file manager built in Rust that leverages non-blocking async I/O to deliver unmatched speed when browsing, previewing, and managing files. With over 35,000 GitHub stars, it has become one of the most popular terminal-based file management tools in the modern developer ecosystem.

The skill wraps Yazi’s extensive feature set into a workflow that agents can use for file system navigation, bulk operations, and workspace management. All I/O operations run asynchronously, and CPU-intensive tasks like syntax highlighting and image decoding are spread across multiple threads, making Yazi responsive even on large directory trees with thousands of files.

Yazi provides built-in support for multiple terminal image protocols including Kitty, iTerm2, and Sixel, allowing image previews directly in the terminal. It includes a concurrent plugin system powered by Lua, enabling custom previewers, preloaders, and fetchers. The built-in package manager lets users install themes and plugins with a single command.

Key integration points include ripgrep for fast search, fd for file finding, fzf for fuzzy selection, and zoxide for smart directory jumping. The tool supports multi-tab workflows, cross-directory selection, bulk renaming, archive extraction, visual mode, and Git integration. Agents can use Yazi to efficiently navigate codebases, organize project files, preview documents and images, and perform batch file operations from the terminal.

The output includes directory listings with metadata, file previews with syntax highlighting, and operation confirmations for moves, copies, and deletions. Yazi runs on Linux, macOS, Windows, and Android, making it a truly cross-platform file management solution.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yazi-async-terminal-file-manager/)

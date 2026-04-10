---
title: "watchexec File Watcher and Command Re-Runner"
description: "watchexec is a standalone file-watching tool written in Rust that automatically executes commands when it detects file modifications. It respects .gitignore rules, coalesces rapid filesystem events, and works cross-platform without requiring any language runtime."
slug: "watchexec-file-watcher-command-rerunner"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/watchexec/watchexec"
tool_ecosystem:
  github_repo: "watchexec/watchexec"
  github_stars: 6882
---

# watchexec File Watcher and Command Re-Runner

watchexec is a standalone file-watching tool written in Rust that automatically executes commands when it detects file modifications. It respects .gitignore rules, coalesces rapid filesystem events, and works cross-platform without requiring any language runtime.

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
clawhub install watchexec-file-watcher-command-rerunner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

watchexec is a standalone command-line tool that monitors filesystem paths and re-executes a specified command whenever it detects modifications. Written in Rust, it provides a fast, reliable file-watching experience that works across macOS, Linux, and Windows without depending on any language runtime or build system.
The tool handles the practical annoyances of file watching that simpler solutions miss. It coalesces multiple rapid filesystem events into a single execution, which is critical for editors that create swap files or write temporary backups during saves. watchexec automatically loads and respects .gitignore and .ignore files, so it skips build artifacts, node_modules, and other directories you would never want to trigger rebuilds. It uses process groups to properly manage forking programs, ensuring child processes are cleaned up when a new execution starts.
Common use cases include automatically running test suites when source files change, triggering linters after edits, rebuilding static assets, and restarting development servers. The command syntax is straightforward — watchexec -e js,css,html npm run build watches for changes to JavaScript, CSS, and HTML files and runs the build command. Adding the -r flag enables restart mode for long-running processes like development servers.
watchexec exposes the changed file paths through environment variables and STDIN, enabling scripts that need to know which files triggered the execution. It supports filtering by file extension, path patterns, and glob expressions. The tool is available through most package managers including Homebrew, apt, pacman, Scoop, Chocolatey, and cargo install, and provides pre-built binaries for all major platforms via GitHub releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/watchexec-file-watcher-command-rerunner/)

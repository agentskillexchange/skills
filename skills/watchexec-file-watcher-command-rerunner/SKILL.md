---
title: watchexec File Watcher and Command Re-Runner
description: watchexec is a standalone command-line tool that monitors filesystem
  paths and re-executes a specified command whenever it detects modifications. Written
  in Rust, it provides a fast, reliable file-watching experience that works across
  macOS, Linux, and Windows without depending on any language runtime or build system.
  The tool handles the practical annoyances of file watching that simpler solutions
  miss. It coalesces multiple rapid filesystem events into a single execution, which
  is critical for editors that create swap files or write temporary backups during
  saves. watchexec automatically loads and respects .gitignore and .ignore files,
  so it skips build artifacts, node_modules, and other directories you would never
  want to trigger rebuilds. It uses process groups to properly manage forking programs,
  ensuring child processes are cleaned up when a new execution starts. Common use
  cases include automatically running test suites when source files change, triggering
  linters after edits, rebuilding static assets, and restarting development servers.
  The command syntax is straightforward — watchexec -e js,css,html npm run build watches
  for changes to JavaScript, CSS, and HTML files and runs the build command. Adding
  the -r flag enables restart mode for long-running processes like development servers.
  watchexec exposes the changed file paths through environment variables and STDIN,
  enabling scripts that need to know which files triggered the execution. It supports
  filtering by file extension, path patterns, and glob expressions. The tool is available
  through most package managers including Homebrew, apt, pacman, Scoop, Chocolatey,
  and cargo install, and provides pre-built binaries for all major platforms via GitHub
  releases.
verification: security_reviewed
source: https://github.com/watchexec/watchexec
category:
- Developer Tools
framework:
- Custom Agents
tool_ecosystem:
  github_repo: watchexec/watchexec
  github_stars: 6882
---

# watchexec File Watcher and Command Re-Runner

watchexec is a standalone command-line tool that monitors filesystem paths and re-executes a specified command whenever it detects modifications. Written in Rust, it provides a fast, reliable file-watching experience that works across macOS, Linux, and Windows without depending on any language runtime or build system. The tool handles the practical annoyances of file watching that simpler solutions miss. It coalesces multiple rapid filesystem events into a single execution, which is critical for editors that create swap files or write temporary backups during saves. watchexec automatically loads and respects .gitignore and .ignore files, so it skips build artifacts, node_modules, and other directories you would never want to trigger rebuilds. It uses process groups to properly manage forking programs, ensuring child processes are cleaned up when a new execution starts. Common use cases include automatically running test suites when source files change, triggering linters after edits, rebuilding static assets, and restarting development servers. The command syntax is straightforward — watchexec -e js,css,html npm run build watches for changes to JavaScript, CSS, and HTML files and runs the build command. Adding the -r flag enables restart mode for long-running processes like development servers. watchexec exposes the changed file paths through environment variables and STDIN, enabling scripts that need to know which files triggered the execution. It supports filtering by file extension, path patterns, and glob expressions. The tool is available through most package managers including Homebrew, apt, pacman, Scoop, Chocolatey, and cargo install, and provides pre-built binaries for all major platforms via GitHub releases.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/watchexec-file-watcher-command-rerunner/)

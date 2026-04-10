---
title: "fd Fast File Finder CLI"
description: "A fast and user-friendly alternative to the find command, written in Rust. fd provides intuitive syntax, regex and glob support, colorized output, parallel execution, and automatic .gitignore awareness."
slug: "fd-fast-file-finder-cli"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/sharkdp/fd"
tool_ecosystem:
  github_repo: "sharkdp/fd"
  github_stars: 42280
---

# fd Fast File Finder CLI

A fast and user-friendly alternative to the find command, written in Rust. fd provides intuitive syntax, regex and glob support, colorized output, parallel execution, and automatic .gitignore awareness.

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
clawhub install fd-fast-file-finder-cli
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

fd (published as fd-find on crates.io) is a program for finding entries in your filesystem. Created by David Peter (sharkdp), it has earned over 42,000 GitHub stars and is one of the most popular modern CLI tools in the Rust ecosystem. It serves as a faster, more ergonomic alternative to the traditional find command, providing sensible defaults that cover the majority of use cases without requiring the complex flag syntax that find demands.
The core design philosophy of fd is intuitive syntax. Where find requires find -iname '*PATTERN*', fd simply uses fd PATTERN. The search is case-insensitive by default but automatically switches to case-sensitive when the pattern contains an uppercase character, following the smart-case convention familiar to users of ripgrep and similar modern tools. fd ignores hidden directories, files, and patterns from .gitignore by default, which eliminates noise in the typical developer workflow.
Performance is a key differentiator. fd uses parallelized directory traversal, making it significantly faster than GNU find in benchmarks, particularly on large directory trees. It supports both regular expressions (the default) and glob-based patterns via the -g flag. The --exec flag enables parallel command execution on matched files, similar to find -exec but with automatic parallelization and a cleaner syntax.
For AI agents performing codebase exploration, file discovery, or automated refactoring workflows, fd provides fast, reliable file searches with output that is both human-readable (with colorized file types matching ls conventions) and easy to parse programmatically. It integrates well with other tools via piping, supports fixed-string search with -F, and can filter by file type, extension, size, and modification time. Available via Homebrew, apt, pacman, cargo, and most other package managers across Linux, macOS, and Windows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fd-fast-file-finder-cli/)

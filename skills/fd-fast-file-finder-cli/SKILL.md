---
name: "fd Fast File Finder CLI"
description: "A fast and user-friendly alternative to the find command, written in Rust. fd provides intuitive syntax, regex and glob support, colorized output, parallel execution, and automatic .gitignore awareness."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/sharkdp/fd"
---
# fd Fast File Finder CLI

A fast and user-friendly alternative to the find command, written in Rust. fd provides intuitive syntax, regex and glob support, colorized output, parallel execution, and automatic .gitignore awareness.

## Overview

fd (published as `fd-find` on crates.io) is a program for finding entries in your filesystem. Created by David Peter (sharkdp), it has earned over 42,000 GitHub stars and is one of the most popular modern CLI tools in the Rust ecosystem. It serves as a faster, more ergonomic alternative to the traditional `find` command, providing sensible defaults that cover the majority of use cases without requiring the complex flag syntax that find demands.

The core design philosophy of fd is intuitive syntax. Where `find` requires `find -iname '*PATTERN*'`, fd simply uses `fd PATTERN`. The search is case-insensitive by default but automatically switches to case-sensitive when the pattern contains an uppercase character, following the smart-case convention familiar to users of ripgrep and similar modern tools. fd ignores hidden directories, files, and patterns from `.gitignore` by default, which eliminates noise in the typical developer workflow.

Performance is a key differentiator. fd uses parallelized directory traversal, making it significantly faster than GNU find in benchmarks, particularly on large directory trees. It supports both regular expressions (the default) and glob-based patterns via the `-g` flag. The `--exec` flag enables parallel command execution on matched files, similar to `find -exec` but with automatic parallelization and a cleaner syntax.

For AI agents performing codebase exploration, file discovery, or automated refactoring workflows, fd provides fast, reliable file searches with output that is both human-readable (with colorized file types matching ls conventions) and easy to parse programmatically. It integrates well with other tools via piping, supports fixed-string search with `-F`, and can filter by file type, extension, size, and modification time. Available via Homebrew, apt, pacman, cargo, and most other package managers across Linux, macOS, and Windows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill fd-fast-file-finder-cli
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill fd-fast-file-finder-cli -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill fd-fast-file-finder-cli -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill fd-fast-file-finder-cli -a codex
```

### OpenClaw

```bash
clawhub install fd-fast-file-finder-cli
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fd-fast-file-finder-cli/)

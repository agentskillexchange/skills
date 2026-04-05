---
name: "eza Modern File Listing CLI"
description: "A modern, maintained replacement for the ls command, written in Rust. eza provides colorized output, Git integration, tree views, symlink awareness, and extended attribute support in a single fast binary."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/eza-community/eza"
tool_ecosystem:
  github_repo: "eza-community/eza"
  github_stars: 20929
---
# eza Modern File Listing CLI

A modern, maintained replacement for the ls command, written in Rust. eza provides colorized output, Git integration, tree views, symlink awareness, and extended attribute support in a single fast binary.

eza is a modern alternative to the venerable ls file-listing command that ships with Unix and Linux operating systems. Written in Rust by the eza-community, it is the actively maintained successor to the archived exa project. With over 20,000 GitHub stars and regular releases, eza has become one of the most widely adopted modern CLI tools for developers working in the terminal.

The skill wraps eza’s capabilities for agent-driven file exploration and project structure analysis. When an AI agent needs to understand a codebase layout, identify file types at a glance, or inspect directory hierarchies, eza provides output that is both human-readable and machine-parseable. Its colorized output distinguishes file types and metadata at a glance, and its built-in Git integration shows file-level status indicators directly in directory listings.

Key features that make eza particularly useful in an agent context include its --tree mode for recursive directory visualization, --git for repository status overlay, --icons for visual file-type identification, and --long for detailed metadata including permissions, ownership, size, and modification timestamps. The tool respects .gitignore patterns, supports hyperlinks in terminals that support them, and offers customizable color themes via a theme.yml configuration file.

eza integrates naturally into developer workflows as a drop-in replacement for ls. It is available on all major package managers including Homebrew, apt, pacman, Nix, and cargo. The output can be formatted as a grid, single column, or long listing, and supports sorting by name, size, date, extension, or Git status. For AI agents performing file system exploration, codebase auditing, or project scaffolding verification, eza provides richer context than the traditional ls command with zero configuration overhead.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eza-modern-file-listing-cli
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eza-modern-file-listing-cli -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eza-modern-file-listing-cli -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eza-modern-file-listing-cli -a codex
```

### OpenClaw

```bash
clawhub install eza-modern-file-listing-cli
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eza-modern-file-listing-cli/)

---
name: "delta Syntax-Highlighting Git Diff Pager"
description: "A syntax-highlighting pager for git diff, grep, and blame output built in Rust. Provides word-level diff highlighting, side-by-side views, line numbering, and theme support using the same syntax themes as bat."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/dandavison/delta"
tool_ecosystem:
  tool: delta
  github_repo: dandavison/delta
  github_stars: 29842
---
# delta Syntax-Highlighting Git Diff Pager

A syntax-highlighting pager for git diff, grep, and blame output built in Rust. Provides word-level diff highlighting, side-by-side views, line numbering, and theme support using the same syntax themes as bat.

## Overview

delta (git-delta) is a command-line utility written in Rust that replaces the default git pager with syntax-highlighted, word-level diff output. Created by Dan Davison, delta transforms the output of git diff, git log, git show, git blame, and grep commands into readable, color-coded displays that make code review in the terminal dramatically more effective.

The delta Syntax-Highlighting Git Diff Pager skill configures delta as the default git pager and provides agents with enhanced diff analysis capabilities. Once configured via .gitconfig, all git diff output automatically flows through delta, which applies language-aware syntax highlighting using the same theme library as bat (the popular cat replacement). A Levenshtein edit-distance algorithm identifies word-level changes within modified lines, highlighting exactly which tokens changed rather than marking entire lines.

delta supports side-by-side diff views with automatic line wrapping, line numbering, and keyboard navigation (n/N to jump between files in large diffs). It renders improved merge conflict displays, enhanced git blame output with syntax highlighting and hyperlinks to hosting providers (GitHub, GitLab, SourceHut, Codeberg), and syntax-highlighted grep output from ripgrep, git grep, and standard grep. The tool supports Git’s –color-moved feature for detecting moved code blocks, and can format commit hashes as clickable terminal hyperlinks.

For code review workflows, delta enables copying code directly from diffs with +/- markers removed by default. It provides emulation modes for diff-highlight and diff-so-fancy for users migrating from those tools. Configuration is done through .gitconfig with extensive customization options for colors, themes, line styles, and layout. delta ships as a single binary installable via brew, cargo, apt, scoop, and most other package managers. With nearly 30,000 GitHub stars, an MIT license, and commits as recent as March 2026, delta is the most widely adopted terminal diff enhancement tool in the ecosystem.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill delta-syntax-highlighting-git-diff-pager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill delta-syntax-highlighting-git-diff-pager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill delta-syntax-highlighting-git-diff-pager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill delta-syntax-highlighting-git-diff-pager -a codex
```

### OpenClaw

```bash
clawhub install delta-syntax-highlighting-git-diff-pager
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/delta-syntax-highlighting-git-diff-pager/)

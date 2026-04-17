---
title: "tokei Code Statistics Counter"
description: "tokei is a high-performance command-line program written in Rust that calculates code statistics for a project. It counts the number of files, total lines, code lines, comment lines, and blank lines grouped by programming language. tokei recognizes over 200 programming languages and can process large codebases in seconds, making it one of the fastest code counting tools available.\nThe tokei Code Statistics Counter skill provides agents with codebase analysis capabilities for understanding project composition, tracking code growth, and generating reports. Running tokei ./src produces a breakdown showing each language detected in the directory tree with file counts and line statistics. The tool accurately distinguishes between code, comments, and blank lines using language-specific parsing rules rather than simple heuristics, handling nested comments, multi-line strings, and language-specific syntax correctly.\ntokei outputs data in multiple structured formats including JSON, YAML, and CBOR (via -o json), enabling programmatic consumption by other tools and pipelines. This makes it straightforward to integrate tokei results into CI pipelines for tracking code metrics over time, generating project documentation, or feeding into dashboards. The tool supports filtering by language type (-t rust,python), sorting by various columns (files, lines, code, comments), and processing multiple directories or files in a single invocation.\nResults can be saved and loaded from previous runs (-i flag), enabling diff-based analysis to see how code statistics change between commits or releases. tokei respects .gitignore files and supports custom exclusion patterns. Installation is available via cargo (cargo install tokei), Homebrew, Chocolatey, apt, and most other package managers. The tool is distributed under a permissive license, has over 14,000 GitHub stars, and millions of downloads across package managers. It provides a reliable, fast foundation for any codebase health or composition analysis task."
verification: security_reviewed
source: "https://github.com/XAMPPRocky/tokei"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "XAMPPRocky/tokei"
  github_stars: 14169
---

# tokei Code Statistics Counter

tokei is a high-performance command-line program written in Rust that calculates code statistics for a project. It counts the number of files, total lines, code lines, comment lines, and blank lines grouped by programming language. tokei recognizes over 200 programming languages and can process large codebases in seconds, making it one of the fastest code counting tools available.
The tokei Code Statistics Counter skill provides agents with codebase analysis capabilities for understanding project composition, tracking code growth, and generating reports. Running tokei ./src produces a breakdown showing each language detected in the directory tree with file counts and line statistics. The tool accurately distinguishes between code, comments, and blank lines using language-specific parsing rules rather than simple heuristics, handling nested comments, multi-line strings, and language-specific syntax correctly.
tokei outputs data in multiple structured formats including JSON, YAML, and CBOR (via -o json), enabling programmatic consumption by other tools and pipelines. This makes it straightforward to integrate tokei results into CI pipelines for tracking code metrics over time, generating project documentation, or feeding into dashboards. The tool supports filtering by language type (-t rust,python), sorting by various columns (files, lines, code, comments), and processing multiple directories or files in a single invocation.
Results can be saved and loaded from previous runs (-i flag), enabling diff-based analysis to see how code statistics change between commits or releases. tokei respects .gitignore files and supports custom exclusion patterns. Installation is available via cargo (cargo install tokei), Homebrew, Chocolatey, apt, and most other package managers. The tool is distributed under a permissive license, has over 14,000 GitHub stars, and millions of downloads across package managers. It provides a reliable, fast foundation for any codebase health or composition analysis task.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/tokei-code-statistics-counter
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/tokei-code-statistics-counter` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tokei-code-statistics-counter/)

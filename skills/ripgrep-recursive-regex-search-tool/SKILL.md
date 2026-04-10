---
title: "ripgrep Recursive Regex Search Tool"
description: "ripgrep (rg) is a line-oriented search tool that recursively searches directories for regex patterns while respecting .gitignore rules. Written in Rust, it outperforms grep, ag, and ack on large codebases by significant margins and supports Unicode by default."
slug: "ripgrep-recursive-regex-search-tool"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/BurntSushi/ripgrep"
tool_ecosystem:
  github_repo: "BurntSushi/ripgrep"
  github_stars: 61743
---

# ripgrep Recursive Regex Search Tool

ripgrep (rg) is a line-oriented search tool that recursively searches directories for regex patterns while respecting .gitignore rules. Written in Rust, it outperforms grep, ag, and ack on large codebases by significant margins and supports Unicode by default.

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
clawhub install ripgrep-recursive-regex-search-tool
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

ripgrep is a command-line search utility written in Rust by Andrew Galloway (BurntSushi). It searches the current directory tree for lines matching a regular expression pattern, printing file names, line numbers, and matched text. By default it skips files listed in .gitignore, hidden directories, and binary files — behavior that can be disabled with the -uuu flag for unrestricted searching.
Performance is ripgrep’s defining characteristic. In benchmarks against the Linux kernel source tree (~70,000 files), ripgrep completes searches 3-8x faster than git grep and 5-35x faster than ack. This speed comes from several Rust-level optimizations: memory-mapped file I/O, SIMD-accelerated literal string matching via the aho-corasick and memchr crates, parallel directory traversal using the ignore crate, and a regex engine that avoids catastrophic backtracking.
The tool supports Perl-compatible regex syntax through the regex crate, with full Unicode support enabled by default. The -w flag restricts matches to word boundaries. The -t flag filters by file type (e.g., rg -tc searches only C/C++ files). The –type-add flag defines custom file type associations. The -g flag applies glob patterns for include/exclude filtering beyond gitignore rules.
ripgrep outputs results in a format compatible with grep, so it integrates with existing tool chains. The –json flag emits structured JSON output for programmatic consumption. The –vimgrep flag formats output for Vim’s quickfix list. Color output is automatic when writing to a terminal and disabled when piping to another command.
The tool is distributed via GitHub releases as static binaries for Linux, macOS, and Windows. It is also available through Homebrew, cargo, apt, pacman, Chocolatey, and Scoop. ripgrep is dual-licensed under MIT and the Unlicense.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ripgrep-recursive-regex-search-tool/)

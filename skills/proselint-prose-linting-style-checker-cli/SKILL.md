---
title: "proselint Prose Linting and Style Checker CLI"
description: "proselint is a Python CLI tool that lints English prose for style and usage issues. It aggregates writing advice from renowned authors and editors including Bryan Garner, David Foster Wallace, and Strunk & White into automated checks that scan text files and flag problems."
slug: "proselint-prose-linting-style-checker-cli"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/amperser/proselint"
tool_ecosystem:
  github_repo: "amperser/proselint"
  github_stars: 4515
---

# proselint Prose Linting and Style Checker CLI

proselint is a Python CLI tool that lints English prose for style and usage issues. It aggregates writing advice from renowned authors and editors including Bryan Garner, David Foster Wallace, and Strunk & White into automated checks that scan text files and flag problems.

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
clawhub install proselint-prose-linting-style-checker-cli
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

proselint is an open-source command-line linter for English prose, created by Amperser Labs. It scans text files and detects writing issues by encoding advice from the world’s greatest writers and style guides into automated checks. The tool draws on expertise from Bryan Garner, David Foster Wallace, Chuck Palahniuk, Steve Pinker, Mary Norris, Mark Twain, Elmore Leonard, George Orwell, Matthew Butterick, William Strunk, and E.B. White, among others.
The tool runs as a CLI command (proselint filename.md) and outputs JSON-structured suggestions including the check type, severity level, line/column positions, and suggested replacements. Each check maps to a specific source and rule category. proselint covers dozens of check categories including uncomparables, redundancy, clichés, jargon, sexism, scare quotes, false plurals, hedging, mixed metaphors, and typography issues.
proselint integrates with major code editors through plugins for Vim (via ALE or Syntastic), Emacs (via Flycheck or Flymake), Neovim (via none-ls.nvim), and VS Code. It also integrates with pre-commit hooks for CI/CD workflows, and can be used as a Python library via proselint.tools.lint() for programmatic access. The tool is available on PyPI (pip install proselint) and through system package managers on Fedora, Ubuntu, Debian, and NixOS.
AI coding agents can use proselint to automatically review documentation, blog posts, README files, and any prose content. It pairs well with other writing tools like Vale and textlint, but uniquely focuses on style advice from specific literary authorities rather than generic grammar rules. With 4,500+ GitHub stars and active development, proselint is a mature and well-maintained tool for automated prose quality assurance.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/proselint-prose-linting-style-checker-cli/)

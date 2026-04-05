---
name: "proselint Prose Linting and Style Checker CLI"
description: "proselint is a Python CLI tool that lints English prose for style and usage issues. It aggregates writing advice from renowned authors and editors including Bryan Garner, David Foster Wallace, and Strunk & White into automated checks that scan text files and flag problems."
category: "Content Writing &amp; SEO"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/amperser/proselint"
tool_ecosystem:
  github_repo: "amperser/proselint"
  github_stars: 4515
  license: "BSD-3-Clause"
---
# proselint Prose Linting and Style Checker CLI

proselint is a Python CLI tool that lints English prose for style and usage issues. It aggregates writing advice from renowned authors and editors including Bryan Garner, David Foster Wallace, and Strunk & White into automated checks that scan text files and flag problems.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill proselint-prose-linting-style-checker-cli
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill proselint-prose-linting-style-checker-cli -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill proselint-prose-linting-style-checker-cli -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill proselint-prose-linting-style-checker-cli -a codex
```

### OpenClaw

```bash
clawhub install proselint-prose-linting-style-checker-cli
```

## Details

proselint is an open-source command-line linter for English prose, created by Amperser Labs. It scans text files and detects writing issues by encoding advice from the world’s greatest writers and style guides into automated checks. The tool draws on expertise from Bryan Garner, David Foster Wallace, Chuck Palahniuk, Steve Pinker, Mary Norris, Mark Twain, Elmore Leonard, George Orwell, Matthew Butterick, William Strunk, and E.B. White, among others.

The tool runs as a CLI command (proselint filename.md) and outputs JSON-structured suggestions including the check type, severity level, line/column positions, and suggested replacements. Each check maps to a specific source and rule category. proselint covers dozens of check categories including uncomparables, redundancy, clichés, jargon, sexism, scare quotes, false plurals, hedging, mixed metaphors, and typography issues.

proselint integrates with major code editors through plugins for Vim (via ALE or Syntastic), Emacs (via Flycheck or Flymake), Neovim (via none-ls.nvim), and VS Code. It also integrates with pre-commit hooks for CI/CD workflows, and can be used as a Python library via proselint.tools.lint() for programmatic access. The tool is available on PyPI (pip install proselint) and through system package managers on Fedora, Ubuntu, Debian, and NixOS.

AI coding agents can use proselint to automatically review documentation, blog posts, README files, and any prose content. It pairs well with other writing tools like Vale and textlint, but uniquely focuses on style advice from specific literary authorities rather than generic grammar rules. With 4,500+ GitHub stars and active development, proselint is a mature and well-maintained tool for automated prose quality assurance.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/proselint-prose-linting-style-checker-cli/)

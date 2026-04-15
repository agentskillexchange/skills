---
title: "typos Source Code Spell Checker"
description: "A blazing-fast source code spell checker written in Rust that finds and corrects typos across entire codebases. Designed to run on monorepos with minimal false positives, typos integrates into CI/CD pipelines, pre-commit hooks, and editor workflows."
verification: security_reviewed
source: "https://github.com/crate-ci/typos"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "crate-ci/typos"
  github_stars: 3864
---

# typos Source Code Spell Checker

typos is an open-source CLI tool from the crate-ci project that scans source code, filenames, and documentation for spelling mistakes. Written in Rust, it prioritizes speed and accuracy, making it practical to run on monorepos with millions of lines of code without slowing down developer workflows.

The tool operates by scanning files for known typos using a curated dictionary that understands programming conventions. Unlike general-purpose spell checkers, typos knows about camelCase identifiers, snake_case variables, and common programming abbreviations. When it finds a typo with an unambiguous correction, it can fix it automatically with the --write-changes flag. For ambiguous cases where multiple corrections are possible, it reports the finding and lets the developer decide.

Configuration is handled through a _typos.toml file where developers can extend the dictionary with project-specific terms, mark certain identifiers as intentional, and exclude files or directories from scanning. The tool supports per-file-type configuration, so localized content files can have their contents skipped while filenames are still checked.

typos integrates with GitHub Actions through an official action, supports pre-commit hooks, has a VS Code extension via typos-lsp, and can output results as JSON for custom integrations. It also provides diff output for review before applying changes. The tool is available through Homebrew, Cargo, Conda, and as pre-built binaries for all major platforms.

With its focus on low false-positive rates and fast execution, typos is particularly valuable for maintaining code quality in large codebases where manual spell checking is impractical. It catches mistakes in variable names, comments, documentation strings, and file paths that other linters miss entirely.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/typos-source-code-spell-checker
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/typos-source-code-spell-checker` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typos-source-code-spell-checker/)

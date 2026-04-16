---
title: "typos Source Code Spell Checker"
description: "A blazing-fast source code spell checker written in Rust that finds and corrects typos across entire codebases. Designed to run on monorepos with minimal false positives, typos integrates into CI/CD pipelines, pre-commit hooks, and editor workflows."
verification: "security_reviewed"
source: "https://github.com/crate-ci/typos"
category:
  - "Code Quality &amp; Review"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typos-source-code-spell-checker/)

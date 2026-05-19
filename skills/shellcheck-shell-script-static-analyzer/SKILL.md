---
name: "ShellCheck Shell Script Static Analyzer"
slug: "shellcheck-shell-script-static-analyzer"
description: "Run static analysis on bash and shell scripts using ShellCheck to detect syntax errors, semantic pitfalls, and portability issues. Produces machine-readable diagnostics with fix suggestions."
github_stars: 39204
verification: "security_reviewed"
source: "https://github.com/koalaman/shellcheck"
category: "Code Quality & Review"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "koalaman/shellcheck"
  github_stars: 39204
---

# ShellCheck Shell Script Static Analyzer

Run static analysis on bash and shell scripts using ShellCheck to detect syntax errors, semantic pitfalls, and portability issues. Produces machine-readable diagnostics with fix suggestions.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install shellcheck
- conda install -c conda-forge shellcheck
- docker run --rm -v "$PWD:/mnt" koalaman/shellcheck:stable myscript
- $ brew install cabal-install

Requirements and caveats from upstream:
- From Docker Hub:
- This section describes how to build ShellCheck from a source directory. ShellCheck is written in Haskell and requires 2GB of RAM to compile.

Basic usage or getting-started notes:
- Run shellcheck yourscript in your terminal for instant output, as seen above.
- For example, in a Makefile:
- To run ShellCheck via [pre-commit](https://pre-commit.com/), add the hook to your .pre-commit-config.yaml:

- Source: https://github.com/koalaman/shellcheck
- Extracted from upstream docs: https://raw.githubusercontent.com/koalaman/shellcheck/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shellcheck-shell-script-static-analyzer/)

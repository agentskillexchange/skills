---
title: "CSpell Codebase Spell Checking CLI"
description: "CSpell is an open source spell checking tool from Street Side Software that is designed specifically for code. Unlike generic spell checkers, it is tuned for identifiers, mixed technical vocabulary, filenames, and repository-specific word lists, which makes it useful for engineering teams that want typo detection without constant false positives. The project is available through an official GitHub repository, a maintained npm package, and project documentation on cspell.org. In day-to-day workflows, CSpell can run as a CLI in local development, inside CI, or through editor integrations such as the VS Code extension. It supports built-in and add-on dictionaries, custom configuration files, ignore paths, and language-specific packages. That makes it a practical fit for checking Markdown docs, comments, commit-facing text, JSON or YAML configuration, and code identifiers in large repositories. For ASE, this is a clean code quality and review skill. An agent can add a baseline cspell.json , customize dictionaries for domain language, wire the command into package scripts or GitHub Actions, and triage misspellings that actually matter. It also pairs well with documentation workflows because the same tool can verify both source code and prose, reducing typo drift across docs, UI strings, and developer-facing content."
source: "https://github.com/streetsidesoftware/cspell"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "streetsidesoftware/cspell"
  github_stars: 1616
---

# CSpell Codebase Spell Checking CLI

CSpell is an open source spell checking tool from Street Side Software that is designed specifically for code. Unlike generic spell checkers, it is tuned for identifiers, mixed technical vocabulary, filenames, and repository-specific word lists, which makes it useful for engineering teams that want typo detection without constant false positives. The project is available through an official GitHub repository, a maintained npm package, and project documentation on cspell.org. In day-to-day workflows, CSpell can run as a CLI in local development, inside CI, or through editor integrations such as the VS Code extension. It supports built-in and add-on dictionaries, custom configuration files, ignore paths, and language-specific packages. That makes it a practical fit for checking Markdown docs, comments, commit-facing text, JSON or YAML configuration, and code identifiers in large repositories. For ASE, this is a clean code quality and review skill. An agent can add a baseline cspell.json , customize dictionaries for domain language, wire the command into package scripts or GitHub Actions, and triage misspellings that actually matter. It also pairs well with documentation workflows because the same tool can verify both source code and prose, reducing typo drift across docs, UI strings, and developer-facing content.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cspell-codebase-spell-checking-cli/)

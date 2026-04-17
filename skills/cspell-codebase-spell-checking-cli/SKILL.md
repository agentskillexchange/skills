---
title: "CSpell Codebase Spell Checking CLI"
description: "CSpell is an open source spell checking tool from Street Side Software that is designed specifically for code. Unlike generic spell checkers, it is tuned for identifiers, mixed technical vocabulary, filenames, and repository-specific word lists, which makes it useful for engineering teams that want typo detection without constant false positives. The project is available through an official GitHub repository, a maintained npm package, and project documentation on cspell.org.\nIn day-to-day workflows, CSpell can run as a CLI in local development, inside CI, or through editor integrations such as the VS Code extension. It supports built-in and add-on dictionaries, custom configuration files, ignore paths, and language-specific packages. That makes it a practical fit for checking Markdown docs, comments, commit-facing text, JSON or YAML configuration, and code identifiers in large repositories.\nFor ASE, this is a clean code quality and review skill. An agent can add a baseline cspell.json, customize dictionaries for domain language, wire the command into package scripts or GitHub Actions, and triage misspellings that actually matter. It also pairs well with documentation workflows because the same tool can verify both source code and prose, reducing typo drift across docs, UI strings, and developer-facing content."
verification: security_reviewed
source: "https://github.com/streetsidesoftware/cspell"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "streetsidesoftware/cspell"
  github_stars: 1616
---

# CSpell Codebase Spell Checking CLI

CSpell is an open source spell checking tool from Street Side Software that is designed specifically for code. Unlike generic spell checkers, it is tuned for identifiers, mixed technical vocabulary, filenames, and repository-specific word lists, which makes it useful for engineering teams that want typo detection without constant false positives. The project is available through an official GitHub repository, a maintained npm package, and project documentation on cspell.org.
In day-to-day workflows, CSpell can run as a CLI in local development, inside CI, or through editor integrations such as the VS Code extension. It supports built-in and add-on dictionaries, custom configuration files, ignore paths, and language-specific packages. That makes it a practical fit for checking Markdown docs, comments, commit-facing text, JSON or YAML configuration, and code identifiers in large repositories.
For ASE, this is a clean code quality and review skill. An agent can add a baseline cspell.json, customize dictionaries for domain language, wire the command into package scripts or GitHub Actions, and triage misspellings that actually matter. It also pairs well with documentation workflows because the same tool can verify both source code and prose, reducing typo drift across docs, UI strings, and developer-facing content.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cspell-codebase-spell-checking-cli
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/cspell-codebase-spell-checking-cli` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cspell-codebase-spell-checking-cli/)

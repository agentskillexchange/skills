---
title: "CSpell Codebase Spell Checking CLI"
description: "CSpell is a spell checker built for source code, configuration files, and documentation, with dictionaries and ignore mechanisms that work well in real repositories. It helps agents and teams catch noisy typos before they land in code review, docs, or CI output."
verification: "security_reviewed"
source: "https://github.com/streetsidesoftware/cspell"
category:
  - "Code Quality & Review"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cspell-codebase-spell-checking-cli/)

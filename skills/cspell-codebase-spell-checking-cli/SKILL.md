---
title: "CSpell Codebase Spell Checking CLI"
description: "CSpell is a spell checker built for source code, configuration files, and documentation, with dictionaries and ignore mechanisms that work well in real repositories. It helps agents and teams catch noisy typos before they land in code review, docs, or CI output."
slug: "cspell-codebase-spell-checking-cli"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/streetsidesoftware/cspell"
---

# CSpell Codebase Spell Checking CLI

CSpell is a spell checker built for source code, configuration files, and documentation, with dictionaries and ignore mechanisms that work well in real repositories. It helps agents and teams catch noisy typos before they land in code review, docs, or CI output.

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
clawhub install cspell-codebase-spell-checking-cli
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

CSpell is an open source spell checking tool from Street Side Software that is designed specifically for code. Unlike generic spell checkers, it is tuned for identifiers, mixed technical vocabulary, filenames, and repository-specific word lists, which makes it useful for engineering teams that want typo detection without constant false positives. The project is available through an official GitHub repository, a maintained npm package, and project documentation on cspell.org.
In day-to-day workflows, CSpell can run as a CLI in local development, inside CI, or through editor integrations such as the VS Code extension. It supports built-in and add-on dictionaries, custom configuration files, ignore paths, and language-specific packages. That makes it a practical fit for checking Markdown docs, comments, commit-facing text, JSON or YAML configuration, and code identifiers in large repositories.
For ASE, this is a clean code quality and review skill. An agent can add a baseline cspell.json, customize dictionaries for domain language, wire the command into package scripts or GitHub Actions, and triage misspellings that actually matter. It also pairs well with documentation workflows because the same tool can verify both source code and prose, reducing typo drift across docs, UI strings, and developer-facing content.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cspell-codebase-spell-checking-cli/)

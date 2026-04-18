---
title: "Lint .env files for duplicated keys and unsafe formatting with dotenv-linter"
description: "Check dotenv files for duplicated keys, malformed values, and formatting mistakes before they break local runs or secret handoffs."
verification: listed
source: "https://github.com/dotenv-linter/dotenv-linter"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dotenv-linter/dotenv-linter"
  github_stars: 2068
---

# Lint .env files for duplicated keys and unsafe formatting with dotenv-linter

Use dotenv-linter when an agent needs to inspect .env files for duplicated keys, malformed delimiters, missing values, quote problems, ordering issues, and other dotenv-specific defects that cause configuration drift. It fits repo hygiene, onboarding cleanup, and pre-merge checks where environment files need to stay predictable.

A user should invoke this instead of using a secret manager or editing environment files by hand when the task is validating and normalizing dotenv syntax. The scope boundary keeps it skill-shaped: dotenv-linter audits and fixes dotenv file structure only, not secret storage, rotation, vault administration, or broader configuration management.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/lint-dotenv-files-for-duplicated-keys-and-unsafe-formatting-with-dotenv-linter
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/lint-dotenv-files-for-duplicated-keys-and-unsafe-formatting-with-dotenv-linter` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-dotenv-files-for-duplicated-keys-and-unsafe-formatting-with-dotenv-linter/)

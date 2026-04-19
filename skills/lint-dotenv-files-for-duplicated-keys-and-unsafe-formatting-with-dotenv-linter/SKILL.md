---
title: "Lint .env files for duplicated keys and unsafe formatting with dotenv-linter"
description: "Use dotenv-linter when an agent needs to inspect .env files for duplicated keys, malformed delimiters, missing values, quote problems, ordering issues, and other dotenv-specific defects that cause configuration drift. It fits repo hygiene, onboarding cleanup, and pre-merge checks where environment files need to stay predictable. A user should invoke this instead of using a secret manager or editing environment files by hand when the task is validating and normalizing dotenv syntax. The scope boundary keeps it skill-shaped: dotenv-linter audits and fixes dotenv file structure only, not secret storage, rotation, vault administration, or broader configuration management."
source: "https://github.com/dotenv-linter/dotenv-linter"
verification: "listed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dotenv-linter/dotenv-linter"
  github_stars: 2068
---

# Lint .env files for duplicated keys and unsafe formatting with dotenv-linter

Use dotenv-linter when an agent needs to inspect .env files for duplicated keys, malformed delimiters, missing values, quote problems, ordering issues, and other dotenv-specific defects that cause configuration drift. It fits repo hygiene, onboarding cleanup, and pre-merge checks where environment files need to stay predictable. A user should invoke this instead of using a secret manager or editing environment files by hand when the task is validating and normalizing dotenv syntax. The scope boundary keeps it skill-shaped: dotenv-linter audits and fixes dotenv file structure only, not secret storage, rotation, vault administration, or broader configuration management.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-dotenv-files-for-duplicated-keys-and-unsafe-formatting-with-dotenv-linter/)

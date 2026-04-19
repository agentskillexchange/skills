---
title: "Prettier Config Conflict Resolver"
description: "The Prettier Config Conflict Resolver skill identifies formatting rule conflicts across the Prettier, ESLint, and EditorConfig toolchain that cause inconsistent code style and CI failures. It uses the Prettier resolveConfig Node.js API to load effective Prettier configuration for each file path and compares settings against ESLint rules loaded via the ESLint CLIEngine. The skill runs eslint-config-prettier compatibility checks to detect ESLint rules that conflict with Prettier formatting, such as conflicting indent, quotes, and semi rules. It parses .editorconfig files to verify alignment with Prettier settings for tab width, end-of-line characters, and max line length. The tool generates a unified configuration recommendation that eliminates conflicts while preserving team preferences. It supports monorepo setups with per-package overrides and can output merged configurations in JSON, YAML, and TOML formats for .prettierrc, .eslintrc, and .editorconfig files."
source: "https://agentskillexchange.com/skills/prettier-config-conflict-resolver/"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Gemini"
---

# Prettier Config Conflict Resolver

The Prettier Config Conflict Resolver skill identifies formatting rule conflicts across the Prettier, ESLint, and EditorConfig toolchain that cause inconsistent code style and CI failures. It uses the Prettier resolveConfig Node.js API to load effective Prettier configuration for each file path and compares settings against ESLint rules loaded via the ESLint CLIEngine. The skill runs eslint-config-prettier compatibility checks to detect ESLint rules that conflict with Prettier formatting, such as conflicting indent, quotes, and semi rules. It parses .editorconfig files to verify alignment with Prettier settings for tab width, end-of-line characters, and max line length. The tool generates a unified configuration recommendation that eliminates conflicts while preserving team preferences. It supports monorepo setups with per-package overrides and can output merged configurations in JSON, YAML, and TOML formats for .prettierrc, .eslintrc, and .editorconfig files.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prettier-config-conflict-resolver/)

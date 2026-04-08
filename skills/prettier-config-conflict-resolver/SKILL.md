---
title: Prettier Config Conflict Resolver
description: The Prettier Config Conflict Resolver skill identifies formatting rule
  conflicts across the Prettier, ESLint, and EditorConfig toolchain that cause inconsistent
  code style and CI failures. It uses the Prettier resolveConfig Node.js API to load
  effective Prettier configuration for each file path and compares settings against
  ESLint rules loaded via the ESLint CLIEngine. The skill runs eslint-config-prettier
  compatibility checks to detect ESLint rules that conflict with Prettier formatting,
  such as conflicting indent, quotes, and semi rules. It parses .editorconfig files
  to verify alignment with Prettier settings for tab width, end-of-line characters,
  and max line length. The tool generates a unified configuration recommendation that
  eliminates conflicts while preserving team preferences. It supports monorepo setups
  with per-package overrides and can output merged configurations in JSON, YAML, and
  TOML formats for .prettierrc, .eslintrc, and .editorconfig files.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prettier-config-conflict-resolver/
category:
- Code Quality &amp; Review
framework:
- Gemini
---

# Prettier Config Conflict Resolver

The Prettier Config Conflict Resolver skill identifies formatting rule conflicts across the Prettier, ESLint, and EditorConfig toolchain that cause inconsistent code style and CI failures. It uses the Prettier resolveConfig Node.js API to load effective Prettier configuration for each file path and compares settings against ESLint rules loaded via the ESLint CLIEngine. The skill runs eslint-config-prettier compatibility checks to detect ESLint rules that conflict with Prettier formatting, such as conflicting indent, quotes, and semi rules. It parses .editorconfig files to verify alignment with Prettier settings for tab width, end-of-line characters, and max line length. The tool generates a unified configuration recommendation that eliminates conflicts while preserving team preferences. It supports monorepo setups with per-package overrides and can output merged configurations in JSON, YAML, and TOML formats for .prettierrc, .eslintrc, and .editorconfig files.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prettier-config-conflict-resolver/)

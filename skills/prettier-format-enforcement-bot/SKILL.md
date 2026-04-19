---
title: "Prettier Format Enforcement Bot"
description: "The Prettier Format Enforcement Bot skill uses the Prettier Node.js API (prettier.format(), prettier.check(), prettier.resolveConfig()) and CLI (npx prettier &#8211;check, npx prettier &#8211;write) to enforce consistent code formatting across projects. It supports JavaScript, TypeScript, CSS, SCSS, HTML, JSON, YAML, Markdown, GraphQL, and 10+ additional languages through parser plugins. The skill manages .prettierrc configuration files (JSON, YAML, TOML, or JS formats) with options including printWidth, tabWidth, useTabs, semi, singleQuote, trailingComma, bracketSpacing, arrowParens, and endOfLine. It handles .prettierignore for excluding files and directories from formatting enforcement. Advanced capabilities include plugin integration with prettier-plugin-organize-imports for import sorting, prettier-plugin-tailwindcss for Tailwind class ordering, prettier-plugin-sql for SQL formatting, and @prettier/plugin-xml for XML documents. The bot supports editor integration configuration for VS Code (editor.defaultFormatter, editor.formatOnSave), pre-commit hook setup via husky and lint-staged, CI check mode with &#8211;check flag for non-zero exit on unformatted files, and format-on-save configuration across IDE platforms."
source: "https://agentskillexchange.com/skills/prettier-format-enforcement-bot/"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
---

# Prettier Format Enforcement Bot

The Prettier Format Enforcement Bot skill uses the Prettier Node.js API (prettier.format(), prettier.check(), prettier.resolveConfig()) and CLI (npx prettier &#8211;check, npx prettier &#8211;write) to enforce consistent code formatting across projects. It supports JavaScript, TypeScript, CSS, SCSS, HTML, JSON, YAML, Markdown, GraphQL, and 10+ additional languages through parser plugins. The skill manages .prettierrc configuration files (JSON, YAML, TOML, or JS formats) with options including printWidth, tabWidth, useTabs, semi, singleQuote, trailingComma, bracketSpacing, arrowParens, and endOfLine. It handles .prettierignore for excluding files and directories from formatting enforcement. Advanced capabilities include plugin integration with prettier-plugin-organize-imports for import sorting, prettier-plugin-tailwindcss for Tailwind class ordering, prettier-plugin-sql for SQL formatting, and @prettier/plugin-xml for XML documents. The bot supports editor integration configuration for VS Code (editor.defaultFormatter, editor.formatOnSave), pre-commit hook setup via husky and lint-staged, CI check mode with &#8211;check flag for non-zero exit on unformatted files, and format-on-save configuration across IDE platforms.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prettier-format-enforcement-bot/)

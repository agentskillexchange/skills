---
title: Prettier Format Enforcement Bot
description: The Prettier Format Enforcement Bot skill uses the Prettier Node.js API
  (prettier.format(), prettier.check(), prettier.resolveConfig()) and CLI (npx prettier
  –check, npx prettier –write) to enforce consistent code formatting across projects.
  It supports JavaScript, TypeScript, CSS, SCSS, HTML, JSON, YAML, Markdown, GraphQL,
  and 10+ additional languages through parser plugins. The skill manages .prettierrc
  configuration files (JSON, YAML, TOML, or JS formats) with options including printWidth,
  tabWidth, useTabs, semi, singleQuote, trailingComma, bracketSpacing, arrowParens,
  and endOfLine. It handles .prettierignore for excluding files and directories from
  formatting enforcement. Advanced capabilities include plugin integration with prettier-plugin-organize-imports
  for import sorting, prettier-plugin-tailwindcss for Tailwind class ordering, prettier-plugin-sql
  for SQL formatting, and @prettier/plugin-xml for XML documents. The bot supports
  editor integration configuration for VS Code (editor.defaultFormatter, editor.formatOnSave),
  pre-commit hook setup via husky and lint-staged, CI check mode with –check flag
  for non-zero exit on unformatted files, and format-on-save configuration across
  IDE platforms.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prettier-format-enforcement-bot/
category:
- Code Quality &amp; Review
framework:
- Claude Code
---

# Prettier Format Enforcement Bot

The Prettier Format Enforcement Bot skill uses the Prettier Node.js API (prettier.format(), prettier.check(), prettier.resolveConfig()) and CLI (npx prettier –check, npx prettier –write) to enforce consistent code formatting across projects. It supports JavaScript, TypeScript, CSS, SCSS, HTML, JSON, YAML, Markdown, GraphQL, and 10+ additional languages through parser plugins. The skill manages .prettierrc configuration files (JSON, YAML, TOML, or JS formats) with options including printWidth, tabWidth, useTabs, semi, singleQuote, trailingComma, bracketSpacing, arrowParens, and endOfLine. It handles .prettierignore for excluding files and directories from formatting enforcement. Advanced capabilities include plugin integration with prettier-plugin-organize-imports for import sorting, prettier-plugin-tailwindcss for Tailwind class ordering, prettier-plugin-sql for SQL formatting, and @prettier/plugin-xml for XML documents. The bot supports editor integration configuration for VS Code (editor.defaultFormatter, editor.formatOnSave), pre-commit hook setup via husky and lint-staged, CI check mode with –check flag for non-zero exit on unformatted files, and format-on-save configuration across IDE platforms.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prettier-format-enforcement-bot/)

---
title: "Prettier Format Enforcement Bot"
description: "The Prettier Format Enforcement Bot skill uses the Prettier Node.js API (prettier.format(), prettier.check(), prettier.resolveConfig()) and CLI (npx prettier –check, npx prettier –write) to enforce consistent code formatting across projects. It supports JavaScript, TypeScript, CSS, SCSS, HTML, JSON, YAML, Markdown, GraphQL, and 10+ additional languages through parser plugins.\nThe skill manages .prettierrc configuration files (JSON, YAML, TOML, or JS formats) with options including printWidth, tabWidth, useTabs, semi, singleQuote, trailingComma, bracketSpacing, arrowParens, and endOfLine. It handles .prettierignore for excluding files and directories from formatting enforcement.\nAdvanced capabilities include plugin integration with prettier-plugin-organize-imports for import sorting, prettier-plugin-tailwindcss for Tailwind class ordering, prettier-plugin-sql for SQL formatting, and @prettier/plugin-xml for XML documents. The bot supports editor integration configuration for VS Code (editor.defaultFormatter, editor.formatOnSave), pre-commit hook setup via husky and lint-staged, CI check mode with –check flag for non-zero exit on unformatted files, and format-on-save configuration across IDE platforms."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prettier-format-enforcement-bot/"
framework:
  - "Claude Code"
---

# Prettier Format Enforcement Bot

The Prettier Format Enforcement Bot skill uses the Prettier Node.js API (prettier.format(), prettier.check(), prettier.resolveConfig()) and CLI (npx prettier –check, npx prettier –write) to enforce consistent code formatting across projects. It supports JavaScript, TypeScript, CSS, SCSS, HTML, JSON, YAML, Markdown, GraphQL, and 10+ additional languages through parser plugins.
The skill manages .prettierrc configuration files (JSON, YAML, TOML, or JS formats) with options including printWidth, tabWidth, useTabs, semi, singleQuote, trailingComma, bracketSpacing, arrowParens, and endOfLine. It handles .prettierignore for excluding files and directories from formatting enforcement.
Advanced capabilities include plugin integration with prettier-plugin-organize-imports for import sorting, prettier-plugin-tailwindcss for Tailwind class ordering, prettier-plugin-sql for SQL formatting, and @prettier/plugin-xml for XML documents. The bot supports editor integration configuration for VS Code (editor.defaultFormatter, editor.formatOnSave), pre-commit hook setup via husky and lint-staged, CI check mode with –check flag for non-zero exit on unformatted files, and format-on-save configuration across IDE platforms.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prettier-format-enforcement-bot
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prettier-format-enforcement-bot` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prettier-format-enforcement-bot/)

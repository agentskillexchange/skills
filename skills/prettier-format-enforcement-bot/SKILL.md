---
title: "Prettier Format Enforcement Bot"
description: "Enforces code formatting standards using the Prettier API (prettier.format(), prettier.check()) and prettier-plugin-organize-imports. Supports 20+ languages with .prettierrc configuration management."
verification: "security_reviewed"
source: "https://github.com/prettier/prettier"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "prettier/prettier"
  github_stars: 51820
  npm_package: "prettier"
  npm_weekly_downloads: 90506007
---

# Prettier Format Enforcement Bot

The Prettier Format Enforcement Bot skill uses the Prettier Node.js API (prettier.format(), prettier.check(), prettier.resolveConfig()) and CLI (npx prettier –check, npx prettier –write) to enforce consistent code formatting across projects. It supports JavaScript, TypeScript, CSS, SCSS, HTML, JSON, YAML, Markdown, GraphQL, and 10+ additional languages through parser plugins.

The skill manages .prettierrc configuration files (JSON, YAML, TOML, or JS formats) with options including printWidth, tabWidth, useTabs, semi, singleQuote, trailingComma, bracketSpacing, arrowParens, and endOfLine. It handles .prettierignore for excluding files and directories from formatting enforcement.

Advanced capabilities include plugin integration with prettier-plugin-organize-imports for import sorting, prettier-plugin-tailwindcss for Tailwind class ordering, prettier-plugin-sql for SQL formatting, and @prettier/plugin-xml for XML documents. The bot supports editor integration configuration for VS Code (editor.defaultFormatter, editor.formatOnSave), pre-commit hook setup via husky and lint-staged, CI check mode with –check flag for non-zero exit on unformatted files, and format-on-save configuration across IDE platforms.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prettier-format-enforcement-bot/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prettier-format-enforcement-bot
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prettier-format-enforcement-bot`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prettier-format-enforcement-bot/)

---
name: Prettier Format Enforcement Bot
description: Enforces code formatting standards using the Prettier API (prettier.format(), prettier.check()) and prettier-plugin-organize-imports. Supports 20+ languages with .prettierrc configuration management.
category: Code Quality & Review
framework: Claude Code
verification: security_reviewed
rating: 4.8
reviews: 85
source: https://agentskillexchange.com/skill/prettier-format-enforcement-bot/
---

# Prettier Format Enforcement Bot

Enforces code formatting standards using the Prettier API (prettier.format(), prettier.check()) and prettier-plugin-organize-imports. Supports 20+ languages with .prettierrc configuration management.

## Overview

The Prettier Format Enforcement Bot skill uses the Prettier Node.js API (prettier.format(), prettier.check(), prettier.resolveConfig()) and CLI (npx prettier –check, npx prettier –write) to enforce consistent code formatting across projects. It supports JavaScript, TypeScript, CSS, SCSS, HTML, JSON, YAML, Markdown, GraphQL, and 10+ additional languages through parser plugins.
The skill manages .prettierrc configuration files (JSON, YAML, TOML, or JS formats) with options including printWidth, tabWidth, useTabs, semi, singleQuote, trailingComma, bracketSpacing, arrowParens, and endOfLine. It handles .prettierignore for excluding files and directories from formatting enforcement.
Advanced capabilities include plugin integration with prettier-plugin-organize-imports for import sorting, prettier-plugin-tailwindcss for Tailwind class ordering, prettier-plugin-sql for SQL formatting, and @prettier/plugin-xml for XML documents. The bot supports editor integration configuration for VS Code (editor.defaultFormatter, editor.formatOnSave), pre-commit hook setup via husky and lint-staged, CI check mode with –check flag for non-zero exit on unformatted files, and format-on-save configuration across IDE platforms.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill prettier-format-enforcement-bot
```

### OpenClaw

```bash
openclaw install prettier-format-enforcement-bot
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Code Quality & Review |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (85 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/prettier-format-enforcement-bot/)*

---
name: "Prettier Format Enforcement Bot"
description: "Enforces code formatting standards using the Prettier API (prettier.format(), prettier.check()) and prettier-plugin-organize-imports. Supports 20+ languages with .prettierrc configuration management."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prettier-format-enforcement-bot/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20332  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Prettier Format Enforcement Bot

Enforces code formatting standards using the Prettier API (prettier.format(), prettier.check()) and prettier-plugin-organize-imports. Supports 20+ languages with .prettierrc configuration management.

## Overview

The Prettier Format Enforcement Bot skill uses the Prettier Node.js API (prettier.format(), prettier.check(), prettier.resolveConfig()) and CLI (npx prettier –check, npx prettier –write) to enforce consistent code formatting across projects. It supports JavaScript, TypeScript, CSS, SCSS, HTML, JSON, YAML, Markdown, GraphQL, and 10+ additional languages through parser plugins.

The skill manages .prettierrc configuration files (JSON, YAML, TOML, or JS formats) with options including printWidth, tabWidth, useTabs, semi, singleQuote, trailingComma, bracketSpacing, arrowParens, and endOfLine. It handles .prettierignore for excluding files and directories from formatting enforcement.

Advanced capabilities include plugin integration with prettier-plugin-organize-imports for import sorting, prettier-plugin-tailwindcss for Tailwind class ordering, prettier-plugin-sql for SQL formatting, and @prettier/plugin-xml for XML documents. The bot supports editor integration configuration for VS Code (editor.defaultFormatter, editor.formatOnSave), pre-commit hook setup via husky and lint-staged, CI check mode with –check flag for non-zero exit on unformatted files, and format-on-save configuration across IDE platforms.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prettier-format-enforcement-bot
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prettier-format-enforcement-bot -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prettier-format-enforcement-bot -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prettier-format-enforcement-bot -a codex
```

### OpenClaw

```bash
clawhub install prettier-format-enforcement-bot
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prettier-format-enforcement-bot/

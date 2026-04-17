---
title: "ESLint Rule Configurator"
description: "Generates optimized ESLint flat config files using @eslint/js, typescript-eslint, and eslint-plugin-import. Provides project-specific rule recommendations based on codebase analysis."
verification: security_reviewed
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality & Review"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
  license: "MIT"
---

# ESLint Rule Configurator

The ESLint Rule Configurator agent generates optimized ESLint configurations tailored to your specific project structure and coding patterns. It analyzes your codebase to recommend appropriate rules from @eslint/js, typescript-eslint, eslint-plugin-import, and other popular plugins.

The agent creates ESLint flat config files (eslint.config.js) following the modern configuration format, properly organizing rule sets by file patterns and project areas. It detects your project type (React, Node.js, library, monorepo) and selects appropriate presets, then fine-tunes individual rules based on static analysis of your existing code patterns to minimize initial violations while enforcing meaningful standards.

For TypeScript projects, it configures typescript-eslint with appropriate parser options, type-aware rules, and proper tsconfig references. The configurator handles eslint-plugin-import settings for path resolution including aliases, module boundaries in monorepos, and import ordering preferences. It can generate migration scripts for projects moving from .eslintrc to flat config format, mapping legacy extends and plugins to their flat config equivalents.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/eslint-rule-configurator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/eslint-rule-configurator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-configurator/)

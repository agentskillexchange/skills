---
title: "Plop.js Code Generator"
description: "Creates Plop.js generators with Handlebars templates and custom action types for scaffolding React components, API routes, and test files. Uses inquirer prompts with validation and the addMany action for batch file generation."
verification: "security_reviewed"
source: "https://github.com/plopjs/plop"
category:
  - "Templates & Workflows"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "plopjs/plop"
  github_stars: 7645
  npm_package: "plop"
  npm_weekly_downloads: 1615370
---

# Plop.js Code Generator

The Plop.js Code Generator skill builds custom code scaffolding pipelines using Plop.js with Handlebars template syntax. It creates plopfile.js configurations that define generators with interactive inquirer prompts, template actions, and custom action handlers. This skill generates Plop generators for common patterns: React component scaffolding (component file, styles, tests, stories, barrel export), Express/Fastify API route creation, Redux slice generation, and database migration file creation. Each generator uses addMany actions with glob patterns for batch file creation from template directories. Prompt configurations include input validation using regex patterns and custom validator functions, dynamic default values computed from previous answers, and conditional prompts using when predicates. The skill supports list, checkbox, confirm, and custom prompt types. Advanced features include custom Handlebars helpers for case transformations (camelCase, pascalCase, kebabCase), modify actions for appending to existing files like route registries and barrel exports, and append patterns with duplicate detection. The skill also creates shareable generator packages publishable to npm.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/plopjs-code-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/plopjs-code-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/plopjs-code-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plopjs-code-generator/)

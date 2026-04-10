---
title: "Plop.js Code Generator"
description: "Creates Plop.js generators with Handlebars templates and custom action types for scaffolding React components, API routes, and test files. Uses inquirer prompts with validation and the addMany action for batch file generation."
slug: "plopjs-code-generator"
category:
  - "Templates &amp; Workflows"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/plopjs-code-generator/"
---

# Plop.js Code Generator

Creates Plop.js generators with Handlebars templates and custom action types for scaffolding React components, API routes, and test files. Uses inquirer prompts with validation and the addMany action for batch file generation.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install plopjs-code-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Plop.js Code Generator skill builds custom code scaffolding pipelines using Plop.js with Handlebars template syntax. It creates plopfile.js configurations that define generators with interactive inquirer prompts, template actions, and custom action handlers.
This skill generates Plop generators for common patterns: React component scaffolding (component file, styles, tests, stories, barrel export), Express/Fastify API route creation, Redux slice generation, and database migration file creation. Each generator uses addMany actions with glob patterns for batch file creation from template directories.
Prompt configurations include input validation using regex patterns and custom validator functions, dynamic default values computed from previous answers, and conditional prompts using when predicates. The skill supports list, checkbox, confirm, and custom prompt types.
Advanced features include custom Handlebars helpers for case transformations (camelCase, pascalCase, kebabCase), modify actions for appending to existing files like route registries and barrel exports, and append patterns with duplicate detection. The skill also creates shareable generator packages publishable to npm.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plopjs-code-generator/)

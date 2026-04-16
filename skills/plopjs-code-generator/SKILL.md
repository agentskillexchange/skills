---
title: "Plop.js Code Generator"
description: "Creates Plop.js generators with Handlebars templates and custom action types for scaffolding React components, API routes, and test files. Uses inquirer prompts with validation and the addMany action for batch file generation."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/plopjs-code-generator/"
category:
  - "Templates &amp; Workflows"
framework:
  - "Cursor"
---

# Plop.js Code Generator

The Plop.js Code Generator skill builds custom code scaffolding pipelines using Plop.js with Handlebars template syntax. It creates plopfile.js configurations that define generators with interactive inquirer prompts, template actions, and custom action handlers.

This skill generates Plop generators for common patterns: React component scaffolding (component file, styles, tests, stories, barrel export), Express/Fastify API route creation, Redux slice generation, and database migration file creation. Each generator uses addMany actions with glob patterns for batch file creation from template directories.

Prompt configurations include input validation using regex patterns and custom validator functions, dynamic default values computed from previous answers, and conditional prompts using when predicates. The skill supports list, checkbox, confirm, and custom prompt types.

Advanced features include custom Handlebars helpers for case transformations (camelCase, pascalCase, kebabCase), modify actions for appending to existing files like route registries and barrel exports, and append patterns with duplicate detection. The skill also creates shareable generator packages publishable to npm.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plopjs-code-generator/)

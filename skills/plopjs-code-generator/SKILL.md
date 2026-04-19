---
title: "Plop.js Code Generator"
description: "The Plop.js Code Generator skill builds custom code scaffolding pipelines using Plop.js with Handlebars template syntax. It creates plopfile.js configurations that define generators with interactive inquirer prompts, template actions, and custom action handlers. This skill generates Plop generators for common patterns: React component scaffolding (component file, styles, tests, stories, barrel export), Express/Fastify API route creation, Redux slice generation, and database migration file creation. Each generator uses addMany actions with glob patterns for batch file creation from template directories. Prompt configurations include input validation using regex patterns and custom validator functions, dynamic default values computed from previous answers, and conditional prompts using when predicates. The skill supports list , checkbox , confirm , and custom prompt types. Advanced features include custom Handlebars helpers for case transformations ( camelCase , pascalCase , kebabCase ), modify actions for appending to existing files like route registries and barrel exports, and append patterns with duplicate detection. The skill also creates shareable generator packages publishable to npm."
source: "https://agentskillexchange.com/skills/plopjs-code-generator/"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Cursor"
---

# Plop.js Code Generator

The Plop.js Code Generator skill builds custom code scaffolding pipelines using Plop.js with Handlebars template syntax. It creates plopfile.js configurations that define generators with interactive inquirer prompts, template actions, and custom action handlers. This skill generates Plop generators for common patterns: React component scaffolding (component file, styles, tests, stories, barrel export), Express/Fastify API route creation, Redux slice generation, and database migration file creation. Each generator uses addMany actions with glob patterns for batch file creation from template directories. Prompt configurations include input validation using regex patterns and custom validator functions, dynamic default values computed from previous answers, and conditional prompts using when predicates. The skill supports list , checkbox , confirm , and custom prompt types. Advanced features include custom Handlebars helpers for case transformations ( camelCase , pascalCase , kebabCase ), modify actions for appending to existing files like route registries and barrel exports, and append patterns with duplicate detection. The skill also creates shareable generator packages publishable to npm.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plopjs-code-generator/)

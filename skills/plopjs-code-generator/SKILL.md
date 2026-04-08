---
title: Plop.js Code Generator
description: 'The Plop.js Code Generator skill builds custom code scaffolding pipelines
  using Plop.js with Handlebars template syntax. It creates plopfile.js configurations
  that define generators with interactive inquirer prompts, template actions, and
  custom action handlers. This skill generates Plop generators for common patterns:
  React component scaffolding (component file, styles, tests, stories, barrel export),
  Express/Fastify API route creation, Redux slice generation, and database migration
  file creation. Each generator uses addMany actions with glob patterns for batch
  file creation from template directories. Prompt configurations include input validation
  using regex patterns and custom validator functions, dynamic default values computed
  from previous answers, and conditional prompts using when predicates. The skill
  supports list , checkbox , confirm , and custom prompt types. Advanced features
  include custom Handlebars helpers for case transformations ( camelCase , pascalCase
  , kebabCase ), modify actions for appending to existing files like route registries
  and barrel exports, and append patterns with duplicate detection. The skill also
  creates shareable generator packages publishable to npm.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/plopjs-code-generator/
category:
- Templates &amp; Workflows
framework:
- Cursor
---

# Plop.js Code Generator

The Plop.js Code Generator skill builds custom code scaffolding pipelines using Plop.js with Handlebars template syntax. It creates plopfile.js configurations that define generators with interactive inquirer prompts, template actions, and custom action handlers. This skill generates Plop generators for common patterns: React component scaffolding (component file, styles, tests, stories, barrel export), Express/Fastify API route creation, Redux slice generation, and database migration file creation. Each generator uses addMany actions with glob patterns for batch file creation from template directories. Prompt configurations include input validation using regex patterns and custom validator functions, dynamic default values computed from previous answers, and conditional prompts using when predicates. The skill supports list , checkbox , confirm , and custom prompt types. Advanced features include custom Handlebars helpers for case transformations ( camelCase , pascalCase , kebabCase ), modify actions for appending to existing files like route registries and barrel exports, and append patterns with duplicate detection. The skill also creates shareable generator packages publishable to npm.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plopjs-code-generator/)

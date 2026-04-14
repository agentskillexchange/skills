---
title: "Plop.js Code Generator"
description: "Creates Plop.js generators with Handlebars templates and custom action types for scaffolding React components, API routes, and test files. Uses inquirer prompts with validation and the addMany action for batch file generation."
verification: security_reviewed
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plopjs-code-generator/)

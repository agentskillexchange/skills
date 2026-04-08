---
title: Plop.js Code Generator Orchestrator
description: The Plop.js Code Generator Orchestrator streamlines code generation workflows
  by managing Plop.js generators defined in plopfile.js. It drives the Plop programmatic
  API to execute generators with predefined or dynamic prompt answers, processing
  Handlebars templates (.hbs) through the addMany, add, modify, and append action
  types. The skill supports custom action functions for complex generation scenarios
  like AST-based code modifications using jscodeshift or babel transforms. It manages
  the Plop generator registry, allowing composition of multiple generators into sequenced
  workflows where one generator’s output feeds into the next generator’s prompts via
  the data parameter. Dynamic prompts are supported through Inquirer.js-compatible
  prompt types including list, checkbox, and recursive prompts for nested structures.
  The skill handles Handlebars helpers registration for custom template logic, partial
  templates for shared snippets, and case transformation helpers like camelCase, pascalCase,
  and kebabCase through the built-in Plop helpers API.
verification: security_reviewed
source: https://github.com/plopjs/plop
category:
- Templates &amp; Workflows
framework:
- ChatGPT Agents
tool_ecosystem:
  github_repo: plopjs/plop
  github_stars: 7636
  npm_package: plop
  npm_weekly_downloads: 1420765
---

# Plop.js Code Generator Orchestrator

The Plop.js Code Generator Orchestrator streamlines code generation workflows by managing Plop.js generators defined in plopfile.js. It drives the Plop programmatic API to execute generators with predefined or dynamic prompt answers, processing Handlebars templates (.hbs) through the addMany, add, modify, and append action types. The skill supports custom action functions for complex generation scenarios like AST-based code modifications using jscodeshift or babel transforms. It manages the Plop generator registry, allowing composition of multiple generators into sequenced workflows where one generator’s output feeds into the next generator’s prompts via the data parameter. Dynamic prompts are supported through Inquirer.js-compatible prompt types including list, checkbox, and recursive prompts for nested structures. The skill handles Handlebars helpers registration for custom template logic, partial templates for shared snippets, and case transformation helpers like camelCase, pascalCase, and kebabCase through the built-in Plop helpers API.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plopjs-code-generator-orchestrator/)

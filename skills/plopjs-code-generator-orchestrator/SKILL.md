---
name: "Plop.js Code Generator Orchestrator"
description: "Manages Plop.js micro-generators to scaffold components, modules, and boilerplate files using Handlebars templates. Drives plopfile.js configuration with custom actions and dynamic prompts."
verification: security_reviewed
source: "https://github.com/plopjs/plop"
category:
  - "Templates &amp; Workflows"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "plopjs/plop"
  github_stars: 7636
  ase_npm_package: "plop"
  npm_weekly_downloads: 1346790
---

# Plop.js Code Generator Orchestrator

The Plop.js Code Generator Orchestrator streamlines code generation workflows by managing Plop.js generators defined in plopfile.js. It drives the Plop programmatic API to execute generators with predefined or dynamic prompt answers, processing Handlebars templates (.hbs) through the addMany, add, modify, and append action types. The skill supports custom action functions for complex generation scenarios like AST-based code modifications using jscodeshift or babel transforms. It manages the Plop generator registry, allowing composition of multiple generators into sequenced workflows where one generator's output feeds into the next generator's prompts via the data parameter. Dynamic prompts are supported through Inquirer.js-compatible prompt types including list, checkbox, and recursive prompts for nested structures. The skill handles Handlebars helpers registration for custom template logic, partial templates for shared snippets, and case transformation helpers like camelCase, pascalCase, and kebabCase through the built-in Plop helpers API.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plopjs-code-generator-orchestrator/)

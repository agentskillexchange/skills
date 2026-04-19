---
title: "Plop.js Code Generator Orchestrator"
description: "The Plop.js Code Generator Orchestrator streamlines code generation workflows by managing Plop.js generators defined in plopfile.js. It drives the Plop programmatic API to execute generators with predefined or dynamic prompt answers, processing Handlebars templates (.hbs) through the addMany, add, modify, and append action types. The skill supports custom action functions for complex generation scenarios like AST-based code modifications using jscodeshift or babel transforms. It manages the Plop generator registry, allowing composition of multiple generators into sequenced workflows where one generator&#8217;s output feeds into the next generator&#8217;s prompts via the data parameter. Dynamic prompts are supported through Inquirer.js-compatible prompt types including list, checkbox, and recursive prompts for nested structures. The skill handles Handlebars helpers registration for custom template logic, partial templates for shared snippets, and case transformation helpers like camelCase, pascalCase, and kebabCase through the built-in Plop helpers API."
source: "https://github.com/plopjs/plop"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "plopjs/plop"
  github_stars: 7636
  npm_package: "plop"
  npm_weekly_downloads: 1512031
---

# Plop.js Code Generator Orchestrator

The Plop.js Code Generator Orchestrator streamlines code generation workflows by managing Plop.js generators defined in plopfile.js. It drives the Plop programmatic API to execute generators with predefined or dynamic prompt answers, processing Handlebars templates (.hbs) through the addMany, add, modify, and append action types. The skill supports custom action functions for complex generation scenarios like AST-based code modifications using jscodeshift or babel transforms. It manages the Plop generator registry, allowing composition of multiple generators into sequenced workflows where one generator&#8217;s output feeds into the next generator&#8217;s prompts via the data parameter. Dynamic prompts are supported through Inquirer.js-compatible prompt types including list, checkbox, and recursive prompts for nested structures. The skill handles Handlebars helpers registration for custom template logic, partial templates for shared snippets, and case transformation helpers like camelCase, pascalCase, and kebabCase through the built-in Plop helpers API.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plopjs-code-generator-orchestrator/)

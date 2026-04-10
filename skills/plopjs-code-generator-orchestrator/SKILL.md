---
title: "Plop.js Code Generator Orchestrator"
description: "Manages Plop.js micro-generators to scaffold components, modules, and boilerplate files using Handlebars templates. Drives plopfile.js configuration with custom actions and dynamic prompts."
slug: "plopjs-code-generator-orchestrator"
category:
  - "Templates &amp; Workflows"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://github.com/plopjs/plop"
tool_ecosystem:
  github_repo: "plopjs/plop"
  github_stars: 7636
  npm_package: "plop"
  npm_weekly_downloads: 1346790
---

# Plop.js Code Generator Orchestrator

Manages Plop.js micro-generators to scaffold components, modules, and boilerplate files using Handlebars templates. Drives plopfile.js configuration with custom actions and dynamic prompts.

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
clawhub install plopjs-code-generator-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Plop.js Code Generator Orchestrator streamlines code generation workflows by managing Plop.js generators defined in plopfile.js. It drives the Plop programmatic API to execute generators with predefined or dynamic prompt answers, processing Handlebars templates (.hbs) through the addMany, add, modify, and append action types. The skill supports custom action functions for complex generation scenarios like AST-based code modifications using jscodeshift or babel transforms. It manages the Plop generator registry, allowing composition of multiple generators into sequenced workflows where one generator’s output feeds into the next generator’s prompts via the data parameter. Dynamic prompts are supported through Inquirer.js-compatible prompt types including list, checkbox, and recursive prompts for nested structures. The skill handles Handlebars helpers registration for custom template logic, partial templates for shared snippets, and case transformation helpers like camelCase, pascalCase, and kebabCase through the built-in Plop helpers API.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plopjs-code-generator-orchestrator/)

---
name: "Plop.js Code Generator Orchestrator"
description: "Manages Plop.js micro-generators to scaffold components, modules, and boilerplate files using Handlebars templates. Drives plopfile.js configuration with custom actions and dynamic prompts."
category: "Templates &amp; Workflows"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://github.com/plopjs/plop"
tool_ecosystem:
  github_repo: "plopjs/plop"
  github_stars: 7636
  npm_package: "plop"
  npm_weekly_downloads: 1420765
---
# Plop.js Code Generator Orchestrator

Manages Plop.js micro-generators to scaffold components, modules, and boilerplate files using Handlebars templates. Drives plopfile.js configuration with custom actions and dynamic prompts.

The Plop.js Code Generator Orchestrator streamlines code generation workflows by managing Plop.js generators defined in plopfile.js. It drives the Plop programmatic API to execute generators with predefined or dynamic prompt answers, processing Handlebars templates (.hbs) through the addMany, add, modify, and append action types. The skill supports custom action functions for complex generation scenarios like AST-based code modifications using jscodeshift or babel transforms. It manages the Plop generator registry, allowing composition of multiple generators into sequenced workflows where one generator’s output feeds into the next generator’s prompts via the data parameter. Dynamic prompts are supported through Inquirer.js-compatible prompt types including list, checkbox, and recursive prompts for nested structures. The skill handles Handlebars helpers registration for custom template logic, partial templates for shared snippets, and case transformation helpers like camelCase, pascalCase, and kebabCase through the built-in Plop helpers API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill plopjs-code-generator-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill plopjs-code-generator-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill plopjs-code-generator-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill plopjs-code-generator-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install plopjs-code-generator-orchestrator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plopjs-code-generator-orchestrator/)

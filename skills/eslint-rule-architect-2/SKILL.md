---
title: "ESLint Rule Architect"
description: "The ESLint Rule Architect designs and implements custom ESLint rules for enforcing project-specific code conventions. It generates rule modules using the ESLint rule API with proper meta objects including fixable declarations, schema definitions, and message IDs for i18n support. The skill creates AST visitor functions targeting specific node types from the ESTree specification, handles scope analysis through eslint-scope, and implements auto-fix suggestions using the Fixer API. For TypeScript projects, it leverages @typescript-eslint/utils to access parserServices for type-checking rules that can inspect resolved types, call signatures, and type narrowing. Rule testing is generated using the ESLint RuleTester with comprehensive valid and invalid test cases including auto-fix verification. The architect also creates shareable config packages following the eslint-config-* naming convention with flat config (eslint.config.js) support. It handles rule composition for complex patterns using eslint-plugin-import resolvers and path alias configurations."
source: "https://github.com/eslint/eslint"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Architect

The ESLint Rule Architect designs and implements custom ESLint rules for enforcing project-specific code conventions. It generates rule modules using the ESLint rule API with proper meta objects including fixable declarations, schema definitions, and message IDs for i18n support. The skill creates AST visitor functions targeting specific node types from the ESTree specification, handles scope analysis through eslint-scope, and implements auto-fix suggestions using the Fixer API. For TypeScript projects, it leverages @typescript-eslint/utils to access parserServices for type-checking rules that can inspect resolved types, call signatures, and type narrowing. Rule testing is generated using the ESLint RuleTester with comprehensive valid and invalid test cases including auto-fix verification. The architect also creates shareable config packages following the eslint-config-* naming convention with flat config (eslint.config.js) support. It handles rule composition for complex patterns using eslint-plugin-import resolvers and path alias configurations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-architect-2/)

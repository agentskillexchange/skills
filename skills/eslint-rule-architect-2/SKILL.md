---
title: "ESLint Rule Architect"
description: "The ESLint Rule Architect designs and implements custom ESLint rules for enforcing project-specific code conventions. It generates rule modules using the ESLint rule API with proper meta objects including fixable declarations, schema definitions, and message IDs for i18n support.\nThe skill creates AST visitor functions targeting specific node types from the ESTree specification, handles scope analysis through eslint-scope, and implements auto-fix suggestions using the Fixer API. For TypeScript projects, it leverages @typescript-eslint/utils to access parserServices for type-checking rules that can inspect resolved types, call signatures, and type narrowing.\nRule testing is generated using the ESLint RuleTester with comprehensive valid and invalid test cases including auto-fix verification. The architect also creates shareable config packages following the eslint-config-* naming convention with flat config (eslint.config.js) support. It handles rule composition for complex patterns using eslint-plugin-import resolvers and path alias configurations."
verification: security_reviewed
source: "https://github.com/eslint/eslint"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  ase_npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Architect

The ESLint Rule Architect designs and implements custom ESLint rules for enforcing project-specific code conventions. It generates rule modules using the ESLint rule API with proper meta objects including fixable declarations, schema definitions, and message IDs for i18n support.
The skill creates AST visitor functions targeting specific node types from the ESTree specification, handles scope analysis through eslint-scope, and implements auto-fix suggestions using the Fixer API. For TypeScript projects, it leverages @typescript-eslint/utils to access parserServices for type-checking rules that can inspect resolved types, call signatures, and type narrowing.
Rule testing is generated using the ESLint RuleTester with comprehensive valid and invalid test cases including auto-fix verification. The architect also creates shareable config packages following the eslint-config-* naming convention with flat config (eslint.config.js) support. It handles rule composition for complex patterns using eslint-plugin-import resolvers and path alias configurations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/eslint-rule-architect-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/eslint-rule-architect-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-architect-2/)

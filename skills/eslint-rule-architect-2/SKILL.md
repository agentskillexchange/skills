---
title: ESLint Rule Architect
description: The ESLint Rule Architect designs and implements custom ESLint rules
  for enforcing project-specific code conventions. It generates rule modules using
  the ESLint rule API with proper meta objects including fixable declarations, schema
  definitions, and message IDs for i18n support. The skill creates AST visitor functions
  targeting specific node types from the ESTree specification, handles scope analysis
  through eslint-scope, and implements auto-fix suggestions using the Fixer API. For
  TypeScript projects, it leverages @typescript-eslint/utils to access parserServices
  for type-checking rules that can inspect resolved types, call signatures, and type
  narrowing. Rule testing is generated using the ESLint RuleTester with comprehensive
  valid and invalid test cases including auto-fix verification. The architect also
  creates shareable config packages following the eslint-config-* naming convention
  with flat config (eslint.config.js) support. It handles rule composition for complex
  patterns using eslint-plugin-import resolvers and path alias configurations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-rule-architect-2/
category:
- Code Quality &amp; Review
framework:
- Cursor
---

# ESLint Rule Architect

The ESLint Rule Architect designs and implements custom ESLint rules for enforcing project-specific code conventions. It generates rule modules using the ESLint rule API with proper meta objects including fixable declarations, schema definitions, and message IDs for i18n support. The skill creates AST visitor functions targeting specific node types from the ESTree specification, handles scope analysis through eslint-scope, and implements auto-fix suggestions using the Fixer API. For TypeScript projects, it leverages @typescript-eslint/utils to access parserServices for type-checking rules that can inspect resolved types, call signatures, and type narrowing. Rule testing is generated using the ESLint RuleTester with comprehensive valid and invalid test cases including auto-fix verification. The architect also creates shareable config packages following the eslint-config-* naming convention with flat config (eslint.config.js) support. It handles rule composition for complex patterns using eslint-plugin-import resolvers and path alias configurations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-architect-2/)

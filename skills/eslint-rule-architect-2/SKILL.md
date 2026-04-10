---
title: "ESLint Rule Architect"
description: "Creates custom ESLint rules and shareable configs using the ESLint RuleTester API and @typescript-eslint/utils. Generates AST visitor patterns with full TypeScript type-checking support via parserServices."
slug: "eslint-rule-architect-2"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-rule-architect-2/"
listed: true
---

# ESLint Rule Architect

Creates custom ESLint rules and shareable configs using the ESLint RuleTester API and @typescript-eslint/utils. Generates AST visitor patterns with full TypeScript type-checking support via parserServices.

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
clawhub install eslint-rule-architect-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ESLint Rule Architect designs and implements custom ESLint rules for enforcing project-specific code conventions. It generates rule modules using the ESLint rule API with proper meta objects including fixable declarations, schema definitions, and message IDs for i18n support.
The skill creates AST visitor functions targeting specific node types from the ESTree specification, handles scope analysis through eslint-scope, and implements auto-fix suggestions using the Fixer API. For TypeScript projects, it leverages @typescript-eslint/utils to access parserServices for type-checking rules that can inspect resolved types, call signatures, and type narrowing.
Rule testing is generated using the ESLint RuleTester with comprehensive valid and invalid test cases including auto-fix verification. The architect also creates shareable config packages following the eslint-config-* naming convention with flat config (eslint.config.js) support. It handles rule composition for complex patterns using eslint-plugin-import resolvers and path alias configurations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-architect-2/)

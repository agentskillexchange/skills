---
name: "ESLint Rule Architect"
description: "Creates custom ESLint rules and shareable configs using the ESLint RuleTester API and @typescript-eslint/utils. Generates AST visitor patterns with full TypeScript type-checking support via parserServices."
category: "Code Quality & Review"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-rule-architect-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Rule Architect

Creates custom ESLint rules and shareable configs using the ESLint RuleTester API and @typescript-eslint/utils. Generates AST visitor patterns with full TypeScript type-checking support via parserServices.

## Overview

The ESLint Rule Architect designs and implements custom ESLint rules for enforcing project-specific code conventions. It generates rule modules using the ESLint rule API with proper meta objects including fixable declarations, schema definitions, and message IDs for i18n support.

The skill creates AST visitor functions targeting specific node types from the ESTree specification, handles scope analysis through eslint-scope, and implements auto-fix suggestions using the Fixer API. For TypeScript projects, it leverages @typescript-eslint/utils to access parserServices for type-checking rules that can inspect resolved types, call signatures, and type narrowing.

Rule testing is generated using the ESLint RuleTester with comprehensive valid and invalid test cases including auto-fix verification. The architect also creates shareable config packages following the eslint-config-* naming convention with flat config (eslint.config.js) support. It handles rule composition for complex patterns using eslint-plugin-import resolvers and path alias configurations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-architect-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-architect-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-architect-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-architect-2 -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-architect-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-rule-architect-2/

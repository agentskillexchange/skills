---
name: "ESLint Rule Composer"
description: "Creates custom ESLint rules using the ESLint RuleTester API and AST Explorer patterns. Generates rule implementations with auto-fix suggestions based on estree node types and scope analysis."
category: "Code Quality & Review"
framework: "Custom Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-rule-composer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Rule Composer

Creates custom ESLint rules using the ESLint RuleTester API and AST Explorer patterns. Generates rule implementations with auto-fix suggestions based on estree node types and scope analysis.

## Overview

The ESLint Rule Composer skill assists in creating custom ESLint rules by leveraging the ESLint RuleTester API for test-driven rule development and AST Explorer patterns for node matching. It generates complete rule implementations including metadata, schema definitions, create functions, and auto-fix suggestions.

The skill understands the estree AST specification and can compose visitor patterns for any JavaScript or TypeScript node type. It handles complex scenarios like scope analysis using eslint-scope, type-aware rules via typescript-eslint parser services, and cross-file analysis through shared settings.

For auto-fix generation, the skill uses the ESLint Fixer API to produce safe, non-overlapping text replacements. It validates fixes against the parser to ensure they produce valid AST output and handles edge cases like comment preservation, whitespace normalization, and parenthesization requirements.

The composer generates accompanying RuleTester test suites with valid and invalid code samples, expected error messages, and fix output verification. It supports flat config format, legacy .eslintrc configurations, and shareable config packaging for npm distribution.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-composer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-composer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-composer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-composer -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-composer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-rule-composer/

---
name: "ESLint Custom Rule Builder"
description: "Scaffolds and tests custom ESLint rules using the RuleTester API and AST Explorer patterns. Generates rule documentation with fixable autofix implementations."
category: "Code Quality & Review"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-custom-rule-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Custom Rule Builder

Scaffolds and tests custom ESLint rules using the RuleTester API and AST Explorer patterns. Generates rule documentation with fixable autofix implementations.

## Overview

The ESLint Custom Rule Builder skill generates production-ready custom ESLint rules from natural language descriptions of code patterns to detect or enforce. It uses the ESLint RuleTester API for comprehensive test generation and the espree parser for AST node targeting.

The builder analyzes target code patterns using AST Explorer-compatible selectors to identify the precise node types and traversal paths needed. It generates rule implementations with proper meta objects including type, docs, fixable properties, and schema definitions for rule options. Autofix implementations use the fixer API with insertTextBefore, replaceText, and remove operations.

Test suites include valid and invalid code samples with expected error messages and fix output verification. The skill handles complex patterns including scope analysis via eslint-scope, type-aware rules using typescript-eslint parser services, and cross-file analysis through shared settings. Documentation generation produces markdown files matching the eslint-plugin-* documentation conventions with examples, options tables, and related rules sections.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-custom-rule-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-custom-rule-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-custom-rule-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-custom-rule-builder -a codex
```

### OpenClaw

```bash
clawhub install eslint-custom-rule-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-custom-rule-builder/

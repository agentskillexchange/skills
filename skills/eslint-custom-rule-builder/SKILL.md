---
name: "ESLint Custom Rule Builder"
description: "Scaffolds and tests custom ESLint rules using the RuleTester API and AST Explorer patterns. Generates rule documentation with fixable autofix implementations."
category: "Code Quality & Review"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/eslint-custom-rule-builder/"
tool_ecosystem:
  tool: eslint
  github_stars: 27185
  npm_weekly_downloads: 109028697
  github_repo: eslint/eslint
  license: MIT
  maintained: true
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

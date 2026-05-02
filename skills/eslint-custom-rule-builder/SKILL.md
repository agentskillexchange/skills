---
title: "ESLint Custom Rule Builder"
description: "Scaffolds and tests custom ESLint rules using the RuleTester API and AST Explorer patterns. Generates rule documentation with fixable autofix implementations."
verification: "security_reviewed"
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality & Review"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Custom Rule Builder

The ESLint Custom Rule Builder skill generates production-ready custom ESLint rules from natural language descriptions of code patterns to detect or enforce. It uses the ESLint RuleTester API for comprehensive test generation and the espree parser for AST node targeting.

The builder analyzes target code patterns using AST Explorer-compatible selectors to identify the precise node types and traversal paths needed. It generates rule implementations with proper meta objects including type, docs, fixable properties, and schema definitions for rule options. Autofix implementations use the fixer API with insertTextBefore, replaceText, and remove operations.

Test suites include valid and invalid code samples with expected error messages and fix output verification. The skill handles complex patterns including scope analysis via eslint-scope, type-aware rules using typescript-eslint parser services, and cross-file analysis through shared settings. Documentation generation produces markdown files matching the eslint-plugin-* documentation conventions with examples, options tables, and related rules sections.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/eslint-custom-rule-builder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/eslint-custom-rule-builder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/eslint-custom-rule-builder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-custom-rule-builder/)

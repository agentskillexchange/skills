---
title: "ESLint Custom Rule Builder"
description: "The ESLint Custom Rule Builder skill generates production-ready custom ESLint rules from natural language descriptions of code patterns to detect or enforce. It uses the ESLint RuleTester API for comprehensive test generation and the espree parser for AST node targeting. The builder analyzes target code patterns using AST Explorer-compatible selectors to identify the precise node types and traversal paths needed. It generates rule implementations with proper meta objects including type, docs, fixable properties, and schema definitions for rule options. Autofix implementations use the fixer API with insertTextBefore, replaceText, and remove operations. Test suites include valid and invalid code samples with expected error messages and fix output verification. The skill handles complex patterns including scope analysis via eslint-scope, type-aware rules using typescript-eslint parser services, and cross-file analysis through shared settings. Documentation generation produces markdown files matching the eslint-plugin-* documentation conventions with examples, options tables, and related rules sections."
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

# ESLint Custom Rule Builder

The ESLint Custom Rule Builder skill generates production-ready custom ESLint rules from natural language descriptions of code patterns to detect or enforce. It uses the ESLint RuleTester API for comprehensive test generation and the espree parser for AST node targeting. The builder analyzes target code patterns using AST Explorer-compatible selectors to identify the precise node types and traversal paths needed. It generates rule implementations with proper meta objects including type, docs, fixable properties, and schema definitions for rule options. Autofix implementations use the fixer API with insertTextBefore, replaceText, and remove operations. Test suites include valid and invalid code samples with expected error messages and fix output verification. The skill handles complex patterns including scope analysis via eslint-scope, type-aware rules using typescript-eslint parser services, and cross-file analysis through shared settings. Documentation generation produces markdown files matching the eslint-plugin-* documentation conventions with examples, options tables, and related rules sections.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-custom-rule-builder/)

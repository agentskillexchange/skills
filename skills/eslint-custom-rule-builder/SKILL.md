---
title: ESLint Custom Rule Builder
description: The ESLint Custom Rule Builder skill generates production-ready custom
  ESLint rules from natural language descriptions of code patterns to detect or enforce.
  It uses the ESLint RuleTester API for comprehensive test generation and the espree
  parser for AST node targeting. The builder analyzes target code patterns using AST
  Explorer-compatible selectors to identify the precise node types and traversal paths
  needed. It generates rule implementations with proper meta objects including type,
  docs, fixable properties, and schema definitions for rule options. Autofix implementations
  use the fixer API with insertTextBefore, replaceText, and remove operations. Test
  suites include valid and invalid code samples with expected error messages and fix
  output verification. The skill handles complex patterns including scope analysis
  via eslint-scope, type-aware rules using typescript-eslint parser services, and
  cross-file analysis through shared settings. Documentation generation produces markdown
  files matching the eslint-plugin-* documentation conventions with examples, options
  tables, and related rules sections.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-custom-rule-builder/
category:
- Code Quality &amp; Review
framework:
- Cursor
---

# ESLint Custom Rule Builder

The ESLint Custom Rule Builder skill generates production-ready custom ESLint rules from natural language descriptions of code patterns to detect or enforce. It uses the ESLint RuleTester API for comprehensive test generation and the espree parser for AST node targeting. The builder analyzes target code patterns using AST Explorer-compatible selectors to identify the precise node types and traversal paths needed. It generates rule implementations with proper meta objects including type, docs, fixable properties, and schema definitions for rule options. Autofix implementations use the fixer API with insertTextBefore, replaceText, and remove operations. Test suites include valid and invalid code samples with expected error messages and fix output verification. The skill handles complex patterns including scope analysis via eslint-scope, type-aware rules using typescript-eslint parser services, and cross-file analysis through shared settings. Documentation generation produces markdown files matching the eslint-plugin-* documentation conventions with examples, options tables, and related rules sections.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-custom-rule-builder/)

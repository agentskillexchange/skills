---
title: ESLint Rule Composer
description: The ESLint Rule Composer skill assists in creating custom ESLint rules
  by leveraging the ESLint RuleTester API for test-driven rule development and AST
  Explorer patterns for node matching. It generates complete rule implementations
  including metadata, schema definitions, create functions, and auto-fix suggestions.
  The skill understands the estree AST specification and can compose visitor patterns
  for any JavaScript or TypeScript node type. It handles complex scenarios like scope
  analysis using eslint-scope, type-aware rules via typescript-eslint parser services,
  and cross-file analysis through shared settings. For auto-fix generation, the skill
  uses the ESLint Fixer API to produce safe, non-overlapping text replacements. It
  validates fixes against the parser to ensure they produce valid AST output and handles
  edge cases like comment preservation, whitespace normalization, and parenthesization
  requirements. The composer generates accompanying RuleTester test suites with valid
  and invalid code samples, expected error messages, and fix output verification.
  It supports flat config format, legacy .eslintrc configurations, and shareable config
  packaging for npm distribution.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-rule-composer/
category:
- Code Quality &amp; Review
framework:
- Custom Agents
---

# ESLint Rule Composer

The ESLint Rule Composer skill assists in creating custom ESLint rules by leveraging the ESLint RuleTester API for test-driven rule development and AST Explorer patterns for node matching. It generates complete rule implementations including metadata, schema definitions, create functions, and auto-fix suggestions. The skill understands the estree AST specification and can compose visitor patterns for any JavaScript or TypeScript node type. It handles complex scenarios like scope analysis using eslint-scope, type-aware rules via typescript-eslint parser services, and cross-file analysis through shared settings. For auto-fix generation, the skill uses the ESLint Fixer API to produce safe, non-overlapping text replacements. It validates fixes against the parser to ensure they produce valid AST output and handles edge cases like comment preservation, whitespace normalization, and parenthesization requirements. The composer generates accompanying RuleTester test suites with valid and invalid code samples, expected error messages, and fix output verification. It supports flat config format, legacy .eslintrc configurations, and shareable config packaging for npm distribution.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-composer/)

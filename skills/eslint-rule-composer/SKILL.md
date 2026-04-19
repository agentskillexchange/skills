---
title: "ESLint Rule Composer"
description: "The ESLint Rule Composer skill assists in creating custom ESLint rules by leveraging the ESLint RuleTester API for test-driven rule development and AST Explorer patterns for node matching. It generates complete rule implementations including metadata, schema definitions, create functions, and auto-fix suggestions. The skill understands the estree AST specification and can compose visitor patterns for any JavaScript or TypeScript node type. It handles complex scenarios like scope analysis using eslint-scope, type-aware rules via typescript-eslint parser services, and cross-file analysis through shared settings. For auto-fix generation, the skill uses the ESLint Fixer API to produce safe, non-overlapping text replacements. It validates fixes against the parser to ensure they produce valid AST output and handles edge cases like comment preservation, whitespace normalization, and parenthesization requirements. The composer generates accompanying RuleTester test suites with valid and invalid code samples, expected error messages, and fix output verification. It supports flat config format, legacy .eslintrc configurations, and shareable config packaging for npm distribution."
source: "https://github.com/eslint/eslint"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Composer

The ESLint Rule Composer skill assists in creating custom ESLint rules by leveraging the ESLint RuleTester API for test-driven rule development and AST Explorer patterns for node matching. It generates complete rule implementations including metadata, schema definitions, create functions, and auto-fix suggestions. The skill understands the estree AST specification and can compose visitor patterns for any JavaScript or TypeScript node type. It handles complex scenarios like scope analysis using eslint-scope, type-aware rules via typescript-eslint parser services, and cross-file analysis through shared settings. For auto-fix generation, the skill uses the ESLint Fixer API to produce safe, non-overlapping text replacements. It validates fixes against the parser to ensure they produce valid AST output and handles edge cases like comment preservation, whitespace normalization, and parenthesization requirements. The composer generates accompanying RuleTester test suites with valid and invalid code samples, expected error messages, and fix output verification. It supports flat config format, legacy .eslintrc configurations, and shareable config packaging for npm distribution.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-composer/)

---
title: "ESLint Rule Composer"
description: "Creates custom ESLint rules using the ESLint RuleTester API and AST Explorer patterns. Generates rule implementations with auto-fix suggestions based on estree node types and scope analysis."
verification: security_reviewed
source: "https://github.com/eslint/eslint"
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

The ESLint Rule Composer skill assists in creating custom ESLint rules by leveraging the ESLint RuleTester API for test-driven rule development and AST Explorer patterns for node matching. It generates complete rule implementations including metadata, schema definitions, create functions, and auto-fix suggestions.

The skill understands the estree AST specification and can compose visitor patterns for any JavaScript or TypeScript node type. It handles complex scenarios like scope analysis using eslint-scope, type-aware rules via typescript-eslint parser services, and cross-file analysis through shared settings.

For auto-fix generation, the skill uses the ESLint Fixer API to produce safe, non-overlapping text replacements. It validates fixes against the parser to ensure they produce valid AST output and handles edge cases like comment preservation, whitespace normalization, and parenthesization requirements.

The composer generates accompanying RuleTester test suites with valid and invalid code samples, expected error messages, and fix output verification. It supports flat config format, legacy .eslintrc configurations, and shareable config packaging for npm distribution.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-composer/)

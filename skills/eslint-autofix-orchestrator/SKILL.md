---
title: ESLint Auto-Fix Orchestrator
description: The ESLint Auto-Fix Orchestrator leverages the ESLint Node.js API (new
  ESLint(), lintFiles(), outputFixes()) to perform automated code linting and fixing
  across JavaScript and TypeScript codebases. It works with both legacy .eslintrc
  and modern flat config (eslint.config.js) formats. The agent scans project files,
  identifies fixable violations, and applies safe auto-fixes while preserving code
  semantics. It integrates typescript-eslint parser and plugin for full TypeScript
  support, including type-aware linting rules via parserOptions.project. Prettier
  compatibility is maintained through eslint-config-prettier and eslint-plugin-prettier,
  ensuring formatting and linting rules never conflict. The agent can generate detailed
  reports in JSON, SARIF, or stylish formats for CI integration. Advanced features
  include incremental linting with cache (–cache flag), custom rule authoring support
  via RuleTester, and automatic suppression comment generation for legacy code migration.
  The agent tracks fix statistics and reports improvement trends over time.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-autofix-orchestrator/
category:
- Code Quality &amp; Review
framework:
- Claude Code
---

# ESLint Auto-Fix Orchestrator

The ESLint Auto-Fix Orchestrator leverages the ESLint Node.js API (new ESLint(), lintFiles(), outputFixes()) to perform automated code linting and fixing across JavaScript and TypeScript codebases. It works with both legacy .eslintrc and modern flat config (eslint.config.js) formats. The agent scans project files, identifies fixable violations, and applies safe auto-fixes while preserving code semantics. It integrates typescript-eslint parser and plugin for full TypeScript support, including type-aware linting rules via parserOptions.project. Prettier compatibility is maintained through eslint-config-prettier and eslint-plugin-prettier, ensuring formatting and linting rules never conflict. The agent can generate detailed reports in JSON, SARIF, or stylish formats for CI integration. Advanced features include incremental linting with cache (–cache flag), custom rule authoring support via RuleTester, and automatic suppression comment generation for legacy code migration. The agent tracks fix statistics and reports improvement trends over time.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-autofix-orchestrator/)

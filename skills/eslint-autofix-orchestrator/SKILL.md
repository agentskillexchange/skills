---
title: "ESLint Auto-Fix Orchestrator"
description: "The ESLint Auto-Fix Orchestrator leverages the ESLint Node.js API (new ESLint(), lintFiles(), outputFixes()) to perform automated code linting and fixing across JavaScript and TypeScript codebases. It works with both legacy .eslintrc and modern flat config (eslint.config.js) formats. The agent scans project files, identifies fixable violations, and applies safe auto-fixes while preserving code semantics. It integrates typescript-eslint parser and plugin for full TypeScript support, including type-aware linting rules via parserOptions.project. Prettier compatibility is maintained through eslint-config-prettier and eslint-plugin-prettier, ensuring formatting and linting rules never conflict. The agent can generate detailed reports in JSON, SARIF, or stylish formats for CI integration. Advanced features include incremental linting with cache (&#8211;cache flag), custom rule authoring support via RuleTester, and automatic suppression comment generation for legacy code migration. The agent tracks fix statistics and reports improvement trends over time."
source: "https://github.com/eslint/eslint"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Auto-Fix Orchestrator

The ESLint Auto-Fix Orchestrator leverages the ESLint Node.js API (new ESLint(), lintFiles(), outputFixes()) to perform automated code linting and fixing across JavaScript and TypeScript codebases. It works with both legacy .eslintrc and modern flat config (eslint.config.js) formats. The agent scans project files, identifies fixable violations, and applies safe auto-fixes while preserving code semantics. It integrates typescript-eslint parser and plugin for full TypeScript support, including type-aware linting rules via parserOptions.project. Prettier compatibility is maintained through eslint-config-prettier and eslint-plugin-prettier, ensuring formatting and linting rules never conflict. The agent can generate detailed reports in JSON, SARIF, or stylish formats for CI integration. Advanced features include incremental linting with cache (&#8211;cache flag), custom rule authoring support via RuleTester, and automatic suppression comment generation for legacy code migration. The agent tracks fix statistics and reports improvement trends over time.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-autofix-orchestrator/)

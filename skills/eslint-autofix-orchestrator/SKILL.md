---
name: ESLint Auto-Fix Orchestrator
description: Runs ESLint with auto-fix capabilities using the ESLint Node.js API and
  flat config system. Supports custom rule sets, TypeScript via typescript-eslint,
  and Prettier integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-autofix-orchestrator/
category:
- Code Quality &amp; Review
framework:
- Claude Code
---
# ESLint Auto-Fix Orchestrator

The ESLint Auto-Fix Orchestrator leverages the ESLint Node.js API (new ESLint(), lintFiles(), outputFixes()) to perform automated code linting and fixing across JavaScript and TypeScript codebases. It works with both legacy .eslintrc and modern flat config (eslint.config.js) formats.
The agent scans project files, identifies fixable violations, and applies safe auto-fixes while preserving code semantics. It integrates typescript-eslint parser and plugin for full TypeScript support, including type-aware linting rules via parserOptions.project.
Prettier compatibility is maintained through eslint-config-prettier and eslint-plugin-prettier, ensuring formatting and linting rules never conflict. The agent can generate detailed reports in JSON, SARIF, or stylish formats for CI integration.
Advanced features include incremental linting with cache (-cache flag), custom rule authoring support via RuleTester, and automatic suppression comment generation for legacy code migration. The agent tracks fix statistics and reports improvement trends over time.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-autofix-orchestrator/)

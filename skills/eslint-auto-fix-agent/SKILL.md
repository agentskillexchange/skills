---
title: ESLint Auto-Fix Agent
description: The ESLint Auto-Fix Agent skill provides automated code quality enforcement
  for JavaScript and TypeScript projects using ESLint v9 with the new flat config
  system (eslint.config.js). It utilizes the ESLint Node.js API (new ESLint(), lintFiles(),
  outputFixes()) to programmatically scan source files, apply auto-fixable corrections,
  and generate detailed reports. The skill integrates with lint-staged and husky for
  pre-commit hook workflows, ensuring only staged files are processed. It supports
  popular plugin ecosystems including @typescript-eslint/parser, eslint-plugin-react,
  eslint-plugin-import, and eslint-plugin-prettier. Configuration management handles
  extending shared configs like eslint-config-airbnb-base and eslint-config-standard.
  The agent can diff before/after states, categorize unfixable issues by rule ID,
  and suggest manual fixes based on rule documentation URLs. It also supports suppression
  comments generation and inline disable directives for acknowledged technical debt.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-auto-fix-agent/
category:
- Code Quality &amp; Review
framework:
- Claude Code
---

# ESLint Auto-Fix Agent

The ESLint Auto-Fix Agent skill provides automated code quality enforcement for JavaScript and TypeScript projects using ESLint v9 with the new flat config system (eslint.config.js). It utilizes the ESLint Node.js API (new ESLint(), lintFiles(), outputFixes()) to programmatically scan source files, apply auto-fixable corrections, and generate detailed reports. The skill integrates with lint-staged and husky for pre-commit hook workflows, ensuring only staged files are processed. It supports popular plugin ecosystems including @typescript-eslint/parser, eslint-plugin-react, eslint-plugin-import, and eslint-plugin-prettier. Configuration management handles extending shared configs like eslint-config-airbnb-base and eslint-config-standard. The agent can diff before/after states, categorize unfixable issues by rule ID, and suggest manual fixes based on rule documentation URLs. It also supports suppression comments generation and inline disable directives for acknowledged technical debt.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-auto-fix-agent/)

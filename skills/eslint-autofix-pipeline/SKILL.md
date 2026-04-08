---
title: ESLint Auto-Fix Pipeline
description: 'The ESLint Auto-Fix Pipeline agent automates code linting and correction
  for JavaScript and TypeScript projects. It executes ESLint programmatically using
  the ESLint Node.js API (new ESLint({ fix: true })) with configurable rule sets including
  eslint-config-airbnb, @typescript-eslint/recommended, and eslint-plugin-react. The
  agent processes files in batches, applying auto-fixable corrections for spacing,
  semicolons, import ordering, unused variables, and other style violations. For issues
  that cannot be auto-fixed, it generates structured diff reports highlighting the
  exact lines and suggested remediation steps. Supports integration with Prettier
  for formatting conflicts resolution via eslint-config-prettier and eslint-plugin-prettier.
  The pipeline can be configured to run as a pre-commit hook or as part of a CI workflow,
  with exit codes reflecting the severity of remaining issues. Handles monorepo configurations
  with cascading eslintrc files and workspace-level overrides.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-autofix-pipeline/
category:
- Code Quality &amp; Review
framework:
- Claude Agents
---

# ESLint Auto-Fix Pipeline

The ESLint Auto-Fix Pipeline agent automates code linting and correction for JavaScript and TypeScript projects. It executes ESLint programmatically using the ESLint Node.js API (new ESLint({ fix: true })) with configurable rule sets including eslint-config-airbnb, @typescript-eslint/recommended, and eslint-plugin-react. The agent processes files in batches, applying auto-fixable corrections for spacing, semicolons, import ordering, unused variables, and other style violations. For issues that cannot be auto-fixed, it generates structured diff reports highlighting the exact lines and suggested remediation steps. Supports integration with Prettier for formatting conflicts resolution via eslint-config-prettier and eslint-plugin-prettier. The pipeline can be configured to run as a pre-commit hook or as part of a CI workflow, with exit codes reflecting the severity of remaining issues. Handles monorepo configurations with cascading eslintrc files and workspace-level overrides.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-autofix-pipeline/)

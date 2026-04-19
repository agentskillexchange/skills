---
title: "ESLint Auto-Fix Pipeline"
description: "The ESLint Auto-Fix Pipeline agent automates code linting and correction for JavaScript and TypeScript projects. It executes ESLint programmatically using the ESLint Node.js API (new ESLint({ fix: true })) with configurable rule sets including eslint-config-airbnb, @typescript-eslint/recommended, and eslint-plugin-react. The agent processes files in batches, applying auto-fixable corrections for spacing, semicolons, import ordering, unused variables, and other style violations. For issues that cannot be auto-fixed, it generates structured diff reports highlighting the exact lines and suggested remediation steps. Supports integration with Prettier for formatting conflicts resolution via eslint-config-prettier and eslint-plugin-prettier. The pipeline can be configured to run as a pre-commit hook or as part of a CI workflow, with exit codes reflecting the severity of remaining issues. Handles monorepo configurations with cascading eslintrc files and workspace-level overrides."
source: "https://github.com/eslint/eslint"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Auto-Fix Pipeline

The ESLint Auto-Fix Pipeline agent automates code linting and correction for JavaScript and TypeScript projects. It executes ESLint programmatically using the ESLint Node.js API (new ESLint({ fix: true })) with configurable rule sets including eslint-config-airbnb, @typescript-eslint/recommended, and eslint-plugin-react. The agent processes files in batches, applying auto-fixable corrections for spacing, semicolons, import ordering, unused variables, and other style violations. For issues that cannot be auto-fixed, it generates structured diff reports highlighting the exact lines and suggested remediation steps. Supports integration with Prettier for formatting conflicts resolution via eslint-config-prettier and eslint-plugin-prettier. The pipeline can be configured to run as a pre-commit hook or as part of a CI workflow, with exit codes reflecting the severity of remaining issues. Handles monorepo configurations with cascading eslintrc files and workspace-level overrides.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-autofix-pipeline/)

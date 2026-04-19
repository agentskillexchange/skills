---
title: "ESLint Config Enforcer"
description: "ESLint Config Enforcer ensures coding standards remain consistent across every package in a monorepo by leveraging eslint-config-inspector and ESLint&#8217;s flat config system. How It Works The skill scans all workspace packages for their ESLint configurations, merges them using the flat config cascade, and identifies rule conflicts or overrides that deviate from the shared baseline. It uses eslint &#8211;inspect-config to produce a detailed report of active rules per package. Key Features Automatic detection of conflicting rules between @eslint/js, typescript-eslint, and custom shared configs Generates override files that resolve conflicts while preserving intentional per-package customizations Compliance dashboard showing rule coverage and deviation percentages across all packages Supports eslint.config.mjs, eslint.config.ts, and legacy .eslintrc migration paths Integration Works with npm, pnpm, and Yarn workspaces. Integrates with CI pipelines to block merges when config drift exceeds configurable thresholds. Outputs JSON reports compatible with SonarQube and CodeClimate."
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

# ESLint Config Enforcer

ESLint Config Enforcer ensures coding standards remain consistent across every package in a monorepo by leveraging eslint-config-inspector and ESLint&#8217;s flat config system. How It Works The skill scans all workspace packages for their ESLint configurations, merges them using the flat config cascade, and identifies rule conflicts or overrides that deviate from the shared baseline. It uses eslint &#8211;inspect-config to produce a detailed report of active rules per package. Key Features Automatic detection of conflicting rules between @eslint/js, typescript-eslint, and custom shared configs Generates override files that resolve conflicts while preserving intentional per-package customizations Compliance dashboard showing rule coverage and deviation percentages across all packages Supports eslint.config.mjs, eslint.config.ts, and legacy .eslintrc migration paths Integration Works with npm, pnpm, and Yarn workspaces. Integrates with CI pipelines to block merges when config drift exceeds configurable thresholds. Outputs JSON reports compatible with SonarQube and CodeClimate.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-config-enforcer/)

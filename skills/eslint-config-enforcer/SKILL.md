---
title: ESLint Config Enforcer
description: ESLint Config Enforcer ensures coding standards remain consistent across
  every package in a monorepo by leveraging eslint-config-inspector and ESLint’s flat
  config system. How It Works The skill scans all workspace packages for their ESLint
  configurations, merges them using the flat config cascade, and identifies rule conflicts
  or overrides that deviate from the shared baseline. It uses eslint –inspect-config
  to produce a detailed report of active rules per package. Key Features Automatic
  detection of conflicting rules between @eslint/js, typescript-eslint, and custom
  shared configs Generates override files that resolve conflicts while preserving
  intentional per-package customizations Compliance dashboard showing rule coverage
  and deviation percentages across all packages Supports eslint.config.mjs, eslint.config.ts,
  and legacy .eslintrc migration paths Integration Works with npm, pnpm, and Yarn
  workspaces. Integrates with CI pipelines to block merges when config drift exceeds
  configurable thresholds. Outputs JSON reports compatible with SonarQube and CodeClimate.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-config-enforcer/
category:
- Code Quality &amp; Review
framework:
- Claude Code
---

# ESLint Config Enforcer

ESLint Config Enforcer ensures coding standards remain consistent across every package in a monorepo by leveraging eslint-config-inspector and ESLint’s flat config system. How It Works The skill scans all workspace packages for their ESLint configurations, merges them using the flat config cascade, and identifies rule conflicts or overrides that deviate from the shared baseline. It uses eslint –inspect-config to produce a detailed report of active rules per package. Key Features Automatic detection of conflicting rules between @eslint/js, typescript-eslint, and custom shared configs Generates override files that resolve conflicts while preserving intentional per-package customizations Compliance dashboard showing rule coverage and deviation percentages across all packages Supports eslint.config.mjs, eslint.config.ts, and legacy .eslintrc migration paths Integration Works with npm, pnpm, and Yarn workspaces. Integrates with CI pipelines to block merges when config drift exceeds configurable thresholds. Outputs JSON reports compatible with SonarQube and CodeClimate.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-config-enforcer/)

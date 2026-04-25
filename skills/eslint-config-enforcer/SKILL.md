---
title: "ESLint Config Enforcer"
description: "Enforces consistent ESLint configurations across monorepo packages using eslint-config-inspector and flat config merging. Detects rule conflicts between shared configs, auto-generates override files, and reports compliance gaps via eslint –inspect-config."
verification: "security_reviewed"
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Config Enforcer

ESLint Config Enforcer ensures coding standards remain consistent across every package in a monorepo by leveraging eslint-config-inspector and ESLint’s flat config system. How It Works The skill scans all workspace packages for their ESLint configurations, merges them using the flat config cascade, and identifies rule conflicts or overrides that deviate from the shared baseline. It uses eslint –inspect-config to produce a detailed report of active rules per package. Key Features Automatic detection of conflicting rules between @eslint/js, typescript-eslint, and custom shared configs Generates override files that resolve conflicts while preserving intentional per-package customizations Compliance dashboard showing rule coverage and deviation percentages across all packages Supports eslint.config.mjs, eslint.config.ts, and legacy .eslintrc migration paths Integration Works with npm, pnpm, and Yarn workspaces. Integrates with CI pipelines to block merges when config drift exceeds configurable thresholds. Outputs JSON reports compatible with SonarQube and CodeClimate.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/eslint-config-enforcer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/eslint-config-enforcer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/eslint-config-enforcer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-config-enforcer/)

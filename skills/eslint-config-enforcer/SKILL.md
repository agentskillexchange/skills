---
name: "ESLint Config Enforcer"
description: "Enforces consistent ESLint configurations across monorepo packages using eslint-config-inspector and flat config merging. Detects rule conflicts between shared configs, auto-generates override files, and reports compliance gaps via eslint –inspect-config."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-config-enforcer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Config Enforcer

Enforces consistent ESLint configurations across monorepo packages using eslint-config-inspector and flat config merging. Detects rule conflicts between shared configs, auto-generates override files, and reports compliance gaps via eslint –inspect-config.

## Overview

ESLint Config Enforcer ensures coding standards remain consistent across every package in a monorepo by leveraging eslint-config-inspector and ESLint’s flat config system.

How It Works

The skill scans all workspace packages for their ESLint configurations, merges them using the flat config cascade, and identifies rule conflicts or overrides that deviate from the shared baseline. It uses eslint –inspect-config to produce a detailed report of active rules per package.

Key Features

Automatic detection of conflicting rules between @eslint/js, typescript-eslint, and custom shared configs

Generates override files that resolve conflicts while preserving intentional per-package customizations

Compliance dashboard showing rule coverage and deviation percentages across all packages

Supports eslint.config.mjs, eslint.config.ts, and legacy .eslintrc migration paths

Integration

Works with npm, pnpm, and Yarn workspaces. Integrates with CI pipelines to block merges when config drift exceeds configurable thresholds. Outputs JSON reports compatible with SonarQube and CodeClimate.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-config-enforcer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-config-enforcer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-config-enforcer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-config-enforcer -a codex
```

### OpenClaw

```bash
clawhub install eslint-config-enforcer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-config-enforcer/

---
name: ESLint Config Enforcer
description: Enforces consistent ESLint configurations across monorepo packages using eslint-config-inspector and flat config merging. Detects rule conflicts between shared configs, auto-generates override files, 
category: Code Quality & Review
framework: Claude Code
verification: security_reviewed
rating: 4.9
reviews: 79
source: https://agentskillexchange.com/skill/eslint-config-enforcer/
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

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill eslint-config-enforcer
```

### OpenClaw

```bash
openclaw install eslint-config-enforcer
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Code Quality & Review |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (79 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/eslint-config-enforcer/)*

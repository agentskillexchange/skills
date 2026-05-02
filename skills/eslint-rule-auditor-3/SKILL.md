---
title: "ESLint Rule Auditor"
description: "Audits ESLint configurations using @eslint/eslintrc and @eslint/js flat config APIs. Detects conflicting rules, deprecated configs, and generates migration paths from eslintrc to eslint.config.js flat config format."
verification: "security_reviewed"
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality & Review"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Auditor

The ESLint Rule Auditor skill performs comprehensive analysis of ESLint configurations across JavaScript and TypeScript projects. It parses both legacy eslintrc and modern flat config formats using @eslint/eslintrc and @eslint/js APIs to build a complete picture of active rules, overrides, and plugin interactions.

The skill detects common configuration issues including conflicting rules between extends chains, deprecated rule usage flagged by eslint –print-config, overlapping plugin rules from @typescript-eslint/eslint-plugin and eslint-plugin-import, and misconfigured parser options. It evaluates rule severity distributions and identifies overly permissive configurations that may miss code quality issues.

For projects still using legacy eslintrc format, the auditor generates detailed migration plans to eslint.config.js flat config, mapping each extends entry to its equivalent flat config import and converting overrides patterns to the new glob-based configuration arrays. It also benchmarks rule execution times using TIMING=1 environment variable to identify slow rules impacting CI performance, and suggests equivalent faster alternatives where available.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/eslint-rule-auditor-3/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/eslint-rule-auditor-3
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/eslint-rule-auditor-3`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-auditor-3/)

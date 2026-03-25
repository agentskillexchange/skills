---
name: "ESLint Rule Analyzer"
description: "Analyzes ESLint configurations using the ESLint Node.js API (new ESLint().calculateConfigForFile) and flat config system. Detects rule conflicts, unused rules, and generates project-specific rule recommendations from eslint-plugin-unicorn and typescript-eslint."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-rule-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Rule Analyzer

Analyzes ESLint configurations using the ESLint Node.js API (new ESLint().calculateConfigForFile) and flat config system. Detects rule conflicts, unused rules, and generates project-specific rule recommendations from eslint-plugin-unicorn and typescript-eslint.

## Overview

The ESLint Rule Analyzer skill provides deep analysis of ESLint configurations to optimize code quality rule sets. It uses the ESLint Node.js API, specifically the ESLint class constructor and calculateConfigForFile method, to resolve the effective configuration for any file path including flat config (eslint.config.js) and legacy .eslintrc formats.

The skill detects configuration issues including conflicting rules between plugins (e.g., @typescript-eslint/no-unused-vars vs no-unused-vars), rules that conflict with Prettier formatting, deprecated rules that should be migrated, and overly permissive configurations. It analyzes plugin compatibility across eslint-plugin-unicorn, eslint-plugin-import, @typescript-eslint/eslint-plugin, and eslint-plugin-react.

Configuration optimization leverages the ESLint RuleTester API to validate custom rules, analyzes fix coverage using the –fix-dry-run flag, and generates migration scripts for moving from legacy to flat config format. The skill reads shareable configs like eslint-config-airbnb and eslint-config-standard to compare rule deltas.

Advanced features include per-directory config analysis for monorepos using overrides and project references, performance profiling via TIMING=1 environment variable analysis, suppression comment auditing (eslint-disable tracking), and integration with lint-staged for pre-commit configuration generation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-analyzer -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-rule-analyzer/

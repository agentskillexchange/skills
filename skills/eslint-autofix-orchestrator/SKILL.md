---
name: "ESLint Auto-Fix Orchestrator"
description: "Runs ESLint with auto-fix capabilities using the ESLint Node.js API and flat config system. Supports custom rule sets, TypeScript via typescript-eslint, and Prettier integration."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-autofix-orchestrator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Auto-Fix Orchestrator

Runs ESLint with auto-fix capabilities using the ESLint Node.js API and flat config system. Supports custom rule sets, TypeScript via typescript-eslint, and Prettier integration.

## Overview

The ESLint Auto-Fix Orchestrator leverages the ESLint Node.js API (new ESLint(), lintFiles(), outputFixes()) to perform automated code linting and fixing across JavaScript and TypeScript codebases. It works with both legacy .eslintrc and modern flat config (eslint.config.js) formats.

The agent scans project files, identifies fixable violations, and applies safe auto-fixes while preserving code semantics. It integrates typescript-eslint parser and plugin for full TypeScript support, including type-aware linting rules via parserOptions.project.

Prettier compatibility is maintained through eslint-config-prettier and eslint-plugin-prettier, ensuring formatting and linting rules never conflict. The agent can generate detailed reports in JSON, SARIF, or stylish formats for CI integration.

Advanced features include incremental linting with cache (–cache flag), custom rule authoring support via RuleTester, and automatic suppression comment generation for legacy code migration. The agent tracks fix statistics and reports improvement trends over time.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-autofix-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-autofix-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-autofix-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-autofix-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install eslint-autofix-orchestrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-autofix-orchestrator/

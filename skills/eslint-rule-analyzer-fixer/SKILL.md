---
name: "ESLint Rule Analyzer and Fixer"
description: "Performs deep ESLint configuration analysis using the ESLint Node.js API and flat config system. Auto-fixes rule conflicts, generates shareable configs, and produces code quality trend reports."
category: "Code Quality & Review"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-rule-analyzer-fixer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27185  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Rule Analyzer and Fixer

Performs deep ESLint configuration analysis using the ESLint Node.js API and flat config system. Auto-fixes rule conflicts, generates shareable configs, and produces code quality trend reports.

## Overview

The ESLint Rule Analyzer and Fixer provides intelligent JavaScript and TypeScript code quality management through the ESLint Node.js API. It loads project configurations using the new flat config system (eslint.config.js), analyzes rule interactions to detect conflicts between extends sources, and identifies performance-heavy rules that slow linting. The skill uses the ESLint Linter API to programmatically lint files, applies auto-fixable corrections via the fix option, and generates detailed reports using custom formatters. It manages plugin resolution through the ESLint plugin system, validates custom rule implementations against the Rule API schema, and generates shareable config packages. The analyzer tracks code quality metrics over time using git-aware file selection, produces trend reports showing issue density by category (errors, warnings, formatting, logic), and identifies hot-spot files that consistently trigger the most violations. It also integrates with editor configurations to synchronize ESLint settings across VS Code, WebStorm, and Neovim, manages override blocks for test files and configuration files, and recommends progressive rule adoption strategies for legacy codebases migrating to stricter standards.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-analyzer-fixer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-analyzer-fixer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-analyzer-fixer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-analyzer-fixer -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-analyzer-fixer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-rule-analyzer-fixer/

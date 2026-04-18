---
title: "ESLint Auto-Fix Orchestrator"
description: "Runs ESLint with auto-fix capabilities using the ESLint Node.js API and flat config system. Supports custom rule sets, TypeScript via typescript-eslint, and Prettier integration."
verification: security_reviewed
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  ase_npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Auto-Fix Orchestrator

The ESLint Auto-Fix Orchestrator leverages the ESLint Node.js API (new ESLint(), lintFiles(), outputFixes()) to perform automated code linting and fixing across JavaScript and TypeScript codebases. It works with both legacy .eslintrc and modern flat config (eslint.config.js) formats.

The agent scans project files, identifies fixable violations, and applies safe auto-fixes while preserving code semantics. It integrates typescript-eslint parser and plugin for full TypeScript support, including type-aware linting rules via parserOptions.project.

Prettier compatibility is maintained through eslint-config-prettier and eslint-plugin-prettier, ensuring formatting and linting rules never conflict. The agent can generate detailed reports in JSON, SARIF, or stylish formats for CI integration.

Advanced features include incremental linting with cache (–cache flag), custom rule authoring support via RuleTester, and automatic suppression comment generation for legacy code migration. The agent tracks fix statistics and reports improvement trends over time.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/eslint-autofix-orchestrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/eslint-autofix-orchestrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-autofix-orchestrator/)

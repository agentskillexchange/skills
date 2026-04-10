---
title: "ESLint Auto-Fix Orchestrator"
description: "Runs ESLint with auto-fix capabilities using the ESLint Node.js API and flat config system. Supports custom rule sets, TypeScript via typescript-eslint, and Prettier integration."
slug: "eslint-autofix-orchestrator"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-autofix-orchestrator/"
---

# ESLint Auto-Fix Orchestrator

Runs ESLint with auto-fix capabilities using the ESLint Node.js API and flat config system. Supports custom rule sets, TypeScript via typescript-eslint, and Prettier integration.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install eslint-autofix-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ESLint Auto-Fix Orchestrator leverages the ESLint Node.js API (new ESLint(), lintFiles(), outputFixes()) to perform automated code linting and fixing across JavaScript and TypeScript codebases. It works with both legacy .eslintrc and modern flat config (eslint.config.js) formats.
The agent scans project files, identifies fixable violations, and applies safe auto-fixes while preserving code semantics. It integrates typescript-eslint parser and plugin for full TypeScript support, including type-aware linting rules via parserOptions.project.
Prettier compatibility is maintained through eslint-config-prettier and eslint-plugin-prettier, ensuring formatting and linting rules never conflict. The agent can generate detailed reports in JSON, SARIF, or stylish formats for CI integration.
Advanced features include incremental linting with cache (–cache flag), custom rule authoring support via RuleTester, and automatic suppression comment generation for legacy code migration. The agent tracks fix statistics and reports improvement trends over time.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-autofix-orchestrator/)

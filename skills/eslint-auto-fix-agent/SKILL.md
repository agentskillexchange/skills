---
name: "ESLint Auto-Fix Agent"
description: "Automatically detect and fix JavaScript/TypeScript linting issues using ESLint v9 flat config and the ESLint Node.js API. Supports custom rule configurations and staged file processing with lint-staged."
category: "Code Quality & Review"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-auto-fix-agent/"
tool_ecosystem:
  tool: eslint
  github_stars: 27185
  npm_weekly_downloads: 109028697
  github_repo: eslint/eslint
  license: MIT
  maintained: true
---

# ESLint Auto-Fix Agent

Automatically detect and fix JavaScript/TypeScript linting issues using ESLint v9 flat config and the ESLint Node.js API. Supports custom rule configurations and staged file processing with lint-staged.

## Overview

The ESLint Auto-Fix Agent skill provides automated code quality enforcement for JavaScript and TypeScript projects using ESLint v9 with the new flat config system (eslint.config.js). It utilizes the ESLint Node.js API (new ESLint(), lintFiles(), outputFixes()) to programmatically scan source files, apply auto-fixable corrections, and generate detailed reports. The skill integrates with lint-staged and husky for pre-commit hook workflows, ensuring only staged files are processed. It supports popular plugin ecosystems including @typescript-eslint/parser, eslint-plugin-react, eslint-plugin-import, and eslint-plugin-prettier. Configuration management handles extending shared configs like eslint-config-airbnb-base and eslint-config-standard. The agent can diff before/after states, categorize unfixable issues by rule ID, and suggest manual fixes based on rule documentation URLs. It also supports suppression comments generation and inline disable directives for acknowledged technical debt.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-auto-fix-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-auto-fix-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-auto-fix-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-auto-fix-agent -a codex
```

### OpenClaw

```bash
clawhub install eslint-auto-fix-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-auto-fix-agent/

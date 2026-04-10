---
title: "ESLint Auto-Fix Agent"
description: "Automatically detect and fix JavaScript/TypeScript linting issues using ESLint v9 flat config and the ESLint Node.js API. Supports custom rule configurations and staged file processing with lint-staged."
slug: "eslint-auto-fix-agent"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-auto-fix-agent/"
---

# ESLint Auto-Fix Agent

Automatically detect and fix JavaScript/TypeScript linting issues using ESLint v9 flat config and the ESLint Node.js API. Supports custom rule configurations and staged file processing with lint-staged.

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
clawhub install eslint-auto-fix-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ESLint Auto-Fix Agent skill provides automated code quality enforcement for JavaScript and TypeScript projects using ESLint v9 with the new flat config system (eslint.config.js). It utilizes the ESLint Node.js API (new ESLint(), lintFiles(), outputFixes()) to programmatically scan source files, apply auto-fixable corrections, and generate detailed reports. The skill integrates with lint-staged and husky for pre-commit hook workflows, ensuring only staged files are processed. It supports popular plugin ecosystems including @typescript-eslint/parser, eslint-plugin-react, eslint-plugin-import, and eslint-plugin-prettier. Configuration management handles extending shared configs like eslint-config-airbnb-base and eslint-config-standard. The agent can diff before/after states, categorize unfixable issues by rule ID, and suggest manual fixes based on rule documentation URLs. It also supports suppression comments generation and inline disable directives for acknowledged technical debt.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-auto-fix-agent/)

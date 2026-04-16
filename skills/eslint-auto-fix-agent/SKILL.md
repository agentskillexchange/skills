---
title: "ESLint Auto-Fix Agent"
description: "Automatically detect and fix JavaScript/TypeScript linting issues using ESLint v9 flat config and the ESLint Node.js API. Supports custom rule configurations and staged file processing with lint-staged."
verification: "security_reviewed"
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  ase_npm_package: "eslint"
  npm_weekly_downloads: 120215107
  license: "MIT"
---

# ESLint Auto-Fix Agent

The ESLint Auto-Fix Agent skill provides automated code quality enforcement for JavaScript and TypeScript projects using ESLint v9 with the new flat config system (eslint.config.js). It utilizes the ESLint Node.js API (new ESLint(), lintFiles(), outputFixes()) to programmatically scan source files, apply auto-fixable corrections, and generate detailed reports. The skill integrates with lint-staged and husky for pre-commit hook workflows, ensuring only staged files are processed. It supports popular plugin ecosystems including @typescript-eslint/parser, eslint-plugin-react, eslint-plugin-import, and eslint-plugin-prettier. Configuration management handles extending shared configs like eslint-config-airbnb-base and eslint-config-standard. The agent can diff before/after states, categorize unfixable issues by rule ID, and suggest manual fixes based on rule documentation URLs. It also supports suppression comments generation and inline disable directives for acknowledged technical debt.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-auto-fix-agent/)

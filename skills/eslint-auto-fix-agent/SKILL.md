---
name: ESLint Auto-Fix Agent
description: Automatically detect and fix JavaScript/TypeScript linting issues using
  ESLint v9 flat config and the ESLint Node.js API. Supports custom rule configurations
  and staged file processing with lint-staged.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-auto-fix-agent/
category:
- Code Quality &amp; Review
framework:
- Claude Code
---
# ESLint Auto-Fix Agent

The ESLint Auto-Fix Agent skill provides automated code quality enforcement for JavaScript and TypeScript projects using ESLint v9 with the new flat config system (eslint.config.js). It utilizes the ESLint Node.js API (new ESLint(), lintFiles(), outputFixes()) to programmatically scan source files, apply auto-fixable corrections, and generate detailed reports. The skill integrates with lint-staged and husky for pre-commit hook workflows, ensuring only staged files are processed. It supports popular plugin ecosystems including @typescript-eslint/parser, eslint-plugin-react, eslint-plugin-import, and eslint-plugin-prettier. Configuration management handles extending shared configs like eslint-config-airbnb-base and eslint-config-standard. The agent can diff before/after states, categorize unfixable issues by rule ID, and suggest manual fixes based on rule documentation URLs. It also supports suppression comments generation and inline disable directives for acknowledged technical debt.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-auto-fix-agent/)

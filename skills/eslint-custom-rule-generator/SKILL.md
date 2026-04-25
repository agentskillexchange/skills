---
title: "ESLint Custom Rule Generator"
description: "Generates custom ESLint rules from natural language descriptions using the ESLint RuleTester API and AST Explorer patterns. Produces complete rule modules with meta schemas, fixers, and comprehensive test suites."
verification: "security_reviewed"
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Custom Rule Generator

The ESLint Custom Rule Generator skill creates production-ready ESLint rules from natural language descriptions of coding patterns to enforce or forbid. It generates complete rule modules compatible with ESLint v8 and v9 flat config, including meta.schema for rule options, meta.messages for configurable error messages, and auto-fix functions using the ESLint Fixer API. The skill uses AST pattern matching based on ESTree node types (as documented on AST Explorer) to construct precise selectors for the code patterns being targeted. It handles complex scenarios like tracking variable scope across function boundaries using the eslint-scope library, detecting patterns in JSX/TSX via @typescript-eslint/parser AST extensions, and analyzing import/export relationships. Generated rules include comprehensive test suites using ESLint RuleTester with valid and invalid code examples, edge cases for commented-out code and string literals, and TypeScript-specific test cases when applicable. The skill also generates rule documentation in the standard ESLint rule doc format with correct/incorrect code examples, and can create shareable ESLint plugin packages with proper exports and peer dependency declarations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/eslint-custom-rule-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/eslint-custom-rule-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/eslint-custom-rule-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-custom-rule-generator/)

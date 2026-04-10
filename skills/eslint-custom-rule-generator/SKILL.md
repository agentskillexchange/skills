---
title: "ESLint Custom Rule Generator"
description: "Generates custom ESLint rules from natural language descriptions using the ESLint RuleTester API and AST Explorer patterns. Produces complete rule modules with meta schemas, fixers, and comprehensive test suites."
slug: "eslint-custom-rule-generator"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-custom-rule-generator/"
---

# ESLint Custom Rule Generator

Generates custom ESLint rules from natural language descriptions using the ESLint RuleTester API and AST Explorer patterns. Produces complete rule modules with meta schemas, fixers, and comprehensive test suites.

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
clawhub install eslint-custom-rule-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ESLint Custom Rule Generator skill creates production-ready ESLint rules from natural language descriptions of coding patterns to enforce or forbid. It generates complete rule modules compatible with ESLint v8 and v9 flat config, including meta.schema for rule options, meta.messages for configurable error messages, and auto-fix functions using the ESLint Fixer API.
The skill uses AST pattern matching based on ESTree node types (as documented on AST Explorer) to construct precise selectors for the code patterns being targeted. It handles complex scenarios like tracking variable scope across function boundaries using the eslint-scope library, detecting patterns in JSX/TSX via @typescript-eslint/parser AST extensions, and analyzing import/export relationships.
Generated rules include comprehensive test suites using ESLint RuleTester with valid and invalid code examples, edge cases for commented-out code and string literals, and TypeScript-specific test cases when applicable. The skill also generates rule documentation in the standard ESLint rule doc format with correct/incorrect code examples, and can create shareable ESLint plugin packages with proper exports and peer dependency declarations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-custom-rule-generator/)

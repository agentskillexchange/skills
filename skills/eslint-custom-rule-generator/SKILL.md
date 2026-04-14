---
title: "ESLint Custom Rule Generator"
description: "Generates custom ESLint rules from natural language descriptions using the ESLint RuleTester API and AST Explorer patterns. Produces complete rule modules with meta schemas, fixers, and comprehensive test suites."
verification: security_reviewed
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Custom Rule Generator

The ESLint Custom Rule Generator skill creates production-ready ESLint rules from natural language descriptions of coding patterns to enforce or forbid. It generates complete rule modules compatible with ESLint v8 and v9 flat config, including meta.schema for rule options, meta.messages for configurable error messages, and auto-fix functions using the ESLint Fixer API.

The skill uses AST pattern matching based on ESTree node types (as documented on AST Explorer) to construct precise selectors for the code patterns being targeted. It handles complex scenarios like tracking variable scope across function boundaries using the eslint-scope library, detecting patterns in JSX/TSX via @typescript-eslint/parser AST extensions, and analyzing import/export relationships.

Generated rules include comprehensive test suites using ESLint RuleTester with valid and invalid code examples, edge cases for commented-out code and string literals, and TypeScript-specific test cases when applicable. The skill also generates rule documentation in the standard ESLint rule doc format with correct/incorrect code examples, and can create shareable ESLint plugin packages with proper exports and peer dependency declarations.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-custom-rule-generator/)

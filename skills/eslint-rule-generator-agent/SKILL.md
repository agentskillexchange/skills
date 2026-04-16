---
title: "ESLint Rule Generator Agent"
description: "Generates custom ESLint rules from natural language descriptions using the ESLint RuleTester API and AST selectors. Integrates with typescript-eslint parser for TypeScript-aware linting."
verification: "security_reviewed"
source: "https://github.com/eslint/eslint"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  ase_npm_package: "eslint"
  npm_weekly_downloads: 120215107
  license: "MIT"
---

# ESLint Rule Generator Agent

The ESLint Rule Generator Agent automates the creation of custom ESLint rules by translating natural language specifications into valid ESLint rule definitions. It leverages the ESLint RuleTester API to validate generated rules against test cases, ensuring correctness before deployment. The agent parses JavaScript and TypeScript ASTs using espree and typescript-eslint, identifying the correct AST node types and selectors for each rule pattern. It supports auto-fixable rules with context.report() fix functions, generates comprehensive documentation with rule metadata, and can publish rules as shareable ESLint plugins via npm. The agent handles edge cases like JSX parsing, decorator support, and module vs script source types. Built for teams that need project-specific linting rules without deep AST knowledge.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-generator-agent/)

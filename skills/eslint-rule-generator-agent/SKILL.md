---
title: "ESLint Rule Generator Agent"
description: "Generates custom ESLint rules from natural language descriptions using the ESLint RuleTester API and AST selectors. Integrates with typescript-eslint parser for TypeScript-aware linting."
slug: "eslint-rule-generator-agent"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-rule-generator-agent/"
---

# ESLint Rule Generator Agent

Generates custom ESLint rules from natural language descriptions using the ESLint RuleTester API and AST selectors. Integrates with typescript-eslint parser for TypeScript-aware linting.

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
clawhub install eslint-rule-generator-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ESLint Rule Generator Agent automates the creation of custom ESLint rules by translating natural language specifications into valid ESLint rule definitions. It leverages the ESLint RuleTester API to validate generated rules against test cases, ensuring correctness before deployment. The agent parses JavaScript and TypeScript ASTs using espree and typescript-eslint, identifying the correct AST node types and selectors for each rule pattern. It supports auto-fixable rules with context.report() fix functions, generates comprehensive documentation with rule metadata, and can publish rules as shareable ESLint plugins via npm. The agent handles edge cases like JSX parsing, decorator support, and module vs script source types. Built for teams that need project-specific linting rules without deep AST knowledge.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-generator-agent/)

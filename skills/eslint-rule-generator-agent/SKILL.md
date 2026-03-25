---
name: "ESLint Rule Generator Agent"
description: "Generates custom ESLint rules from natural language descriptions using the ESLint RuleTester API and AST selectors. Integrates with typescript-eslint parser for TypeScript-aware linting."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-rule-generator-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Rule Generator Agent

Generates custom ESLint rules from natural language descriptions using the ESLint RuleTester API and AST selectors. Integrates with typescript-eslint parser for TypeScript-aware linting.

## Overview

The ESLint Rule Generator Agent automates the creation of custom ESLint rules by translating natural language specifications into valid ESLint rule definitions. It leverages the ESLint RuleTester API to validate generated rules against test cases, ensuring correctness before deployment. The agent parses JavaScript and TypeScript ASTs using espree and typescript-eslint, identifying the correct AST node types and selectors for each rule pattern. It supports auto-fixable rules with context.report() fix functions, generates comprehensive documentation with rule metadata, and can publish rules as shareable ESLint plugins via npm. The agent handles edge cases like JSX parsing, decorator support, and module vs script source types. Built for teams that need project-specific linting rules without deep AST knowledge.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-generator-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-generator-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-generator-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-generator-agent -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-generator-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-rule-generator-agent/

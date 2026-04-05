---
name: "ESLint Rule Generator Agent"
description: "Generates custom ESLint rules from natural language descriptions using the ESLint RuleTester API and AST selectors. Integrates with typescript-eslint parser for TypeScript-aware linting."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/eslint-rule-generator-agent/"
---
# ESLint Rule Generator Agent

Generates custom ESLint rules from natural language descriptions using the ESLint RuleTester API and AST selectors. Integrates with typescript-eslint parser for TypeScript-aware linting.

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

## Details

The ESLint Rule Generator Agent automates the creation of custom ESLint rules by translating natural language specifications into valid ESLint rule definitions. It leverages the ESLint RuleTester API to validate generated rules against test cases, ensuring correctness before deployment. The agent parses JavaScript and TypeScript ASTs using espree and typescript-eslint, identifying the correct AST node types and selectors for each rule pattern. It supports auto-fixable rules with context.report() fix functions, generates comprehensive documentation with rule metadata, and can publish rules as shareable ESLint plugins via npm. The agent handles edge cases like JSX parsing, decorator support, and module vs script source types. Built for teams that need project-specific linting rules without deep AST knowledge.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-generator-agent/)

---
name: ESLint Rule Conflict Resolver
description: Detects and resolves conflicting ESLint rules across .eslintrc configurations
  using the ESLint Node.js API. Analyzes rule interactions between eslint-config-airbnb,
  eslint-config-prettier, and typescript-eslint plugins.
category: "Code Quality &amp; Review"
framework: Cursor
verification: security_reviewed
source: "https://agentskillexchange.com/skills/eslint-rule-conflict-resolver/"
---
# ESLint Rule Conflict Resolver

Detects and resolves conflicting ESLint rules across .eslintrc configurations using the ESLint Node.js API. Analyzes rule interactions between eslint-config-airbnb, eslint-config-prettier, and typescript-eslint plugins.

The ESLint Rule Conflict Resolver identifies and resolves conflicting rule configurations across ESLint setup files. Using the ESLint Node.js API, it loads and merges configuration cascades from .eslintrc.js, .eslintrc.json, and flat config files to build a complete rule resolution map. The skill detects conflicts between popular config packages including eslint-config-airbnb, eslint-config-prettier, eslint-config-standard, and typescript-eslint recommended configurations. It analyzes rule severity overrides, option incompatibilities, and plugin version constraints using the eslint-plugin-import, eslint-plugin-react, and eslint-plugin-jsx-a11y APIs. The resolver generates a unified configuration that eliminates conflicts while preserving intent, with detailed explanations for each resolution decision. It supports migration from legacy .eslintrc format to the new ESLint flat config system, automatically translating extends chains into proper import statements and config arrays.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-conflict-resolver
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-conflict-resolver -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-conflict-resolver -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-conflict-resolver -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-conflict-resolver
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-conflict-resolver/)

---
title: "ESLint Rule Enforcer Agent"
description: "Runs ESLint with custom rulesets via the ESLint Node.js API and eslint-plugin-import to enforce project-specific code standards. Parses AST violations, groups by severity, and generates fix-ready patches using eslint –fix output diffs."
verification: security_reviewed
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality & Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  ase_npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Enforcer Agent

The ESLint Rule Enforcer Agent integrates directly with the ESLint Node.js API to perform deep static analysis on JavaScript and TypeScript codebases. It loads project-specific configurations from .eslintrc.json or eslint.config.mjs (flat config), applies rule overrides per directory, and leverages eslint-plugin-import for module resolution checks. The agent parses the JSON formatter output to extract violation nodes, maps them to AST locations, and groups findings by severity (error, warning, off). For auto-fixable issues, it invokes eslint –fix in dry-run mode to generate unified diff patches that can be applied via git apply. It supports custom rule authoring through the RuleContext API, enabling teams to codify domain-specific patterns. Integrates with GitHub Actions via problem matchers for inline annotations and supports caching via eslint –cache to minimize re-analysis on incremental changes.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/eslint-rule-enforcer-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/eslint-rule-enforcer-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-enforcer-agent/)

---
title: "ESLint Rule Enforcer Agent"
description: "The ESLint Rule Enforcer Agent integrates directly with the ESLint Node.js API to perform deep static analysis on JavaScript and TypeScript codebases. It loads project-specific configurations from .eslintrc.json or eslint.config.mjs (flat config), applies rule overrides per directory, and leverages eslint-plugin-import for module resolution checks. The agent parses the JSON formatter output to extract violation nodes, maps them to AST locations, and groups findings by severity (error, warning, off). For auto-fixable issues, it invokes eslint &#8211;fix in dry-run mode to generate unified diff patches that can be applied via git apply. It supports custom rule authoring through the RuleContext API, enabling teams to codify domain-specific patterns. Integrates with GitHub Actions via problem matchers for inline annotations and supports caching via eslint &#8211;cache to minimize re-analysis on incremental changes."
source: "https://github.com/eslint/eslint"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Enforcer Agent

The ESLint Rule Enforcer Agent integrates directly with the ESLint Node.js API to perform deep static analysis on JavaScript and TypeScript codebases. It loads project-specific configurations from .eslintrc.json or eslint.config.mjs (flat config), applies rule overrides per directory, and leverages eslint-plugin-import for module resolution checks. The agent parses the JSON formatter output to extract violation nodes, maps them to AST locations, and groups findings by severity (error, warning, off). For auto-fixable issues, it invokes eslint &#8211;fix in dry-run mode to generate unified diff patches that can be applied via git apply. It supports custom rule authoring through the RuleContext API, enabling teams to codify domain-specific patterns. Integrates with GitHub Actions via problem matchers for inline annotations and supports caching via eslint &#8211;cache to minimize re-analysis on incremental changes.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-enforcer-agent/)

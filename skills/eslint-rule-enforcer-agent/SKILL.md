---
title: ESLint Rule Enforcer Agent
description: The ESLint Rule Enforcer Agent integrates directly with the ESLint Node.js
  API to perform deep static analysis on JavaScript and TypeScript codebases. It loads
  project-specific configurations from .eslintrc.json or eslint.config.mjs (flat config),
  applies rule overrides per directory, and leverages eslint-plugin-import for module
  resolution checks. The agent parses the JSON formatter output to extract violation
  nodes, maps them to AST locations, and groups findings by severity (error, warning,
  off). For auto-fixable issues, it invokes eslint –fix in dry-run mode to generate
  unified diff patches that can be applied via git apply. It supports custom rule
  authoring through the RuleContext API, enabling teams to codify domain-specific
  patterns. Integrates with GitHub Actions via problem matchers for inline annotations
  and supports caching via eslint –cache to minimize re-analysis on incremental changes.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-rule-enforcer-agent/
category:
- Code Quality &amp; Review
framework:
- OpenClaw
---

# ESLint Rule Enforcer Agent

The ESLint Rule Enforcer Agent integrates directly with the ESLint Node.js API to perform deep static analysis on JavaScript and TypeScript codebases. It loads project-specific configurations from .eslintrc.json or eslint.config.mjs (flat config), applies rule overrides per directory, and leverages eslint-plugin-import for module resolution checks. The agent parses the JSON formatter output to extract violation nodes, maps them to AST locations, and groups findings by severity (error, warning, off). For auto-fixable issues, it invokes eslint –fix in dry-run mode to generate unified diff patches that can be applied via git apply. It supports custom rule authoring through the RuleContext API, enabling teams to codify domain-specific patterns. Integrates with GitHub Actions via problem matchers for inline annotations and supports caching via eslint –cache to minimize re-analysis on incremental changes.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-enforcer-agent/)

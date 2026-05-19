---
name: "ESLint Config Enforcer"
slug: "eslint-config-enforcer"
description: "Enforces consistent ESLint configurations across monorepo packages using eslint-config-inspector and flat config merging. Detects rule conflicts between shared configs, auto-generates override files, and reports compliance gaps via eslint --inspect-config."
github_stars: 27188
verification: "security_reviewed"
source: "https://github.com/eslint/eslint"
category: "Code Quality & Review"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Config Enforcer

Enforces consistent ESLint configurations across monorepo packages using eslint-config-inspector and flat config merging. Detects rule conflicts between shared configs, auto-generates override files, and reports compliance gaps via eslint --inspect-config.

## Installation

Use the upstream install or setup path that matches your environment:
- npm init @eslint/config@latest
- npx eslint yourfile.js

Requirements and caveats from upstream:
- To use ESLint, you must have [Node.js](https://nodejs.org/) (^20.19.0, ^22.13.0, or >=24) installed and built with SSL support. (If you are using an official Node.js distribution, SSL is always built in.)
- node-linker=hoisted
- ### Which Node.js versions does ESLint support?

Basic usage or getting-started notes:
- [Installation and Usage](#installation-and-usage)
- If you use ESLint's TypeScript type definitions, TypeScript 5.3 or later is required.
- ### npm Installation

- Source: https://github.com/eslint/eslint
- Extracted from upstream docs: https://raw.githubusercontent.com/eslint/eslint/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-config-enforcer/)

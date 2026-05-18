---
name: "ESLint Auto-Fix Pipeline"
slug: "eslint-autofix-pipeline"
description: "Runs ESLint with the --fix flag across JavaScript and TypeScript codebases, applying auto-fixable rules from eslint-config-airbnb and @typescript-eslint/recommended. Generates diff reports for manual review of remaining issues."
github_stars: 27188
verification: "security_reviewed"
source: "https://github.com/eslint/eslint"
category: "Code Quality & Review"
framework: "Claude Agents"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Auto-Fix Pipeline

Runs ESLint with the --fix flag across JavaScript and TypeScript codebases, applying auto-fixable rules from eslint-config-airbnb and @typescript-eslint/recommended. Generates diff reports for manual review of remaining issues.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-autofix-pipeline/)

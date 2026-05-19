---
name: "ESLint Rule Enforcer Agent"
slug: "eslint-rule-enforcer-agent"
description: "Runs ESLint with custom rulesets via the ESLint Node.js API and eslint-plugin-import to enforce project-specific code standards. Parses AST violations, groups by severity, and generates fix-ready patches using eslint --fix output diffs."
github_stars: 27188
verification: "security_reviewed"
source: "https://github.com/eslint/eslint"
category: "Code Quality & Review"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Enforcer Agent

Runs ESLint with custom rulesets via the ESLint Node.js API and eslint-plugin-import to enforce project-specific code standards. Parses AST violations, groups by severity, and generates fix-ready patches using eslint --fix output diffs.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-enforcer-agent/)

---
title: "ESLint Auto-Fixer"
description: "Applies ESLint fixes automatically using the ESLint Node.js API with flat config support. Handles rule conflicts across TypeScript-ESLint and eslint-plugin-react. Generates fix reports in SARIF format."
verification: "security_reviewed"
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  ase_npm_package: "eslint"
  npm_weekly_downloads: 120215107
  license: "MIT"
---

# ESLint Auto-Fixer

The ESLint Auto-Fixer skill leverages the ESLint Node.js API to programmatically lint and fix JavaScript and TypeScript files. It supports the new flat config format (eslint.config.js) and legacy .eslintrc configurations.

The skill loads project-specific ESLint configurations, including plugins like typescript-eslint, eslint-plugin-react, eslint-plugin-import, and eslint-plugin-prettier. It applies automatic fixes using the fix option in the ESLint API, tracking which rules were applied and which required manual intervention.

Output is available in multiple formats including stylish console output, JSON, and SARIF (Static Analysis Results Interchange Format) for integration with GitHub Code Scanning. The skill handles monorepo configurations with separate configs per package. It supports custom rule overrides via command parameters and can operate in dry-run mode to preview changes before applying them. Particularly useful for enforcing consistent code style across large codebases.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-auto-fixer/)

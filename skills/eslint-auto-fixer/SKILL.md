---
title: ESLint Auto-Fixer
description: The ESLint Auto-Fixer skill leverages the ESLint Node.js API to programmatically
  lint and fix JavaScript and TypeScript files. It supports the new flat config format
  (eslint.config.js) and legacy .eslintrc configurations. The skill loads project-specific
  ESLint configurations, including plugins like typescript-eslint, eslint-plugin-react,
  eslint-plugin-import, and eslint-plugin-prettier. It applies automatic fixes using
  the fix option in the ESLint API, tracking which rules were applied and which required
  manual intervention. Output is available in multiple formats including stylish console
  output, JSON, and SARIF (Static Analysis Results Interchange Format) for integration
  with GitHub Code Scanning. The skill handles monorepo configurations with separate
  configs per package. It supports custom rule overrides via command parameters and
  can operate in dry-run mode to preview changes before applying them. Particularly
  useful for enforcing consistent code style across large codebases.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-auto-fixer/
category:
- Code Quality &amp; Review
framework:
- OpenClaw
---

# ESLint Auto-Fixer

The ESLint Auto-Fixer skill leverages the ESLint Node.js API to programmatically lint and fix JavaScript and TypeScript files. It supports the new flat config format (eslint.config.js) and legacy .eslintrc configurations. The skill loads project-specific ESLint configurations, including plugins like typescript-eslint, eslint-plugin-react, eslint-plugin-import, and eslint-plugin-prettier. It applies automatic fixes using the fix option in the ESLint API, tracking which rules were applied and which required manual intervention. Output is available in multiple formats including stylish console output, JSON, and SARIF (Static Analysis Results Interchange Format) for integration with GitHub Code Scanning. The skill handles monorepo configurations with separate configs per package. It supports custom rule overrides via command parameters and can operate in dry-run mode to preview changes before applying them. Particularly useful for enforcing consistent code style across large codebases.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-auto-fixer/)

---
title: "ESLint Auto-Fixer"
description: "Applies ESLint fixes automatically using the ESLint Node.js API with flat config support. Handles rule conflicts across TypeScript-ESLint and eslint-plugin-react. Generates fix reports in SARIF format."
slug: "eslint-auto-fixer"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-auto-fixer/"
listed: true
---

# ESLint Auto-Fixer

Applies ESLint fixes automatically using the ESLint Node.js API with flat config support. Handles rule conflicts across TypeScript-ESLint and eslint-plugin-react. Generates fix reports in SARIF format.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install eslint-auto-fixer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ESLint Auto-Fixer skill leverages the ESLint Node.js API to programmatically lint and fix JavaScript and TypeScript files. It supports the new flat config format (eslint.config.js) and legacy .eslintrc configurations.
The skill loads project-specific ESLint configurations, including plugins like typescript-eslint, eslint-plugin-react, eslint-plugin-import, and eslint-plugin-prettier. It applies automatic fixes using the fix option in the ESLint API, tracking which rules were applied and which required manual intervention.
Output is available in multiple formats including stylish console output, JSON, and SARIF (Static Analysis Results Interchange Format) for integration with GitHub Code Scanning. The skill handles monorepo configurations with separate configs per package. It supports custom rule overrides via command parameters and can operate in dry-run mode to preview changes before applying them. Particularly useful for enforcing consistent code style across large codebases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-auto-fixer/)

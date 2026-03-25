---
name: "ESLint Auto-Fixer"
description: "Applies ESLint fixes automatically using the ESLint Node.js API with flat config support. Handles rule conflicts across TypeScript-ESLint and eslint-plugin-react. Generates fix reports in SARIF format."
category: "Code Quality & Review"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-auto-fixer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Auto-Fixer

Applies ESLint fixes automatically using the ESLint Node.js API with flat config support. Handles rule conflicts across TypeScript-ESLint and eslint-plugin-react. Generates fix reports in SARIF format.

## Overview

The ESLint Auto-Fixer skill leverages the ESLint Node.js API to programmatically lint and fix JavaScript and TypeScript files. It supports the new flat config format (eslint.config.js) and legacy .eslintrc configurations.

The skill loads project-specific ESLint configurations, including plugins like typescript-eslint, eslint-plugin-react, eslint-plugin-import, and eslint-plugin-prettier. It applies automatic fixes using the fix option in the ESLint API, tracking which rules were applied and which required manual intervention.

Output is available in multiple formats including stylish console output, JSON, and SARIF (Static Analysis Results Interchange Format) for integration with GitHub Code Scanning. The skill handles monorepo configurations with separate configs per package. It supports custom rule overrides via command parameters and can operate in dry-run mode to preview changes before applying them. Particularly useful for enforcing consistent code style across large codebases.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-auto-fixer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-auto-fixer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-auto-fixer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-auto-fixer -a codex
```

### OpenClaw

```bash
clawhub install eslint-auto-fixer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-auto-fixer/

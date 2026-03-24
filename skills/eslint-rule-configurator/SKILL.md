---
name: "ESLint Rule Configurator"
description: "Generates optimized ESLint flat config files using @eslint/js, typescript-eslint, and eslint-plugin-import. Provides project-specific rule recommendations based on codebase analysis."
category: "Code Quality & Review"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-rule-configurator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Rule Configurator

Generates optimized ESLint flat config files using @eslint/js, typescript-eslint, and eslint-plugin-import. Provides project-specific rule recommendations based on codebase analysis.

## Overview

The ESLint Rule Configurator agent generates optimized ESLint configurations tailored to your specific project structure and coding patterns. It analyzes your codebase to recommend appropriate rules from @eslint/js, typescript-eslint, eslint-plugin-import, and other popular plugins.

The agent creates ESLint flat config files (eslint.config.js) following the modern configuration format, properly organizing rule sets by file patterns and project areas. It detects your project type (React, Node.js, library, monorepo) and selects appropriate presets, then fine-tunes individual rules based on static analysis of your existing code patterns to minimize initial violations while enforcing meaningful standards.

For TypeScript projects, it configures typescript-eslint with appropriate parser options, type-aware rules, and proper tsconfig references. The configurator handles eslint-plugin-import settings for path resolution including aliases, module boundaries in monorepos, and import ordering preferences. It can generate migration scripts for projects moving from .eslintrc to flat config format, mapping legacy extends and plugins to their flat config equivalents.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-configurator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-configurator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-configurator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-configurator -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-configurator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-rule-configurator/

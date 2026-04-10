---
title: "ESLint Rule Configurator"
description: "Generates optimized ESLint flat config files using @eslint/js, typescript-eslint, and eslint-plugin-import. Provides project-specific rule recommendations based on codebase analysis."
slug: "eslint-rule-configurator"
category:
  - "Code Quality &amp; Review"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-rule-configurator/"
---

# ESLint Rule Configurator

Generates optimized ESLint flat config files using @eslint/js, typescript-eslint, and eslint-plugin-import. Provides project-specific rule recommendations based on codebase analysis.

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
clawhub install eslint-rule-configurator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ESLint Rule Configurator agent generates optimized ESLint configurations tailored to your specific project structure and coding patterns. It analyzes your codebase to recommend appropriate rules from @eslint/js, typescript-eslint, eslint-plugin-import, and other popular plugins.
The agent creates ESLint flat config files (eslint.config.js) following the modern configuration format, properly organizing rule sets by file patterns and project areas. It detects your project type (React, Node.js, library, monorepo) and selects appropriate presets, then fine-tunes individual rules based on static analysis of your existing code patterns to minimize initial violations while enforcing meaningful standards.
For TypeScript projects, it configures typescript-eslint with appropriate parser options, type-aware rules, and proper tsconfig references. The configurator handles eslint-plugin-import settings for path resolution including aliases, module boundaries in monorepos, and import ordering preferences. It can generate migration scripts for projects moving from .eslintrc to flat config format, mapping legacy extends and plugins to their flat config equivalents.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-configurator/)

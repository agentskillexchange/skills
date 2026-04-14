---
title: "ESLint Rule Configurator"
description: "Generates optimized ESLint flat config files using @eslint/js, typescript-eslint, and eslint-plugin-import. Provides project-specific rule recommendations based on codebase analysis."
verification: security_reviewed
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality &amp; Review"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Configurator

The ESLint Rule Configurator agent generates optimized ESLint configurations tailored to your specific project structure and coding patterns. It analyzes your codebase to recommend appropriate rules from @eslint/js, typescript-eslint, eslint-plugin-import, and other popular plugins.

The agent creates ESLint flat config files (eslint.config.js) following the modern configuration format, properly organizing rule sets by file patterns and project areas. It detects your project type (React, Node.js, library, monorepo) and selects appropriate presets, then fine-tunes individual rules based on static analysis of your existing code patterns to minimize initial violations while enforcing meaningful standards.

For TypeScript projects, it configures typescript-eslint with appropriate parser options, type-aware rules, and proper tsconfig references. The configurator handles eslint-plugin-import settings for path resolution including aliases, module boundaries in monorepos, and import ordering preferences. It can generate migration scripts for projects moving from .eslintrc to flat config format, mapping legacy extends and plugins to their flat config equivalents.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-configurator/)

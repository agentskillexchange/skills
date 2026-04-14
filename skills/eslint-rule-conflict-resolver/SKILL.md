---
title: "ESLint Rule Conflict Resolver"
description: "Detects and resolves conflicting ESLint rules across .eslintrc configurations using the ESLint Node.js API. Analyzes rule interactions between eslint-config-airbnb, eslint-config-prettier, and typescript-eslint plugins."
verification: security_reviewed
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Conflict Resolver

The ESLint Rule Conflict Resolver identifies and resolves conflicting rule configurations across ESLint setup files. Using the ESLint Node.js API, it loads and merges configuration cascades from .eslintrc.js, .eslintrc.json, and flat config files to build a complete rule resolution map. The skill detects conflicts between popular config packages including eslint-config-airbnb, eslint-config-prettier, eslint-config-standard, and typescript-eslint recommended configurations. It analyzes rule severity overrides, option incompatibilities, and plugin version constraints using the eslint-plugin-import, eslint-plugin-react, and eslint-plugin-jsx-a11y APIs. The resolver generates a unified configuration that eliminates conflicts while preserving intent, with detailed explanations for each resolution decision. It supports migration from legacy .eslintrc format to the new ESLint flat config system, automatically translating extends chains into proper import statements and config arrays.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-conflict-resolver/)

---
title: ESLint Rule Conflict Resolver
description: The ESLint Rule Conflict Resolver identifies and resolves conflicting
  rule configurations across ESLint setup files. Using the ESLint Node.js API, it
  loads and merges configuration cascades from .eslintrc.js, .eslintrc.json, and flat
  config files to build a complete rule resolution map. The skill detects conflicts
  between popular config packages including eslint-config-airbnb, eslint-config-prettier,
  eslint-config-standard, and typescript-eslint recommended configurations. It analyzes
  rule severity overrides, option incompatibilities, and plugin version constraints
  using the eslint-plugin-import, eslint-plugin-react, and eslint-plugin-jsx-a11y
  APIs. The resolver generates a unified configuration that eliminates conflicts while
  preserving intent, with detailed explanations for each resolution decision. It supports
  migration from legacy .eslintrc format to the new ESLint flat config system, automatically
  translating extends chains into proper import statements and config arrays.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-rule-conflict-resolver/
category:
- Code Quality &amp; Review
framework:
- Cursor
---

# ESLint Rule Conflict Resolver

The ESLint Rule Conflict Resolver identifies and resolves conflicting rule configurations across ESLint setup files. Using the ESLint Node.js API, it loads and merges configuration cascades from .eslintrc.js, .eslintrc.json, and flat config files to build a complete rule resolution map. The skill detects conflicts between popular config packages including eslint-config-airbnb, eslint-config-prettier, eslint-config-standard, and typescript-eslint recommended configurations. It analyzes rule severity overrides, option incompatibilities, and plugin version constraints using the eslint-plugin-import, eslint-plugin-react, and eslint-plugin-jsx-a11y APIs. The resolver generates a unified configuration that eliminates conflicts while preserving intent, with detailed explanations for each resolution decision. It supports migration from legacy .eslintrc format to the new ESLint flat config system, automatically translating extends chains into proper import statements and config arrays.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-conflict-resolver/)

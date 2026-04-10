---
title: "ESLint Rule Conflict Resolver"
description: "Detects and resolves conflicting ESLint rules across .eslintrc configurations using the ESLint Node.js API. Analyzes rule interactions between eslint-config-airbnb, eslint-config-prettier, and typescript-eslint plugins."
slug: "eslint-rule-conflict-resolver"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-rule-conflict-resolver/"
listed: true
---

# ESLint Rule Conflict Resolver

Detects and resolves conflicting ESLint rules across .eslintrc configurations using the ESLint Node.js API. Analyzes rule interactions between eslint-config-airbnb, eslint-config-prettier, and typescript-eslint plugins.

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
clawhub install eslint-rule-conflict-resolver
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ESLint Rule Conflict Resolver identifies and resolves conflicting rule configurations across ESLint setup files. Using the ESLint Node.js API, it loads and merges configuration cascades from .eslintrc.js, .eslintrc.json, and flat config files to build a complete rule resolution map. The skill detects conflicts between popular config packages including eslint-config-airbnb, eslint-config-prettier, eslint-config-standard, and typescript-eslint recommended configurations. It analyzes rule severity overrides, option incompatibilities, and plugin version constraints using the eslint-plugin-import, eslint-plugin-react, and eslint-plugin-jsx-a11y APIs. The resolver generates a unified configuration that eliminates conflicts while preserving intent, with detailed explanations for each resolution decision. It supports migration from legacy .eslintrc format to the new ESLint flat config system, automatically translating extends chains into proper import statements and config arrays.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-conflict-resolver/)

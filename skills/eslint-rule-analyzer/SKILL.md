---
title: "ESLint Rule Analyzer"
description: "Analyzes ESLint configurations using the ESLint Node.js API (new ESLint().calculateConfigForFile) and flat config system. Detects rule conflicts, unused rules, and generates project-specific rule recommendations from eslint-plugin-unicorn and typescript-eslint."
slug: "eslint-rule-analyzer"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-rule-analyzer/"
---

# ESLint Rule Analyzer

Analyzes ESLint configurations using the ESLint Node.js API (new ESLint().calculateConfigForFile) and flat config system. Detects rule conflicts, unused rules, and generates project-specific rule recommendations from eslint-plugin-unicorn and typescript-eslint.

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
clawhub install eslint-rule-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ESLint Rule Analyzer skill provides deep analysis of ESLint configurations to optimize code quality rule sets. It uses the ESLint Node.js API, specifically the ESLint class constructor and calculateConfigForFile method, to resolve the effective configuration for any file path including flat config (eslint.config.js) and legacy .eslintrc formats.
The skill detects configuration issues including conflicting rules between plugins (e.g., @typescript-eslint/no-unused-vars vs no-unused-vars), rules that conflict with Prettier formatting, deprecated rules that should be migrated, and overly permissive configurations. It analyzes plugin compatibility across eslint-plugin-unicorn, eslint-plugin-import, @typescript-eslint/eslint-plugin, and eslint-plugin-react.
Configuration optimization leverages the ESLint RuleTester API to validate custom rules, analyzes fix coverage using the –fix-dry-run flag, and generates migration scripts for moving from legacy to flat config format. The skill reads shareable configs like eslint-config-airbnb and eslint-config-standard to compare rule deltas.
Advanced features include per-directory config analysis for monorepos using overrides and project references, performance profiling via TIMING=1 environment variable analysis, suppression comment auditing (eslint-disable tracking), and integration with lint-staged for pre-commit configuration generation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-analyzer/)

---
name: "ESLint Rule Analyzer"
description: "Analyzes ESLint configurations using the ESLint Node.js API (new ESLint().calculateConfigForFile) and flat config system. Detects rule conflicts, unused rules, and generates project-specific rule recommendations from eslint-plugin-unicorn and typescript-eslint."
category: "Code Quality &amp; Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/eslint-rule-analyzer/"
---
# ESLint Rule Analyzer

Analyzes ESLint configurations using the ESLint Node.js API (new ESLint().calculateConfigForFile) and flat config system. Detects rule conflicts, unused rules, and generates project-specific rule recommendations from eslint-plugin-unicorn and typescript-eslint.

## Overview

The ESLint Rule Analyzer skill provides deep analysis of ESLint configurations to optimize code quality rule sets. It uses the ESLint Node.js API, specifically the ESLint class constructor and calculateConfigForFile method, to resolve the effective configuration for any file path including flat config (eslint.config.js) and legacy .eslintrc formats.

The skill detects configuration issues including conflicting rules between plugins (e.g., @typescript-eslint/no-unused-vars vs no-unused-vars), rules that conflict with Prettier formatting, deprecated rules that should be migrated, and overly permissive configurations. It analyzes plugin compatibility across eslint-plugin-unicorn, eslint-plugin-import, @typescript-eslint/eslint-plugin, and eslint-plugin-react.

Configuration optimization leverages the ESLint RuleTester API to validate custom rules, analyzes fix coverage using the -fix-dry-run flag, and generates migration scripts for moving from legacy to flat config format. The skill reads shareable configs like eslint-config-airbnb and eslint-config-standard to compare rule deltas.

Advanced features include per-directory config analysis for monorepos using overrides and project references, performance profiling via TIMING=1 environment variable analysis, suppression comment auditing (eslint-disable tracking), and integration with lint-staged for pre-commit configuration generation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-analyzer -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-analyzer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-analyzer/)

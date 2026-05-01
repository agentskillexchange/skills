---
title: "ESLint Rule Impact Analyzer"
description: "Measures the impact of enabling new ESLint rules across a codebase using the ESLint Node.js API and @typescript-eslint/parser. Generates violation heatmaps, estimates auto-fix coverage, and prioritizes rules by fix effort."
verification: "security_reviewed"
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality & Review"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Impact Analyzer

The ESLint Rule Impact Analyzer skill helps teams adopt stricter linting rules incrementally by measuring the real impact before enabling them. Using the ESLint Node.js API programmatically, it runs candidate rules against the entire codebase without modifying configuration files. For each rule, it counts violations per file, calculates auto-fix coverage using the fix metadata, and estimates manual remediation effort based on violation complexity scoring. The skill generates interactive heatmaps showing violation density across directories, helping teams identify hotspots. Supports @typescript-eslint/parser rules, eslint-plugin-react, eslint-plugin-import, and custom rule packages. Can simulate enabling multiple rules simultaneously to detect interaction effects. Outputs prioritized adoption plans as markdown or Jira tickets with per-rule effort estimates. Integrates with SonarQube for combined static analysis reporting.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/eslint-rule-impact-analyzer-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/eslint-rule-impact-analyzer-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/eslint-rule-impact-analyzer-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-impact-analyzer-2/)

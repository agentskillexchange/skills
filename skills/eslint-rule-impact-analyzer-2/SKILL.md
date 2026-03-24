---
name: "ESLint Rule Impact Analyzer"
description: "Measures the impact of enabling new ESLint rules across a codebase using the ESLint Node.js API and @typescript-eslint/parser. Generates violation heatmaps, estimates auto-fix coverage, and prioritizes rules by fix effort."
category: "Code Quality & Review"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-rule-impact-analyzer-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Rule Impact Analyzer

Measures the impact of enabling new ESLint rules across a codebase using the ESLint Node.js API and @typescript-eslint/parser. Generates violation heatmaps, estimates auto-fix coverage, and prioritizes rules by fix effort.

## Overview

The ESLint Rule Impact Analyzer skill helps teams adopt stricter linting rules incrementally by measuring the real impact before enabling them. Using the ESLint Node.js API programmatically, it runs candidate rules against the entire codebase without modifying configuration files. For each rule, it counts violations per file, calculates auto-fix coverage using the fix metadata, and estimates manual remediation effort based on violation complexity scoring. The skill generates interactive heatmaps showing violation density across directories, helping teams identify hotspots. Supports @typescript-eslint/parser rules, eslint-plugin-react, eslint-plugin-import, and custom rule packages. Can simulate enabling multiple rules simultaneously to detect interaction effects. Outputs prioritized adoption plans as markdown or Jira tickets with per-rule effort estimates. Integrates with SonarQube for combined static analysis reporting.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-impact-analyzer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-impact-analyzer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-impact-analyzer-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-impact-analyzer-2 -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-impact-analyzer-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-rule-impact-analyzer-2/

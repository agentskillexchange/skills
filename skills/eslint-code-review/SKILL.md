---
name: "ESLint Code Review"
description: "Use this skill when you need to run ESLint analysis on JavaScript or TypeScript code and get structured lint results with fix suggestions. It runs ESLint with your project config, parses the output, and presents actionable findings grouped by severity and rule."
category: "Developer Tools"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-code-review/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Code Review

Use this skill when you need to run ESLint analysis on JavaScript or TypeScript code and get structured lint results with fix suggestions. It runs ESLint with your project config, parses the output, and presents actionable findings grouped by severity and rule.

## Overview

Use this skill when you need to run ESLint analysis on JavaScript or TypeScript code and get structured lint results with fix suggestions. It runs ESLint with your project config, parses the output, and presents actionable findings grouped by severity and rule.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-code-review
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-code-review -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-code-review -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-code-review -a codex
```

### OpenClaw

```bash
clawhub install eslint-code-review
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-code-review/

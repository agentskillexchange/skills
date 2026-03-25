---
name: "ESLint Rule Violation Summarizer"
description: "Runs ESLint against a JS/TS codebase, groups violations by rule and file, and produces a prioritized fix plan. Distinguishes auto-fixable violations from manual ones. Outputs Markdown for GitHub PR comments."
category: "Code Quality & Review"
framework: "Cursor"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-rule-violation-summarizer-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ESLint Rule Violation Summarizer

Runs ESLint against a JS/TS codebase, groups violations by rule and file, and produces a prioritized fix plan. Distinguishes auto-fixable violations from manual ones. Outputs Markdown for GitHub PR comments.

## Overview

Runs ESLint against a JS/TS codebase, groups violations by rule and file, and produces a prioritized fix plan. Distinguishes auto-fixable violations from manual ones. Outputs Markdown for GitHub PR comments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-violation-summarizer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-violation-summarizer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-violation-summarizer-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-violation-summarizer-2 -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-violation-summarizer-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-rule-violation-summarizer-2/

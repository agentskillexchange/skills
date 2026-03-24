---
name: "Git Branch Analyzer"
description: "Analyzes Git repository branch topology using libgit2 bindings and git-log parsing. Identifies stale branches, merge conflicts, and divergence points via the GitHub GraphQL API."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20335  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Git Branch Analyzer

Analyzes Git repository branch topology using libgit2 bindings and git-log parsing. Identifies stale branches, merge conflicts, and divergence points via the GitHub GraphQL API.

## Overview

Git Branch Analyzer leverages libgit2 native bindings to perform deep repository analysis without spawning shell processes. It maps branch topology, identifies stale feature branches older than configurable thresholds, and detects potential merge conflicts by analyzing three-way merge bases. The tool integrates with the GitHub GraphQL API to correlate local branches with open pull requests, flagging orphaned branches that have already been merged remotely. It supports monorepo setups by analyzing subtree splits and sparse-checkout boundaries. Output includes structured JSON reports compatible with CI/CD dashboards, with optional Mermaid diagram generation for visual branch graphs. Configuration supports .gitbranchanalyzer.yml files for per-repository rules including protected branch patterns and auto-cleanup policies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill git-branch-analyzer-libgit2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill git-branch-analyzer-libgit2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill git-branch-analyzer-libgit2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill git-branch-analyzer-libgit2 -a codex
```

### OpenClaw

```bash
clawhub install git-branch-analyzer-libgit2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/

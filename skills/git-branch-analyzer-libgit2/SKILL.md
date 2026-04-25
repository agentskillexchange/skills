---
title: "Git Branch Analyzer"
description: "Analyzes Git repository branch topology using libgit2 bindings and git-log parsing. Identifies stale branches, merge conflicts, and divergence points via the GitHub GraphQL API."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
---

# Git Branch Analyzer

Git Branch Analyzer leverages libgit2 native bindings to perform deep repository analysis without spawning shell processes. It maps branch topology, identifies stale feature branches older than configurable thresholds, and detects potential merge conflicts by analyzing three-way merge bases. The tool integrates with the GitHub GraphQL API to correlate local branches with open pull requests, flagging orphaned branches that have already been merged remotely. It supports monorepo setups by analyzing subtree splits and sparse-checkout boundaries. Output includes structured JSON reports compatible with CI/CD dashboards, with optional Mermaid diagram generation for visual branch graphs. Configuration supports .gitbranchanalyzer.yml files for per-repository rules including protected branch patterns and auto-cleanup policies.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/git-branch-analyzer-libgit2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/git-branch-analyzer-libgit2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/)

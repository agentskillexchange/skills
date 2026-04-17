---
title: "Git Branch Analyzer"
description: "Git Branch Analyzer leverages libgit2 native bindings to perform deep repository analysis without spawning shell processes. It maps branch topology, identifies stale feature branches older than configurable thresholds, and detects potential merge conflicts by analyzing three-way merge bases. The tool integrates with the GitHub GraphQL API to correlate local branches with open pull requests, flagging orphaned branches that have already been merged remotely. It supports monorepo setups by analyzing subtree splits and sparse-checkout boundaries. Output includes structured JSON reports compatible with CI/CD dashboards, with optional Mermaid diagram generation for visual branch graphs. Configuration supports .gitbranchanalyzer.yml files for per-repository rules including protected branch patterns and auto-cleanup policies."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/"
framework:
  - "Claude Code"
---

# Git Branch Analyzer

Git Branch Analyzer leverages libgit2 native bindings to perform deep repository analysis without spawning shell processes. It maps branch topology, identifies stale feature branches older than configurable thresholds, and detects potential merge conflicts by analyzing three-way merge bases. The tool integrates with the GitHub GraphQL API to correlate local branches with open pull requests, flagging orphaned branches that have already been merged remotely. It supports monorepo setups by analyzing subtree splits and sparse-checkout boundaries. Output includes structured JSON reports compatible with CI/CD dashboards, with optional Mermaid diagram generation for visual branch graphs. Configuration supports .gitbranchanalyzer.yml files for per-repository rules including protected branch patterns and auto-cleanup policies.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/git-branch-analyzer-libgit2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/git-branch-analyzer-libgit2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/)

---
title: "Git Branch Analyzer"
description: "Analyzes Git repository branch topology using libgit2 bindings and git-log parsing. Identifies stale branches, merge conflicts, and divergence points via the GitHub GraphQL API."
slug: "git-branch-analyzer-libgit2"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/"
---

# Git Branch Analyzer

Analyzes Git repository branch topology using libgit2 bindings and git-log parsing. Identifies stale branches, merge conflicts, and divergence points via the GitHub GraphQL API.

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
clawhub install git-branch-analyzer-libgit2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Git Branch Analyzer leverages libgit2 native bindings to perform deep repository analysis without spawning shell processes. It maps branch topology, identifies stale feature branches older than configurable thresholds, and detects potential merge conflicts by analyzing three-way merge bases. The tool integrates with the GitHub GraphQL API to correlate local branches with open pull requests, flagging orphaned branches that have already been merged remotely. It supports monorepo setups by analyzing subtree splits and sparse-checkout boundaries. Output includes structured JSON reports compatible with CI/CD dashboards, with optional Mermaid diagram generation for visual branch graphs. Configuration supports .gitbranchanalyzer.yml files for per-repository rules including protected branch patterns and auto-cleanup policies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/)

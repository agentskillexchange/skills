---
name: Git Branch Analyzer
description: Analyzes Git repository branch topology using libgit2 bindings and git-log
  parsing. Identifies stale branches, merge conflicts, and divergence points via the
  GitHub GraphQL API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/
category:
- Developer Tools
framework:
- Claude Code
---
# Git Branch Analyzer

Git Branch Analyzer leverages libgit2 native bindings to perform deep repository analysis without spawning shell processes. It maps branch topology, identifies stale feature branches older than configurable thresholds, and detects potential merge conflicts by analyzing three-way merge bases. The tool integrates with the GitHub GraphQL API to correlate local branches with open pull requests, flagging orphaned branches that have already been merged remotely. It supports monorepo setups by analyzing subtree splits and sparse-checkout boundaries. Output includes structured JSON reports compatible with CI/CD dashboards, with optional Mermaid diagram generation for visual branch graphs. Configuration supports .gitbranchanalyzer.yml files for per-repository rules including protected branch patterns and auto-cleanup policies.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/)

---
title: Git Branch Analyzer
description: Git Branch Analyzer leverages libgit2 native bindings to perform deep
  repository analysis without spawning shell processes. It maps branch topology, identifies
  stale feature branches older than configurable thresholds, and detects potential
  merge conflicts by analyzing three-way merge bases. The tool integrates with the
  GitHub GraphQL API to correlate local branches with open pull requests, flagging
  orphaned branches that have already been merged remotely. It supports monorepo setups
  by analyzing subtree splits and sparse-checkout boundaries. Output includes structured
  JSON reports compatible with CI/CD dashboards, with optional Mermaid diagram generation
  for visual branch graphs. Configuration supports .gitbranchanalyzer.yml files for
  per-repository rules including protected branch patterns and auto-cleanup policies.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/)

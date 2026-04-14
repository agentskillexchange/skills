---
title: "Git Branch Analyzer"
description: "Analyzes Git repository branch topology using libgit2 bindings and git-log parsing. Identifies stale branches, merge conflicts, and divergence points via the GitHub GraphQL API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
---

# Git Branch Analyzer

Git Branch Analyzer leverages libgit2 native bindings to perform deep repository analysis without spawning shell processes. It maps branch topology, identifies stale feature branches older than configurable thresholds, and detects potential merge conflicts by analyzing three-way merge bases. The tool integrates with the GitHub GraphQL API to correlate local branches with open pull requests, flagging orphaned branches that have already been merged remotely. It supports monorepo setups by analyzing subtree splits and sparse-checkout boundaries. Output includes structured JSON reports compatible with CI/CD dashboards, with optional Mermaid diagram generation for visual branch graphs. Configuration supports .gitbranchanalyzer.yml files for per-repository rules including protected branch patterns and auto-cleanup policies.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-branch-analyzer-libgit2/)

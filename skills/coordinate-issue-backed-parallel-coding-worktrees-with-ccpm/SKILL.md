---
title: "Coordinate issue-backed parallel coding worktrees with CCPM"
description: "Use CCPM when an agent team needs one issue-backed workflow that turns plans into GitHub issues, isolates execution in worktrees, and keeps parallel coding runs reviewable instead of relying on ad hoc chat memory."
verification: "security_reviewed"
source: "https://github.com/automazeio/ccpm"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "automazeio/ccpm"
  github_stars: 7995
---

# Coordinate issue-backed parallel coding worktrees with CCPM

Tool: CCPM. This skill gives agents a bounded project-delivery workflow: turn a PRD or epic into GitHub issues, decompose the work into parallelizable tasks, map each task to a worktree, and keep execution traceable through issue state and repo structure instead of loose chat coordination.

When to use it: invoke this when a coding project is large enough that one agent session is no longer sufficient, and you need explicit task breakdown, handoffs, worktree isolation, and GitHub-backed status tracking before implementation drifts or parallel changes collide. The value is not “use a PM tool” in the abstract, it is the repeatable operator workflow that moves from planning to issue sync to parallel execution.

Scope boundary: this is not a generic project-management product listing and not a broad GitHub Issues card. Its boundary is narrower: coordinate issue-backed parallel agent work with worktrees and traceable execution rules. If you just need a task tracker, this is too much. If you need a repo-native orchestration method for parallel coding agents, this is the job.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/coordinate-issue-backed-parallel-coding-worktrees-with-ccpm/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/coordinate-issue-backed-parallel-coding-worktrees-with-ccpm
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/coordinate-issue-backed-parallel-coding-worktrees-with-ccpm`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coordinate-issue-backed-parallel-coding-worktrees-with-ccpm/)

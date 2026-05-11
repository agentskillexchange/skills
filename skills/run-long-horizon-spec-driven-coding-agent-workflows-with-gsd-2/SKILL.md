---
title: "Run long-horizon spec-driven coding agent workflows with GSD 2"
slug: "run-long-horizon-spec-driven-coding-agent-workflows-with-gsd-2"
description: "Use GSD 2 to break a project into milestones, manage agent context and branches, recover from drift, and let coding agents advance through supervised long-running implementation work."
verification: "listed"
source: "https://github.com/gsd-build/gsd-2"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "gsd-build/gsd-2"
  github_stars: 7340
  npm_package: "gsd-pi"
  npm_weekly_downloads: 11369
---

# Run long-horizon spec-driven coding agent workflows with GSD 2

Use GSD 2 when an operator wants a coding agent to execute a planned project over multiple tasks without losing the roadmap, branch state, or verification loop. GSD 2 provides a standalone CLI built on the Pi SDK for context injection, milestone dispatch, worktree and git-branch management, cost and token tracking, stuck-loop detection, crash recovery, and reconciliation of roadmap/database drift.

## When to invoke it

Invoke this skill for long-horizon implementation work where a normal one-shot prompt or manual Claude Code session is too fragile: multi-step feature builds, milestone-based refactors, autonomous slice execution, or recovery/resume after interrupted agent work. The operator still owns the goal, review, and final merge; GSD 2 supplies the orchestration layer around the coding agent.

## Scope boundary

This skill is bounded to using the GSD 2 CLI and repository-documented workflow to plan, dispatch, monitor, reconcile, and resume spec-driven coding milestones with explicit files, git state, and verification gates. It does not claim arbitrary software delivery automation outside that managed agent-workflow loop.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-long-horizon-spec-driven-coding-agent-workflows-with-gsd-2/)

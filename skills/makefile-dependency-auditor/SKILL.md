---
title: "Makefile Dependency Auditor"
description: "Parses GNU Makefiles using pymake and builds complete dependency DAGs. Detects circular dependencies, unreachable targets, missing prerequisites, and generates optimal parallel build orderings."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/makefile-dependency-auditor/"
category:
  - "Developer Tools"
framework:
  - "Codex"
---

# Makefile Dependency Auditor

The Makefile Dependency Auditor skill performs deep analysis of GNU Makefiles to identify build system issues that cause flaky builds, unnecessary rebuilds, and missed parallelism opportunities. Using pymake for Makefile parsing with full variable expansion and conditional evaluation, it constructs a complete directed acyclic graph (DAG) of all targets and their prerequisites. The auditor detects circular dependencies that cause make to skip rules silently, unreachable targets that can never be built, prerequisites referencing files that neither exist nor have build rules, and order-only prerequisites that could be converted to normal prerequisites for correctness. The parallel build analyzer computes the critical path through the dependency graph and identifies the theoretical maximum parallelism, comparing it against the actual parallelism achieved with various -j values. It suggests dependency additions that would enable more parallelism and dependency removals that would not affect correctness. The tool also detects common anti-patterns: .PHONY targets with file prerequisites, recursive make invocations that break dependency tracking, shell commands that modify files not listed as targets, and variables used before definition. Output includes a visual dependency graph (via Graphviz), a prioritized issue list with severity ratings, and a refactored Makefile with fixes applied.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/makefile-dependency-auditor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/makefile-dependency-auditor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makefile-dependency-auditor/)

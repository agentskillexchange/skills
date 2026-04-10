---
title: "Makefile Dependency Auditor"
description: "Parses GNU Makefiles using pymake and builds complete dependency DAGs. Detects circular dependencies, unreachable targets, missing prerequisites, and generates optimal parallel build orderings."
slug: "makefile-dependency-auditor"
category:
  - "Developer Tools"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/makefile-dependency-auditor/"
---

# Makefile Dependency Auditor

Parses GNU Makefiles using pymake and builds complete dependency DAGs. Detects circular dependencies, unreachable targets, missing prerequisites, and generates optimal parallel build orderings.

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
clawhub install makefile-dependency-auditor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Makefile Dependency Auditor skill performs deep analysis of GNU Makefiles to identify build system issues that cause flaky builds, unnecessary rebuilds, and missed parallelism opportunities. Using pymake for Makefile parsing with full variable expansion and conditional evaluation, it constructs a complete directed acyclic graph (DAG) of all targets and their prerequisites. The auditor detects circular dependencies that cause make to skip rules silently, unreachable targets that can never be built, prerequisites referencing files that neither exist nor have build rules, and order-only prerequisites that could be converted to normal prerequisites for correctness. The parallel build analyzer computes the critical path through the dependency graph and identifies the theoretical maximum parallelism, comparing it against the actual parallelism achieved with various -j values. It suggests dependency additions that would enable more parallelism and dependency removals that would not affect correctness. The tool also detects common anti-patterns: .PHONY targets with file prerequisites, recursive make invocations that break dependency tracking, shell commands that modify files not listed as targets, and variables used before definition. Output includes a visual dependency graph (via Graphviz), a prioritized issue list with severity ratings, and a refactored Makefile with fixes applied.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makefile-dependency-auditor/)

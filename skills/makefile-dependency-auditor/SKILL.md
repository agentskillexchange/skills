---
name: "Makefile Dependency Auditor"
description: "Parses GNU Makefiles using pymake and builds complete dependency DAGs. Detects circular dependencies, unreachable targets, missing prerequisites, and generates optimal parallel build orderings."
category: "Developer Tools"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/makefile-dependency-auditor/"
---

# Makefile Dependency Auditor

Parses GNU Makefiles using pymake and builds complete dependency DAGs. Detects circular dependencies, unreachable targets, missing prerequisites, and generates optimal parallel build orderings.

## Overview

The Makefile Dependency Auditor skill performs deep analysis of GNU Makefiles to identify build system issues that cause flaky builds, unnecessary rebuilds, and missed parallelism opportunities. Using pymake for Makefile parsing with full variable expansion and conditional evaluation, it constructs a complete directed acyclic graph (DAG) of all targets and their prerequisites. The auditor detects circular dependencies that cause make to skip rules silently, unreachable targets that can never be built, prerequisites referencing files that neither exist nor have build rules, and order-only prerequisites that could be converted to normal prerequisites for correctness. The parallel build analyzer computes the critical path through the dependency graph and identifies the theoretical maximum parallelism, comparing it against the actual parallelism achieved with various -j values. It suggests dependency additions that would enable more parallelism and dependency removals that would not affect correctness. The tool also detects common anti-patterns: .PHONY targets with file prerequisites, recursive make invocations that break dependency tracking, shell commands that modify files not listed as targets, and variables used before definition. Output includes a visual dependency graph (via Graphviz), a prioritized issue list with severity ratings, and a refactored Makefile with fixes applied.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill makefile-dependency-auditor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill makefile-dependency-auditor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill makefile-dependency-auditor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill makefile-dependency-auditor -a codex
```

### OpenClaw

```bash
clawhub install makefile-dependency-auditor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/makefile-dependency-auditor/

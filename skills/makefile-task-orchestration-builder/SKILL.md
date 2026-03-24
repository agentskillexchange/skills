---
name: "Makefile Task Orchestration Builder"
description: "Builds GNU Make task orchestration files with proper prerequisite chains, pattern rules, and automatic variables. Handles parallel execution flags, phony targets, and recursive make invocations for monorepo builds."
category: "Templates & Workflows"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/makefile-task-orchestration-builder/"
---

# Makefile Task Orchestration Builder

Builds GNU Make task orchestration files with proper prerequisite chains, pattern rules, and automatic variables. Handles parallel execution flags, phony targets, and recursive make invocations for monorepo builds.

## Overview

The Makefile Task Orchestration Builder generates GNU Make compatible Makefiles with correct syntax for complex build and automation workflows. It constructs prerequisite chains using both order-only and normal prerequisites to model task dependencies accurately. Pattern rules with stem matching handle repetitive build targets across multiple source files. Automatic variables ($@, $

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill makefile-task-orchestration-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill makefile-task-orchestration-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill makefile-task-orchestration-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill makefile-task-orchestration-builder -a codex
```

### OpenClaw

```bash
clawhub install makefile-task-orchestration-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/makefile-task-orchestration-builder/

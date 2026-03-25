---
name: "Bun Shell Script Executor"
description: "Leverages Bun’s built-in $ shell API (Bun.Shell) to orchestrate cross-platform shell scripts from TypeScript with tagged template literals, automatic glob expansion, and piped process composition."
category: "Developer Tools"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/bun-shell-script-executor/"
---

# Bun Shell Script Executor

Leverages Bun’s built-in $ shell API (Bun.Shell) to orchestrate cross-platform shell scripts from TypeScript with tagged template literals, automatic glob expansion, and piped process composition.

## Overview

The Bun Shell Script Executor uses Bun’s native $ tagged template literal API (Bun.Shell) to run shell commands directly from TypeScript without spawning external processes through child_process. It composes multi-step build pipelines using Bun’s pipe operator, automatic glob expansion, and environment variable interpolation. The agent generates type-safe shell scripts that work cross-platform by leveraging Bun’s built-in implementations of common Unix utilities (cat, ls, rm, echo) that run natively on Windows, macOS, and Linux. It handles process composition with $.cwd(), $.env(), and $.throws() for error handling. Output streams are processed using Bun’s ReadableStream integration with async iterators. Particularly useful for replacing complex Makefile or npm script chains with type-checked, debuggable TypeScript that runs at near-native speed. Supports Bun.spawn() for long-running processes and Bun.file() for efficient file I/O within build pipelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill bun-shell-script-executor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill bun-shell-script-executor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill bun-shell-script-executor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill bun-shell-script-executor -a codex
```

### OpenClaw

```bash
clawhub install bun-shell-script-executor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/bun-shell-script-executor/

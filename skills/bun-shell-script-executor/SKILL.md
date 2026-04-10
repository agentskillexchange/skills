---
title: "Bun Shell Script Executor"
description: "Leverages Bun’s built-in $ shell API (Bun.Shell) to orchestrate cross-platform shell scripts from TypeScript with tagged template literals, automatic glob expansion, and piped process composition."
slug: "bun-shell-script-executor"
category:
  - "Developer Tools"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://github.com/oven-sh/bun"
tool_ecosystem:
  github_repo: "oven-sh/bun"
  github_stars: 88912
listed: true
---

# Bun Shell Script Executor

Leverages Bun’s built-in $ shell API (Bun.Shell) to orchestrate cross-platform shell scripts from TypeScript with tagged template literals, automatic glob expansion, and piped process composition.

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
clawhub install bun-shell-script-executor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Bun Shell Script Executor uses Bun’s native $ tagged template literal API (Bun.Shell) to run shell commands directly from TypeScript without spawning external processes through child_process. It composes multi-step build pipelines using Bun’s pipe operator, automatic glob expansion, and environment variable interpolation. The agent generates type-safe shell scripts that work cross-platform by leveraging Bun’s built-in implementations of common Unix utilities (cat, ls, rm, echo) that run natively on Windows, macOS, and Linux. It handles process composition with $.cwd(), $.env(), and $.throws() for error handling. Output streams are processed using Bun’s ReadableStream integration with async iterators. Particularly useful for replacing complex Makefile or npm script chains with type-checked, debuggable TypeScript that runs at near-native speed. Supports Bun.spawn() for long-running processes and Bun.file() for efficient file I/O within build pipelines.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bun-shell-script-executor/)

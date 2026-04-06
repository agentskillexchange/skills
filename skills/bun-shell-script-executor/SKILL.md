---
name: "Bun Shell Script Executor"
description: "Leverages Bun’s built-in $ shell API (Bun.Shell) to orchestrate cross-platform shell scripts from TypeScript with tagged template literals, automatic glob expansion, and piped process composition."
category: "Developer Tools"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/oven-sh/bun"
tool_ecosystem:
  github_repo: "oven-sh/bun"
  github_stars: 88702
---
# Bun Shell Script Executor

Leverages Bun’s built-in $ shell API (Bun.Shell) to orchestrate cross-platform shell scripts from TypeScript with tagged template literals, automatic glob expansion, and piped process composition.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bun-shell-script-executor/)

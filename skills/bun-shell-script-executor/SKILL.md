---
title: "Bun Shell Script Executor"
description: "The Bun Shell Script Executor uses Bun&#8217;s native $ tagged template literal API (Bun.Shell) to run shell commands directly from TypeScript without spawning external processes through child_process. It composes multi-step build pipelines using Bun&#8217;s pipe operator, automatic glob expansion, and environment variable interpolation. The agent generates type-safe shell scripts that work cross-platform by leveraging Bun&#8217;s built-in implementations of common Unix utilities (cat, ls, rm, echo) that run natively on Windows, macOS, and Linux. It handles process composition with $.cwd(), $.env(), and $.throws() for error handling. Output streams are processed using Bun&#8217;s ReadableStream integration with async iterators. Particularly useful for replacing complex Makefile or npm script chains with type-checked, debuggable TypeScript that runs at near-native speed. Supports Bun.spawn() for long-running processes and Bun.file() for efficient file I/O within build pipelines."
source: "https://github.com/oven-sh/bun"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "oven-sh/bun"
  github_stars: 88912
---

# Bun Shell Script Executor

The Bun Shell Script Executor uses Bun&#8217;s native $ tagged template literal API (Bun.Shell) to run shell commands directly from TypeScript without spawning external processes through child_process. It composes multi-step build pipelines using Bun&#8217;s pipe operator, automatic glob expansion, and environment variable interpolation. The agent generates type-safe shell scripts that work cross-platform by leveraging Bun&#8217;s built-in implementations of common Unix utilities (cat, ls, rm, echo) that run natively on Windows, macOS, and Linux. It handles process composition with $.cwd(), $.env(), and $.throws() for error handling. Output streams are processed using Bun&#8217;s ReadableStream integration with async iterators. Particularly useful for replacing complex Makefile or npm script chains with type-checked, debuggable TypeScript that runs at near-native speed. Supports Bun.spawn() for long-running processes and Bun.file() for efficient file I/O within build pipelines.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bun-shell-script-executor/)

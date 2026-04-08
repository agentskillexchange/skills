---
title: Bun Shell Script Executor
description: The Bun Shell Script Executor uses Bun’s native $ tagged template literal
  API (Bun.Shell) to run shell commands directly from TypeScript without spawning
  external processes through child_process. It composes multi-step build pipelines
  using Bun’s pipe operator, automatic glob expansion, and environment variable interpolation.
  The agent generates type-safe shell scripts that work cross-platform by leveraging
  Bun’s built-in implementations of common Unix utilities (cat, ls, rm, echo) that
  run natively on Windows, macOS, and Linux. It handles process composition with $.cwd(),
  $.env(), and $.throws() for error handling. Output streams are processed using Bun’s
  ReadableStream integration with async iterators. Particularly useful for replacing
  complex Makefile or npm script chains with type-checked, debuggable TypeScript that
  runs at near-native speed. Supports Bun.spawn() for long-running processes and Bun.file()
  for efficient file I/O within build pipelines.
verification: security_reviewed
source: https://github.com/oven-sh/bun
category:
- Developer Tools
framework:
- Codex
tool_ecosystem:
  github_repo: oven-sh/bun
  github_stars: 88702
---

# Bun Shell Script Executor

The Bun Shell Script Executor uses Bun’s native $ tagged template literal API (Bun.Shell) to run shell commands directly from TypeScript without spawning external processes through child_process. It composes multi-step build pipelines using Bun’s pipe operator, automatic glob expansion, and environment variable interpolation. The agent generates type-safe shell scripts that work cross-platform by leveraging Bun’s built-in implementations of common Unix utilities (cat, ls, rm, echo) that run natively on Windows, macOS, and Linux. It handles process composition with $.cwd(), $.env(), and $.throws() for error handling. Output streams are processed using Bun’s ReadableStream integration with async iterators. Particularly useful for replacing complex Makefile or npm script chains with type-checked, debuggable TypeScript that runs at near-native speed. Supports Bun.spawn() for long-running processes and Bun.file() for efficient file I/O within build pipelines.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bun-shell-script-executor/)

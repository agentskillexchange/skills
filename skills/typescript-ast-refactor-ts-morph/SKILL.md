---
title: "TypeScript AST Refactor"
description: "TypeScript AST Refactor uses ts-morph to programmatically manipulate TypeScript abstract syntax trees for large-scale codebase transformations. It supports extract-function refactoring by analyzing variable scope and closure dependencies, rename-symbol operations that propagate across import/export boundaries, and dead code elimination by tracing reachability from entry points. The tool leverages the TypeScript Compiler API diagnostics to validate transformations before writing, ensuring type safety is preserved. It handles complex scenarios like generic type parameter inference, conditional types, and mapped types. Batch mode processes entire directories with configurable glob patterns, and a dry-run mode generates unified diffs for review. Integration with ESLint auto-fix rules ensures code style consistency after transformation."
source: "https://agentskillexchange.com/skills/typescript-ast-refactor-ts-morph/"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Cursor"
---

# TypeScript AST Refactor

TypeScript AST Refactor uses ts-morph to programmatically manipulate TypeScript abstract syntax trees for large-scale codebase transformations. It supports extract-function refactoring by analyzing variable scope and closure dependencies, rename-symbol operations that propagate across import/export boundaries, and dead code elimination by tracing reachability from entry points. The tool leverages the TypeScript Compiler API diagnostics to validate transformations before writing, ensuring type safety is preserved. It handles complex scenarios like generic type parameter inference, conditional types, and mapped types. Batch mode processes entire directories with configurable glob patterns, and a dry-run mode generates unified diffs for review. Integration with ESLint auto-fix rules ensures code style consistency after transformation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typescript-ast-refactor-ts-morph/)

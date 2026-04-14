---
title: "TypeScript AST Refactor"
description: "Performs automated TypeScript refactoring using ts-morph and the TypeScript Compiler API. Handles rename operations, extract-function, and dead code elimination across large codebases."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/typescript-ast-refactor-ts-morph/"
category:
  - "Developer Tools"
framework:
  - "Cursor"
---

# TypeScript AST Refactor

TypeScript AST Refactor uses ts-morph to programmatically manipulate TypeScript abstract syntax trees for large-scale codebase transformations. It supports extract-function refactoring by analyzing variable scope and closure dependencies, rename-symbol operations that propagate across import/export boundaries, and dead code elimination by tracing reachability from entry points. The tool leverages the TypeScript Compiler API diagnostics to validate transformations before writing, ensuring type safety is preserved. It handles complex scenarios like generic type parameter inference, conditional types, and mapped types. Batch mode processes entire directories with configurable glob patterns, and a dry-run mode generates unified diffs for review. Integration with ESLint auto-fix rules ensures code style consistency after transformation.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typescript-ast-refactor-ts-morph/)

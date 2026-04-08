---
title: TypeScript AST Refactor
description: TypeScript AST Refactor uses ts-morph to programmatically manipulate
  TypeScript abstract syntax trees for large-scale codebase transformations. It supports
  extract-function refactoring by analyzing variable scope and closure dependencies,
  rename-symbol operations that propagate across import/export boundaries, and dead
  code elimination by tracing reachability from entry points. The tool leverages the
  TypeScript Compiler API diagnostics to validate transformations before writing,
  ensuring type safety is preserved. It handles complex scenarios like generic type
  parameter inference, conditional types, and mapped types. Batch mode processes entire
  directories with configurable glob patterns, and a dry-run mode generates unified
  diffs for review. Integration with ESLint auto-fix rules ensures code style consistency
  after transformation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/typescript-ast-refactor-ts-morph/
category:
- Developer Tools
framework:
- Cursor
---

# TypeScript AST Refactor

TypeScript AST Refactor uses ts-morph to programmatically manipulate TypeScript abstract syntax trees for large-scale codebase transformations. It supports extract-function refactoring by analyzing variable scope and closure dependencies, rename-symbol operations that propagate across import/export boundaries, and dead code elimination by tracing reachability from entry points. The tool leverages the TypeScript Compiler API diagnostics to validate transformations before writing, ensuring type safety is preserved. It handles complex scenarios like generic type parameter inference, conditional types, and mapped types. Batch mode processes entire directories with configurable glob patterns, and a dry-run mode generates unified diffs for review. Integration with ESLint auto-fix rules ensures code style consistency after transformation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typescript-ast-refactor-ts-morph/)

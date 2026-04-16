---
title: "TypeScript AST Refactor"
description: "Performs automated TypeScript refactoring using ts-morph and the TypeScript Compiler API. Handles rename operations, extract-function, and dead code elimination across large codebases."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/typescript-ast-refactor-ts-morph/"
category:
  - "Developer Tools"
framework:
  - "Cursor"
---

# TypeScript AST Refactor

TypeScript AST Refactor uses ts-morph to programmatically manipulate TypeScript abstract syntax trees for large-scale codebase transformations. It supports extract-function refactoring by analyzing variable scope and closure dependencies, rename-symbol operations that propagate across import/export boundaries, and dead code elimination by tracing reachability from entry points. The tool leverages the TypeScript Compiler API diagnostics to validate transformations before writing, ensuring type safety is preserved. It handles complex scenarios like generic type parameter inference, conditional types, and mapped types. Batch mode processes entire directories with configurable glob patterns, and a dry-run mode generates unified diffs for review. Integration with ESLint auto-fix rules ensures code style consistency after transformation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typescript-ast-refactor-ts-morph/)

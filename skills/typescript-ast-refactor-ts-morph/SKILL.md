---
title: "TypeScript AST Refactor"
description: "Performs automated TypeScript refactoring using ts-morph and the TypeScript Compiler API. Handles rename operations, extract-function, and dead code elimination across large codebases."
slug: "typescript-ast-refactor-ts-morph"
category:
  - "Developer Tools"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/typescript-ast-refactor-ts-morph/"
---

# TypeScript AST Refactor

Performs automated TypeScript refactoring using ts-morph and the TypeScript Compiler API. Handles rename operations, extract-function, and dead code elimination across large codebases.

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
clawhub install typescript-ast-refactor-ts-morph
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

TypeScript AST Refactor uses ts-morph to programmatically manipulate TypeScript abstract syntax trees for large-scale codebase transformations. It supports extract-function refactoring by analyzing variable scope and closure dependencies, rename-symbol operations that propagate across import/export boundaries, and dead code elimination by tracing reachability from entry points. The tool leverages the TypeScript Compiler API diagnostics to validate transformations before writing, ensuring type safety is preserved. It handles complex scenarios like generic type parameter inference, conditional types, and mapped types. Batch mode processes entire directories with configurable glob patterns, and a dry-run mode generates unified diffs for review. Integration with ESLint auto-fix rules ensures code style consistency after transformation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typescript-ast-refactor-ts-morph/)

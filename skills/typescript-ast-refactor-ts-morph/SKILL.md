---
name: "TypeScript AST Refactor"
description: "Performs automated TypeScript refactoring using ts-morph and the TypeScript Compiler API. Handles rename operations, extract-function, and dead code elimination across large codebases."
category: "Developer Tools"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/typescript-ast-refactor-ts-morph/"
tool_ecosystem:
  tool: "eslint"
  github_stars: 27185
  npm_weekly_downloads: 109028697
  github_repo: "eslint/eslint"
  license: "MIT"
  maintained: true
---

# TypeScript AST Refactor

Performs automated TypeScript refactoring using ts-morph and the TypeScript Compiler API. Handles rename operations, extract-function, and dead code elimination across large codebases.

## Overview

TypeScript AST Refactor uses ts-morph to programmatically manipulate TypeScript abstract syntax trees for large-scale codebase transformations. It supports extract-function refactoring by analyzing variable scope and closure dependencies, rename-symbol operations that propagate across import/export boundaries, and dead code elimination by tracing reachability from entry points. The tool leverages the TypeScript Compiler API diagnostics to validate transformations before writing, ensuring type safety is preserved. It handles complex scenarios like generic type parameter inference, conditional types, and mapped types. Batch mode processes entire directories with configurable glob patterns, and a dry-run mode generates unified diffs for review. Integration with ESLint auto-fix rules ensures code style consistency after transformation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill typescript-ast-refactor-ts-morph
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill typescript-ast-refactor-ts-morph -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill typescript-ast-refactor-ts-morph -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill typescript-ast-refactor-ts-morph -a codex
```

### OpenClaw

```bash
clawhub install typescript-ast-refactor-ts-morph
```

## Source

- Marketplace: https://agentskillexchange.com/skills/typescript-ast-refactor-ts-morph/

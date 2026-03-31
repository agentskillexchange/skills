---
name: "ast-grep Structural Code Search and Rewrite"
description: "Use ast-grep (sg) to search, lint, and rewrite code across large codebases using AST pattern matching. A blazing-fast alternative to regex-based code transformations that understands syntax structure."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ast-grep-structural-code-search-rewrite/"
---
# ast-grep Structural Code Search and Rewrite

Use ast-grep (sg) to search, lint, and rewrite code across large codebases using AST pattern matching. A blazing-fast alternative to regex-based code transformations that understands syntax structure.

## Overview

Overview

ast-grep is a CLI tool for code structural search, linting, and rewriting built on top of tree-sitter. Unlike traditional text-based grep or regex tools, ast-grep operates on abstract syntax trees (ASTs), meaning it understands the syntactic structure of your code rather than just matching character patterns.

With ast-grep, you write search patterns as ordinary code using dollar-sign meta-variables (e.g., `$MATCH`) as wildcards that match any single AST node. This makes complex code transformations intuitive — you describe the pattern you want to find and what you want to replace it with, and ast-grep handles the rest across entire codebases.

How It Works

The skill wraps the `@ast-grep/cli` package (also available via pip, cargo, homebrew, and other package managers). Agents can use ast-grep to perform large-scale code migrations, enforce custom lint rules via YAML configuration, and execute interactive search-and-replace sessions across multiple files and languages including TypeScript, JavaScript, Python, Rust, Go, Java, and more.

A typical workflow involves running `ast-grep -p '$A && $A()' -r '$A?.()' -l ts` to find and rewrite patterns like optional chaining conversions. For linting, teams define rules in YAML that describe forbidden patterns and their suggested fixes, getting pretty error reporting out of the box.

Key Capabilities

ast-grep produces structured output (JSON, SARIF) suitable for CI/CD integration and automated code review pipelines. It supports jQuery-like API traversal for programmatic AST manipulation via its Node.js bindings. The tool is written in Rust and compiles to native code, delivering performance orders of magnitude faster than JavaScript-based AST tools. With over 13,000 GitHub stars and active development, ast-grep is used by teams for codemod operations, enforcing coding conventions, and building custom static analysis rules.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ast-grep-structural-code-search-rewrite
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ast-grep-structural-code-search-rewrite -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ast-grep-structural-code-search-rewrite -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ast-grep-structural-code-search-rewrite -a codex
```

### OpenClaw

```bash
clawhub install ast-grep-structural-code-search-rewrite
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ast-grep-structural-code-search-rewrite/)

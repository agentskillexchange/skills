---
name: "Oxlint High-Performance JavaScript Linter"
description: "Run Oxlint from the Oxc toolchain to lint JavaScript and TypeScript codebases at extreme speed. Written in Rust, Oxlint is 50-100x faster than ESLint and used by Shopify, ByteDance, and Preact."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/oxlint-high-performance-javascript-linter/"
tool_ecosystem:
  tool: "eslint"
  github_stars: 27185
  npm_weekly_downloads: 109028697
  github_repo: "eslint/eslint"
  license: "MIT"
  maintained: true
---

# Oxlint High-Performance JavaScript Linter

Run Oxlint from the Oxc toolchain to lint JavaScript and TypeScript codebases at extreme speed. Written in Rust, Oxlint is 50-100x faster than ESLint and used by Shopify, ByteDance, and Preact.

## Overview

Overview

Oxlint is a high-performance linter for JavaScript and TypeScript built on the Oxc (Oxidation Compiler) stack. Part of VoidZero’s vision for a unified, Rust-powered JavaScript toolchain, Oxlint delivers lint results 50-100x faster than ESLint by leveraging Rust’s performance characteristics and a purpose-built parser and resolver.

The Oxc project provides more than just linting — it includes a parser, transformer, minifier, formatter (Oxfmt), and module resolver. Oxlint specifically focuses on catching bugs, enforcing code quality rules, and providing instant feedback during development. Major companies including Shopify, ByteDance, Shopee, and Preact use Oxlint in production.

How It Works

Agents can invoke Oxlint via `npx oxlint@latest` to instantly lint a JavaScript or TypeScript codebase with zero configuration. Oxlint supports most of ESLint’s commonly used rules and includes rules from popular plugins like typescript-eslint, eslint-plugin-react, eslint-plugin-jest, and eslint-plugin-jsx-a11y. Configuration uses an `.oxlintrc.json` file that follows a familiar format.

With the Oxc project’s tsgolint integration, Oxlint also supports type-aware linting rules using a novel architecture where Go-based type checking runs alongside Rust-based linting for maximum throughput.

Output and Integration

Oxlint outputs diagnostics in multiple formats including terminal-friendly colored output, JSON, and checkstyle XML for CI integration. It integrates with Rolldown (Vite’s future bundler) and the broader Oxc ecosystem. The npm package `oxlint` has extensive weekly downloads and the GitHub project has over 20,000 stars with active daily commits. Oxlint is MIT licensed and suitable for both open source and commercial projects.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill oxlint-high-performance-javascript-linter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill oxlint-high-performance-javascript-linter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill oxlint-high-performance-javascript-linter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill oxlint-high-performance-javascript-linter -a codex
```

### OpenClaw

```bash
clawhub install oxlint-high-performance-javascript-linter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/oxlint-high-performance-javascript-linter/

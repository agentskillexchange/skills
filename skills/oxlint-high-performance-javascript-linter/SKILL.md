---
title: "Oxlint High-Performance JavaScript Linter"
description: "Run Oxlint from the Oxc toolchain to lint JavaScript and TypeScript codebases at extreme speed. Written in Rust, Oxlint is 50-100x faster than ESLint and used by Shopify, ByteDance, and Preact."
slug: "oxlint-high-performance-javascript-linter"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/oxc-project/oxc"
tool_ecosystem:
  github_repo: "oxc-project/oxc"
  github_stars: 20468
  npm_package: "oxlint"
  npm_weekly_downloads: 3983578
listed: true
---

# Oxlint High-Performance JavaScript Linter

Run Oxlint from the Oxc toolchain to lint JavaScript and TypeScript codebases at extreme speed. Written in Rust, Oxlint is 50-100x faster than ESLint and used by Shopify, ByteDance, and Preact.

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
clawhub install oxlint-high-performance-javascript-linter
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
Oxlint is a high-performance linter for JavaScript and TypeScript built on the Oxc (Oxidation Compiler) stack. Part of VoidZero’s vision for a unified, Rust-powered JavaScript toolchain, Oxlint delivers lint results 50-100x faster than ESLint by leveraging Rust’s performance characteristics and a purpose-built parser and resolver.
The Oxc project provides more than just linting — it includes a parser, transformer, minifier, formatter (Oxfmt), and module resolver. Oxlint specifically focuses on catching bugs, enforcing code quality rules, and providing instant feedback during development. Major companies including Shopify, ByteDance, Shopee, and Preact use Oxlint in production.
How It Works
Agents can invoke Oxlint via npx oxlint@latest to instantly lint a JavaScript or TypeScript codebase with zero configuration. Oxlint supports most of ESLint’s commonly used rules and includes rules from popular plugins like typescript-eslint, eslint-plugin-react, eslint-plugin-jest, and eslint-plugin-jsx-a11y. Configuration uses an .oxlintrc.json file that follows a familiar format.
With the Oxc project’s tsgolint integration, Oxlint also supports type-aware linting rules using a novel architecture where Go-based type checking runs alongside Rust-based linting for maximum throughput.
Output and Integration
Oxlint outputs diagnostics in multiple formats including terminal-friendly colored output, JSON, and checkstyle XML for CI integration. It integrates with Rolldown (Vite’s future bundler) and the broader Oxc ecosystem. The npm package oxlint has extensive weekly downloads and the GitHub project has over 20,000 stars with active daily commits. Oxlint is MIT licensed and suitable for both open source and commercial projects.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/oxlint-high-performance-javascript-linter/)

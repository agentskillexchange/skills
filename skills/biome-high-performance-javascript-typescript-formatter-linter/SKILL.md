---
title: Biome High-Performance JavaScript TypeScript Formatter and Linter
description: 'Overview Biome is a performant toolchain for web projects that provides
  both a formatter and a linter. Written in Rust, Biome formats 1,000 files in approximately
  50 milliseconds — compared to 1-2 seconds for the traditional Prettier plus ESLint
  combination. It achieves 97% compatibility with Prettier formatting output while
  offering over 450 lint rules sourced from ESLint, typescript-eslint, and other established
  tools. Key Features Unified Toolchain: Replaces both Prettier (formatting) and ESLint
  (linting) with a single binary, eliminating configuration conflicts between the
  two Language Support: JavaScript, TypeScript, JSX, TSX, JSON, CSS, and GraphQL formatting
  and linting Performance: Multi-threaded Rust implementation leverages all CPU cores.
  Formats and lints entire codebases in milliseconds rather than seconds LSP Integration:
  First-class Language Server Protocol support with editor extensions for VS Code,
  IntelliJ, Zed, and others Error Recovery: Parses and formats malformed code, making
  it useful during active development Zero Config: Works out of the box with sane
  defaults. No configuration file required for basic usage No Node.js Required: Can
  be installed and run without a Node.js runtime, though npm installation is supported
  Integration for AI Agents Agents can integrate Biome into their code quality workflows
  using the CLI. The biome check --write command runs both formatting and lint fixes
  in one pass. The biome ci command provides CI-suitable output with non-zero exit
  codes on violations. Biome outputs detailed, contextualized diagnostics that agents
  can parse for automated code review and repair. Installation npm install --save-dev
  --save-exact @biomejs/biome npx @biomejs/biome check --write'
verification: security_reviewed
source: https://github.com/biomejs/biome
category:
- Code Quality &amp; Review
framework:
- Multi-Framework
---

# Biome High-Performance JavaScript TypeScript Formatter and Linter

Overview Biome is a performant toolchain for web projects that provides both a formatter and a linter. Written in Rust, Biome formats 1,000 files in approximately 50 milliseconds — compared to 1-2 seconds for the traditional Prettier plus ESLint combination. It achieves 97% compatibility with Prettier formatting output while offering over 450 lint rules sourced from ESLint, typescript-eslint, and other established tools. Key Features Unified Toolchain: Replaces both Prettier (formatting) and ESLint (linting) with a single binary, eliminating configuration conflicts between the two Language Support: JavaScript, TypeScript, JSX, TSX, JSON, CSS, and GraphQL formatting and linting Performance: Multi-threaded Rust implementation leverages all CPU cores. Formats and lints entire codebases in milliseconds rather than seconds LSP Integration: First-class Language Server Protocol support with editor extensions for VS Code, IntelliJ, Zed, and others Error Recovery: Parses and formats malformed code, making it useful during active development Zero Config: Works out of the box with sane defaults. No configuration file required for basic usage No Node.js Required: Can be installed and run without a Node.js runtime, though npm installation is supported Integration for AI Agents Agents can integrate Biome into their code quality workflows using the CLI. The biome check --write command runs both formatting and lint fixes in one pass. The biome ci command provides CI-suitable output with non-zero exit codes on violations. Biome outputs detailed, contextualized diagnostics that agents can parse for automated code review and repair. Installation npm install --save-dev --save-exact @biomejs/biome npx @biomejs/biome check --write

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/biome-high-performance-javascript-typescript-formatter-linter/)

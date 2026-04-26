---
title: "Biome High-Performance JavaScript TypeScript Formatter and Linter"
description: "Biome is a high-performance Rust-based toolchain for JavaScript, TypeScript, JSX, JSON, CSS, and GraphQL that unifies formatting and linting in a single tool. With 97% Prettier compatibility and over 450 lint rules, Biome replaces ESLint and Prettier with dramatically faster execution."
verification: "security_reviewed"
source: "https://github.com/biomejs/biome"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "biomejs/biome"
  github_stars: 24340
---

# Biome High-Performance JavaScript TypeScript Formatter and Linter

Overview
Biome is a performant toolchain for web projects that provides both a formatter and a linter. Written in Rust, Biome formats 1,000 files in approximately 50 milliseconds — compared to 1-2 seconds for the traditional Prettier plus ESLint combination. It achieves 97% compatibility with Prettier formatting output while offering over 450 lint rules sourced from ESLint, typescript-eslint, and other established tools.

Key Features

Unified Toolchain: Replaces both Prettier (formatting) and ESLint (linting) with a single binary, eliminating configuration conflicts between the two
Language Support: JavaScript, TypeScript, JSX, TSX, JSON, CSS, and GraphQL formatting and linting
Performance: Multi-threaded Rust implementation leverages all CPU cores. Formats and lints entire codebases in milliseconds rather than seconds
LSP Integration: First-class Language Server Protocol support with editor extensions for VS Code, IntelliJ, Zed, and others
Error Recovery: Parses and formats malformed code, making it useful during active development
Zero Config: Works out of the box with sane defaults. No configuration file required for basic usage
No Node.js Required: Can be installed and run without a Node.js runtime, though npm installation is supported

Integration for AI Agents
Agents can integrate Biome into their code quality workflows using the CLI. The biome check --write command runs both formatting and lint fixes in one pass. The biome ci command provides CI-suitable output with non-zero exit codes on violations. Biome outputs detailed, contextualized diagnostics that agents can parse for automated code review and repair.

Installation
npm install --save-dev --save-exact @biomejs/biome
npx @biomejs/biome check --write

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/biome-high-performance-javascript-typescript-formatter-linter/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/biome-high-performance-javascript-typescript-formatter-linter
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/biome-high-performance-javascript-typescript-formatter-linter`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/biome-high-performance-javascript-typescript-formatter-linter/)

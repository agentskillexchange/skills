---
title: "Biome High-Performance JavaScript TypeScript Formatter and Linter"
description: "Biome is a high-performance Rust-based toolchain for JavaScript, TypeScript, JSX, JSON, CSS, and GraphQL that unifies formatting and linting in a single tool. With 97% Prettier compatibility and over 450 lint rules, Biome replaces ESLint and Prettier with dramatically faster execution."
slug: "biome-high-performance-javascript-typescript-formatter-linter"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/biomejs/biome"
---

# Biome High-Performance JavaScript TypeScript Formatter and Linter

Biome is a high-performance Rust-based toolchain for JavaScript, TypeScript, JSX, JSON, CSS, and GraphQL that unifies formatting and linting in a single tool. With 97% Prettier compatibility and over 450 lint rules, Biome replaces ESLint and Prettier with dramatically faster execution.

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
clawhub install biome-high-performance-javascript-typescript-formatter-linter
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
Biome is a performant toolchain for web projects that provides both a formatter and a linter. Written in Rust, Biome formats 1,000 files in approximately 50 milliseconds — compared to 1-2 seconds for the traditional Prettier plus ESLint combination. It achieves 97% compatibility with Prettier formatting output while offering over 450 lint rules sourced from ESLint, typescript-eslint, and other established tools.
Key Features
- Unified Toolchain: Replaces both Prettier (formatting) and ESLint (linting) with a single binary, eliminating configuration conflicts between the two
- Language Support: JavaScript, TypeScript, JSX, TSX, JSON, CSS, and GraphQL formatting and linting
- Performance: Multi-threaded Rust implementation leverages all CPU cores. Formats and lints entire codebases in milliseconds rather than seconds
- LSP Integration: First-class Language Server Protocol support with editor extensions for VS Code, IntelliJ, Zed, and others
- Error Recovery: Parses and formats malformed code, making it useful during active development
- Zero Config: Works out of the box with sane defaults. No configuration file required for basic usage
- No Node.js Required: Can be installed and run without a Node.js runtime, though npm installation is supported
Integration for AI Agents
Agents can integrate Biome into their code quality workflows using the CLI. The biome check --write command runs both formatting and lint fixes in one pass. The biome ci command provides CI-suitable output with non-zero exit codes on violations. Biome outputs detailed, contextualized diagnostics that agents can parse for automated code review and repair.
Installation
npm install --save-dev --save-exact @biomejs/biome
npx @biomejs/biome check --write

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/biome-high-performance-javascript-typescript-formatter-linter/)

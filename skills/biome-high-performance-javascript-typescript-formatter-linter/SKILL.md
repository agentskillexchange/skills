---
title: "Biome High-Performance JavaScript TypeScript Formatter and Linter"
description: "Overview Biome is a performant toolchain for web projects that provides both a formatter and a linter. Written in Rust, Biome formats 1,000 files in approximately 50 milliseconds — compared to 1-2 seconds for the traditional Prettier plus ESLint combination. It achieves 97% compatibility with Prettier formatting output while offering over 450 lint rules sourced from ESLint, typescript-eslint, and other established tools. Key Features Unified Toolchain: Replaces both Prettier (formatting) and ESLint (linting) with a single binary, eliminating configuration conflicts between the two Language Support: JavaScript, TypeScript, JSX, TSX, JSON, CSS, and GraphQL formatting and linting Performance: Multi-threaded Rust implementation leverages all CPU cores. Formats and lints entire codebases in milliseconds rather than seconds LSP Integration: First-class Language Server Protocol support with editor extensions for VS Code, IntelliJ, Zed, and others Error Recovery: Parses and formats malformed code, making it useful during active development Zero Config: Works out of the box with sane defaults. No configuration file required for basic usage No Node.js Required: Can be installed and run without a Node.js runtime, though npm installation is supported Integration for AI Agents Agents can integrate Biome into their code quality workflows using the CLI. The biome check --write command runs both formatting and lint fixes in one pass. The biome ci command provides CI-suitable output with non-zero exit codes on violations. Biome outputs detailed, contextualized diagnostics that agents can parse for automated code review and repair. Installation npm install --save-dev --save-exact @biomejs/biome npx @biomejs/biome check --write"
source: "https://github.com/biomejs/biome"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "biomejs/biome"
  github_stars: 24340
---

# Biome High-Performance JavaScript TypeScript Formatter and Linter

Overview Biome is a performant toolchain for web projects that provides both a formatter and a linter. Written in Rust, Biome formats 1,000 files in approximately 50 milliseconds — compared to 1-2 seconds for the traditional Prettier plus ESLint combination. It achieves 97% compatibility with Prettier formatting output while offering over 450 lint rules sourced from ESLint, typescript-eslint, and other established tools. Key Features Unified Toolchain: Replaces both Prettier (formatting) and ESLint (linting) with a single binary, eliminating configuration conflicts between the two Language Support: JavaScript, TypeScript, JSX, TSX, JSON, CSS, and GraphQL formatting and linting Performance: Multi-threaded Rust implementation leverages all CPU cores. Formats and lints entire codebases in milliseconds rather than seconds LSP Integration: First-class Language Server Protocol support with editor extensions for VS Code, IntelliJ, Zed, and others Error Recovery: Parses and formats malformed code, making it useful during active development Zero Config: Works out of the box with sane defaults. No configuration file required for basic usage No Node.js Required: Can be installed and run without a Node.js runtime, though npm installation is supported Integration for AI Agents Agents can integrate Biome into their code quality workflows using the CLI. The biome check --write command runs both formatting and lint fixes in one pass. The biome ci command provides CI-suitable output with non-zero exit codes on violations. Biome outputs detailed, contextualized diagnostics that agents can parse for automated code review and repair. Installation npm install --save-dev --save-exact @biomejs/biome npx @biomejs/biome check --write

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/biome-high-performance-javascript-typescript-formatter-linter/)

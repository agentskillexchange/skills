---
name: "Bun All-in-One JavaScript Runtime Bundler and Package Manager"
description: "Bun is an all-in-one toolkit for JavaScript and TypeScript apps that ships as a single executable. It includes a fast JavaScript runtime (Node.js-compatible), bundler, test runner, and package manager, dramatically reducing startup times and memory usage compared to Node.js."
category: "Developer Tools"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/oven-sh/bun"
---
# Bun All-in-One JavaScript Runtime Bundler and Package Manager

Bun is an all-in-one toolkit for JavaScript and TypeScript apps that ships as a single executable. It includes a fast JavaScript runtime (Node.js-compatible), bundler, test runner, and package manager, dramatically reducing startup times and memory usage compared to Node.js.

## Overview

Bun is a modern all-in-one JavaScript and TypeScript toolkit developed by Oven. It ships as a single binary called `bun` and combines a runtime, bundler, test runner, script runner, and package manager into one tool. Built in Zig and powered by JavaScriptCore (the engine behind Safari), Bun achieves significantly faster startup times and lower memory usage than Node.js.

Runtime

The Bun runtime is designed as a drop-in replacement for Node.js. It natively supports TypeScript, JSX, and ESM out of the box without any configuration. It implements most Node.js built-in modules and APIs, making it compatible with the vast majority of the npm ecosystem. Bun also provides its own high-performance APIs for HTTP serving (`Bun.serve`), file I/O (`Bun.file`), SQLite (`bun:sqlite`), PostgreSQL (`Bun.sql`), Redis (`Bun.redis`), S3 (`Bun.s3`), WebSockets, and more.

Package Manager

`bun install` is a dramatically faster alternative to npm, yarn, and pnpm. It reads `package.json` and generates a binary lockfile for reproducible installs. Workspace support, scoped registries, lifecycle scripts, and overrides are all supported. `bunx` serves as a faster replacement for `npx`.

Bundler

`Bun.build` provides a fast JavaScript and TypeScript bundler with plugin support, CSS bundling, HTML entry points, hot module replacement, and the ability to compile single-file executables. It handles loaders for various file types and supports macros for compile-time code execution.

Test Runner

`bun test` is a Jest-compatible test runner built into Bun. It supports snapshots, mocks, lifecycle hooks, code coverage, DOM testing, watch mode, and custom reporters. Tests run significantly faster than Jest or Vitest due to Bun’s fast startup and native test infrastructure.

Agent Integration

AI agents working on JavaScript and TypeScript projects can use Bun as a faster alternative to Node.js for running scripts, installing dependencies, executing tests, and bundling code. The single-binary design simplifies environment setup, and the built-in shell (`Bun.$`) enables cross-platform scripting within agent workflows.

Installation

Install via the official script: `curl -fsSL https://bun.com/install | bash`. Also available via npm (`npm install -g bun`), Homebrew (`brew install bun`), and Docker (`docker pull oven/bun`). Supports Linux (x64, arm64), macOS (x64, Apple Silicon), and Windows (x64, arm64).

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill bun-all-in-one-javascript-runtime-bundler-package-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill bun-all-in-one-javascript-runtime-bundler-package-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill bun-all-in-one-javascript-runtime-bundler-package-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill bun-all-in-one-javascript-runtime-bundler-package-manager -a codex
```

### OpenClaw

```bash
clawhub install bun-all-in-one-javascript-runtime-bundler-package-manager
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bun-all-in-one-javascript-runtime-bundler-package-manager/)

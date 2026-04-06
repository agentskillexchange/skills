---
name: Concurrently Parallel Command Runner for npm Scripts
description: Concurrently runs multiple commands in parallel with color-coded output,
  prefix labels, and process lifecycle management. With 14M+ weekly npm downloads,
  it is the standard tool for running dev servers, watchers, and build processes simultaneously.
category: Developer Tools
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/open-cli-tools/concurrently"
tool_ecosystem:
  github_repo: "https://github.com/open-cli-tools/concurrently"
  github_stars: 7726
---
# Concurrently Parallel Command Runner for npm Scripts

Concurrently runs multiple commands in parallel with color-coded output, prefix labels, and process lifecycle management. With 14M+ weekly npm downloads, it is the standard tool for running dev servers, watchers, and build processes simultaneously.

Concurrently is an npm package that runs multiple commands in parallel, replacing manual use of background processes and ampersand chaining in shell scripts. It provides color-coded, prefixed output so developers can distinguish which command produced which log line, and it manages process lifecycle including kill-on-failure and restart-on-exit behaviors.

Why Concurrently Exists

Modern development workflows typically require multiple long-running processes: a frontend dev server, a backend API server, a CSS watcher, a TypeScript compiler in watch mode, and perhaps a test runner. Running these with cmd1 & cmd2 & cmd3 loses output attribution, makes cleanup unreliable, and behaves inconsistently across operating systems. Concurrently solves all of these problems with a cross-platform implementation.

Basic Usage

The simplest invocation is concurrently "npm:watch-*" which runs all npm scripts matching the glob pattern. Named processes get automatic color-coded prefixes: concurrently -n server,client "npm run server" "npm run client". The --kill-others flag terminates all processes if any one exits, and --kill-others-on-fail does so only on non-zero exit codes.

Advanced Features

Concurrently supports process restart with --restart-tries and --restart-after, input passthrough to specific processes with --handle-input and --default-input-target, and custom success conditions with --success first|last|all|command-NAME. Prefix templates support timestamps, PID, process index, and command name.

Programmatic API

The package exports a concurrently() function for use in Node.js scripts and build tools. It returns a promise that resolves with an array of close events, enabling integration into custom orchestration logic. Options mirror the CLI flags.

Integration with Package Managers

Concurrently works with npm, yarn, pnpm, and bun scripts. The npm: prefix syntax lets you reference package.json scripts directly: concurrently "npm:lint" "npm:test" "npm:build". Glob patterns like npm:watch-* automatically expand to matching script names.

Installation

Install with npm install concurrently or npm install -g concurrently for global use. The package has zero runtime dependencies and works on Node.js 18+.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill concurrently-parallel-command-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill concurrently-parallel-command-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill concurrently-parallel-command-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill concurrently-parallel-command-runner -a codex
```

### OpenClaw

```bash
clawhub install concurrently-parallel-command-runner
```


## Source

- [GitHub](https://github.com/open-cli-tools/concurrently)

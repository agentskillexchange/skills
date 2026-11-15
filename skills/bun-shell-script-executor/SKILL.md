---
name: "Bun Shell Script Executor"
slug: "bun-shell-script-executor"
description: "Leverages Bun's built-in $ shell API (Bun.Shell) to orchestrate cross-platform shell scripts from TypeScript with tagged template literals, automatic glob expansion, and piped process composition."
github_stars: 88912
verification: "security_reviewed"
source: "https://github.com/oven-sh/bun"
author: "oven-sh"
category: "Developer Tools"
framework: "Codex"
tool_ecosystem:
  github_repo: "oven-sh/bun"
  github_stars: 88912
  npm_package: "bun"
  npm_weekly_downloads: 1705197
---

# Bun Shell Script Executor

Leverages Bun's built-in $ shell API (Bun.Shell) to orchestrate cross-platform shell scripts from TypeScript with tagged template literals, automatic glob expansion, and piped process composition.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g bun
- brew tap oven-sh/bun
- brew install bun
- docker pull oven/bun

Requirements and caveats from upstream:
- At its core is the _Bun runtime_, a fast JavaScript runtime designed as **a drop-in replacement for Node.js**. It's written in Zig and powered by JavaScriptCore under the hood, dramatically reducing startup times and...
- The bun command-line tool also implements a test runner, script runner, and Node.js-compatible package manager. Instead of 1,000 node_modules for development, you only need bun. Bun's built-in tools are significantly...
- # with Docker

Basic usage or getting-started notes:
- bun run index.tsx # TS and JSX supported out-of-the-box
- bun test # run tests
- bun run start # run the start script in package.json

- Source: https://github.com/oven-sh/bun
- Extracted from upstream docs: https://raw.githubusercontent.com/oven-sh/bun/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bun-shell-script-executor/)

---
title: "Vite Plugin Hot Module Analyzer"
description: "Monitors and analyzes Vite HMR (Hot Module Replacement) update chains using the vite.config.ts plugin API and ws WebSocket events. Identifies slow module boundaries, circular dependency hot paths, and generates flamegraph-compatible output for Chrome DevTools Performance panel."
verification: "security_reviewed"
source: "https://github.com/vitejs/vite"
category:
  - "Developer Tools"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "vitejs/vite"
  github_stars: 79927
  npm_package: "vite"
  npm_weekly_downloads: 96756115
---

# Vite Plugin Hot Module Analyzer

The Vite Plugin Hot Module Analyzer inspects your Vite development server’s HMR pipeline in real time. It hooks into the Vite plugin API via the handleHotUpdate() lifecycle to intercept module graph changes, then correlates these with WebSocket frame timestamps from the Vite dev server’s ws connection. The agent identifies modules that consistently trigger full-page reloads instead of surgical HMR updates, flags circular import chains that cause cascading invalidation, and benchmarks update latency per module boundary. Output includes a JSON trace compatible with Chrome DevTools Performance panel import, plus a ranked list of the slowest HMR chains. It leverages vite.createServer() internals, the ModuleGraph API, and ssrLoadModule for server-side module tracing. Particularly useful for large monorepo setups using Turborepo or Nx where HMR performance degrades as the module graph grows beyond 5,000 nodes.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/vite-plugin-hmr-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/vite-plugin-hmr-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/vite-plugin-hmr-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vite-plugin-hmr-analyzer/)

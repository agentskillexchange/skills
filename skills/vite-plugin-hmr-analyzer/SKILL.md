---
name: "Vite Plugin Hot Module Analyzer"
description: "Monitors and analyzes Vite HMR (Hot Module Replacement) update chains using the vite.config.ts plugin API and ws WebSocket events. Identifies slow module boundaries, circular dependency hot paths, and generates flamegraph-compatible output for Chrome DevTools Performance panel."
category: "Developer Tools"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/vite-plugin-hmr-analyzer/"
tool_ecosystem:
  tool: vite
  github_stars: 79330
  npm_weekly_downloads: 76344516
  github_repo: vitejs/vite
  license: MIT
  maintained: true
---

# Vite Plugin Hot Module Analyzer

Monitors and analyzes Vite HMR (Hot Module Replacement) update chains using the vite.config.ts plugin API and ws WebSocket events. Identifies slow module boundaries, circular dependency hot paths, and generates flamegraph-compatible output for Chrome DevTools Performance panel.

## Overview

The Vite Plugin Hot Module Analyzer inspects your Vite development server’s HMR pipeline in real time. It hooks into the Vite plugin API via the handleHotUpdate() lifecycle to intercept module graph changes, then correlates these with WebSocket frame timestamps from the Vite dev server’s ws connection. The agent identifies modules that consistently trigger full-page reloads instead of surgical HMR updates, flags circular import chains that cause cascading invalidation, and benchmarks update latency per module boundary. Output includes a JSON trace compatible with Chrome DevTools Performance panel import, plus a ranked list of the slowest HMR chains. It leverages vite.createServer() internals, the ModuleGraph API, and ssrLoadModule for server-side module tracing. Particularly useful for large monorepo setups using Turborepo or Nx where HMR performance degrades as the module graph grows beyond 5,000 nodes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill vite-plugin-hmr-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill vite-plugin-hmr-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill vite-plugin-hmr-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill vite-plugin-hmr-analyzer -a codex
```

### OpenClaw

```bash
clawhub install vite-plugin-hmr-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/vite-plugin-hmr-analyzer/

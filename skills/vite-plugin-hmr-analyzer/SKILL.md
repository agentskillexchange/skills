---
title: "Vite Plugin Hot Module Analyzer"
description: "Monitors and analyzes Vite HMR (Hot Module Replacement) update chains using the vite.config.ts plugin API and ws WebSocket events. Identifies slow module boundaries, circular dependency hot paths, and generates flamegraph-compatible output for Chrome DevTools Performance panel."
slug: "vite-plugin-hmr-analyzer"
category:
  - "Developer Tools"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/vite-plugin-hmr-analyzer/"
listed: true
---

# Vite Plugin Hot Module Analyzer

Monitors and analyzes Vite HMR (Hot Module Replacement) update chains using the vite.config.ts plugin API and ws WebSocket events. Identifies slow module boundaries, circular dependency hot paths, and generates flamegraph-compatible output for Chrome DevTools Performance panel.

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
clawhub install vite-plugin-hmr-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Vite Plugin Hot Module Analyzer inspects your Vite development server’s HMR pipeline in real time. It hooks into the Vite plugin API via the handleHotUpdate() lifecycle to intercept module graph changes, then correlates these with WebSocket frame timestamps from the Vite dev server’s ws connection. The agent identifies modules that consistently trigger full-page reloads instead of surgical HMR updates, flags circular import chains that cause cascading invalidation, and benchmarks update latency per module boundary. Output includes a JSON trace compatible with Chrome DevTools Performance panel import, plus a ranked list of the slowest HMR chains. It leverages vite.createServer() internals, the ModuleGraph API, and ssrLoadModule for server-side module tracing. Particularly useful for large monorepo setups using Turborepo or Nx where HMR performance degrades as the module graph grows beyond 5,000 nodes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vite-plugin-hmr-analyzer/)

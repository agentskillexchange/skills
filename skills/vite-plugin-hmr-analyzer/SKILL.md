---
name: "Vite Plugin Hot Module Analyzer"
description: "Monitors and analyzes Vite HMR (Hot Module Replacement) update chains using the vite.config.ts plugin API and ws WebSocket events. Identifies slow module boundaries, circular dependency hot paths, and generates flamegraph-compatible output for Chrome DevTools Performance panel."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/vite-plugin-hmr-analyzer/"
category:
  - "Developer Tools"
framework:
  - "Cursor"
---

# Vite Plugin Hot Module Analyzer

The Vite Plugin Hot Module Analyzer inspects your Vite development server's HMR pipeline in real time. It hooks into the Vite plugin API via the handleHotUpdate() lifecycle to intercept module graph changes, then correlates these with WebSocket frame timestamps from the Vite dev server's ws connection. The agent identifies modules that consistently trigger full-page reloads instead of surgical HMR updates, flags circular import chains that cause cascading invalidation, and benchmarks update latency per module boundary. Output includes a JSON trace compatible with Chrome DevTools Performance panel import, plus a ranked list of the slowest HMR chains. It leverages vite.createServer() internals, the ModuleGraph API, and ssrLoadModule for server-side module tracing. Particularly useful for large monorepo setups using Turborepo or Nx where HMR performance degrades as the module graph grows beyond 5,000 nodes.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vite-plugin-hmr-analyzer/)

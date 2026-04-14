---
title: "Vite Plugin Hot Module Analyzer"
description: "Monitors and analyzes Vite HMR (Hot Module Replacement) update chains using the vite.config.ts plugin API and ws WebSocket events. Identifies slow module boundaries, circular dependency hot paths, and generates flamegraph-compatible output for Chrome DevTools Performance panel."
verification: security_reviewed
source: "https://github.com/vitejs/vite"
category:
  - "Developer Tools"
framework:
  - "Cursor"
---

# Vite Plugin Hot Module Analyzer

The Vite Plugin Hot Module Analyzer inspects your Vite development server’s HMR pipeline in real time. It hooks into the Vite plugin API via the handleHotUpdate() lifecycle to intercept module graph changes, then correlates these with WebSocket frame timestamps from the Vite dev server’s ws connection. The agent identifies modules that consistently trigger full-page reloads instead of surgical HMR updates, flags circular import chains that cause cascading invalidation, and benchmarks update latency per module boundary. Output includes a JSON trace compatible with Chrome DevTools Performance panel import, plus a ranked list of the slowest HMR chains. It leverages vite.createServer() internals, the ModuleGraph API, and ssrLoadModule for server-side module tracing. Particularly useful for large monorepo setups using Turborepo or Nx where HMR performance degrades as the module graph grows beyond 5,000 nodes.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vite-plugin-hmr-analyzer/)

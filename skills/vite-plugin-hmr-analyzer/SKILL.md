---
title: "Vite Plugin Hot Module Analyzer"
description: "The Vite Plugin Hot Module Analyzer inspects your Vite development server&#8217;s HMR pipeline in real time. It hooks into the Vite plugin API via the handleHotUpdate() lifecycle to intercept module graph changes, then correlates these with WebSocket frame timestamps from the Vite dev server&#8217;s ws connection. The agent identifies modules that consistently trigger full-page reloads instead of surgical HMR updates, flags circular import chains that cause cascading invalidation, and benchmarks update latency per module boundary. Output includes a JSON trace compatible with Chrome DevTools Performance panel import, plus a ranked list of the slowest HMR chains. It leverages vite.createServer() internals, the ModuleGraph API, and ssrLoadModule for server-side module tracing. Particularly useful for large monorepo setups using Turborepo or Nx where HMR performance degrades as the module graph grows beyond 5,000 nodes."
source: "https://github.com/vitejs/vite"
verification: "security_reviewed"
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

The Vite Plugin Hot Module Analyzer inspects your Vite development server&#8217;s HMR pipeline in real time. It hooks into the Vite plugin API via the handleHotUpdate() lifecycle to intercept module graph changes, then correlates these with WebSocket frame timestamps from the Vite dev server&#8217;s ws connection. The agent identifies modules that consistently trigger full-page reloads instead of surgical HMR updates, flags circular import chains that cause cascading invalidation, and benchmarks update latency per module boundary. Output includes a JSON trace compatible with Chrome DevTools Performance panel import, plus a ranked list of the slowest HMR chains. It leverages vite.createServer() internals, the ModuleGraph API, and ssrLoadModule for server-side module tracing. Particularly useful for large monorepo setups using Turborepo or Nx where HMR performance degrades as the module graph grows beyond 5,000 nodes.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vite-plugin-hmr-analyzer/)

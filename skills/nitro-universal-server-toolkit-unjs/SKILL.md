---
title: Nitro Next-Generation Universal Server Toolkit by UnJS
description: 'Nitro is an open-source, TypeScript-first server toolkit created by
  the UnJS team (the same group behind Nuxt). It provides a unified abstraction for
  building web servers, API routes, and server middleware that deploy to over 15 hosting
  platforms without changing application code. Nitro powers the server layer of Nuxt
  3 and is used independently for standalone API services, edge functions, and serverless
  deployments. Core Architecture Nitro uses file-based routing for API endpoints in
  the routes/ directory, with automatic HTTP method detection from filenames (e.g.,
  routes/users.get.ts ). It provides a built-in key-value storage layer via useStorage()
  that abstracts filesystem, Redis, Cloudflare KV, and other backends. The framework
  includes an auto-imported utility system, server middleware support, scheduled tasks
  via cron syntax, and WebSocket support through defineWebSocketHandler . Agent Integration
  Points For coding agents, Nitro offers scaffolding and deployment automation opportunities.
  An agent can generate API endpoints using file-based conventions, configure deployment
  presets for target platforms, manage storage driver configurations, and set up caching
  rules. The nitro.config.ts configuration file controls presets, route rules, storage
  mounts, and runtime configuration — all of which an agent can generate or modify
  programmatically. Deployment Presets Nitro ships with presets for Node.js standalone,
  Cloudflare Workers/Pages, Vercel Edge/Serverless, Netlify Edge/Functions, Deno Deploy,
  Bun, AWS Lambda, Azure Functions, and more. Switching targets requires changing
  a single preset configuration value. The build output is automatically optimized
  with tree-shaking and code-splitting for each target. Installation Install via npm:
  npx giget@latest nitro my-app or add to an existing project with npm install nitropack
  . Run the dev server with npx nitropack dev and build for production with npx nitropack
  build . The CLI handles preset detection, output bundling, and platform-specific
  packaging automatically.'
verification: security_reviewed
source: https://github.com/nitrojs/nitro
category:
- Developer Tools
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: nitrojs/nitro
  github_stars: 10640
---

# Nitro Next-Generation Universal Server Toolkit by UnJS

Nitro is an open-source, TypeScript-first server toolkit created by the UnJS team (the same group behind Nuxt). It provides a unified abstraction for building web servers, API routes, and server middleware that deploy to over 15 hosting platforms without changing application code. Nitro powers the server layer of Nuxt 3 and is used independently for standalone API services, edge functions, and serverless deployments. Core Architecture Nitro uses file-based routing for API endpoints in the routes/ directory, with automatic HTTP method detection from filenames (e.g., routes/users.get.ts ). It provides a built-in key-value storage layer via useStorage() that abstracts filesystem, Redis, Cloudflare KV, and other backends. The framework includes an auto-imported utility system, server middleware support, scheduled tasks via cron syntax, and WebSocket support through defineWebSocketHandler . Agent Integration Points For coding agents, Nitro offers scaffolding and deployment automation opportunities. An agent can generate API endpoints using file-based conventions, configure deployment presets for target platforms, manage storage driver configurations, and set up caching rules. The nitro.config.ts configuration file controls presets, route rules, storage mounts, and runtime configuration — all of which an agent can generate or modify programmatically. Deployment Presets Nitro ships with presets for Node.js standalone, Cloudflare Workers/Pages, Vercel Edge/Serverless, Netlify Edge/Functions, Deno Deploy, Bun, AWS Lambda, Azure Functions, and more. Switching targets requires changing a single preset configuration value. The build output is automatically optimized with tree-shaking and code-splitting for each target. Installation Install via npm: npx giget@latest nitro my-app or add to an existing project with npm install nitropack . Run the dev server with npx nitropack dev and build for production with npx nitropack build . The CLI handles preset detection, output bundling, and platform-specific packaging automatically.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nitro-universal-server-toolkit-unjs/)

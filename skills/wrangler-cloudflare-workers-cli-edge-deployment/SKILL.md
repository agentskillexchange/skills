---
title: Wrangler Cloudflare Workers CLI for Edge Deployment
description: 'Overview Wrangler is Cloudflare official CLI for the Workers platform,
  the leading edge compute environment. It handles the full lifecycle of serverless
  edge applications — from project scaffolding and local development to production
  deployment across Cloudflare 300+ global data centers. Key Features Local Development:
  Built-in local dev server powered by Miniflare and the workerd runtime, providing
  accurate local simulation of the Workers environment including KV, R2, D1, Durable
  Objects, and Queues. Zero-Config Deploy: Ship code to the edge with wrangler deploy
  — no infrastructure configuration required. Automatic bundling with esbuild handles
  TypeScript, JSX, and module resolution. Storage Bindings: First-class support for
  Cloudflare storage products including Workers KV (key-value), R2 (S3-compatible
  object storage), D1 (SQLite at the edge), and Durable Objects (stateful coordination).
  Tail and Logs: Stream real-time logs from production Workers with wrangler tail
  for debugging and observability. Pages Integration: Deploy full-stack applications
  with Cloudflare Pages, combining static assets with Workers functions. How It Works
  Wrangler reads a wrangler.toml configuration file that defines your Worker name,
  routes, environment variables, and storage bindings. During development, wrangler
  dev starts a local server that accurately simulates the Cloudflare runtime. When
  ready, wrangler deploy bundles your code and pushes it to the Cloudflare network
  where it runs in V8 isolates at the edge. Agent Integration AI agents can leverage
  Wrangler to deploy tool servers, API endpoints, and webhook handlers to the edge.
  The CLI-driven workflow is ideal for automated deployment pipelines — agents can
  scaffold projects with npm create cloudflare@latest , configure bindings in wrangler.toml,
  and deploy with a single command. The local dev server enables agents to test and
  iterate before production deployment. Installation npm install -g wrangler # or
  create a new project: npm create cloudflare@latest Quick Start # Create a new Worker
  npm create cloudflare@latest my-worker cd my-worker # Start local development wrangler
  dev # Deploy to Cloudflare wrangler deploy'
verification: security_reviewed
source: https://github.com/cloudflare/workers-sdk
category:
- Developer Tools
framework:
- Custom Agents
tool_ecosystem:
  github_repo: cloudflare/workers-sdk
  github_stars: 3951
---

# Wrangler Cloudflare Workers CLI for Edge Deployment

Overview Wrangler is Cloudflare official CLI for the Workers platform, the leading edge compute environment. It handles the full lifecycle of serverless edge applications — from project scaffolding and local development to production deployment across Cloudflare 300+ global data centers. Key Features Local Development: Built-in local dev server powered by Miniflare and the workerd runtime, providing accurate local simulation of the Workers environment including KV, R2, D1, Durable Objects, and Queues. Zero-Config Deploy: Ship code to the edge with wrangler deploy — no infrastructure configuration required. Automatic bundling with esbuild handles TypeScript, JSX, and module resolution. Storage Bindings: First-class support for Cloudflare storage products including Workers KV (key-value), R2 (S3-compatible object storage), D1 (SQLite at the edge), and Durable Objects (stateful coordination). Tail and Logs: Stream real-time logs from production Workers with wrangler tail for debugging and observability. Pages Integration: Deploy full-stack applications with Cloudflare Pages, combining static assets with Workers functions. How It Works Wrangler reads a wrangler.toml configuration file that defines your Worker name, routes, environment variables, and storage bindings. During development, wrangler dev starts a local server that accurately simulates the Cloudflare runtime. When ready, wrangler deploy bundles your code and pushes it to the Cloudflare network where it runs in V8 isolates at the edge. Agent Integration AI agents can leverage Wrangler to deploy tool servers, API endpoints, and webhook handlers to the edge. The CLI-driven workflow is ideal for automated deployment pipelines — agents can scaffold projects with npm create cloudflare@latest , configure bindings in wrangler.toml, and deploy with a single command. The local dev server enables agents to test and iterate before production deployment. Installation npm install -g wrangler # or create a new project: npm create cloudflare@latest Quick Start # Create a new Worker npm create cloudflare@latest my-worker cd my-worker # Start local development wrangler dev # Deploy to Cloudflare wrangler deploy

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wrangler-cloudflare-workers-cli-edge-deployment/)

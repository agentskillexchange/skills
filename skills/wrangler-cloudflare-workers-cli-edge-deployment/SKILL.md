---
name: "Wrangler Cloudflare Workers CLI for Edge Deployment"
description: "Wrangler is the official command-line tool for building, testing, and deploying Cloudflare Workers. It provides a complete development workflow for serverless edge applications including local development with Miniflare, KV/R2/D1 bindings, and zero-config deployment to Cloudflare global network."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/cloudflare/workers-sdk"
tool_ecosystem:
  github_repo: "cloudflare/workers-sdk"
  github_stars: 3946
---
# Wrangler Cloudflare Workers CLI for Edge Deployment

Wrangler is the official command-line tool for building, testing, and deploying Cloudflare Workers. It provides a complete development workflow for serverless edge applications including local development with Miniflare, KV/R2/D1 bindings, and zero-config deployment to Cloudflare global network.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wrangler-cloudflare-workers-cli-edge-deployment
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wrangler-cloudflare-workers-cli-edge-deployment -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wrangler-cloudflare-workers-cli-edge-deployment -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wrangler-cloudflare-workers-cli-edge-deployment -a codex
```

### OpenClaw

```bash
clawhub install wrangler-cloudflare-workers-cli-edge-deployment
```

## Details

Overview
Wrangler is Cloudflare official CLI for the Workers platform, the leading edge compute environment. It handles the full lifecycle of serverless edge applications — from project scaffolding and local development to production deployment across Cloudflare 300+ global data centers.

Key Features

Local Development: Built-in local dev server powered by Miniflare and the workerd runtime, providing accurate local simulation of the Workers environment including KV, R2, D1, Durable Objects, and Queues.
Zero-Config Deploy: Ship code to the edge with wrangler deploy — no infrastructure configuration required. Automatic bundling with esbuild handles TypeScript, JSX, and module resolution.
Storage Bindings: First-class support for Cloudflare storage products including Workers KV (key-value), R2 (S3-compatible object storage), D1 (SQLite at the edge), and Durable Objects (stateful coordination).
Tail and Logs: Stream real-time logs from production Workers with wrangler tail for debugging and observability.
Pages Integration: Deploy full-stack applications with Cloudflare Pages, combining static assets with Workers functions.

How It Works
Wrangler reads a wrangler.toml configuration file that defines your Worker name, routes, environment variables, and storage bindings. During development, wrangler dev starts a local server that accurately simulates the Cloudflare runtime. When ready, wrangler deploy bundles your code and pushes it to the Cloudflare network where it runs in V8 isolates at the edge.

Agent Integration
AI agents can leverage Wrangler to deploy tool servers, API endpoints, and webhook handlers to the edge. The CLI-driven workflow is ideal for automated deployment pipelines — agents can scaffold projects with npm create cloudflare@latest, configure bindings in wrangler.toml, and deploy with a single command. The local dev server enables agents to test and iterate before production deployment.

Installation
npm install -g wrangler
# or create a new project:
npm create cloudflare@latest
Quick Start
# Create a new Worker
npm create cloudflare@latest my-worker
cd my-worker

# Start local development
wrangler dev

# Deploy to Cloudflare
wrangler deploy

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wrangler-cloudflare-workers-cli-edge-deployment/)

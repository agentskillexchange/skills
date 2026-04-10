---
title: "Sharp Image CDN Optimizer"
description: "On-the-fly image optimization using Sharp (libvips Node.js bindings) with CDN-aware caching headers. Supports responsive srcset generation, AVIF/WebP transcoding, and blur placeholder (LQIP) creation."
slug: "sharp-image-cdn-optimizer"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sharp-image-cdn-optimizer/"
---

# Sharp Image CDN Optimizer

On-the-fly image optimization using Sharp (libvips Node.js bindings) with CDN-aware caching headers. Supports responsive srcset generation, AVIF/WebP transcoding, and blur placeholder (LQIP) creation.

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
clawhub install sharp-image-cdn-optimizer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Sharp Image CDN Optimizer is built around Sharp image processing library powered by libvips. The underlying ecosystem is represented by lovell/sharp (32,068+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like resize, format conversion, AVIF/WebP, metadata, pipelines, buffers and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to sharp so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: On-the-fly image optimization using Sharp (libvips Node.js bindings) with CDN-aware caching headers. Supports responsive srcset generation, AVIF/WebP transcoding, and blur placeholder (LQIP) creation. The implementation typically relies on resize, format conversion, AVIF/WebP, metadata, pipelines, buffers, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses resize, format conversion, AVIF/WebP, metadata, pipelines, buffers instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as image optimization, CDN transforms, placeholders, and responsive assets.
Key integration points include image optimization, CDN transforms, placeholders, and responsive assets. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sharp-image-cdn-optimizer/)

---
title: "Sharp Image CDN Optimizer"
description: "On-the-fly image optimization using Sharp (libvips Node.js bindings) with CDN-aware caching headers. Supports responsive srcset generation, AVIF/WebP transcoding, and blur placeholder (LQIP) creation."
verification: "security_reviewed"
source: "https://github.com/lovell/sharp"
category:
  - "Image & Creative Automation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "lovell/sharp"
  github_stars: 32138
  ase_npm_package: "sharp"
  npm_weekly_downloads: 52472150
  license: "Apache-2.0"
---

# Sharp Image CDN Optimizer

Sharp Image CDN Optimizer is built around Sharp image processing library powered by libvips. The underlying ecosystem is represented by lovell/sharp (32,068+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like resize, format conversion, AVIF/WebP, metadata, pipelines, buffers and preserving the operational context that matters for real tasks.


In practice, the skill gives an agent a stable interface to sharp so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: On-the-fly image optimization using Sharp (libvips Node.js bindings) with CDN-aware caching headers. Supports responsive srcset generation, AVIF/WebP transcoding, and blur placeholder (LQIP) creation. The implementation typically relies on resize, format conversion, AVIF/WebP, metadata, pipelines, buffers, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.



Accesses resize, format conversion, AVIF/WebP, metadata, pipelines, buffers instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as image optimization, CDN transforms, placeholders, and responsive assets.

 Key integration points include image optimization, CDN transforms, placeholders, and responsive assets. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sharp-image-cdn-optimizer/)

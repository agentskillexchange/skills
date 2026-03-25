---
name: "Sharp Image CDN Optimizer"
description: "On-the-fly image optimization using Sharp (libvips Node.js bindings) with CDN-aware caching headers. Supports responsive srcset generation, AVIF/WebP transcoding, and blur placeholder (LQIP) creation."
category: "Image & Creative Automation"
framework: "Custom Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sharp-image-cdn-optimizer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sharp"  # from ase_tool_match
  github_stars: 32068  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 54450041  # from ase_npm_downloads
  github_repo: "lovell/sharp"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Sharp Image CDN Optimizer

On-the-fly image optimization using Sharp (libvips Node.js bindings) with CDN-aware caching headers. Supports responsive srcset generation, AVIF/WebP transcoding, and blur placeholder (LQIP) creation.

## Overview

The Sharp Image CDN Optimizer provides production-grade image optimization using Sharp, the high-performance Node.js bindings for libvips. It processes images on-the-fly or in batch mode, generating optimized variants for web delivery with proper CDN cache headers (Cache-Control, ETag, Vary: Accept).

Core capabilities include responsive image generation with automatic srcset creation at configurable breakpoints (320w, 640w, 1024w, 1920w), format transcoding to AVIF (sharp.avif({quality: 50})) and WebP (sharp.webp({effort: 6})) with Accept header-based content negotiation, and Low Quality Image Placeholder (LQIP) generation using sharp.blur(20).resize(20) for progressive loading.

The skill handles advanced transformations including smart cropping with sharp.resize({fit: ‘cover’, position: sharp.strategy.attention}), color space conversion, animated GIF/WebP processing, and SVG rasterization. It integrates with S3-compatible storage for origin serving, supports Cloudflare/Fastly cache purge APIs on source updates, and generates image processing manifests tracking all variants. Performance monitoring includes processing time histograms and cache hit ratio tracking.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sharp-image-cdn-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sharp-image-cdn-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sharp-image-cdn-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sharp-image-cdn-optimizer -a codex
```

### OpenClaw

```bash
clawhub install sharp-image-cdn-optimizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sharp-image-cdn-optimizer/

---
name: Cloudinary Media Transform Skill
description: Manages image and video assets through the Cloudinary Upload and Admin
  APIs. Applies on-the-fly transformations, generates responsive breakpoints, and
  optimizes delivery with f_auto and q_auto parameters.
category: "Image &amp; Creative Automation"
framework: Custom Agents
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cloudinary-media-transform-skill/"
---
# Cloudinary Media Transform Skill

Manages image and video assets through the Cloudinary Upload and Admin APIs. Applies on-the-fly transformations, generates responsive breakpoints, and optimizes delivery with f_auto and q_auto parameters.

The Cloudinary Media Transform Skill connects Claude to Cloudinary’s cloud-based media management platform through its Upload API and Admin API. It handles the full lifecycle of visual assets from upload through transformation to delivery optimization.

Upload operations support direct file upload, remote URL fetching, and base64-encoded content with automatic format detection. The skill sets upload presets, tags, and contextual metadata during ingestion. Folder organization and asset tagging enable structured media library management.

Transformation capabilities leverage Cloudinary’s URL-based transformation pipeline: resize with crop modes (fill, fit, limit, pad, scale), overlay composition for watermarks and text, color adjustments, and artistic filters. The skill constructs chained transformation URLs with proper parameter ordering and encoding.

Delivery optimization uses f_auto for automatic format selection (WebP for Chrome, AVIF for supported browsers, JPEG fallback) and q_auto for perceptual quality optimization. The responsive breakpoints API generates optimal image dimensions based on actual content, eliminating guesswork in srcset generation. The Admin API provides usage analytics, storage quotas, and asset search across the media library. Authentication uses cloud_name, api_key, and api_secret with SHA-1 signature generation for secure uploads. Ideal for content platforms and e-commerce teams managing large media catalogs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cloudinary-media-transform-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cloudinary-media-transform-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cloudinary-media-transform-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cloudinary-media-transform-skill -a codex
```

### OpenClaw

```bash
clawhub install cloudinary-media-transform-skill
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-media-transform-skill/)

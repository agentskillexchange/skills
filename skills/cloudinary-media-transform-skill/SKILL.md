---
title: "Cloudinary Media Transform Skill"
description: "Manages image and video assets through the Cloudinary Upload and Admin APIs. Applies on-the-fly transformations, generates responsive breakpoints, and optimizes delivery with f_auto and q_auto parameters."
slug: "cloudinary-media-transform-skill"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cloudinary-media-transform-skill/"
---

# Cloudinary Media Transform Skill

Manages image and video assets through the Cloudinary Upload and Admin APIs. Applies on-the-fly transformations, generates responsive breakpoints, and optimizes delivery with f_auto and q_auto parameters.

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
clawhub install cloudinary-media-transform-skill
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Cloudinary Media Transform Skill connects Claude to Cloudinary’s cloud-based media management platform through its Upload API and Admin API. It handles the full lifecycle of visual assets from upload through transformation to delivery optimization.
Upload operations support direct file upload, remote URL fetching, and base64-encoded content with automatic format detection. The skill sets upload presets, tags, and contextual metadata during ingestion. Folder organization and asset tagging enable structured media library management.
Transformation capabilities leverage Cloudinary’s URL-based transformation pipeline: resize with crop modes (fill, fit, limit, pad, scale), overlay composition for watermarks and text, color adjustments, and artistic filters. The skill constructs chained transformation URLs with proper parameter ordering and encoding.
Delivery optimization uses f_auto for automatic format selection (WebP for Chrome, AVIF for supported browsers, JPEG fallback) and q_auto for perceptual quality optimization. The responsive breakpoints API generates optimal image dimensions based on actual content, eliminating guesswork in srcset generation. The Admin API provides usage analytics, storage quotas, and asset search across the media library. Authentication uses cloud_name, api_key, and api_secret with SHA-1 signature generation for secure uploads. Ideal for content platforms and e-commerce teams managing large media catalogs.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-media-transform-skill/)

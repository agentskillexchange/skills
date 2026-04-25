---
title: "Cloudinary Media Transform Skill"
description: "Manages image and video assets through the Cloudinary Upload and Admin APIs. Applies on-the-fly transformations, generates responsive breakpoints, and optimizes delivery with f_auto and q_auto parameters."
verification: "security_reviewed"
source: "https://cloudinary.com/documentation"
category:
  - "Image & Creative Automation"
framework:
  - "Custom Agents"
---

# Cloudinary Media Transform Skill

The Cloudinary Media Transform Skill connects Claude to Cloudinary’s cloud-based media management platform through its Upload API and Admin API. It handles the full lifecycle of visual assets from upload through transformation to delivery optimization. Upload operations support direct file upload, remote URL fetching, and base64-encoded content with automatic format detection. The skill sets upload presets, tags, and contextual metadata during ingestion. Folder organization and asset tagging enable structured media library management. Transformation capabilities leverage Cloudinary’s URL-based transformation pipeline: resize with crop modes (fill, fit, limit, pad, scale), overlay composition for watermarks and text, color adjustments, and artistic filters. The skill constructs chained transformation URLs with proper parameter ordering and encoding. Delivery optimization uses f_auto for automatic format selection (WebP for Chrome, AVIF for supported browsers, JPEG fallback) and q_auto for perceptual quality optimization. The responsive breakpoints API generates optimal image dimensions based on actual content, eliminating guesswork in srcset generation. The Admin API provides usage analytics, storage quotas, and asset search across the media library. Authentication uses cloud_name, api_key, and api_secret with SHA-1 signature generation for secure uploads. Ideal for content platforms and e-commerce teams managing large media catalogs.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cloudinary-media-transform-skill/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cloudinary-media-transform-skill
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cloudinary-media-transform-skill`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-media-transform-skill/)

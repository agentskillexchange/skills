---
title: "Cloudinary DAM Pipeline"
description: "Manage digital assets through the Cloudinary Upload, Admin, and Transformation APIs. Automates image optimization with responsive breakpoints, AI-powered cropping via g_auto, and CDN delivery URL generation."
slug: "cloudinary-dam-pipeline-skill"
category:
  - "Image &amp; Creative Automation"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cloudinary-dam-pipeline-skill/"
---

# Cloudinary DAM Pipeline

Manage digital assets through the Cloudinary Upload, Admin, and Transformation APIs. Automates image optimization with responsive breakpoints, AI-powered cropping via g_auto, and CDN delivery URL generation.

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
clawhub install cloudinary-dam-pipeline-skill
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Build automated digital asset management workflows using the Cloudinary platform APIs. This skill handles the complete asset lifecycle from upload through transformation to CDN delivery.
The upload pipeline uses the Cloudinary Upload API with unsigned and signed presets, supporting eager transformations that process images immediately on upload. Automatic format selection (f_auto) and quality optimization (q_auto) are applied by default for web delivery.
AI-powered features include automatic gravity cropping (g_auto) for intelligent subject detection, background removal (e_background_removal), and generative fill (e_gen_fill) for extending image canvas. Responsive breakpoint generation creates optimized image variants for srcset delivery.
The Admin API handles folder management, tag operations, and bulk metadata updates across asset collections. Search capabilities use the Cloudinary Search API with Lucene query syntax for filtering by dimensions, format, tags, and custom metadata fields.
Transformation URLs are constructed programmatically using the cloudinary-node SDK with chained transformation parameters for resize, crop, overlay, and effect operations. The skill manages transformation counts against account quotas.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-dam-pipeline-skill/)

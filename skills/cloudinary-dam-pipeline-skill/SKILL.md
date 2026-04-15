---
title: "Cloudinary DAM Pipeline"
description: "Manage digital assets through the Cloudinary Upload, Admin, and Transformation APIs. Automates image optimization with responsive breakpoints, AI-powered cropping via g_auto, and CDN delivery URL generation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cloudinary-dam-pipeline-skill/"
category:
  - "Image & Creative Automation"
framework:
  - "ChatGPT Agents"
---

# Cloudinary DAM Pipeline

Build automated digital asset management workflows using the Cloudinary platform APIs. This skill handles the complete asset lifecycle from upload through transformation to CDN delivery.

The upload pipeline uses the Cloudinary Upload API with unsigned and signed presets, supporting eager transformations that process images immediately on upload. Automatic format selection (f_auto) and quality optimization (q_auto) are applied by default for web delivery.

AI-powered features include automatic gravity cropping (g_auto) for intelligent subject detection, background removal (e_background_removal), and generative fill (e_gen_fill) for extending image canvas. Responsive breakpoint generation creates optimized image variants for srcset delivery.

The Admin API handles folder management, tag operations, and bulk metadata updates across asset collections. Search capabilities use the Cloudinary Search API with Lucene query syntax for filtering by dimensions, format, tags, and custom metadata fields.

Transformation URLs are constructed programmatically using the cloudinary-node SDK with chained transformation parameters for resize, crop, overlay, and effect operations. The skill manages transformation counts against account quotas.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cloudinary-dam-pipeline-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/cloudinary-dam-pipeline-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-dam-pipeline-skill/)

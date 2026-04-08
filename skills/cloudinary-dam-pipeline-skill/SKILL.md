---
title: Cloudinary DAM Pipeline
description: Build automated digital asset management workflows using the Cloudinary
  platform APIs. This skill handles the complete asset lifecycle from upload through
  transformation to CDN delivery. The upload pipeline uses the Cloudinary Upload API
  with unsigned and signed presets, supporting eager transformations that process
  images immediately on upload. Automatic format selection (f_auto) and quality optimization
  (q_auto) are applied by default for web delivery. AI-powered features include automatic
  gravity cropping (g_auto) for intelligent subject detection, background removal
  (e_background_removal), and generative fill (e_gen_fill) for extending image canvas.
  Responsive breakpoint generation creates optimized image variants for srcset delivery.
  The Admin API handles folder management, tag operations, and bulk metadata updates
  across asset collections. Search capabilities use the Cloudinary Search API with
  Lucene query syntax for filtering by dimensions, format, tags, and custom metadata
  fields. Transformation URLs are constructed programmatically using the cloudinary-node
  SDK with chained transformation parameters for resize, crop, overlay, and effect
  operations. The skill manages transformation counts against account quotas.
verification: security_reviewed
source: https://agentskillexchange.com/skills/cloudinary-dam-pipeline-skill/
category:
- Image &amp; Creative Automation
framework:
- ChatGPT Agents
---

# Cloudinary DAM Pipeline

Build automated digital asset management workflows using the Cloudinary platform APIs. This skill handles the complete asset lifecycle from upload through transformation to CDN delivery. The upload pipeline uses the Cloudinary Upload API with unsigned and signed presets, supporting eager transformations that process images immediately on upload. Automatic format selection (f_auto) and quality optimization (q_auto) are applied by default for web delivery. AI-powered features include automatic gravity cropping (g_auto) for intelligent subject detection, background removal (e_background_removal), and generative fill (e_gen_fill) for extending image canvas. Responsive breakpoint generation creates optimized image variants for srcset delivery. The Admin API handles folder management, tag operations, and bulk metadata updates across asset collections. Search capabilities use the Cloudinary Search API with Lucene query syntax for filtering by dimensions, format, tags, and custom metadata fields. Transformation URLs are constructed programmatically using the cloudinary-node SDK with chained transformation parameters for resize, crop, overlay, and effect operations. The skill manages transformation counts against account quotas.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-dam-pipeline-skill/)

---
name: Cloudinary DAM Pipeline
description: Manage digital assets through the Cloudinary Upload, Admin, and Transformation
  APIs. Automates image optimization with responsive breakpoints, AI-powered cropping
  via g_auto, and CDN delivery URL generation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/cloudinary-dam-pipeline-skill/
category:
- Image &amp; Creative Automation
framework:
- ChatGPT Agents
---
# Cloudinary DAM Pipeline

Build automated digital asset management workflows using the Cloudinary platform APIs. This skill handles the complete asset lifecycle from upload through transformation to CDN delivery.
The upload pipeline uses the Cloudinary Upload API with unsigned and signed presets, supporting eager transformations that process images immediately on upload. Automatic format selection (f_auto) and quality optimization (q_auto) are applied by default for web delivery.
AI-powered features include automatic gravity cropping (g_auto) for intelligent subject detection, background removal (e_background_removal), and generative fill (e_gen_fill) for extending image canvas. Responsive breakpoint generation creates optimized image variants for srcset delivery.
The Admin API handles folder management, tag operations, and bulk metadata updates across asset collections. Search capabilities use the Cloudinary Search API with Lucene query syntax for filtering by dimensions, format, tags, and custom metadata fields.
Transformation URLs are constructed programmatically using the cloudinary-node SDK with chained transformation parameters for resize, crop, overlay, and effect operations. The skill manages transformation counts against account quotas.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-dam-pipeline-skill/)

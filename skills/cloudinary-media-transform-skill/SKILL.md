---
title: "Cloudinary Media Transform Skill"
description: "The Cloudinary Media Transform Skill connects Claude to Cloudinary&#8217;s cloud-based media management platform through its Upload API and Admin API. It handles the full lifecycle of visual assets from upload through transformation to delivery optimization. Upload operations support direct file upload, remote URL fetching, and base64-encoded content with automatic format detection. The skill sets upload presets, tags, and contextual metadata during ingestion. Folder organization and asset tagging enable structured media library management. Transformation capabilities leverage Cloudinary&#8217;s URL-based transformation pipeline: resize with crop modes (fill, fit, limit, pad, scale), overlay composition for watermarks and text, color adjustments, and artistic filters. The skill constructs chained transformation URLs with proper parameter ordering and encoding. Delivery optimization uses f_auto for automatic format selection (WebP for Chrome, AVIF for supported browsers, JPEG fallback) and q_auto for perceptual quality optimization. The responsive breakpoints API generates optimal image dimensions based on actual content, eliminating guesswork in srcset generation. The Admin API provides usage analytics, storage quotas, and asset search across the media library. Authentication uses cloud_name, api_key, and api_secret with SHA-1 signature generation for secure uploads. Ideal for content platforms and e-commerce teams managing large media catalogs."
source: "https://agentskillexchange.com/skills/cloudinary-media-transform-skill/"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
---

# Cloudinary Media Transform Skill

The Cloudinary Media Transform Skill connects Claude to Cloudinary&#8217;s cloud-based media management platform through its Upload API and Admin API. It handles the full lifecycle of visual assets from upload through transformation to delivery optimization. Upload operations support direct file upload, remote URL fetching, and base64-encoded content with automatic format detection. The skill sets upload presets, tags, and contextual metadata during ingestion. Folder organization and asset tagging enable structured media library management. Transformation capabilities leverage Cloudinary&#8217;s URL-based transformation pipeline: resize with crop modes (fill, fit, limit, pad, scale), overlay composition for watermarks and text, color adjustments, and artistic filters. The skill constructs chained transformation URLs with proper parameter ordering and encoding. Delivery optimization uses f_auto for automatic format selection (WebP for Chrome, AVIF for supported browsers, JPEG fallback) and q_auto for perceptual quality optimization. The responsive breakpoints API generates optimal image dimensions based on actual content, eliminating guesswork in srcset generation. The Admin API provides usage analytics, storage quotas, and asset search across the media library. Authentication uses cloud_name, api_key, and api_secret with SHA-1 signature generation for secure uploads. Ideal for content platforms and e-commerce teams managing large media catalogs.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-media-transform-skill/)

---
title: "Cloudinary Media Optimization Agent"
description: "Automates image and video optimization workflows via the Cloudinary Upload and Admin APIs. Applies responsive breakpoints, format negotiation, and intelligent cropping with gravity detection."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cloudinary-media-optimization-agent/"
category:
  - "Image & Creative Automation"
framework:
  - "Claude Agents"
---

# Cloudinary Media Optimization Agent

The Cloudinary Media Optimization Agent manages automated image and video processing workflows through the Cloudinary Upload API and Admin API. It handles bulk asset optimization with intelligent format selection (AVIF, WebP, JPEG XL) based on browser capability detection.

Responsive image breakpoint generation uses Cloudinary responsive breakpoints API to calculate optimal image widths, generating srcset attributes that minimize bandwidth while maintaining visual quality. The agent configures automatic format (f_auto) and quality (q_auto) transformations for delivery optimization.

Intelligent cropping leverages Cloudinary AI-powered gravity detection modes including g_auto, g_face, and g_custom for content-aware composition. Named transformations are managed programmatically for consistent brand styling across asset libraries.

Video optimization includes adaptive bitrate streaming with HLS and DASH manifest generation, automatic thumbnail extraction, and video-to-GIF conversion for social media assets. The skill supports webhook notifications for asynchronous processing status and integrates with DAM workflows through Cloudinary metadata and structured metadata schemas.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cloudinary-media-optimization-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cloudinary-media-optimization-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cloudinary-media-optimization-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-media-optimization-agent/)

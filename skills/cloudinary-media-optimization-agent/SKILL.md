---
title: "Cloudinary Media Optimization Agent"
description: "Automates image and video optimization workflows via the Cloudinary Upload and Admin APIs. Applies responsive breakpoints, format negotiation, and intelligent cropping with gravity detection."
slug: "cloudinary-media-optimization-agent"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cloudinary-media-optimization-agent/"
listed: true
---

# Cloudinary Media Optimization Agent

Automates image and video optimization workflows via the Cloudinary Upload and Admin APIs. Applies responsive breakpoints, format negotiation, and intelligent cropping with gravity detection.

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
clawhub install cloudinary-media-optimization-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Cloudinary Media Optimization Agent manages automated image and video processing workflows through the Cloudinary Upload API and Admin API. It handles bulk asset optimization with intelligent format selection (AVIF, WebP, JPEG XL) based on browser capability detection.
Responsive image breakpoint generation uses Cloudinary responsive breakpoints API to calculate optimal image widths, generating srcset attributes that minimize bandwidth while maintaining visual quality. The agent configures automatic format (f_auto) and quality (q_auto) transformations for delivery optimization.
Intelligent cropping leverages Cloudinary AI-powered gravity detection modes including g_auto, g_face, and g_custom for content-aware composition. Named transformations are managed programmatically for consistent brand styling across asset libraries.
Video optimization includes adaptive bitrate streaming with HLS and DASH manifest generation, automatic thumbnail extraction, and video-to-GIF conversion for social media assets. The skill supports webhook notifications for asynchronous processing status and integrates with DAM workflows through Cloudinary metadata and structured metadata schemas.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-media-optimization-agent/)
